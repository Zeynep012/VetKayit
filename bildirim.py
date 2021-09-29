from PyQt5.QtWidgets import QMessageBox
def mesaj_kutusu(baslik,mesaj):
	kutu = QMessageBox()
	kutu.setWindowTitle(baslik)
	kutu.setText(mesaj)
	kutu.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
	buttonY = kutu.button(QMessageBox.Yes)
	buttonY.setText('Evet')
	buttonN = kutu.button(QMessageBox.No)
	buttonN.setText('Iptal')
	kutu.exec_()
def uyari_kutusu(uyari_mesaji):
	uyari_kutu = QMessageBox()
	uyari_kutu.setWindowTitle("UYARI")
	uyari_kutu.setText(uyari_mesaji)
	uyari_kutu.exec_()