# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSlider, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 300))
        MainWindow.setMaximumSize(QSize(400, 300))
        MainWindow.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.actionLight_Mode = QAction(MainWindow)
        self.actionLight_Mode.setObjectName(u"actionLight_Mode")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(400, 267))
        self.centralwidget.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setEnabled(True)
        self.verticalFrame.setGeometry(QRect(0, 0, 400, 246))
        sizePolicy1.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy1)
        self.verticalFrame.setMaximumSize(QSize(400, 267))
        self.verticalFrame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalFrame.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_Top = QFrame(self.verticalFrame)
        self.horizontalFrame_Top.setObjectName(u"horizontalFrame_Top")
        self.horizontalFrame_Top.setMaximumSize(QSize(400, 36))
        self.horizontalFrame_Top.setFrameShape(QFrame.Shape.Box)
        self.horizontalLayout_Mid = QHBoxLayout(self.horizontalFrame_Top)
        self.horizontalLayout_Mid.setObjectName(u"horizontalLayout_Mid")
        self.horizontalLayout_Mid.setContentsMargins(1, -1, 1, -1)
        self.label_Name = QLabel(self.horizontalFrame_Top)
        self.label_Name.setObjectName(u"label_Name")
        self.label_Name.setMaximumSize(QSize(400, 36))
        self.label_Name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_Mid.addWidget(self.label_Name)


        self.verticalLayout.addWidget(self.horizontalFrame_Top)

        self.horizontalFrame_Mid = QFrame(self.verticalFrame)
        self.horizontalFrame_Mid.setObjectName(u"horizontalFrame_Mid")
        self.horizontalFrame_Mid.setMaximumSize(QSize(400, 190))
        self.horizontalFrame_Mid.setFrameShape(QFrame.Shape.Box)
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame_Mid)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.label = QLabel(self.horizontalFrame_Mid)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.horizontalFrame_Mid)

        self.horizontalFrame_Bot = QFrame(self.verticalFrame)
        self.horizontalFrame_Bot.setObjectName(u"horizontalFrame_Bot")
        self.horizontalFrame_Bot.setMaximumSize(QSize(400, 20))
        self.horizontalFrame_Bot.setFrameShape(QFrame.Shape.Box)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_Bot)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, -1)
        self.horizontalSlider = QSlider(self.horizontalFrame_Bot)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(396, 30))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.horizontalSlider)


        self.verticalLayout.addWidget(self.horizontalFrame_Bot)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 33))
        self.menubar.setMaximumSize(QSize(400, 33))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuMode = QMenu(self.menubar)
        self.menuMode.setObjectName(u"menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menuSettings.addAction(self.action1)
        self.menuMode.addAction(self.actionLight_Mode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My Robot Online", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"Name Setting", None))
        self.actionLight_Mode.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.label_Name.setText(QCoreApplication.translate("MainWindow", u"<Lv.1> Lailla", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"asdasdads", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
    # retranslateUi

