# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:14:46 2018

@author: USER
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from figuser import Ui_MainWindow16
from txtoutput import Ui_MainWindow17

class Ui_MainWindow15(object):

     def otherwindow(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow16()
         self.ui.setupUi(self.window)
         self.window.show()

     def otherwindow1(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow17()
         self.ui.setupUi(self.window)
         self.window.show()



     def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1405, 843)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 60, 55, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 1031, 781))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/gfh.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 50, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 270, 181, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 210, 341, 231))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/gj.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-200, 170, 751, 91))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 140, 791, 61))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 260, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox.currentIndexChanged.connect(self.open1)
        self.pushButton.clicked.connect(self.otherwindow1)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 310, 551, 101))
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 430, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")



        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(240, 430, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")




        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(570, 30, 171, 101))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/download.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(80, 480, 861, 291))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/fsdf.jpeg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 430, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.comboBox_2.currentIndexChanged.connect(self.open2)
        self.comboBox_3.currentIndexChanged.connect(self.open2)
        self.pushButton_2.clicked.connect(self.otherwindow)


        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.label_8.raise_()
        self.comboBox_2.raise_()
        self.comboBox_3.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1405, 26))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">DATA</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffff00;\">Please Select The State </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">Following provides amount of numerical data on Different States of India</span></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Uttar Pradesh"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Maharastra"))
        self.comboBox.setItemText(2, _translate("MainWindow", "West Bengal"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Bihar"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Andhra Pradesh"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Madhya Pradesh"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Tamil Nadu"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Rajasthan"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Karnataka"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Gujarat"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Orissa"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Kerala"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Jharkhand"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Assam"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Punjab"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Chhattisgarh"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Haryana"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Delhi"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Jammu and Kashmir"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Uttarakhand"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Himachal Pradesh"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Tripura"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Meghalaya"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Manipur"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Nagaland"))
        self.comboBox.setItemText(25, _translate("MainWindow", "Goa"))
        self.comboBox.setItemText(26, _translate("MainWindow", "Arunachal Pradesh"))
        self.comboBox.setItemText(27, _translate("MainWindow", "Puducherry"))
        self.comboBox.setItemText(28, _translate("MainWindow", "Mizoram"))
        self.comboBox.setItemText(29, _translate("MainWindow", "Chandigarh"))
        self.comboBox.setItemText(30, _translate("MainWindow", "Sikkim"))
        self.comboBox.setItemText(31, _translate("MainWindow", "Andaman and Nicobar Islands"))
        self.comboBox.setItemText(32, _translate("MainWindow", "Dadra and Nagar Haveli"))
        self.comboBox.setItemText(33, _translate("MainWindow", "Daman and Diu"))
        self.comboBox.setItemText(34, _translate("MainWindow", "Lakshadweep"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffff00;\">Please Select The Two Parameters Which You Need </span></p><p><span style=\" font-size:14pt; color:#ffff00;\"> To Compare State Wise</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "rural_house"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "urban_house"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "male literacy"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "female literacy"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Hindus"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Muslims"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "workers"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "non workers"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Population"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Male Population"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "christans"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "sikhs"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "buddhisits"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "jains"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "agriculture workers"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "household workers"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "literate"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "illiterate"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "rural_house"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "urban_house"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "male literacy"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "female literacy"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Hindus"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "New Item"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Muslims"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "workers"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "non workers"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "Population"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Male Population"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "christans"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "sikhs"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "buddhisits"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "jains"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "agriculture workers"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "household workers"))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "literate"))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "illiterate"))
        self.pushButton_2.setText(_translate("MainWindow", "Enter"))



     def open1(self):
        state=self.comboBox.currentText()
        import user1 as us1
        us1.openwindow(state)

     def open2(self):
        statename1=self.comboBox_2.currentText()
        statename2=self.comboBox_3.currentText()
        import userbar as br
        br.openwindow(statename1,statename2)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow15()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
