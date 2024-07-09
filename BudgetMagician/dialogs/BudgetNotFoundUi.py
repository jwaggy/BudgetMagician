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
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget


class Ui_BudgetNotFound(object):
    def setupUi(self, BudgetNotFound):
        if not BudgetNotFound.objectName():
            BudgetNotFound.setObjectName("BudgetNotFound")
        BudgetNotFound.resize(392, 324)
        self.verticalLayout = QVBoxLayout(BudgetNotFound)
        self.verticalLayout.setObjectName("verticalLayout")
        self.new_button = QPushButton(BudgetNotFound)
        self.new_button.setObjectName("new_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_button.sizePolicy().hasHeightForWidth())
        self.new_button.setSizePolicy(sizePolicy)
        self.new_button.setMinimumSize(QSize(200, 100))

        self.verticalLayout.addWidget(self.new_button, 0, Qt.AlignHCenter)

        self.open_button = QPushButton(BudgetNotFound)
        self.open_button.setObjectName("open_button")
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setMinimumSize(QSize(200, 100))
        self.open_button.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout.addWidget(self.open_button, 0, Qt.AlignHCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.budget_name_label = QLabel(BudgetNotFound)
        self.budget_name_label.setObjectName("budget_name_label")

        self.horizontalLayout_2.addWidget(self.budget_name_label)

        self.file_text = QLineEdit(BudgetNotFound)
        self.file_text.setObjectName("file_text")
        self.file_text.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_2.addWidget(self.file_text)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QPushButton(BudgetNotFound)
        self.ok_button.setObjectName("ok_button")
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.ok_button)

        self.cancel_button = QPushButton(BudgetNotFound)
        self.cancel_button.setObjectName("cancel_button")
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cancel_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(BudgetNotFound)

        QMetaObject.connectSlotsByName(BudgetNotFound)

    # setupUi

    def retranslateUi(self, BudgetNotFound):
        BudgetNotFound.setWindowTitle(QCoreApplication.translate("BudgetNotFound", "Open Budget", None))
        self.new_button.setText(QCoreApplication.translate("BudgetNotFound", "New Budget", None))
        self.open_button.setText(QCoreApplication.translate("BudgetNotFound", "Open Budget", None))
        self.budget_name_label.setText(QCoreApplication.translate("BudgetNotFound", "Budget FIle", None))
        self.ok_button.setText(QCoreApplication.translate("BudgetNotFound", "OK", None))
        self.cancel_button.setText(QCoreApplication.translate("BudgetNotFound", "Cancel", None))

    # retranslateUi
