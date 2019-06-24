# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 07:00:22 2018

@author: USER
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from visualization import Ui_MainWindow2
from data3 import Ui_MainWindow15

class Ui_MainWindow(object):

    def OtherWindow(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow2()
         self.ui.setupUi(self.window)
         self.window.show()

    def OtherWindow1(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow15()
         self.ui.setupUi(self.window)
         self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 832)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(324, 40, 191, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 210, 55, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.MainWindow_2 = QtWidgets.QLabel(self.centralwidget)
        self.MainWindow_2.setGeometry(QtCore.QRect(30, -20, 1101, 781))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MainWindow_2.setFont(font)
        self.MainWindow_2.setText("")
        self.MainWindow_2.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/img1.jpg"))
        self.MainWindow_2.setScaledContents(True)
        self.MainWindow_2.setObjectName("MainWindow_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, -10, 771, 141))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 130, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Century")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
       # self.introduction = QtWidgets.QPushButton(self.centralwidget)
        #self.introduction.setGeometry(QtCore.QRect(80, 250, 141, 31))
        #font = QtGui.QFont()
        #font.setPointSize(11)
        #self.introduction.setFont(font)
        #self.introduction.setObjectName("introduction")
        self.visualization = QtWidgets.QPushButton(self.centralwidget)
        self.visualization.setGeometry(QtCore.QRect(80, 320, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.visualization.setFont(font)
        self.visualization.setObjectName("visualization")
        self.visualization.clicked.connect(self.OtherWindow)
        self.data = QtWidgets.QPushButton(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(80, 390, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.data.setFont(font)
        self.data.setObjectName("data")

        self.data.clicked.connect(self.OtherWindow1)


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 610, 541, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/crowd-drawing-cartoon-1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.MainWindow_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        #self.introduction.raise_()
        self.visualization.raise_()
        self.data.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">WELCOME TO DATA ANALYSIS PROJECT</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffff00;\">Please Select The Following Options</span></p></body></html>"))
       # self.introduction.setText(_translate("MainWindow", "Introduction"))
        self.visualization.setText(_translate("MainWindow", "Visualization"))
        self.data.setText(_translate("MainWindow", "Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())