# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LightModeGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QWidget)

class Ui_LightModeWindow(object):
    def setupUi(self, LightModeWindow):
        if not LightModeWindow.objectName():
            LightModeWindow.setObjectName(u"LightModeWindow")
        LightModeWindow.resize(172, 172)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LightModeWindow.sizePolicy().hasHeightForWidth())
        LightModeWindow.setSizePolicy(sizePolicy)
        LightModeWindow.setMinimumSize(QSize(0, 0))
        LightModeWindow.setMaximumSize(QSize(172, 172))
        LightModeWindow.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))
        self.centralwidget = QWidget(LightModeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(172, 172))
        self.label_CharHeadImg = QLabel(self.centralwidget)
        self.label_CharHeadImg.setObjectName(u"label_CharHeadImg")
        self.label_CharHeadImg.setGeometry(QRect(40, 40, 100, 100))
        self.label_CharHeadImg.setFrameShape(QFrame.Shape.NoFrame)
        self.label_CharHeadImg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        LightModeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LightModeWindow)

        QMetaObject.connectSlotsByName(LightModeWindow)
    # setupUi

    def retranslateUi(self, LightModeWindow):
        LightModeWindow.setWindowTitle(QCoreApplication.translate("LightModeWindow", u"MainWindow", None))
        self.label_CharHeadImg.setText(QCoreApplication.translate("LightModeWindow", u"Logo Image", None))
    # retranslateUi

