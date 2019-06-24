# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 08:55:45 2018

@author: USER
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'figpopulation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow6(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1416, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, -10, 1431, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/fd.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 1361, 811))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../Users/USER/population.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1160, 370, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1080, 550, 231, 81))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 690, 1001, 91))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1416, 26))
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
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>PERCENTAGE</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">DARKER COLOUR REPRESENT HIGHER</span></p><p><span style=\" font-size:7pt;\">POPULATION DENSITY AND THE OTHER</span></p><p><span style=\" font-size:7pt;\">VISE VERSA</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>THE ABOVE GRAPH REPRESENTS POPULATION DENSITY ACROSS THE CONTRY IN DIFFERENT STATES.</p><p>THE DATA CAN BE USED BY GOVERMENT DEPARTMENTS TO TAKE DECISIONS ACCORDING TO THE</p><p> ANALYSIS WHICH COULD ALSO BE A GREATE HELP TO POLITICAL PARTIES TO ANALYSIS THE POPULATION AND MAKE THEIR STRATEGIES ACCORDINGLY</p><p><br/></p><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow6()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())