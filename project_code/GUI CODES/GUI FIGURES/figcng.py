# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:00:43 2018

@author: USER
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'figcng.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow8(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-36, -50, 1221, 911))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/gfh.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(14, 40, 1011, 731))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../Users/USER/cng.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(780, 550, 231, 81))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(860, 390, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 670, 641, 71))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 26))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">DARKER COLOUR REPRESENT HIGHER</span></p><p><span style=\" font-size:7pt;\">PERCENTAGE OF CNG GAS CONNECTION</span></p><p><span style=\" font-size:7pt;\"> AND THE OTHER VISE VERSA</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>PERCENTAGE</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>THE ABOVE MAP CAN BE USED BY VARIOUS GOVERMENT DEPARTMENTS AND PRIVATE COMPANIES TO</p><p> ANALYSIS CNG GAS CONNECTION ACROSS THE COUNTRY AND TAKE FOLLOWING MEASURES</p><p> ACCORDINGLY i.e WHICH STATE HAS MORE NEED OF CNG GAS CONNECTION. </p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow8()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
