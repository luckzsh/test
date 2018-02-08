import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtQuickWidgets
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtWidgets import QApplication, QWidget

def on_button_clicked():
    printer = QPrinter(QPrinter.HiResolution)
    previe = QPrintPreviewDialog(printer, )
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 300)
    w.move(300, 300)
    w.setWindowTitle('First PyQt5')
	
    tab = QtWidgets.QTabWidget()
    tab.addTab(QtWidgets.QLabel("Tab content 1"), "Tab &1")
    tab.setCurrentIndex(0)
    button = QPushButton("打印")
    button.clicked.connect(on_button_clicked)
    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(tab)
    vbox.addWidget(button)
    
    w.setLayout(vbox)
    
    
    w.show()
    
    img = QtGui.QGuiApplication.primaryScreen().grabWindow(0)
    img.save("img.png", "png")
    sys.exit(app.exec_())


    
