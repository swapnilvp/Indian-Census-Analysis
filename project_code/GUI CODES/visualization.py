# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 05:09:30 2018

@author: USER
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualization8.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from img import Ui_MainWindow3
from figage import Ui_MainWindow4
from figliteracy import Ui_MainWindow5
from figpopulation import Ui_MainWindow6
from figagriculture import Ui_MainWindow7
from figcng import Ui_MainWindow8
from figreligion import Ui_MainWindow9
from figrural import Ui_MainWindow10
from figsexratio1 import Ui_MainWindow11

class Ui_MainWindow2(object):

    def img1(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow3()
         self.ui.setupUi(self.window)
         self.window.show()

    def img2(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow4()
         self.ui.setupUi(self.window)
         self.window.show()

    def img3(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow5()
         self.ui.setupUi(self.window)
         self.window.show()

    def img4(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow6()
         self.ui.setupUi(self.window)
         self.window.show()

    def img5(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow7()
         self.ui.setupUi(self.window)
         self.window.show()

    def img6(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow8()
         self.ui.setupUi(self.window)
         self.window.show()

    def img7(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow9()
         self.ui.setupUi(self.window)
         self.window.show()

    def img8(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow10()
         self.ui.setupUi(self.window)
         self.window.show()

    def img9(self):
         self.window=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow11()
         self.ui.setupUi(self.window)
         self.window.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 1051, 771))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/fd.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, -10, 1041, 781))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/fd.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 20, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Castellar")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 121, 51))
        self.label_4.setObjectName("label_4")
        self.literacy = QtWidgets.QPushButton(self.centralwidget)
        self.literacy.setGeometry(QtCore.QRect(100, 200, 121, 31))
        self.literacy.setObjectName("literacy")

        self.literacy.clicked.connect(self.open1)
        self.literacy.clicked.connect(self.img3)

        self.population = QtWidgets.QPushButton(self.centralwidget)
        self.population.setGeometry(QtCore.QRect(100, 240, 121, 31))
        self.population.setObjectName("population")

        self.population.clicked.connect(self.open6)
        self.population.clicked.connect(self.img4)

        self.agriculture = QtWidgets.QPushButton(self.centralwidget)
        self.agriculture.setGeometry(QtCore.QRect(100, 280, 121, 31))
        self.agriculture.setObjectName("agriculture")

        self.agriculture.clicked.connect(self.open2)
        self.agriculture.clicked.connect(self.img5)

        self.lpg = QtWidgets.QPushButton(self.centralwidget)
        self.lpg.setGeometry(QtCore.QRect(100, 320, 121, 31))
        self.lpg.setObjectName("lpg")

        self.lpg.clicked.connect(self.open4)
        self.lpg.clicked.connect(self.img6)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 55, 41))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_6.setGeometry(QtCore.QRect(40, 230, 55, 41))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 310, 55, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 270, 55, 41))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 140, 231, 51))
        self.label_7.setObjectName("label_7")
        self.religion = QtWidgets.QPushButton(self.centralwidget)
        self.religion.setGeometry(QtCore.QRect(440, 200, 121, 31))
        self.religion.setObjectName("religion")

        self.religion.clicked.connect(self.open7)
        self.religion.clicked.connect(self.img7)

        self.agegroup = QtWidgets.QPushButton(self.centralwidget)
        self.agegroup.setGeometry(QtCore.QRect(440, 250, 121, 31))
        self.agegroup.setObjectName("agegroup")

        self.agegroup.clicked.connect(self.open9)
        self.agegroup.clicked.connect(self.img2)

        self.castegroup = QtWidgets.QPushButton(self.centralwidget)
        self.castegroup.setGeometry(QtCore.QRect(440, 300, 121, 31))
        self.castegroup.setObjectName("castegroup")

        self.castegroup.clicked.connect(self.open3)
        self.castegroup.clicked.connect(self.img1)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 240, 55, 41))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(700, 190, 55, 41))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(380, 290, 55, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(380, 240, 55, 41))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(380, 190, 55, 41))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(710, 140, 231, 51))
        self.label_15.setObjectName("label_15")
        self.rural = QtWidgets.QPushButton(self.centralwidget)
        self.rural.setGeometry(QtCore.QRect(760, 250, 151, 31))
        self.rural.setObjectName("rural")

        self.rural.clicked.connect(self.open8)
        self.rural.clicked.connect(self.img8)
        self.sexratio = QtWidgets.QPushButton(self.centralwidget)
        self.sexratio.setGeometry(QtCore.QRect(760, 200, 151, 31))
        self.sexratio.setObjectName("sexratio")

        self.sexratio.clicked.connect(self.open5)
        self.sexratio.clicked.connect(self.img9)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(650, 480, 55, 16))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(750, 20, 161, 111))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/jshdkj.jpg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 490, 971, 241))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("../../../../../Users/USER/Downloads/ThinkstockPhotos-472589250.jpg"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 26))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Visualization</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#00ffff;\">Maps</span></p></body></html>"))
        self.literacy.setText(_translate("MainWindow", "Literacy Rate"))
        self.population.setText(_translate("MainWindow", "Population Density"))
        self.agriculture.setText(_translate("MainWindow", "Agriculture Workers"))
        self.lpg.setText(_translate("MainWindow", "CNG Gas connections"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">----&gt;</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">----&gt;</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">----&gt;</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#aaffff;\">----&gt;</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#00ffff;\">Pie Charts</span></p></body></html>"))
        self.religion.setText(_translate("MainWindow", "Religions"))
        self.agegroup.setText(_translate("MainWindow", "Age Groups"))
        self.castegroup.setText(_translate("MainWindow", "Education Groups"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">----&gt;</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">----&gt;</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">----&gt;</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">----&gt;</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ffff;\">----&gt;</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#00ffff;\">Bar Graphs</span></p></body></html>"))
        self.rural.setText(_translate("MainWindow", "Rural and Urban House"))
        self.sexratio.setText(_translate("MainWindow", "Sex Ratio"))



    def open1(self):
        import mainPro as mp
        mp.openwindow()

    def open2(self):
        import agriculture as ag
        ag.openwindow1()

    def open3(self):
        import educationgroup as ed
        ed.openwindow2()

    def open4(self):
        import cng as cn
        cn.openwindow3()

    def open5(self):
        import sexratio as sr
        sr.openwindow4()

    def open6(self):
        import population as pp
        pp.openwindow5()

    def open7(self):
        import Religions as re
        re.openwindow6()


    def open8(self):
        import rural as rl
        rl.openwindow7()

    def open9(self):
        import age as ae
        ae.openwindow8()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
