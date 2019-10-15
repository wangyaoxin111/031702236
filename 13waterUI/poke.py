# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poke.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_h3(object):
    def setupUi(self, h3):
        h3.setObjectName("h3")
        h3.resize(1400, 700)
        h3.setStyleSheet("border-image: url(:/newPrefix/backgroung.jpg);")
        self.pushButton = QtWidgets.QPushButton(h3)
        self.pushButton.setGeometry(QtCore.QRect(635, 599, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(h3)
        self.listView.setGeometry(QtCore.QRect(260, 260, 181, 301))
        self.listView.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(h3)
        self.listView_2.setGeometry(QtCore.QRect(600, 260, 181, 301))
        self.listView_2.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(h3)
        self.listView_3.setGeometry(QtCore.QRect(970, 260, 181, 301))
        self.listView_3.setStyleSheet("image: url(:/newPrefix/white.jpg);\n"
"border-image: url(:/newPrefix/white.jpg);")
        self.listView_3.setObjectName("listView_3")
        self.label = QtWidgets.QLabel(h3)
        self.label.setGeometry(QtCore.QRect(260, 140, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(h3)
        self.label_2.setGeometry(QtCore.QRect(600, 140, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(h3)
        self.label_3.setGeometry(QtCore.QRect(970, 140, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image: url(:/newPrefix/white.jpg);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(h3)
        QtCore.QMetaObject.connectSlotsByName(h3)

    def retranslateUi(self, h3):
        _translate = QtCore.QCoreApplication.translate
        h3.setWindowTitle(_translate("h3", "Dialog"))
        self.pushButton.setText(_translate("h3", "出牌"))
        self.label.setText(_translate("h3", "前墩"))
        self.label_2.setText(_translate("h3", "中墩"))
        self.label_3.setText(_translate("h3", "后墩"))
import aaa_rc
