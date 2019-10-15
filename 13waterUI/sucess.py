# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sucess.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_m2(object):
    def setupUi(self, m2):
        m2.setObjectName("m2")
        m2.resize(250, 250)
        m2.setStyleSheet("QDialog#m2\n"
"{\n"
"image: url(:/newPrefix/smile.jpg);\n"
"}")
        self.label = QtWidgets.QLabel(m2)
        self.label.setGeometry(QtCore.QRect(80, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(m2)
        QtCore.QMetaObject.connectSlotsByName(m2)

    def retranslateUi(self, m2):
        _translate = QtCore.QCoreApplication.translate
        m2.setWindowTitle(_translate("m2", "Dialog"))
        self.label.setText(_translate("m2", "注册成功"))
import aaa_rc
