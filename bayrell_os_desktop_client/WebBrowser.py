# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WebBrowser(object):
    def setupUi(self, WebBrowser):
        WebBrowser.setObjectName("WebBrowser")
        WebBrowser.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(WebBrowser)
        self.centralwidget.setObjectName("centralwidget")
        self.webBrowser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webBrowser.setGeometry(QtCore.QRect(10, 10, 561, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webBrowser.sizePolicy().hasHeightForWidth())
        self.webBrowser.setSizePolicy(sizePolicy)
        self.webBrowser.setObjectName("webBrowser")
        WebBrowser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WebBrowser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 29))
        self.menubar.setObjectName("menubar")
        WebBrowser.setMenuBar(self.menubar)

        self.retranslateUi(WebBrowser)
        QtCore.QMetaObject.connectSlotsByName(WebBrowser)

    def retranslateUi(self, WebBrowser):
        _translate = QtCore.QCoreApplication.translate
        WebBrowser.setWindowTitle(_translate("WebBrowser", "MainWindow"))
from PyQt5 import QtWebEngineWidgets
