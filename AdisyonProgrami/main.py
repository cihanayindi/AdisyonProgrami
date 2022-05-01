#-------------------KÜTÜPHANE------------------#
#----------------------------------------------#

import sys
import os
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import *
from hesap import *
from masalar import *
from giris import *
from OnayKutusu import *

#---------------UYGULAMA OLUŞTUR---------------#
#----------------------------------------------#

Uygulama = QApplication(sys.argv)

penMasalar = QMainWindow()
ui1 = Ui_MainWindow1()
ui1.setupUi(penMasalar)

penHesap = QMainWindow()
ui2 = Ui_mainWindow2()
ui2.setupUi(penHesap)

penGiris = QMainWindow()
ui3 = Ui_MainWindow3()
ui3.setupUi(penGiris)

penOnay = QDialog()
ui4 = Ui_OnayKutusu()
ui4.setupUi(penOnay)
penGiris.show()

#------------VERİTABANI BAĞLANTISI------------#
#---------------------------------------------#

conn = sqlite3.connect("veritabani.db")
curs = conn.cursor()

sorguCreTblKullaniciVerileri = ('CREATE TABLE IF NOT EXISTS KullaniciVerileri(    \
                                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,   \
                                 KullaniciAdi TEXT NOT NULL,                      \
                                 Sifre TEXT NOT NULL)')

curs.execute(sorguCreTblKullaniciVerileri)
conn.commit()

#---------------GİRİŞ DOĞRULAMA---------------#
#---------------------------------------------#

def GIRISYAP():

    KullaniciAdi = ui3.lneKullaniciAdi.text()
    Sifre = ui3.lneSifre.text()

    if len(KullaniciAdi) == 0 and len(Sifre) == 0:
        ui3.lblBilgilendirme.setText("Bilgi Girmediniz!")

    elif (len(KullaniciAdi) == 0):
        ui3.lblBilgilendirme.setText("Bilgileri Eksik Girdiniz!")

    elif (len(Sifre) == 0):
        ui3.lblBilgilendirme.setText("Bilgileri Eksik Girdiniz!")

    else:
        curs.execute('SELECT COUNT(*) FROM KullaniciVerileri WHERE KullaniciAdi = ?',(KullaniciAdi,))
        data = curs.fetchall()

        if data[0][0] == 1:
            curs.execute('SELECT Sifre FROM KullaniciVerileri WHERE KullaniciAdi = ?',(KullaniciAdi,))
            data = curs.fetchall()
            if data[0][0] == Sifre:
                penGiris.close()
                penMasalar.show()
                yenimetin = ui1.lblKasaGorevlisi.text().replace("x",f"{KullaniciAdi}")
                ui1.lblKasaGorevlisi.setText(yenimetin)

                an = datetime.now()
                tarih = str(an.day) + "." + str(an.month) + "." + str(an.year)
                ui1.lblTarih.setText(tarih)

            else:
                ui3.lblBilgilendirme.setText("Yanlış kullanıcı adı veya şifre girdiniz.")
        else:
            ui3.lblBilgilendirme.setText("Böyle bir kullanıcı bulunamadı.")

#---------------MASA İŞLEMLERİ---------------#
#--------------------------------------------#

class MASAISLEMLERI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

    def MASA(self,masano):
        penMasalar.close()
        ui2.tblwHesap.clear()
        try:
            masaadidb = f"masa{masano}"
            curs.execute(f"SELECT * FROM {masaadidb}")
            for satirIndeks, satirVeri in enumerate(curs):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui2.tblwHesap.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
        except:
            pass
        try:
            masaadidb = f"masa{masano}"
            curs.execute(f"SELECT SUM(ToplamFiyat) FROM {masaadidb}")
            toplam = curs.fetchall()
            deger = ui2.lblToplamFiyat.text().split(" ")
            deger[0] = str(toplam[0][0])
            if deger[0] == "None":
                deger[0] = "0"
            deger = " ".join(deger)
            ui2.lblToplamFiyat.setText(deger)
            conn.commit()
        except:
            deger = ui2.lblToplamFiyat.text().split(" ")
            deger[0] = "0"
            deger = " ".join(deger)
            ui2.lblToplamFiyat.setText(deger)
        ui2.lstwUrunler.clear()
        penHesap.show()
        ui2.lblMasaNo.setText(masano)

    def MASAANLAMA(self):
        sender = self.sender()
        global masano
        masano = (sender.text().split("\n")[0].split(" ")[-1])

        self.MASA(masano)

    def ANAEKRANADON(self):

        penHesap.close()
        penMasalar.show()

    def SICAKICECEK(self):

        ui2.lstwUrunler.clear()
        sicakicecekler = ["Çay - 5 TL","Oralet - 5 TL","Sıcak Çikolata - 8 TL","Sahlep - 10 TL"]
        j = 0
        #deneme = icecekler[0].split(" ")
        #print(deneme[2])
        for i in sicakicecekler:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(sicakicecekler[j])
            j += 1

    def SOGUKICECEK(self):

        ui2.lstwUrunler.clear()
        sogukicecekler = ["Kola - 10 TL","Ice Tea - 10 TL","Churcill - 8 TL"]
        j = 0
        for i in sogukicecekler:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(sogukicecekler[j])
            j += 1

    def ESPRESSOKAHVE(self):

        ui2.lstwUrunler.clear()
        espressokahveler = ["French Press - 15 TL","Espresso Shot - 17 TL","Macchiato - 17 TL"]
        j = 0
        for i in espressokahveler:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(espressokahveler[j])
            j += 1

    def DUNYAKAHVE(self):

        ui2.lstwUrunler.clear()
        dunyakahve = ["Türk Kahvesi - 13 TL","Yemen Kahvesi - 15 TL"]
        j = 0
        for i in dunyakahve:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(dunyakahve[j])
            j += 1

    def SERINLETENKAHVE(self):

        ui2.lstwUrunler.clear()
        serinletenkahve = ["Ice Americano - 20 TL","Ice Latte - 15 TL"]
        j = 0
        for i in serinletenkahve:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(serinletenkahve[j])
            j += 1

    def KOKTEYL(self):

        ui2.lstwUrunler.clear()
        kokteyl = ["Virgin Colada - 30 TL","Virgin Mojito - 35 TL"]
        j = 0
        for i in kokteyl:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(kokteyl[j])
            j += 1

    def FROZEN(self):

        ui2.lstwUrunler.clear()
        frozen = ["Çilek - 25 TL","Mango - 25 TL"]
        j = 0
        for i in frozen:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(frozen[j])
            j += 1

    def MILKSHAKE(self):

        ui2.lstwUrunler.clear()
        milkshake = ["Çilek - 27 TL","Çikolata - 27 TL"]
        j = 0
        for i in milkshake:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(milkshake[j])
            j += 1

    def BASLANGIC(self):

        ui2.lstwUrunler.clear()
        baslangic = ["Atıştırma Tabağı - 20 TL","Karışık Çıtır - 15 TL"]
        j = 0
        for i in baslangic:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(baslangic[j])
            j += 1

    def SANDVIC(self):

        ui2.lstwUrunler.clear()
        sandvic = ["Soğuk Sandviç - 10 TL","Hellim Sandviç - 12 TL"]
        j = 0
        for i in sandvic:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(sandvic[j])
            j += 1

    def TOST(self):

        ui2.lstwUrunler.clear()
        tost = ["Kaşarlı Tost - 13 TL","Sucuklu Tost - 13 TL","Karışık Tost - 15 TL"]
        j = 0
        for i in tost:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(tost[j])
            j += 1

    def YUMURTA(self):

        ui2.lstwUrunler.clear()
        yumurta = ["Omlet - 15 TL","Sahanda Yumurta - 20 TL"]
        j = 0
        for i in yumurta:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(yumurta[j])
            j += 1

    def GOZLEME(self):

        ui2.lstwUrunler.clear()
        gozleme = ["Peynirli Gözleme - 20 TL","Sade Gözleme - 15 TL"]
        j = 0
        for i in gozleme:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(gozleme[j])
            j += 1

    def KAHVALTI(self):

        ui2.lstwUrunler.clear()
        kahvalti = ["Fit Tabak Kahvaltı - 35 TL","Eko Kahvaltı - 25 TL"]
        j = 0
        for i in kahvalti:
            i = QtWidgets.QListWidgetItem()
            ui2.lstwUrunler.addItem(i)
            i = ui2.lstwUrunler.item(j)
            i.setText(kahvalti[j])
            j += 1

    def EKLE(self):
        try:
            urun = (ui2.lstwUrunler.selectedItems()[0].text())
            urun = urun.split("-")
            isim = urun[0]
            isim = isim.strip()
            urun = urun[1].split(" ")
            fiyat = int(urun[1])

            masaadidb = f"masa{masano}"
            curs.execute(f"CREATE TABLE IF NOT EXISTS {masaadidb}(         \
                           UrunAdi TEXT NOT NULL,                          \
                           UrunAdeti INTEGER NOT NULL,                     \
                           ToplamFiyat INTEGER NOT NULL)")
            conn.commit()
            curs.execute(f"SELECT * FROM {masaadidb}")
            for satirIndeks, satirVeri in enumerate(curs):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui2.tblwHesap.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

            try:
                curs.execute(f"SELECT UrunAdeti FROM {masaadidb} WHERE UrunAdi = ?",(isim,))
                data = curs.fetchall()
                if data[0][0] != 0:
                    adet = data[0][0] + 1
                    curs.execute(f"UPDATE {masaadidb} SET UrunAdeti = ?, ToplamFiyat = ? WHERE UrunAdi = ?",(adet,adet*fiyat,isim))
                    conn.commit()
            except:
                curs.execute(f"INSERT INTO {masaadidb} VALUES(?,?,?)",(isim,1,fiyat*1))
                conn.commit()

            curs.execute(f"SELECT SUM(ToplamFiyat) FROM {masaadidb}")
            toplam = curs.fetchall()
            deger = ui2.lblToplamFiyat.text().split(" ")
            deger[0] = str(toplam[0][0])
            deger = " ".join(deger)
            ui2.lblToplamFiyat.setText(deger)
            conn.commit()

            curs.execute(f"SELECT COUNT(*) FROM {masaadidb}")
            data = curs.fetchall()
            ui2.tblwHesap.setRowCount(data[0][0])
            conn.commit()

            curs.execute(f"SELECT * FROM {masaadidb}")
            for satirIndeks, satirVeri in enumerate(curs):
                for sutunIndeks, sutunVeri in enumerate(satirVeri):
                    ui2.tblwHesap.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
        except:
            pass

    def IKITANEEKLE(self):
        MASAISLEMLERI().EKLE()
        MASAISLEMLERI().EKLE()

    def SIL(self):
        masaadidb = f"masa{masano}"
        try:
            deger = ui2.tblwHesap.selectedItems()
            curs.execute(f"DELETE FROM {masaadidb} WHERE UrunAdi = ?",(deger[0].text(),))
            conn.commit()
            ui2.tblwHesap.clear()
            masaadidb = f"masa{masano}"
            curs.execute(f"SELECT SUM(ToplamFiyat) FROM {masaadidb}")
            toplam = curs.fetchall()
            deger = ui2.lblToplamFiyat.text().split(" ")
            deger[0] = str(toplam[0][0])
            if deger[0] == "None":
                deger[0] = "0"
            deger = " ".join(deger)
            ui2.lblToplamFiyat.setText(deger)
            conn.commit()
        except:
            pass
        curs.execute(f"SELECT * FROM {masaadidb}")
        for satirIndeks, satirVeri in enumerate(curs):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                ui2.tblwHesap.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    def DUSUR(self):
        masaadidb = f"masa{masano}"
        try:
            deger = ui2.tblwHesap.selectedItems()
            adet = int(deger[1].text())
            toplamfiyat = (int(deger[2].text()) / adet) * (adet - 1)
            curs.execute(f"UPDATE {masaadidb} SET UrunAdeti = ?, ToplamFiyat = ? WHERE UrunAdi = ?",(adet-1,toplamfiyat,deger[0].text()))
            conn.commit()
            ui2.tblwHesap.clear()
            curs.execute(f"SELECT SUM(ToplamFiyat) FROM {masaadidb}")
            toplam = curs.fetchall()
            deger = ui2.lblToplamFiyat.text().split(" ")
            deger[0] = str(toplam[0][0])
            if deger[0] == "None":
                deger[0] = "0"
            deger = " ".join(deger)
            ui2.lblToplamFiyat.setText(deger)
            conn.commit()
        except:
            pass
        curs.execute(f"SELECT * FROM {masaadidb}")
        for satirIndeks, satirVeri in enumerate(curs):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                ui2.tblwHesap.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

    def ODE(self):
        masaadidb = f"masa{masano}"
        curs.execute('CREATE TABLE IF NOT EXISTS GunlukRapor(       \
                      MasaNo INTEGER NOT NULL,                      \
                      UrunAdi TEXT NOT NULL,                        \
                      UrunAdeti INTEGER NOT NULL,                   \
                      ToplamFiyat INTEGER NOT NULL,                 \
                      SatisZamani DATETİME2 TEXT NOT NULL,          \
                      Kasiyer TEXT NOT NULL,                        \
                      OdemeTipi TEXT NOT NULL)')
        conn.commit()

        deger = ui2.tblwHesap.selectedItems()
        masaadi = int(masano)
        urunadi = deger[0].text()
        urunadeti = int(deger[1].text())
        toplamfiyat = int(deger[2].text())
        an = datetime.now()
        global tarih
        tarih = str(an.day) + "/" + str(an.month) + "/" + str(an.year)
        satiszamani = tarih
        kasiyer = ui1.lblKasaGorevlisi.text().split(":")
        kasiyer = kasiyer[1].strip()
        odemetipi = ''

        if ui2.rdbtnNakit.isChecked():
            odemetipi = 'Nakit'
        elif ui2.rdbtnKart.isChecked():
            odemetipi = 'Kart'
        else:
            odemetipi = "Seçim yok"

        curs.execute("INSERT INTO GunlukRapor VALUES(?,?,?,?,?,?,?)",(masaadi,urunadi,urunadeti,toplamfiyat,satiszamani,kasiyer,odemetipi))
        conn.commit()

        curs.execute(f"DELETE FROM {masaadidb} WHERE UrunAdi = ?",(deger[0].text(),))
        conn.commit()

        ui2.tblwHesap.clear()
        curs.execute(f"SELECT * FROM {masaadidb}")
        for satirIndeks, satirVeri in enumerate(curs):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                ui2.tblwHesap.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

#-----------------GÜNÜ KAPAT------------------#
#---------------------------------------------#

def GUNUKAPAT():
    cevap = QMessageBox.question(penMasalar, "UYARI!", "Tüm masaların kapatılarak günün aylık\n"
                                                        "rapora eklenmesini ve günü kapatmayı\n"
                                                        "onaylıyor musunuz?",
                                 QMessageBox.Yes | QMessageBox.No)

    if cevap == QMessageBox.Yes:

        curs.execute('CREATE TABLE IF NOT EXISTS AylikRapor(           \
                      Tarih TEXT NOT NULL,                             \
                      NakitGelir INTEGER NOT NULL,                     \
                      KartGelir INTEGER NOT NULL,                      \
                      SecimYok INTEGER NOT NULL,                       \
                      ToplamGelir INTEGER NOT NULL)')
        conn.commit()

        curs.execute("SELECT ToplamFiyat FROM GunlukRapor WHERE OdemeTipi = ?",("Nakit",))
        data = curs.fetchall()
        NakitMiktari = 0
        for i in data:
            NakitMiktari += int(i[0])
        conn.commit()

        curs.execute("SELECT ToplamFiyat FROM GunlukRapor WHERE OdemeTipi = ?", ("Kart",))
        data = curs.fetchall()
        KartMiktari = 0
        for i in data:
            KartMiktari += int(i[0])
        conn.commit()

        curs.execute("SELECT ToplamFiyat FROM GunlukRapor WHERE OdemeTipi = ?", ("Seçim yok",))
        data = curs.fetchall()
        SecimYokMiktari = 0
        for i in data:
            SecimYokMiktari += int(i[0])
        conn.commit()

        ToplamGelir = NakitMiktari + KartMiktari + SecimYokMiktari

        curs.execute("INSERT INTO AylikRapor VALUES(?,?,?,?,?)",(tarih,NakitMiktari,KartMiktari,SecimYokMiktari,ToplamGelir,))
        conn.commit()
        ui1.statusbar.showMessage("GÜN KAPATILDI!..", 10000)

    elif cevap == QMessageBox.No:
        ui1.statusbar.showMessage("GÜNÜ KAPATMA İŞLEMİ İPTAL EDİLDİ!..", 10000)

#-----------------SINYAL SLOT-----------------#
#---------------------------------------------#

ui3.btnGirisYap.clicked.connect(lambda : GIRISYAP())
ui1.btnMasa1.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa2.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa3.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa4.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa5.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa6.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa7.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa8.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa9.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa10.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa11.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa12.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa13.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa14.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa15.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa16.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa17.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa18.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa19.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa20.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa21.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa22.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa23.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa24.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa25.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa26.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa27.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa28.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa29.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui1.btnMasa30.clicked.connect(lambda : MASAISLEMLERI().MASAANLAMA())
ui2.btnAnaEkranaGeriDon.clicked.connect(lambda : MASAISLEMLERI().ANAEKRANADON())
ui2.btnSicakIcecek.clicked.connect(lambda : MASAISLEMLERI().SICAKICECEK())
ui2.btnSogukIcecek.clicked.connect(lambda : MASAISLEMLERI().SOGUKICECEK())
ui2.btnEspresso.clicked.connect(lambda : MASAISLEMLERI().ESPRESSOKAHVE())
ui2.btnDunya.clicked.connect(lambda : MASAISLEMLERI().DUNYAKAHVE())
ui2.btnSerinleten.clicked.connect(lambda : MASAISLEMLERI().SERINLETENKAHVE())
ui2.btnDondurmali.clicked.connect(lambda : MASAISLEMLERI().KOKTEYL())
ui2.btnFrozen.clicked.connect(lambda : MASAISLEMLERI().FROZEN())
ui2.btnMilkshake.clicked.connect(lambda : MASAISLEMLERI().MILKSHAKE())
ui2.btnBaslangic.clicked.connect(lambda : MASAISLEMLERI().BASLANGIC())
ui2.btnSandvic.clicked.connect(lambda : MASAISLEMLERI().SANDVIC())
ui2.btnTost.clicked.connect(lambda : MASAISLEMLERI().TOST())
ui2.btnYumurta.clicked.connect(lambda : MASAISLEMLERI().YUMURTA())
ui2.btnGozleme.clicked.connect(lambda : MASAISLEMLERI().GOZLEME())
ui2.btnKahvalti.clicked.connect(lambda : MASAISLEMLERI().KAHVALTI())
ui2.btnEkle.clicked.connect(lambda : MASAISLEMLERI().EKLE())
ui2.btnIkiEkle.clicked.connect(lambda : MASAISLEMLERI().IKITANEEKLE())
ui2.btnSil.clicked.connect(lambda : MASAISLEMLERI().SIL())
ui2.btnDusur.clicked.connect(lambda : MASAISLEMLERI().DUSUR())
ui2.btnOde.clicked.connect(lambda : MASAISLEMLERI().ODE())
ui1.btnGunuKapa.clicked.connect(lambda : GUNUKAPAT())

sys.exit(Uygulama.exec_())