# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:02:54 2018

@author: USER
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'figreligion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow9(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1141, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/gfh.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 591, 501))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../Users/USER/religions.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 30, 351, 311))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 26))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">HINDUS == 80.5 DATA=</span><span style=\" font-family:\'monospace\'; font-size:11pt; color:#000000; background-color:#ffffff;\">966257353</span></p><p><span style=\" font-size:11pt; color:#000000;\">MUSLIMS == 14.4 DATA=</span><span style=\" font-family:\'monospace\'; font-size:11pt; color:#000000; background-color:#ffffff;\">172245158</span></p><p><span style=\" font-size:11pt; color:#000000;\">SIKHS == 1.7 DATA=</span><span style=\" font-family:\'monospace\'; font-size:11pt; color:#000000; background-color:#ffffff;\">20833116</span></p><p><span style=\" font-size:11pt; color:#000000;\">BUDDHISTS == 0.7 DATA=</span><span style=\" font-family:\'monospace\'; font-size:11pt; color:#000000; background-color:#ffffff;\">8442972</span></p><p><span style=\" font-size:11pt; color:#000000;\">CHRISTANS == 2.3 DATA=</span><span style=\" font-family:\'monospace\'; font-size:11pt; color:#000000; background-color:#ffffff;\">27819588</span></p><p><span style=\" font-size:11pt; color:#000000;\">JAINS == 0.4 DATA=</span><span style=\" font-family:\'monospace\'; font-size:11pt; color:#000000; background-color:#ffffff;\">4451753</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow9()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())