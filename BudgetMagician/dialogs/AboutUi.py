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
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout, QWidget


class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName("About")
        About.resize(800, 700)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setModal(False)
        self.verticalLayout = QVBoxLayout(About)
        self.verticalLayout.setObjectName("verticalLayout")
        self.app_name_title = QLabel(About)
        self.app_name_title.setObjectName("app_name_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.app_name_title.sizePolicy().hasHeightForWidth())
        self.app_name_title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.app_name_title.setFont(font)

        self.verticalLayout.addWidget(self.app_name_title, 0, Qt.AlignHCenter)

        self.version = QLabel(About)
        self.version.setObjectName("version")
        sizePolicy1.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.version)

        self.info_box = QTextBrowser(About)
        self.info_box.setObjectName("info_box")
        sizePolicy.setHeightForWidth(self.info_box.sizePolicy().hasHeightForWidth())
        self.info_box.setSizePolicy(sizePolicy)
        self.info_box.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.info_box)

        self.citations_box = QTextBrowser(About)
        self.citations_box.setObjectName("citations_box")
        self.citations_box.setMinimumSize(QSize(0, 400))
        self.citations_box.setBaseSize(QSize(0, 0))
        self.citations_box.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.citations_box)

        self.ok = QPushButton(About)
        self.ok.setObjectName("ok")
        sizePolicy1.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.ok, 0, Qt.AlignHCenter)

        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)

    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", "About", None))
        self.app_name_title.setText("")
        self.version.setText("")
        self.ok.setText(QCoreApplication.translate("About", "OK", None))

    # retranslateUi
