import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from giris_sayfasi_arayuz import Ui_MainWindow as baglan_giris
from sifre_degistir_arayuz import Ui_Form as sifre_degisim
from kullanici_isim_degistir_arayuz import Ui_Form as isim_degisim_arayuz
from gecis_sayfasi_arayuz import Ui_MainWindow as gecis
from vet_arayuz import Ui_MainWindow as vet_arayuz
from vet_giris import Ui_Form as vet_giris
import mainB as coban
import mainA as vet
import sifreleme
import bildirim

class gecis_sayfasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baglantilar()
    def geri_cbn(self):
        cb.close()
        gc.show()
    def giris_coban(self):
        gc.close()
        cb.show()
        cb.buton_geri.clicked.connect(self.geri_cbn)
        cb.action_sifre_degistir.triggered.connect(lambda: sifre_degisimi("sifre"))
        cb.actionKullan_c_Ad_De_i_tir.triggered.connect(isim_degisim)
    def geri_vt_giris(self):
        vt_s.girdi_vet_sifre.setText("")
        vt_s_pencere.close()
        gc.show()
    def geri_vt(self):
        vt.temizle_tablo()
        vt.close()
        gc.show()
    def guvenlik_vet(self):
        girilen_vet_sifre = vt_s.girdi_vet_sifre.text()
        if sifreleme.guvenlik_dosya_yaz(girilen_vet_sifre,"sifre_vet") == 1:
            vt_s.girdi_vet_sifre.setText("")
            vt_s_pencere.close()
            vt.show()
            vt.buton_geri.clicked.connect(self.geri_vt)
            vt.actionVetSifreDegisim.triggered.connect(lambda: sifre_degisimi("sifre_vet"))
        else:
            bildirim.uyari_kutusu("Şifrenizi yanlış girdiniz.Lütfen tekrar giriniz!")

    def giris_vet(self):
        gc.close()
        vt_s_pencere.show()
        vt_s.buton_geri.clicked.connect(self.geri_vt_giris)
        vt_s.buton_gir_vet.clicked.connect(self.guvenlik_vet)     

    def baglantilar(self):
        gecis_pencere = gecis()
        gecis_pencere.setupUi(self)
        gecis_pencere.buton_coban.clicked.connect(self.giris_coban)
        gecis_pencere.buton_vet.clicked.connect(self.giris_vet)
        gecis_pencere.action_sifre_degistir.triggered.connect(lambda: sifre_degisimi("sifre"))
        gecis_pencere.action_isim_degistir.triggered.connect(isim_degisim)
        
class giris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sayfa_giris()
    def guvenlik(self):
        girilen_sifre = self.ui.girdi_sifre.text()
        girilen_kullanici_ismi = self.ui.girdi_kullanici_isim.text()
        if sifreleme.guvenlik_dosya_yaz(girilen_sifre,"sifre") & sifreleme.guvenlik_dosya_yaz(girilen_kullanici_ismi, "isim") == 1 :
            pencere_giris.close()
            gc.show()
        else:
            bildirim.uyari_kutusu("Şifrenizi veya kullanıcı adınızı yanlış girdiniz.Lütfen tekrar giriniz!")
    def sayfa_giris(self):
        self.ui = baglan_giris()
        self.ui.setupUi(self)
        self.ui.buton_giris.clicked.connect(self.guvenlik)  
        
if __name__ == "__main__":
    uygulama = QApplication(sys.argv)

    pencere_giris = giris()
    pencere_giris.show()
    
    isim_pencere = QWidget()
    ui_isim = isim_degisim_arayuz()
    ui_isim.setupUi(isim_pencere)
 
    def kapat_isim_degisim():
        ui_isim.girdi_eski_isim.setText("")
        ui_isim.girdi_yeni_isim.setText("")
        isim_pencere.close()
    def isim_degistir():
        eski_isim = ui_isim.girdi_eski_isim.text()
        if sifreleme.guvenlik_dosya_yaz(eski_isim,"isim"):
            sifreleme.giris_dosya_yaz(ui_isim.girdi_yeni_isim.text(),"isim")
            bildirim.uyari_kutusu("Kullanıcı adınız başarıyla değiştirildi.")
            kapat_isim_degisim()
        else:
            bildirim.uyari_kutusu("Eski kullanıcı adınızı yanlış girdiniz.Lütfen tekrar giriniz!")
    def isim_degisim():
        isim_pencere.show()
        ui_isim.buton_isim_degistir.clicked.connect(isim_degistir)
        ui_isim.buton_iptal.clicked.connect(kapat_isim_degisim)
 
    sifre_pencere = QWidget()
    ui_sifre = sifre_degisim()
    ui_sifre.setupUi(sifre_pencere)
    
    vt_s_pencere = QWidget()
    vt_s = vet_giris()
    vt_s.setupUi(vt_s_pencere)
    
    def kapat_sifre_degisim():
        ui_sifre.girdi_eski_sifre.setText("")
        ui_sifre.girdi_yeni_sifre.setText("")
        sifre_pencere.close()
    def sifre_degistir(cesit):
        eski_sifre = ui_sifre.girdi_eski_sifre.text()
        if sifreleme.guvenlik_dosya_yaz(eski_sifre,cesit):
            sifreleme.giris_dosya_yaz(ui_sifre.girdi_yeni_sifre.text(),cesit)
            bildirim.uyari_kutusu("Şifreniz başarıyla değiştirildi.")
            kapat_sifre_degisim()
        else:
            bildirim.uyari_kutusu("Eski şifrenizi yanlış girdiniz.Lütfen tekrar giriniz!")
    def sifre_degisimi(cesit):
        sifre_pencere.show()
        ui_sifre.buton_sifre_degistir.clicked.connect(lambda: sifre_degistir(cesit))
        ui_sifre.buton_iptal.clicked.connect(kapat_sifre_degisim)

    
    gc = gecis_sayfasi()
    cb = coban.coban_sınıf()
    vt = vet.vet_sinifi()
    uygulama.exec_()
