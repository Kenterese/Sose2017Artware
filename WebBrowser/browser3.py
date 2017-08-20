# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QToolButton, QLabel, QMessageBox
from PyQt5.QtGui import QColor, QBrush, QPainter, QKeySequence, QPixmap
from PyQt5.QtCore import Qt
import random
import pygame, pygame.mixer
#from pygame import *

class Ui_MainWindow(QWidget):
    pygame.init()
    #Click Actions
    def CryAct(self):


        pygame.mixer.music.load("sound/whatsapp.mp3")
        pygame.mixer.music.play(1)

        for i in range(4):
          x = random.randint(1, 790)
          y = random.randint(1, 790)
          x1 = random.randint(1, 790)
          y2 = random.randint(1, 790)
          QMessageBox.about(self, 'StarMan says:', "Is that really funny??")
          self.setGeometry(x1,y2,x,y)
          QMessageBox.about(self, 'SpicyChicken says:', "bad taste XD")
          self.setGeometry(x1,y,x,y2)
          QMessageBox.about(self, 'syg002 says:',"To cry as performance :)")
          self.setGeometry(x,y,x1,y2)

    def KillAct(self):
        pygame.mixer.music.load("sound/skype.mp3")
        pygame.mixer.music.play(1)
        self.webView.back()
    def DislikeAct(self):
        pygame.mixer.music.load("sound/facebook.mp3")
        pygame.mixer.music.play(1)
        self.webView.load(QtCore.QUrl("http://hackertyper.net" ))

    def SexyAct(self):
        pygame.mixer.music.load("sound/Dance.mp3")
        pygame.mixer.music.play(1)
        self.webView.load(QtCore.QUrl("http://gifdanceparty.giphy.com/"))

    def MoneyAct(self):
        pygame.mixer.music.load("sound/MSN.mp3")
        pygame.mixer.music.play(1)
        self.webView.load(QtCore.QUrl("http://10.211.55.8:5000/"))

    def FingerAct(self):
        pygame.mixer.music.load("sound/whatsapp.mp3")
        pygame.mixer.music.play(1)
        self.webView.load(QtCore.QUrl ("http://elgoog.im/search/?q=What%27s+wrong+with+Google&newwindow=1&source=lnms&tbm=nws&sa=X&ved=0ahUKEwinyvbC4LLQAhXBqFQKHZTLCDIQ_AUICCgB"))

    def searchAct(self):
        pygame.mixer.music.load("sound/call.mp3")
        pygame.mixer.music.play(1)
        url = self.ln_addressbar.text()
        self.webView.load(QtCore.QUrl(url))



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Live Now")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.show()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # address
        self.ln_addressbar = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_addressbar.setGeometry(QtCore.QRect(80,10,400,31))
        self.ln_addressbar.setObjectName("ln_addressbar")
        ##web
        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(0, 60, 800, 680))
        self.webView.setProperty("url", QtCore.QUrl("http://10.211.55.8:5000/"))
        self.webView.setObjectName("webView")
        ##buttons
        self.cry = QtWidgets.QToolButton(self.centralwidget)
        self.cry.setGeometry(QtCore.QRect(100, 750, 50, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/cry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cry.setIcon(icon)
        self.cry.setIconSize(QtCore.QSize(50, 50))
        self.cry.setObjectName("cry")
        #action0
        self.cry.clicked.connect(self.CryAct)

        self.kill = QtWidgets.QToolButton(self.centralwidget)
        self.kill.setGeometry(QtCore.QRect(200, 750, 50, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/kill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kill.setIcon(icon1)
        self.kill.setIconSize(QtCore.QSize(50, 50))
        self.kill.setObjectName("kill")
        # action1
        self.kill.clicked.connect(self.KillAct)

        self.dislike = QtWidgets.QToolButton(self.centralwidget)
        self.dislike.setGeometry(QtCore.QRect(300, 750, 50, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/dislike.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dislike.setIcon(icon2)
        self.dislike.setIconSize(QtCore.QSize(50, 50))
        self.dislike.setObjectName("dislike")
        # action2
        self.dislike.clicked.connect(self.DislikeAct)
        ##buttons
        self.sexy = QtWidgets.QToolButton(self.centralwidget)
        self.sexy.setGeometry(QtCore.QRect(400, 750, 50, 50))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/sexy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sexy.setIcon(icon3)
        self.sexy.setIconSize(QtCore.QSize(50, 50))
        self.sexy.setObjectName("sexy")
        # action3
        self.sexy.clicked.connect(self.SexyAct)

        self.money = QtWidgets.QToolButton(self.centralwidget)
        self.money.setGeometry(QtCore.QRect(500, 750, 50, 50))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.money.setIcon(icon4)
        self.money.setIconSize(QtCore.QSize(50, 50))
        self.money.setObjectName("money")
        # action4
        self.money.clicked.connect(self.MoneyAct)

        self.finger = QtWidgets.QToolButton(self.centralwidget)
        self.finger.setGeometry(QtCore.QRect(600, 750, 50, 50))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/finger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.finger.setIcon(icon5)
        self.finger.setIconSize(QtCore.QSize(50, 50))
        self.finger.setObjectName("finger")
        # action5
        self.finger.clicked.connect(self.FingerAct)

        self.search = QtWidgets.QToolButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(600,0,50,50))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon6)
        self.search.setIconSize(QtCore.QSize(50, 50))
        self.search.setObjectName("search")
        # action5
        self.search.clicked.connect(self.searchAct)


        self.dislike.raise_()
        self.cry.raise_()
        self.kill.raise_()
        self.ln_addressbar.raise_()
        self.webView.raise_()
        self.sexy.raise_()
        self.money.raise_()
        self.finger.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cry.setText(_translate("MainWindow", "..."))
        self.kill.setText(_translate("MainWindow", "..."))
        self.dislike.setText(_translate("MainWindow", "..."))
        self.sexy.setText(_translate("MainWindow", "..."))
        self.money.setText(_translate("MainWindow", "..."))
        self.finger.setText(_translate("MainWindow", "..."))


from PyQt5 import QtWebKitWidgets


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)

        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.KillAct()
        MainWindow.show()

        sys.exit(app.exec_())