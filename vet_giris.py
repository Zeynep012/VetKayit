
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(957, 599)
        Form.setMinimumSize(QtCore.QSize(957, 599))
        Form.setMaximumSize(QtCore.QSize(957, 599))
        Form.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.005, y1:0, x2:1, y2:0.636, stop:0.621891 rgba(0, 0, 0, 255), stop:1 rgba(38, 152, 159, 255));")
        self.girdi_vet_sifre = QtWidgets.QLineEdit(Form)
        self.girdi_vet_sifre.setGeometry(QtCore.QRect(320, 220, 350, 50))
        self.girdi_vet_sifre.setMinimumSize(QtCore.QSize(350, 50))
        self.girdi_vet_sifre.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.girdi_vet_sifre.setFont(font)
        self.girdi_vet_sifre.setMouseTracking(False)
        self.girdi_vet_sifre.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.girdi_vet_sifre.setFrame(False)
        self.girdi_vet_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.girdi_vet_sifre.setClearButtonEnabled(True)
        self.girdi_vet_sifre.setObjectName("girdi_vet_sifre")
        self.buton_gir_vet = QtWidgets.QPushButton(Form)
        self.buton_gir_vet.setGeometry(QtCore.QRect(400, 350, 180, 55))
        self.buton_gir_vet.setMinimumSize(QtCore.QSize(180, 55))
        self.buton_gir_vet.setMaximumSize(QtCore.QSize(180, 55))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buton_gir_vet.setFont(font)
        self.buton_gir_vet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton_gir_vet.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.buton_gir_vet.setObjectName("buton_gir_vet")
        self.buton_geri = QtWidgets.QPushButton(Form)
        self.buton_geri.setGeometry(QtCore.QRect(30, 510, 60, 55))
        self.buton_geri.setMinimumSize(QtCore.QSize(60, 55))
        self.buton_geri.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buton_geri.setFont(font)
        self.buton_geri.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"color: rgb(247, 246, 246);")
        self.buton_geri.setObjectName("buton_geri")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.girdi_vet_sifre.setPlaceholderText(_translate("Form", "Veteriner girişi için şifrenizi giriniz"))
        self.buton_gir_vet.setText(_translate("Form", "GİRİŞ"))
        self.buton_geri.setText(_translate("Form", "<-"))

