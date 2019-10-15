# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_h2(object):
    def setupUi(self, h2):
        h2.setObjectName("h2")
        h2.resize(1400, 700)
        h2.setStyleSheet("border-image: url(:/newPrefix/backgroung.jpg);")
        self.pushButton = QtWidgets.QPushButton(h2)
        self.pushButton.setGeometry(QtCore.QRect(640, 370, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(h2)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 450, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(h2)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 530, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(h2)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 620, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(h2)
        self.pushButton.clicked.connect(h2.go_2)
        self.pushButton_2.clicked.connect(h2.go_3)
        self.pushButton_3.clicked.connect(h2.go_4)
        self.pushButton_4.clicked.connect(h2.close)
        self.pushButton_4.clicked.connect(h2.logout)
        QtCore.QMetaObject.connectSlotsByName(h2)

    def retranslateUi(self, h2):
        _translate = QtCore.QCoreApplication.translate
        h2.setWindowTitle(_translate("h2", "Dialog"))
        self.pushButton.setText(_translate("h2", "开始游戏"))
        self.pushButton_2.setText(_translate("h2", "历史对局"))
        self.pushButton_3.setText(_translate("h2", "排行榜"))
        self.pushButton_4.setText(_translate("h2", "退出游戏"))
import aaa_rc
