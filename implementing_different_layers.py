# Implementing Different Layers
#---------------------------------------
#
# We will illustrate how to use different types
# of layers in TensorFlow
#
# The layers of interest are:
#  (1) Convolutional Layer
#  (2) Activation Layer
#  (3) Max-Pool Layer
#  (4) Fully Connected Layer
#
# We will generate two different data sets for this
#  script, a 1-D data set (row of data) and
#  a 2-D data set (similar to picture)

import tensorflow as tf
import matplotlib.pyplot as plt
import csv
import os
import random
import numpy as np
import random
from tensorflow.python.framework import ops
ops.reset_default_graph()

#---------------------------------------------------|
#----------------1D-data，1维向量-------------------|
#---------------------------------------------------|

# 创建计算图 
ops.reset_default_graph()
sess = tf.Session()

# 运行参数
data_size = 25  # 向量长度
conv_size = 5   # 卷积核大小
maxpool_size = 5 
stride_size = 1 # 卷积核位移

# 确保可重现，指定随机数
seed=13
np.random.seed(seed)
tf.set_random_seed(seed)

# 1D data, 生成1维向量
data_1d = np.random.normal(size=data_size)

# Placeholder
x_input_1d = tf.placeholder(dtype=tf.float32, shape=[data_size])

#--------1D Convolution--------
def conv_layer_1d(input_1d, my_filter,stride):
    # tensorflow的"conv2d()"函数只能使用4D数组：[batch#, width, height, channels]
    # 这里使用 batck=1, width=1, height=input length, channel=1，所以必须扩维到4D
    input_2d = tf.expand_dims(input_1d, 0)
    input_3d = tf.expand_dims(input_2d, 0)
    input_4d = tf.expand_dims(input_3d, 3)
	# 使用卷积stride=1, 如果需要增加到2，使用strides=[1,1,2,1]
    convolution_output = tf.nn.conv2d(input_4d, filter=my_filter, strides=[1,1,stride,1], padding="VALID")
    # 降低维度
    conv_output_1d = tf.squeeze(convolution_output)
    return(conv_output_1d)  # 输出1D向量，padding= valid时的长度=data_size - filter +1

# 创建卷积滤波器，设定滤波器pattern，filter与input做矩阵乘法
my_filter = tf.Variable(tf.random_normal(shape=[1,conv_size,1,1]))
# 创建1D卷积层
my_convolution_output = conv_layer_1d(x_input_1d, my_filter,stride=stride_size)

#--------激活函数--------
def activation(input_1d):
    return(tf.nn.relu(input_1d))

# 创建激活层
my_activation_output = activation(my_convolution_output)

#--------Max Pool，池化--------
def max_pool(input_1d, width,stride):
    # 和'conv2d()' 类似, max_pool()需要输入4D arrays.
    # [batch_size=1, width=1, height=num_input, channels=1]
    input_2d = tf.expand_dims(input_1d, 0)
    input_3d = tf.expand_dims(input_2d, 0)
    input_4d = tf.expand_dims(input_3d, 3)
    # Perform the max pooling with strides = [1,1,1,1]
    # If we wanted to increase the stride on our data dimension, say by
    # a factor of '2', we put strides = [1, 1, 2, 1]
    # We will also need to specify the width of the max-window ('width')
    pool_output = tf.nn.max_pool(input_4d, ksize=[1, 1, width, 1],
                                 strides=[1, 1, stride, 1],
                                 padding='VALID')
    # 降维
    pool_output_1d = tf.squeeze(pool_output)
    return(pool_output_1d)

my_maxpool_output = max_pool(my_activation_output, width=maxpool_size,stride=stride_size)

#--------Fully Connected--------
def fully_connected(input_layer, num_outputs):
    # First we find the needed shape of the multiplication weight matrix:
    # The dimension will be (length of input) by (num_outputs)
    weight_shape = tf.squeeze(tf.stack([tf.shape(input_layer),[num_outputs]]))
    # Initialize such weight
    weight = tf.random_normal(weight_shape, stddev=0.1)
    # Initialize the bias
    bias = tf.random_normal(shape=[num_outputs])
    # Make the 1D input array into a 2D array for matrix multiplication
    input_layer_2d = tf.expand_dims(input_layer, 0)
    # Perform the matrix multiplication and add the bias
    full_output = tf.add(tf.matmul(input_layer_2d, weight), bias)
    # Get rid of extra dimensions
    full_output_1d = tf.squeeze(full_output)
    return(full_output_1d)

my_full_output = fully_connected(my_maxpool_output, 5)

# Run graph
# Initialize Variables
init = tf.global_variables_initializer()
sess.run(init)

feed_dict = {x_input_1d: data_1d}

print('>>>> 1D Data <<<<')

# Convolution Output
print('Input = array of length %d' % (x_input_1d.shape.as_list()[0]))
print(sess.run(x_input_1d, feed_dict=feed_dict))
print('my_filter shape = %s, value as below:' %(my_filter.shape.as_list()))
print(sess.run(my_filter))
print('Convolution w/ filter, length = %d, stride size = %d, results in an array of length %d:' % 
      (conv_size,stride_size,my_convolution_output.shape.as_list()[0]))
print(sess.run(my_convolution_output, feed_dict=feed_dict))

# Activation Output
print('\nInput = above array of length %d' % (my_convolution_output.shape.as_list()[0]))
print('ReLU element wise returns an array of length %d:' % (my_activation_output.shape.as_list()[0]))
print(sess.run(my_activation_output, feed_dict=feed_dict))

# Max Pool Output
print('\nInput = above array of length %d' % (my_activation_output.shape.as_list()[0]))
print('MaxPool, window length = %d, stride size = %d, results in the array of length %d' %
     (maxpool_size,stride_size,my_maxpool_output.shape.as_list()[0]))
print(sess.run(my_maxpool_output, feed_dict=feed_dict))

# Fully Connected Output
print('\nInput = above array of length %d' % (my_maxpool_output.shape.as_list()[0]))
print('Fully connected layer on all 4 rows with %d outputs:' % 
      (my_full_output.shape.as_list()[0]))
print(sess.run(my_full_output, feed_dict=feed_dict))


#---------------------------------------------------|
#-------------------2D-data-------------------------|
#---------------------------------------------------|

# Reset Graph
ops.reset_default_graph()
sess = tf.Session()

# parameters for the run
row_size = 10
col_size = 10
conv_size = 2
conv_stride_size = 2
maxpool_size = 2
maxpool_stride_size = 1


# ensure reproducibility
seed=13
np.random.seed(seed)
tf.set_random_seed(seed)

#Generate 2D data
data_size = [row_size,col_size]
data_2d = np.random.normal(size=data_size)

#--------Placeholder--------
x_input_2d = tf.placeholder(dtype=tf.float32, shape=data_size)

# Convolution
def conv_layer_2d(input_2d, my_filter,stride_size):
    # TensorFlow's 'conv2d()' function only works with 4D arrays:
    # [batch#, width, height, channels], we have 1 batch, and
    # 1 channel, but we do have width AND height this time.
    # So next we create the 4D array by inserting dimension 1's.
    input_3d = tf.expand_dims(input_2d, 0)
    input_4d = tf.expand_dims(input_3d, 3)
    # Note the stride difference below!
    convolution_output = tf.nn.conv2d(input_4d, filter=my_filter, 
                                      strides=[1,stride_size,stride_size,1], padding="VALID")
    # Get rid of unnecessary dimensions
    conv_output_2d = tf.squeeze(convolution_output)
    return(conv_output_2d)

# Create Convolutional Filter
my_filter = tf.Variable(tf.random_normal(shape=[conv_size,conv_size,1,1]))
# Create Convolutional Layer
my_convolution_output = conv_layer_2d(x_input_2d, my_filter,stride_size=conv_stride_size)

#--------Activation--------
def activation(input_1d):
    return(tf.nn.relu(input_1d))

# Create Activation Layer
my_activation_output = activation(my_convolution_output)

#--------Max Pool--------
def max_pool(input_2d, width, height,stride):
    # Just like 'conv2d()' above, max_pool() works with 4D arrays.
    # [batch_size=1, width=given, height=given, channels=1]
    input_3d = tf.expand_dims(input_2d, 0)
    input_4d = tf.expand_dims(input_3d, 3)
    # Perform the max pooling with strides = [1,1,1,1]
    # If we wanted to increase the stride on our data dimension, say by
    # a factor of '2', we put strides = [1, 2, 2, 1]
    pool_output = tf.nn.max_pool(input_4d, ksize=[1, height, width, 1],
                                 strides=[1, stride, stride, 1],
                                 padding='VALID')
    # Get rid of unnecessary dimensions
    pool_output_2d = tf.squeeze(pool_output)
    return(pool_output_2d)

# Create Max-Pool Layer
my_maxpool_output = max_pool(my_activation_output, 
                             width=maxpool_size, height=maxpool_size,stride=maxpool_stride_size)


#--------Fully Connected--------
def fully_connected(input_layer, num_outputs):
    # In order to connect our whole W byH 2d array, we first flatten it out to
    # a W times H 1D array.
    flat_input = tf.reshape(input_layer, [-1])
    # We then find out how long it is, and create an array for the shape of
    # the multiplication weight = (WxH) by (num_outputs)
    weight_shape = tf.squeeze(tf.stack([tf.shape(flat_input),[num_outputs]]))
    # Initialize the weight
    weight = tf.random_normal(weight_shape, stddev=0.1)
    # Initialize the bias
    bias = tf.random_normal(shape=[num_outputs])
    # Now make the flat 1D array into a 2D array for multiplication
    input_2d = tf.expand_dims(flat_input, 0)
    # Multiply and add the bias
    full_output = tf.add(tf.matmul(input_2d, weight), bias)
    # Get rid of extra dimension
    full_output_2d = tf.squeeze(full_output)
    return(full_output_2d)

# Create Fully Connected Layer
my_full_output = fully_connected(my_maxpool_output, 5)

# Run graph
# Initialize Variables
init = tf.global_variables_initializer()
sess.run(init)

feed_dict = {x_input_2d: data_2d}

print('\n>>>> 2D Data <<<<')

# Convolution Output
print('Input = %s array' % (x_input_2d.shape.as_list()))
print('%s Convolution, stride size = [%d, %d] , results in the %s array' % 
      (my_filter.get_shape().as_list()[:2],conv_stride_size,conv_stride_size,my_convolution_output.shape.as_list()))
print(sess.run(my_convolution_output, feed_dict=feed_dict))

# Activation Output
print('\nInput = the above %s array' % (my_convolution_output.shape.as_list()))
print('ReLU element wise returns the %s array' % (my_activation_output.shape.as_list()))
print(sess.run(my_activation_output, feed_dict=feed_dict))

# Max Pool Output
print('\nInput = the above %s array' % (my_activation_output.shape.as_list()))
print('MaxPool, stride size = [%d, %d], results in %s array' % 
      (maxpool_stride_size,maxpool_stride_size,my_maxpool_output.shape.as_list()))
print(sess.run(my_maxpool_output, feed_dict=feed_dict))

# Fully Connected Output
print('\nInput = the above %s array' % (my_maxpool_output.shape.as_list()))
print('Fully connected layer on all %d rows results in %s outputs:' % 
      (my_maxpool_output.shape.as_list()[0],my_full_output.shape.as_list()[0]))
print(sess.run(my_full_output, feed_dict=feed_dict))