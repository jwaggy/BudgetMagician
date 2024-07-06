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
from PySide6.QtWidgets import QApplication, QDateEdit, QDialog, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget


class Ui_ReconcileAccount(object):
    def setupUi(self, ReconcileAccount):
        if not ReconcileAccount.objectName():
            ReconcileAccount.setObjectName("ReconcileAccount")
        ReconcileAccount.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ReconcileAccount)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QLabel(ReconcileAccount)
        self.title_label.setObjectName("title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.title_label.setFont(font)

        self.verticalLayout.addWidget(self.title_label, 0, Qt.AlignHCenter)

        self.instructions_label = QLabel(ReconcileAccount)
        self.instructions_label.setObjectName("instructions_label")
        sizePolicy.setHeightForWidth(self.instructions_label.sizePolicy().hasHeightForWidth())
        self.instructions_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.instructions_label.setFont(font1)

        self.verticalLayout.addWidget(self.instructions_label)

        self.line = QFrame(ReconcileAccount)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.date_to_reconcile_label = QLabel(ReconcileAccount)
        self.date_to_reconcile_label.setObjectName("date_to_reconcile_label")
        sizePolicy.setHeightForWidth(self.date_to_reconcile_label.sizePolicy().hasHeightForWidth())
        self.date_to_reconcile_label.setSizePolicy(sizePolicy)
        self.date_to_reconcile_label.setFont(font1)

        self.horizontalLayout.addWidget(self.date_to_reconcile_label)

        self.date = QDateEdit(ReconcileAccount)
        self.date.setObjectName("date")
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.date)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.account_balance_label = QLabel(ReconcileAccount)
        self.account_balance_label.setObjectName("account_balance_label")
        sizePolicy.setHeightForWidth(self.account_balance_label.sizePolicy().hasHeightForWidth())
        self.account_balance_label.setSizePolicy(sizePolicy)
        self.account_balance_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.account_balance_label)

        self.amount = QLineEdit(ReconcileAccount)
        self.amount.setObjectName("amount")
        self.amount.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_2.addWidget(self.amount)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.your_cleared_balance_is_label = QLabel(ReconcileAccount)
        self.your_cleared_balance_is_label.setObjectName("your_cleared_balance_is_label")
        sizePolicy.setHeightForWidth(self.your_cleared_balance_is_label.sizePolicy().hasHeightForWidth())
        self.your_cleared_balance_is_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.your_cleared_balance_is_label)

        self.cleared_balance = QLabel(ReconcileAccount)
        self.cleared_balance.setObjectName("cleared_balance")
        sizePolicy.setHeightForWidth(self.cleared_balance.sizePolicy().hasHeightForWidth())
        self.cleared_balance.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.cleared_balance)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ok_button = QPushButton(ReconcileAccount)
        self.ok_button.setObjectName("ok_button")
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.ok_button)

        self.cancel_button = QPushButton(ReconcileAccount)
        self.cancel_button.setObjectName("cancel_button")
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.cancel_button)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(ReconcileAccount)

        QMetaObject.connectSlotsByName(ReconcileAccount)

    # setupUi

    def retranslateUi(self, ReconcileAccount):
        ReconcileAccount.setWindowTitle(QCoreApplication.translate("ReconcileAccount", "Reconcile Account", None))
        self.title_label.setText(QCoreApplication.translate("ReconcileAccount", "Reconcile Account", None))
        self.instructions_label.setText(QCoreApplication.translate("ReconcileAccount", "Enter your current account balance from your statement.", None))
        self.date_to_reconcile_label.setText(QCoreApplication.translate("ReconcileAccount", "Date to reconcile against:", None))
        self.account_balance_label.setText(QCoreApplication.translate("ReconcileAccount", "Account balance on that date:", None))
        self.your_cleared_balance_is_label.setText(QCoreApplication.translate("ReconcileAccount", "Your cleared BudgetMagician balance is: ", None))
        self.cleared_balance.setText("")
        self.ok_button.setText(QCoreApplication.translate("ReconcileAccount", "OK", None))
        self.cancel_button.setText(QCoreApplication.translate("ReconcileAccount", "Cancel", None))

    # retranslateUi
