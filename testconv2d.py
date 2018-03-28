# coding=utf-8

import tensorflow as tf
import numpy as np

state = [[1.0000037e+00, 1.0000037e+00, 1.0000000e+00, 4.5852923e-01],
         [1.0000000e+00, 1.0000000e+00, 1.0000000e+00, 8.3596563e-01],
         [1.0000478e+00, 1.0000000e+00, 1.0000478e+00, 1.4663711e+00],
         [1.0000037e+00, 1.0000478e+00, 1.0000037e+00, 2.2898180e+00],
         [1.0000000e+00, 1.0000000e+00, 1.0000000e+00, 1.1520940e+00],
         [1.0025654e+00, 1.0000037e+00, 1.0025654e+00, 1.1330953e+00],
         [9.9988985e-01, 1.0015163e+00, 9.9989718e-01, 3.2291660e-01],
         [1.0000074e+00, 1.0007313e+00, 1.0000000e+00, 1.3017136e+00],
         [1.0000000e+00, 1.0002130e+00, 1.0000000e+00, 5.5019444e-01],
         [1.0004810e+00, 1.0000000e+00, 1.0004810e+00, 4.6343117e+00],
         [1.0005982e+00, 1.0004810e+00, 1.0005982e+00, 1.4715418e+00],
         [1.0019695e+00, 1.0006936e+00, 1.0019695e+00, 2.6879137e+00],
         [1.0003624e+00, 1.0018740e+00, 1.0003624e+00, 2.1107325e-01],
         [1.0007318e+00, 1.0003587e+00, 1.0007318e+00, 6.0730678e-01],
         [1.0022414e+00, 1.0007354e+00, 1.0022414e+00, 3.6850076e+00],
         [1.0002189e+00, 1.0022377e+00, 1.0002226e+00, 3.1635866e-01],
         [1.0000985e+00, 1.0002261e+00, 1.0000985e+00, 3.7566774e-02],
         [1.0000000e+00, 1.0000948e+00, 1.0000000e+00, 3.4551585e+00],
         [1.0000037e+00, 1.0000000e+00, 1.0000000e+00, 2.0110803e+00],
         [1.0000000e+00, 1.0000000e+00, 1.0000000e+00, 4.1560230e+00],
         [9.9999636e-01, 1.0000000e+00, 1.0000000e+00, 5.2758682e-01],
         [1.0009884e+00, 1.0000000e+00, 1.0009847e+00, 7.1787882e+00],
         [1.0004736e+00, 1.0010941e+00, 1.0004736e+00, 1.9821526e-01],
         [1.0014385e+00, 1.0003643e+00, 1.0014385e+00, 2.6534543e+00],
         [1.0000110e+00, 1.0014458e+00, 1.0000145e+00, 1.3187310e-01],
         [1.0000037e+00, 1.0000110e+00, 1.0000000e+00, 5.4083563e-02],
         [1.0000037e+00, 1.0000000e+00, 1.0000037e+00, 1.0267736e+02],
         [9.9999636e-01, 1.0000000e+00, 1.0000000e+00, 1.2240252e-01],
         [9.9883270e-01, 9.9860728e-01, 1.0000000e+00, 2.5922091e+00],
         [1.0001420e+00, 1.0003678e+00, 9.9897093e-01, 4.8789456e-02],
         [9.9811441e-01, 9.9811441e-01, 1.0000000e+00, 3.6449478e+01],
         [1.0004449e+00, 1.0004413e+00, 9.9914092e-01, 2.6223356e-01],
         [9.9755394e-01, 9.9668634e-01, 9.9941343e-01, 5.9868164e+00],
         [9.9938607e-01, 1.0000219e+00, 9.9694884e-01, 6.7625743e-01],
         [1.0026985e+00, 1.0002377e+00, 1.0026948e+00, 6.9658375e-01],
         [1.0023047e+00, 1.0030642e+00, 1.0023156e+00, 3.3709707e+00],
         [9.9980354e-01, 1.0017425e+00, 9.9979264e-01, 3.9518688e-02],
         [9.9800944e-01, 9.9800944e-01, 9.9999636e-01, 1.1397472e+01],
         [9.9951142e-01, 9.9893892e-01, 9.9800944e-01, 1.6633330e-01],
         [9.9993432e-01, 1.0005038e+00, 9.9944943e-01, 6.1848432e-01],
         [9.9934697e-01, 9.9858081e-01, 1.0000000e+00, 1.2730729e+01],
         [1.0000000e+00, 1.0000439e+00, 9.9935061e-01, 2.7382636e-01],
         [9.9964225e-01, 1.0003690e+00, 9.9998903e-01, 8.0884582e-01],
         [1.0003396e+00, 1.0003396e+00, 1.0000000e+00, 1.1051704e+00],
         [9.9856526e-01, 9.9856526e-01, 9.9988681e-01, 4.2217617e+00],
         [1.0006508e+00, 1.0003839e+00, 9.9940121e-01, 2.4998356e-01],
         [1.0007343e+00, 1.0001937e+00, 1.0006503e+00, 1.2478063e+00],
         [9.9991238e-01, 1.0007198e+00, 1.0000876e+00, 9.0076250e-01],
         [1.0006719e+00, 1.0001680e+00, 1.0004965e+00, 1.1675052e-01],
         [1.0001423e+00, 1.0003358e+00, 1.0001423e+00, 1.5750233e+00],
         [1.0000693e+00, 1.0003102e+00, 1.0000730e+00, 8.6596227e-01],
         [1.0000037e+00, 1.0000693e+00, 1.0000000e+00, 4.4483128e-01],
         [1.0000000e+00, 1.0000000e+00, 1.0000000e+00, 9.0220652e+00],
         [9.9591053e-01, 9.9591416e-01, 9.9999636e-01, 5.2908678e+00],
         [9.9952745e-01, 9.9952745e-01, 9.9625713e-01, 5.1447195e-01],
         [9.9799907e-01, 9.9791110e-01, 9.9916875e-01, 2.8284600e+00],
         [1.0000000e+00, 1.0000881e+00, 9.9801368e-01, 3.6261553e-01],
         [1.0013660e+00, 1.0003525e+00, 1.0015863e+00, 4.5040986e-01],
         [1.0020353e+00, 1.0010132e+00, 1.0018148e+00, 5.9262075e+00],
         [1.0004795e+00, 1.0018336e+00, 1.0004795e+00, 2.6766129e-02],
         [1.0000000e+00, 1.0006808e+00, 1.0000000e+00, 1.3004695e+00],
         [1.0004133e+00, 1.0001390e+00, 1.0004170e+00, 3.0653101e-01],
         [1.0000000e+00, 1.0002706e+00, 9.9999636e-01, 8.8930998e+00],
         [1.0009323e+00, 1.0000037e+00, 1.0009323e+00, 1.1688923e+00],
         [1.0008073e+00, 1.0002706e+00, 1.0008255e+00, 2.3573229e+00],
         [1.0008943e+00, 1.0014695e+00, 1.0014564e+00, 8.2072916e+00],
         [9.9835533e-01, 9.9924809e-01, 9.9942052e-01, 6.7818984e-02],
         [9.9547058e-01, 9.9547058e-01, 9.9819118e-01, 1.8739729e+01],
         [1.0011302e+00, 9.9961841e-01, 9.9737322e-01, 8.4949577e-01],
         [9.9999636e-01, 1.0007929e+00, 9.9938828e-01, 2.4047704e-02],
         [9.9964082e-01, 1.0003008e+00, 1.0000000e+00, 2.3303616e+01],
         [1.0006710e+00, 9.9926299e-01, 1.0004765e+00, 1.5378336e+00],
         [9.9894476e-01, 1.0004073e+00, 1.0001392e+00, 4.5283547e-01],
         [1.0013168e+00, 1.0013168e+00, 9.9994874e-01, 2.8568311e-02],
         [9.9961168e-01, 9.9847978e-01, 9.9999636e-01, 4.3409687e+01],
         [1.0003628e+00, 1.0002202e+00, 1.0000000e+00, 5.4002404e-01],
         [9.9915743e-01, 9.9998534e-01, 9.9964833e-01, 1.6760775e-01],
         [9.9970669e-01, 9.9973959e-01, 9.9948329e-01, 3.2992566e+00],
         [9.9944991e-01, 9.9986422e-01, 9.9965900e-01, 7.3027074e-01],
         [1.0001541e+00, 9.9957436e-01, 9.9965888e-01, 4.6144853e+00],
         [1.0013025e+00, 1.0005836e+00, 1.0013025e+00, 5.1441771e-01],
         [1.0000037e+00, 1.0012988e+00, 1.0000000e+00, 2.7368376e-01],
         [1.0000000e+00, 1.0000037e+00, 1.0000000e+00, 7.1176308e-01],
         [1.0002931e+00, 1.0000000e+00, 1.0002968e+00, 7.0013076e-01],
         [9.9833333e-01, 9.9862599e-01, 9.9999636e-01, 4.4356618e+00],
         [9.9953038e-01, 9.9953038e-01, 9.9909890e-01, 3.4925804e-01],
         [1.0011857e+00, 1.0011857e+00, 9.9994868e-01, 5.7747304e-01],
         [1.0000000e+00, 1.0000000e+00, 1.0000000e+00, 3.7471976e+00],
         [9.9962968e-01, 9.9954170e-01, 1.0000000e+00, 1.2463460e+00],
         [9.9968088e-01, 9.9976891e-01, 1.0000000e+00, 1.3109040e+00],
         [1.0000000e+00, 9.9999630e-01, 9.9931067e-01, 1.3606377e+00],
         [9.9988991e-01, 9.9989361e-01, 1.0000991e+00, 9.4597393e-01],
         [1.0007999e+00, 1.0000000e+00, 1.0005907e+00, 4.7434125e+00],
         [9.9878269e-01, 9.9958169e-01, 1.0000367e+00, 2.7460583e-02],
         [1.0000074e+00, 9.9997431e-01, 9.9875343e-01, 7.2948947e+00],
         [1.0025660e+00, 1.0000330e+00, 1.0025660e+00, 1.0637591e+00],
         [1.0020907e+00, 1.0025660e+00, 1.0020907e+00, 2.8522357e-01],
         [9.9930209e-01, 1.0013914e+00, 1.0000731e+00, 5.8429270e+00],
         [1.0002303e+00, 9.9776953e-01, 9.9980271e-01, 1.7989714e+00],
         [9.9936390e-01, 1.0018287e+00, 9.9974787e-01, 3.1775057e-01],
         [1.0000000e+00, 1.0000000e+00, 9.9927628e-01, 1.8160661e-01],
         [9.9877459e-01, 9.9871969e-01, 9.9999636e-01, 9.3605161e-01],
         [1.0013918e+00, 1.0000550e+00, 1.0002012e+00, 1.0985806e+00],
         [1.0006510e+00, 1.0017506e+00, 1.0006144e+00, 2.5814357e+00],
         [9.9984282e-01, 9.9973679e-01, 1.0000695e+00, 3.3408213e-01],
         [1.0002303e+00, 1.0006289e+00, 1.0000037e+00, 1.3414766e-01],
         [1.0000000e+00, 9.9999636e-01, 1.0000000e+00, 1.7838446e+01],
         [1.0000000e+00, 1.0000037e+00, 1.0000000e+00, 8.3536047e-01],
         [9.9928731e-01, 9.9928731e-01, 9.9999636e-01, 5.4223043e-01],
         [1.0001097e+00, 1.0001097e+00, 9.9944812e-01, 4.3785262e+00],
         [9.9854457e-01, 9.9854457e-01, 9.9995613e-01, 4.5171154e-01],
         [9.9767447e-01, 9.9722767e-01, 9.9908942e-01, 1.1091426e+01],
         [1.0000293e+00, 1.0002681e+00, 9.9715602e-01, 1.2069954e-01],
         [1.0014242e+00, 1.0000625e+00, 1.0014316e+00, 1.4433969e+00],
         [1.0015651e+00, 1.0015750e+00, 1.0015578e+00, 9.6098411e-01],
         [1.0013723e+00, 1.0018364e+00, 1.0017749e+00, 7.5566912e-01],
         [9.9895477e-01, 1.0000513e+00, 9.9959815e-01, 8.1964232e-02],
         [1.0007354e+00, 1.0006769e+00, 9.9975878e-01, 1.6638399e+00],
         [1.0012978e+00, 1.0003327e+00, 1.0013379e+00, 2.1380491e+00],
         [9.9991965e-01, 1.0008260e+00, 9.9981016e-01, 3.8806599e-01],
         [1.0004784e+00, 1.0001132e+00, 1.0004784e+00, 1.0268871e+01],
         [1.0000767e+00, 1.0004857e+00, 1.0000767e+00, 5.5289781e-01],
         [1.0000000e+00, 1.0000694e+00, 1.0000000e+00, 1.7833089e+00],
         [1.0000037e+00, 1.0000073e+00, 1.0000037e+00, 1.2945263e-02],
         [9.9963504e-01, 9.9963504e-01, 1.0000000e+00, 7.9770073e+01],
         [9.9780595e-01, 9.9780595e-01, 9.9963140e-01, 3.1662747e-01],
         [1.0003695e+00, 9.9953902e-01, 9.9871492e-01, 4.0821886e+00],
         [9.9894667e-01, 9.9893117e-01, 9.9945903e-01, 1.6124320e+00],
         [1.0015341e+00, 1.0012165e+00, 1.0005376e+00, 5.4633446e-02],
         [1.0000768e+00, 1.0012407e+00, 1.0000256e+00, 5.2312702e-01],
         [9.9902403e-01, 9.9870968e-01, 9.9999636e-01, 1.4360392e+01],
         [9.9968535e-01, 1.0000000e+00, 9.9891073e-01, 2.7689624e-01],
         [1.0003331e+00, 9.9978405e-01, 1.0001317e+00, 1.5892577e+00],
         [1.0000182e+00, 1.0005674e+00, 1.0000182e+00, 2.9608828e-01],
         [1.0000000e+00, 1.0000000e+00, 1.0000037e+00, 7.9447589e+00],
         [1.0014927e+00, 1.0000037e+00, 1.0014892e+00, 6.9757897e-01],
         [1.0001096e+00, 1.0015988e+00, 1.0001096e+00, 2.3838118e-02],
         [1.0000000e+00, 1.0000000e+00, 1.0000000e+00, 1.3727959e+00],
         [1.0000037e+00, 1.0000037e+00, 1.0000037e+00, 1.5357798e+00],
         [1.0000073e+00, 1.0000073e+00, 1.0000110e+00, 7.8537841e+00],
         [1.0000037e+00, 1.0000000e+00, 1.0000000e+00, 5.1222291e+00],
         [1.0000000e+00, 1.0000037e+00, 1.0000000e+00, 1.2102352e+00],
         [9.9941921e-01, 9.9941921e-01, 1.0000000e+00, 4.7011951e-01],
         [1.0000768e+00, 9.9971491e-01, 9.9949592e-01, 2.7753963e+00],
         [9.9968934e-01, 1.0000511e+00, 1.0000000e+00, 3.1682637e-01],
         [1.0008628e+00, 1.0006763e+00, 1.0005518e+00, 2.8207576e-01],
         [1.0000950e+00, 9.9964195e-01, 1.0000950e+00, 1.2079760e+00],
         [1.0000913e+00, 1.0006396e+00, 1.0000913e+00, 4.5529306e-01],
         [1.0000511e+00, 1.0001425e+00, 1.0002812e+00, 6.6403847e+00],
         [1.0005186e+00, 1.0002228e+00, 1.0003577e+00, 4.8837531e-01],
         [1.0001971e+00, 1.0000037e+00, 1.0001278e+00, 4.6924916e-01],
         [9.9998540e-01, 1.0000839e+00, 9.9998540e-01, 2.6365486e-01],
         [1.0000694e+00, 1.0002774e+00, 1.0000694e+00, 1.1816318e+00],
         [9.9990511e-01, 1.0000876e+00, 1.0004160e+00, 1.9651167e+01],
         [9.9966425e-01, 9.9963504e-01, 9.9948573e-01, 2.1069668e-01],
         [9.9996716e-01, 9.9999636e-01, 9.9967158e-01, 6.9688112e-01],
         [9.9978459e-01, 9.9978459e-01, 1.0000767e+00, 1.4935952e-01],
         [1.0001241e+00, 1.0001241e+00, 1.0000110e+00, 1.2045263e+01],
         [1.0001862e+00, 9.9979192e-01, 9.9997079e-01, 1.1947027e+00],
         [1.0000876e+00, 1.0003579e+00, 1.0000876e+00, 1.1323529e+00],
         [9.9993795e-01, 1.0000621e+00, 1.0003796e+00, 1.4615406e+00],
         [1.0008469e+00, 9.9994892e-01, 1.0004050e+00, 1.5914217e+00],
         [9.9965715e-01, 1.0005549e+00, 9.9995989e-01, 2.4419294e-01],
         [1.0004014e+00, 1.0000949e+00, 1.0000985e+00, 6.6721039e+00],
         [9.9982858e-01, 1.0000620e+00, 9.9986869e-01, 2.6552710e-01],
         [1.0001714e+00, 1.0000730e+00, 1.0001312e+00, 1.0065858e-01],
         [1.0000000e+00, 1.0001678e+00, 1.0000000e+00, 2.8208659e+00],
         [1.0004340e+00, 1.0000693e+00, 1.0004340e+00, 9.4247788e-01],
         [1.0003937e+00, 1.0003684e+00, 1.0003937e+00, 3.0226307e+00],
         [1.0004227e+00, 1.0003937e+00, 1.0004227e+00, 3.3974197e+00],
         [1.0006338e+00, 1.0004227e+00, 1.0006338e+00, 1.2969593e+00],
         [1.0002985e+00, 1.0006374e+00, 1.0002985e+00, 1.5663968e-01],
         [1.0000000e+00, 1.0002912e+00, 1.0000000e+00, 1.0392715e+00],
         [1.0007278e+00, 1.0000037e+00, 1.0007278e+00, 2.0675045e+01],
         [1.0000000e+00, 1.0007242e+00, 1.0000000e+00, 6.4647868e-02],
         [1.0000000e+00, 1.0000037e+00, 1.0000000e+00, 9.3014984e+00],
         [1.0000000e+00, 1.0000000e+00, 1.0000000e+00, 2.1045491e-01],
         [1.0000000e+00, 9.9999636e-01, 1.0000000e+00, 1.6283804e+00],
         [1.0000000e+00, 1.0000037e+00, 1.0000000e+00, 1.9846686e+00],
         [1.0004218e+00, 1.0000000e+00, 1.0004218e+00, 2.8680152e-01]]
state = np.zeros((20, 4))
state = np.random.randint(1,5,size=(20,4))
state[0:5, :] = 1

split_size, window_size, history_length, num_channels = (2, 10, 20, 4)
batch_size = 1
s_t = tf.placeholder(dtype=tf.float32, shape=[None, history_length, num_channels])
reshape = tf.reshape(s_t, shape=[batch_size, split_size, window_size, num_channels])
kernel_size = 2
filter_size = 3 # 滤波器数量，1输出1列数据，n输出n列数据
conv2d = tf.layers.conv2d(inputs=reshape, filters=filter_size,
                          kernel_size=[1, kernel_size], strides=(1, 1),
                          padding='valid', activation=None)
'''列卷积'''
normal = tf.layers.batch_normalization(inputs=reshape, training=True, scale=True)
'''对一列数据做正规化，独立计算列，如果一列数据都相同，此列输出0'''

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    result = sess.run(fetches=s_t, feed_dict={s_t: [state]})
    print(result)
    result = sess.run(fetches=conv2d, feed_dict={s_t: [state]})
    print(result)
