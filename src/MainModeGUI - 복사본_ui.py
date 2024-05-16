# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainModeGUI - 복사본.ui'
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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainModeWindow(object):
    def setupUi(self, MainModeWindow):
        if not MainModeWindow.objectName():
            MainModeWindow.setObjectName(u"MainModeWindow")
        MainModeWindow.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainModeWindow.sizePolicy().hasHeightForWidth())
        MainModeWindow.setSizePolicy(sizePolicy)
        MainModeWindow.setMinimumSize(QSize(400, 300))
        MainModeWindow.setMaximumSize(QSize(400, 300))
        MainModeWindow.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))
        self.action1 = QAction(MainModeWindow)
        self.action1.setObjectName(u"action1")
        self.actionLight_Mode = QAction(MainModeWindow)
        self.actionLight_Mode.setObjectName(u"actionLight_Mode")
        self.centralwidget = QWidget(MainModeWindow)
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
        self.verticalFrame_Left = QFrame(self.horizontalFrame_Mid)
        self.verticalFrame_Left.setObjectName(u"verticalFrame_Left")
        self.verticalFrame_Left.setMaximumSize(QSize(100, 186))
        self.verticalFrame_Left.setFrameShape(QFrame.Shape.Box)
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame_Left)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_1 = QPushButton(self.verticalFrame_Left)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMaximumSize(QSize(100, 30))

        self.verticalLayout_2.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.verticalFrame_Left)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.verticalFrame_Left)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.verticalFrame_Left)

        self.label_CharImg = QLabel(self.horizontalFrame_Mid)
        self.label_CharImg.setObjectName(u"label_CharImg")
        self.label_CharImg.setEnabled(True)
        self.label_CharImg.setFrameShape(QFrame.Shape.Box)
        self.label_CharImg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_CharImg)

        self.verticalFrame_right = QFrame(self.horizontalFrame_Mid)
        self.verticalFrame_right.setObjectName(u"verticalFrame_right")
        self.verticalFrame_right.setMaximumSize(QSize(100, 186))
        self.verticalFrame_right.setFrameShape(QFrame.Shape.Box)
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame_right)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_4 = QPushButton(self.verticalFrame_right)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(100, 34))

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.verticalFrame_right)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.verticalFrame_right)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.horizontalLayout.addWidget(self.verticalFrame_right)


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

        MainModeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainModeWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 33))
        self.menubar.setMaximumSize(QSize(400, 33))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuMode = QMenu(self.menubar)
        self.menuMode.setObjectName(u"menuMode")
        MainModeWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainModeWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainModeWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menuSettings.addAction(self.action1)
        self.menuMode.addAction(self.actionLight_Mode)

        self.retranslateUi(MainModeWindow)

        QMetaObject.connectSlotsByName(MainModeWindow)
    # setupUi

    def retranslateUi(self, MainModeWindow):
        MainModeWindow.setWindowTitle(QCoreApplication.translate("MainModeWindow", u"My Robot Online", None))
        self.action1.setText(QCoreApplication.translate("MainModeWindow", u"Name Setting", None))
        self.actionLight_Mode.setText(QCoreApplication.translate("MainModeWindow", u"Light Mode", None))
        self.label_Name.setText(QCoreApplication.translate("MainModeWindow", u"<Lv.1> Lailla", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainModeWindow", u"\uc778\uc0ac\ud558\uae30", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainModeWindow", u"\ub180\uc544\uc8fc\uae30", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainModeWindow", u"\uc74c\uc2dd\uc8fc\uae30", None))
        self.label_CharImg.setText(QCoreApplication.translate("MainModeWindow", u"<Character Img>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainModeWindow", u"\uc815\ubcf4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainModeWindow", u"\ub3c4\uac10", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainModeWindow", u"\uc77c\uae30", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainModeWindow", u"Settings", None))
        self.menuMode.setTitle(QCoreApplication.translate("MainModeWindow", u"Mode", None))
    # retranslateUi

