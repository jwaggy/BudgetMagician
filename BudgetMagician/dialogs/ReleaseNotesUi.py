from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout, QWidget


class Ui_ReleaseNotes(object):
    def setupUi(self, ReleaseNotes):
        if not ReleaseNotes.objectName():
            ReleaseNotes.setObjectName("ReleaseNotes")
        ReleaseNotes.resize(800, 600)
        self.verticalLayout = QVBoxLayout(ReleaseNotes)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_box = QTextBrowser(ReleaseNotes)
        self.text_box.setObjectName("text_box")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_box.sizePolicy().hasHeightForWidth())
        self.text_box.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.text_box)

        self.ok = QPushButton(ReleaseNotes)
        self.ok.setObjectName("ok")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.ok, 0, Qt.AlignHCenter)

        self.retranslateUi(ReleaseNotes)

        QMetaObject.connectSlotsByName(ReleaseNotes)

    # setupUi

    def retranslateUi(self, ReleaseNotes):
        ReleaseNotes.setWindowTitle(QCoreApplication.translate("ReleaseNotes", "Release Notes", None))
        self.ok.setText(QCoreApplication.translate("ReleaseNotes", "OK", None))

    # retranslateUi
