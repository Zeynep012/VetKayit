# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Zeynep/Desktop/projeVet_calisma/AB/sifre_degistir.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 241)
        Form.setMinimumSize(QtCore.QSize(500, 241))
        Form.setMaximumSize(QtCore.QSize(500, 241))
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        Form.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.005, y1:0, x2:1, y2:0.636, stop:0.621891 rgba(0, 0, 0, 255), stop:1 rgba(38, 152, 159, 255));")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(100, 30))
        self.label.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.girdi_eski_sifre = QtWidgets.QLineEdit(Form)
        self.girdi_eski_sifre.setMinimumSize(QtCore.QSize(210, 30))
        self.girdi_eski_sifre.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.girdi_eski_sifre.setFont(font)
        self.girdi_eski_sifre.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.girdi_eski_sifre.setFrame(False)
        self.girdi_eski_sifre.setClearButtonEnabled(True)
        self.girdi_eski_sifre.setObjectName("girdi_eski_sifre")
        self.gridLayout.addWidget(self.girdi_eski_sifre, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(100, 30))
        self.label_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.girdi_yeni_sifre = QtWidgets.QLineEdit(Form)
        self.girdi_yeni_sifre.setMinimumSize(QtCore.QSize(210, 30))
        self.girdi_yeni_sifre.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.girdi_yeni_sifre.setFont(font)
        self.girdi_yeni_sifre.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.girdi_yeni_sifre.setFrame(False)
        self.girdi_yeni_sifre.setClearButtonEnabled(True)
        self.girdi_yeni_sifre.setObjectName("girdi_yeni_sifre")
        self.gridLayout.addWidget(self.girdi_yeni_sifre, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buton_iptal = QtWidgets.QPushButton(Form)
        self.buton_iptal.setMinimumSize(QtCore.QSize(100, 55))
        self.buton_iptal.setMaximumSize(QtCore.QSize(100, 55))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buton_iptal.setFont(font)
        self.buton_iptal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_iptal.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.buton_iptal.setObjectName("buton_iptal")
        self.horizontalLayout.addWidget(self.buton_iptal)
        self.buton_sifre_degistir = QtWidgets.QPushButton(Form)
        self.buton_sifre_degistir.setMinimumSize(QtCore.QSize(180, 55))
        self.buton_sifre_degistir.setMaximumSize(QtCore.QSize(180, 55))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buton_sifre_degistir.setFont(font)
        self.buton_sifre_degistir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_sifre_degistir.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.buton_sifre_degistir.setObjectName("buton_sifre_degistir")
        self.horizontalLayout.addWidget(self.buton_sifre_degistir)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Eski Şifre:"))
        self.girdi_eski_sifre.setPlaceholderText(_translate("Form", "Yoksa boş bırakınız!"))
        self.label_2.setText(_translate("Form", "Yeni Şifre"))
        self.buton_iptal.setText(_translate("Form", "İPTAL"))
        self.buton_sifre_degistir.setText(_translate("Form", "Şifre Değiştir"))
