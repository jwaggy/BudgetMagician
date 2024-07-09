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


class Ui_PrivacyPolicy(object):
    def setupUi(self, PrivacyPolicy):
        if not PrivacyPolicy.objectName():
            PrivacyPolicy.setObjectName("PrivacyPolicy")
        PrivacyPolicy.resize(800, 600)
        self.verticalLayout = QVBoxLayout(PrivacyPolicy)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_box = QTextBrowser(PrivacyPolicy)
        self.text_box.setObjectName("text_box")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_box.sizePolicy().hasHeightForWidth())
        self.text_box.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.text_box)

        self.ok = QPushButton(PrivacyPolicy)
        self.ok.setObjectName("ok")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.ok, 0, Qt.AlignHCenter)

        self.retranslateUi(PrivacyPolicy)

        QMetaObject.connectSlotsByName(PrivacyPolicy)

    # setupUi

    def retranslateUi(self, PrivacyPolicy):
        PrivacyPolicy.setWindowTitle(QCoreApplication.translate("PrivacyPolicy", "Privacy Policy", None))
        self.ok.setText(QCoreApplication.translate("PrivacyPolicy", "OK", None))

    # retranslateUi
