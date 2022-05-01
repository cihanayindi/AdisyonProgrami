# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girisUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(500, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow3.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblKullaniciAdi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblKullaniciAdi.setFont(font)
        self.lblKullaniciAdi.setObjectName("lblKullaniciAdi")
        self.verticalLayout.addWidget(self.lblKullaniciAdi)
        self.lneKullaniciAdi = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lneKullaniciAdi.setFont(font)
        self.lneKullaniciAdi.setObjectName("lneKullaniciAdi")
        self.verticalLayout.addWidget(self.lneKullaniciAdi)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblSifre = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblSifre.setFont(font)
        self.lblSifre.setObjectName("lblSifre")
        self.verticalLayout_2.addWidget(self.lblSifre)
        self.lneSifre = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lneSifre.setFont(font)
        self.lneSifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lneSifre.setObjectName("lneSifre")
        self.verticalLayout_2.addWidget(self.lneSifre)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.btnGirisYap = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnGirisYap.setFont(font)
        self.btnGirisYap.setObjectName("btnGirisYap")
        self.gridLayout.addWidget(self.btnGirisYap, 2, 0, 1, 1)
        self.lblBilgilendirme = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblBilgilendirme.setFont(font)
        self.lblBilgilendirme.setText("")
        self.lblBilgilendirme.setObjectName("lblBilgilendirme")
        self.gridLayout.addWidget(self.lblBilgilendirme, 1, 0, 1, 1)
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "Giriş Ekranı"))
        self.lblKullaniciAdi.setText(_translate("MainWindow3", "Kullanıcı Adı:"))
        self.lblSifre.setText(_translate("MainWindow3", "Şifre:"))
        self.btnGirisYap.setText(_translate("MainWindow3", "GİRİŞ YAP"))

