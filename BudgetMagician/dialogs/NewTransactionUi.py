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
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDateEdit,
    QDialog,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_NewTransaction(object):
    def setupUi(self, NewTransaction):
        if not NewTransaction.objectName():
            NewTransaction.setObjectName("NewTransaction")
        NewTransaction.resize(400, 300)
        self.verticalLayout = QVBoxLayout(NewTransaction)
        self.verticalLayout.setObjectName("verticalLayout")
        self.new_transaction_title_label = QLabel(NewTransaction)
        self.new_transaction_title_label.setObjectName("new_transaction_title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_transaction_title_label.sizePolicy().hasHeightForWidth())
        self.new_transaction_title_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.new_transaction_title_label.setFont(font)

        self.verticalLayout.addWidget(self.new_transaction_title_label, 0, Qt.AlignHCenter)

        self.line = QFrame(NewTransaction)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.date_label = QLabel(NewTransaction)
        self.date_label.setObjectName("date_label")
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.date_label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.date_label)

        self.date = QDateEdit(NewTransaction)
        self.date.setObjectName("date")
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.date)

        self.category_label = QLabel(NewTransaction)
        self.category_label.setObjectName("category_label")
        sizePolicy.setHeightForWidth(self.category_label.sizePolicy().hasHeightForWidth())
        self.category_label.setSizePolicy(sizePolicy)
        self.category_label.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.category_label)

        self.category = QComboBox(NewTransaction)
        self.category.setObjectName("category")
        sizePolicy.setHeightForWidth(self.category.sizePolicy().hasHeightForWidth())
        self.category.setSizePolicy(sizePolicy)
        self.category.setFocusPolicy(Qt.WheelFocus)
        self.category.setEditable(False)
        self.category.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.category)

        self.payee_label = QLabel(NewTransaction)
        self.payee_label.setObjectName("payee_label")
        sizePolicy.setHeightForWidth(self.payee_label.sizePolicy().hasHeightForWidth())
        self.payee_label.setSizePolicy(sizePolicy)
        self.payee_label.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.payee_label)

        self.payee = QComboBox(NewTransaction)
        self.payee.setObjectName("payee")
        sizePolicy.setHeightForWidth(self.payee.sizePolicy().hasHeightForWidth())
        self.payee.setSizePolicy(sizePolicy)
        self.payee.setFocusPolicy(Qt.ClickFocus)
        self.payee.setEditable(True)
        self.payee.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.payee)

        self.memo_label = QLabel(NewTransaction)
        self.memo_label.setObjectName("memo_label")
        sizePolicy.setHeightForWidth(self.memo_label.sizePolicy().hasHeightForWidth())
        self.memo_label.setSizePolicy(sizePolicy)
        self.memo_label.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.memo_label)

        self.memo = QLineEdit(NewTransaction)
        self.memo.setObjectName("memo")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.memo)

        self.amount_label = QLabel(NewTransaction)
        self.amount_label.setObjectName("amount_label")
        sizePolicy.setHeightForWidth(self.amount_label.sizePolicy().hasHeightForWidth())
        self.amount_label.setSizePolicy(sizePolicy)
        self.amount_label.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.amount_label)

        self.amount = QLineEdit(NewTransaction)
        self.amount.setObjectName("amount")
        sizePolicy.setHeightForWidth(self.amount.sizePolicy().hasHeightForWidth())
        self.amount.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.amount)

        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QPushButton(NewTransaction)
        self.ok_button.setObjectName("ok_button")
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.ok_button)

        self.cancel_button = QPushButton(NewTransaction)
        self.cancel_button.setObjectName("cancel_button")
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cancel_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(NewTransaction)

        QMetaObject.connectSlotsByName(NewTransaction)

    # setupUi

    def retranslateUi(self, NewTransaction):
        NewTransaction.setWindowTitle(QCoreApplication.translate("NewTransaction", "New Transaction", None))
        self.new_transaction_title_label.setText(QCoreApplication.translate("NewTransaction", "New Transaction", None))
        self.date_label.setText(QCoreApplication.translate("NewTransaction", "Date:", None))
        self.category_label.setText(QCoreApplication.translate("NewTransaction", "Category:", None))

        self.category.setToolTip("")

        self.payee_label.setText(QCoreApplication.translate("NewTransaction", "Payee:", None))

        self.payee.setToolTip(QCoreApplication.translate("NewTransaction", "Type here and press enter to add a payee", None))

        self.memo_label.setText(QCoreApplication.translate("NewTransaction", "Memo:", None))
        self.amount_label.setText(QCoreApplication.translate("NewTransaction", "Amount:", None))
        self.ok_button.setText(QCoreApplication.translate("NewTransaction", "OK", None))
        self.cancel_button.setText(QCoreApplication.translate("NewTransaction", "Cancel", None))

    # retranslateUi
