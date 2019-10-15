# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_h(object):
    def setupUi(self, h):
        h.setObjectName("h")
        h.resize(1040, 700)
        h.setStyleSheet("border-image: url(:/newPrefix/login.jpg);")
        self.label = QtWidgets.QLabel(h)
        self.label.setGeometry(QtCore.QRect(370, 392, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(h)
        self.label_2.setGeometry(QtCore.QRect(370, 483, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(h)
        self.lineEdit.setGeometry(QtCore.QRect(510, 393, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(h)
        self.lineEdit_2.setGeometry(QtCore.QRect(512, 483, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(h)
        self.pushButton.setGeometry(QtCore.QRect(470, 550, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(h)
        self.pushButton.clicked.connect(h.read)
        QtCore.QMetaObject.connectSlotsByName(h)

    def retranslateUi(self, h):
        _translate = QtCore.QCoreApplication.translate
        h.setWindowTitle(_translate("h", "Dialog"))
        self.label.setText(_translate("h", "用户名"))
        self.label_2.setText(_translate("h", "密码"))
        self.pushButton.setText(_translate("h", "注册"))
import aaa_rc
