# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_h1(object):
    def setupUi(self, h1):
        h1.setObjectName("h1")
        h1.resize(1040, 700)
        h1.setStyleSheet("border-image: url(:/newPrefix/login.jpg);")
        self.pushButton = QtWidgets.QPushButton(h1)
        self.pushButton.setGeometry(QtCore.QRect(410, 520, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(h1)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 521, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(h1)
        self.lineEdit.setGeometry(QtCore.QRect(510, 400, 181, 41))
        self.lineEdit.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(h1)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 460, 181, 41))
        self.lineEdit_2.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(h1)
        self.label.setGeometry(QtCore.QRect(410, 399, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(h1)
        self.label_2.setGeometry(QtCore.QRect(410, 459, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(h1)
        self.pushButton.clicked.connect(h1.go_1)
        self.pushButton_2.clicked.connect(h1.go)
        QtCore.QMetaObject.connectSlotsByName(h1)

    def retranslateUi(self, h1):
        _translate = QtCore.QCoreApplication.translate
        h1.setWindowTitle(_translate("h1", "Dialog"))
        self.pushButton.setText(_translate("h1", "登录"))
        self.pushButton_2.setText(_translate("h1", "注册"))
        self.label.setText(_translate("h1", "账号"))
        self.label_2.setText(_translate("h1", "密码"))
import aaa_rc
