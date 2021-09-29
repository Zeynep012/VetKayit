import os
import hedef_dosya_ayarla as hda
import hashlib

def sifre_kontrol(supheli,kayitli):
    if supheli == kayitli:
        return 1
    else:
        return 0
def dosya_oku(cesit):
    guvenlik_dosyasi_oku = open(hda.hedef_dosya_ayarla("guvenlik.txt"), "r")
    guvenlik = guvenlik_dosyasi_oku.readline()
    guvenlik_dosyasi_oku.close()
    if cesit == "sifre":
        giris_dosyasi_oku = open(hda.hedef_dosya_ayarla("giris_bilgisi.txt"), "r")
    elif cesit == "isim":
        giris_dosyasi_oku = open(hda.hedef_dosya_ayarla("giris_bilgisi_i.txt"), "r")
    elif cesit == "sifre_vet":
        giris_dosyasi_oku = open(hda.hedef_dosya_ayarla("giris_bilgisi_v.txt"), "r")
    sifre = giris_dosyasi_oku.readline()
    giris_dosyasi_oku.close()
    return sifre_kontrol(guvenlik,sifre)
def giris_dosya_yaz(girilen,cesit):
    if cesit == "sifre":
        giris_dosyasi = open(hda.hedef_dosya_ayarla("giris_bilgisi.txt"), "w")
    elif cesit == "isim":
        giris_dosyasi = open(hda.hedef_dosya_ayarla("giris_bilgisi_i.txt"), "w")
    elif cesit == "sifre_vet":
        giris_dosyasi = open(hda.hedef_dosya_ayarla("giris_bilgisi_v.txt"), "w")
    sifrele(girilen, giris_dosyasi)
    giris_dosyasi.close()
def guvenlik_dosya_yaz(girdi_sifre,cesit):
    guvenlik_dosyasi = open(hda.hedef_dosya_ayarla("guvenlik.txt") , "w")
    sifrele(girdi_sifre, guvenlik_dosyasi)
    guvenlik_dosyasi.close()
    return dosya_oku(cesit)
def sifrele(girdi,dosya):
    dosya.write(str(hashlib.sha512(girdi.encode("utf-8")).hexdigest()))
    
#giris_dosya_yaz("zeynep","isim")
#giris_dosya_yaz("123","sifre")
#giris_dosya_yaz("456","sifre_vet")
