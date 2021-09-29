import sys
from PyQt5.QtWidgets import *
from coban_arayuz import Ui_Degisim as cbn_arayuz
#from iletisim_arayuz import Ui_iletisim
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import QIcon
import hedef_dosya_ayarla as hda
#import arkaplan_rc
import bildirim

def veri_tabani():
	import sqlite3
	global imlec
	global baglanti
	baglanti = sqlite3.connect(hda.hedef_dosya_ayarla("kayit.db"))
	imlec = baglanti.cursor()
	sorgu_tablo = ("CREATE TABLE IF NOT EXISTS tablo_kayit(  \
                	kupeNum TEXT NOT NULL,           \
                	ozellik1 TEXT NOT NULL,             \
                	ozellik2 TEXT NOT NULL,             \
                	ozellik3 TEXT NOT NULL,             \
                	ozellik4 TEXT NOT NULL          )")
	imlec.execute(sorgu_tablo)
	baglanti.commit()
        
class coban_sınıf(QMainWindow,cbn_arayuz):
    veri_tabani() 
    def __init__(self):
        super().__init__()
        self.num_secilen = None
        self.secili_satir = None
        self.sayfa_degisim()
    def temizle_tablo(self):
        self.tablo_degisim.clear()
    def listele(self):
        self.tablo_degisim.setHorizontalHeaderLabels(('Kupe Numarasi',\
                                                   'ozellik1','ozellik2','ozellik3','ozellik4'))
        imlec.execute("SELECT *FROM tablo_kayit")
        for satir_indeks, satir_veri in enumerate(imlec):
            for sutun_indeks, sutun_veri in enumerate(satir_veri):
                self.tablo_degisim.setItem(satir_indeks,sutun_indeks,QTableWidgetItem(str(sutun_veri)))
        imlec.execute("SELECT COUNT(*) FROM tablo_kayit")
        kayitSayisi = imlec.fetchone()
        self.cikti_kayit_sayisi.setText(str(kayitSayisi[0]))
    def id_kontrol(self,id):
        imlec.execute("SELECT *FROM tablo_kayit")
        kayitli_veriler = imlec.fetchall()
        for kupeNumarasi in kayitli_veriler:
            if int(id) == int(kupeNumarasi[0]) :
                bildirim.uyari_kutusu("Bu kupe numarasinda kayıt zaten var.Ayni kupe numarasinda iki hayvan kaydı yapılamaz.")
                return 0
    def ekle(self):
        try:
            alinan1 = self.girdi_kupeNum.text()
            alinan2 = self.girdi_ozellik1.text()
            alinan3 = self.girdi_ozellik3.value()
            alinan4 = self.girdi_tarih.selectedDate().toString(QtCore.Qt.ISODate)
            alinan5 = self.girdi_ozellik4.currentText()
            if self.id_kontrol(alinan1) != 0:  
                imlec.execute("INSERT INTO tablo_kayit \
                    (kupeNum,ozellik1,ozellik2,ozellik3,ozellik4) \
                     VALUES (?,?,?,?,?)" ,\
                    (alinan1,alinan2,alinan3,alinan4,alinan5))
                baglanti.commit()
                self.listele()
                self.statusbar.showMessage("Ekleme islemi gerceklestirildi.",1000)
        except Exception as Hata:
            self.statusbar.showMessage("Lutfen ekleme islemini tekrar deneyin.Bir hata ile karsilasildi:"+str(Hata),1000)
    def secilen_satir_alma(self):
        try:
            self.secili_satir = self.tablo_degisim.selectedItems()
            if self.secili_satir == [] :
                for x in range(5):
                    self.secili_satir.append("")
                self.num_secilen = self.secili_satir[0]
                return 0
            else:
                self.num_secilen = self.secili_satir[0].text()
                return 1
        except Exception as Hata:
            self.statusbar.showMessage("Veri tabanı yuklenemedı.Bir hata ile karsilasildi:"+str(Hata),8000)
    def doldur(self):
        try:
            if self.secilen_satir_alma() == 1 : 
                self.girdi_kupeNum.setText(self.num_secilen)
                self.girdi_ozellik1.setText(self.secili_satir[1].text())
                self.girdi_ozellik3.setValue(int(self.secili_satir[2].text()))
                yil = int(self.secili_satir[3].text()[0:4])
                ay = int(self.secili_satir[3].text()[5:7])
                gun = int(self.secili_satir[3].text()[8:10])
                self.girdi_tarih.setSelectedDate(QtCore.QDate(yil,ay,gun))
                self.girdi_ozellik4.setCurrentText(self.secili_satir[4].text())
            elif self.secilen_satir_alma() == 0 :
                self.girdi_kupeNum.setText(self.num_secilen)
                self.girdi_ozellik1.setText(self.secili_satir[1])
                self.girdi_ozellik3.setValue(int(0))
            self.statusbar.showMessage("Secilen satir verileri gösterimde.",1500)
        except Exception as Hata:
            self.statusbar.showMessage("Bos satira tiklandi:"+str(Hata),1500)
            
    def guncelle(self):
        try:
            self.secilen_satir_alma()
            alinan1 = self.girdi_kupeNum.text()
            alinan2 = self.girdi_ozellik1.text()
            alinan3 = self.girdi_ozellik3.value()
            alinan4 = self.girdi_tarih.selectedDate().toString(QtCore.Qt.ISODate)
            alinan5 = self.girdi_ozellik4.currentText()
            imlec.execute("UPDATE tablo_kayit SET kupeNum=?,ozellik1=?,ozellik2=?,ozellik3=?,ozellik4=? WHERE kupeNum=?",\
                      (alinan1,alinan2,alinan3,alinan4,alinan5,self.num_secilen))
            baglanti.commit()
            self.listele()
            self.statusbar.showMessage("Guncelleme islemi gerceklestirildi.",1500)
        except Exception as Hata:
            self.statusbar.showMessage("Lutfen guncelleme islemini tekrar deneyin.Bir hata ile karsilasildi:"+str(Hata),1000)
    def sil(self):
        try:
            self.secilen_satir_alma()
            imlec.execute("DELETE FROM tablo_kayit WHERE kupeNum='%s'" %(self.num_secilen))
            baglanti.commit()
            self.temizle_tablo()
            self.listele()
            self.statusbar.showMessage("Secilen satir  basariyla silindi.", 1500)
        except Exception as Hata:
            self.statusbar.showMessage("Lutfen silme islemini tekrar deneyin.Bir hata ile karsilasildi:"+str(Hata),1000)
    def bul(self):
        aranan_id = self.girdi_aranacak.text()
        imlec.execute("SELECT * FROM tablo_kayit WHERE kupeNum='%s'" %(aranan_id))
        baglanti.commit()
        self.tablo_degisim.clear()
        for satir_indeks, satir_veri in enumerate(imlec):
            for sutun_indeks, sutun_veri in enumerate(satir_veri):
                self.tablo_degisim.setItem(satir_indeks,sutun_indeks,QTableWidgetItem(str(sutun_veri)))
    def sayfa_degisim(self):
        self.setupUi(self)
        #self.setWindowIcon(QIcon(":/ikon/ikon/logo.png"))
        self.listele()
        #--------------SİGNAL/SLOT--------------
        self.tablo_degisim.itemSelectionChanged.connect(self.doldur)
        self.buton_listele.clicked.connect(self.listele)
        self.buton_ekle.clicked.connect(self.ekle)
        self.buton_guncelle.clicked.connect(self.guncelle)
        self.buton_sil.clicked.connect(self.sil)
        self.buton_bul.clicked.connect(self.bul)
