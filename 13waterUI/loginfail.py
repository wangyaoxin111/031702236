# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginfail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_m3(object):
    def setupUi(self, m3):
        m3.setObjectName("m3")
        m3.resize(250, 250)
        m3.setStyleSheet("QDialog#m3\n"
"{\n"
"border-image: url(:/newPrefix/sad.jpg);\n"
"}")
        self.label = QtWidgets.QLabel(m3)
        self.label.setGeometry(QtCore.QRect(80, 208, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(m3)
        QtCore.QMetaObject.connectSlotsByName(m3)

    def retranslateUi(self, m3):
        _translate = QtCore.QCoreApplication.translate
        m3.setWindowTitle(_translate("m3", "Dialog"))
        self.label.setText(_translate("m3", "登录失败"))
import aaa_rc
