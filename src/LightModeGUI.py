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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)

class Ui_LightModeWindow(object):
    def setupUi(self, LightModeWindow):
        if not LightModeWindow.objectName():
            LightModeWindow.setObjectName(u"LightModeWindow")
        LightModeWindow.resize(200, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LightModeWindow.sizePolicy().hasHeightForWidth())
        LightModeWindow.setSizePolicy(sizePolicy)
        LightModeWindow.setMinimumSize(QSize(200, 200))
        LightModeWindow.setMaximumSize(QSize(200, 200))
        LightModeWindow.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))
        self.centralwidget = QWidget(LightModeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_CharImg = QLabel(self.centralwidget)
        self.label_CharImg.setObjectName(u"label_CharImg")
        self.label_CharImg.setGeometry(QRect(0, 0, 200, 200))
        self.label_CharImg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        LightModeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LightModeWindow)

        QMetaObject.connectSlotsByName(LightModeWindow)
    # setupUi

    def retranslateUi(self, LightModeWindow):
        LightModeWindow.setWindowTitle(QCoreApplication.translate("LightModeWindow", u"MainWindow", None))
        self.label_CharImg.setText(QCoreApplication.translate("LightModeWindow", u"Logo Image", None))
    # retranslateUi

