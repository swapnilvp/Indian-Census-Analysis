# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 08:52:54 2018

@author: USER
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'figliteracy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1396, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-36, -10, 1421, 821))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/sddsf.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, -20, 1331, 821))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../Users/USER/literacy.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1050, 530, 231, 81))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1140, 370, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 670, 1291, 121))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 26))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">DARKER COLOUR REPRESENT HIGHER</span></p><p><span style=\" font-size:7pt;\">LITERCY RATE AND THE OTHER</span></p><p><span style=\" font-size:7pt;\"> VISE VERSA</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>PERCENTAGE</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "\n"
"States like Bihar, Arunachal Pradesh, Jharkhand, Rajasthan and Jammu Kashmir have low literacy rates. This can be also verified by the map of India visualized for literacy rates above as well.\n"
"One important thing to note here is this:\n"
"\n"
"Literacy is defined as the ability to read, write and use arithmetic, for people having age more than 7 years.\n"
"\n"
"In our calculations, we have also counted children aged from 0-6 years in total population. The correct way to calculate it would be to subtract child population from total population and then compute the percentage.\n"
"\n"
"Because there is no related column in our data which states no. of children(age 0-6), are results are slightly lesser than the actual literacy rates, but the overall visualization for the above heatmap seems reasonable and is relatable with the actual data."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
