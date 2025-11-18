# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_view_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_image_view_dialog(object):
    def setupUi(self, image_view_dialog):
        if not image_view_dialog.objectName():
            image_view_dialog.setObjectName(u"image_view_dialog")
        image_view_dialog.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(image_view_dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_view_label = QLabel(image_view_dialog)
        self.image_view_label.setObjectName(u"image_view_label")
        self.image_view_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.image_view_label)


        self.retranslateUi(image_view_dialog)

        QMetaObject.connectSlotsByName(image_view_dialog)
    # setupUi

    def retranslateUi(self, image_view_dialog):
        image_view_dialog.setWindowTitle(QCoreApplication.translate("image_view_dialog", u"Dialog", None))
        self.image_view_label.setText(QCoreApplication.translate("image_view_dialog", u"TextLabel", None))
    # retranslateUi

