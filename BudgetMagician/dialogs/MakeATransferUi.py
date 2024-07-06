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


class Ui_MakeATransfer(object):
    def setupUi(self, MakeATransfer):
        if not MakeATransfer.objectName():
            MakeATransfer.setObjectName("MakeATransfer")
        MakeATransfer.resize(400, 300)
        self.verticalLayout = QVBoxLayout(MakeATransfer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QLabel(MakeATransfer)
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

        self.line = QFrame(MakeATransfer)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.from_label = QLabel(MakeATransfer)
        self.from_label.setObjectName("from_label")
        sizePolicy.setHeightForWidth(self.from_label.sizePolicy().hasHeightForWidth())
        self.from_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.from_label.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.from_label)

        self.from_combo = QComboBox(MakeATransfer)
        self.from_combo.setObjectName("from_combo")
        sizePolicy.setHeightForWidth(self.from_combo.sizePolicy().hasHeightForWidth())
        self.from_combo.setSizePolicy(sizePolicy)
        self.from_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.from_combo)

        self.to_label = QLabel(MakeATransfer)
        self.to_label.setObjectName("to_label")
        sizePolicy.setHeightForWidth(self.to_label.sizePolicy().hasHeightForWidth())
        self.to_label.setSizePolicy(sizePolicy)
        self.to_label.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.to_label)

        self.to_combo = QComboBox(MakeATransfer)
        self.to_combo.setObjectName("to_combo")
        sizePolicy.setHeightForWidth(self.to_combo.sizePolicy().hasHeightForWidth())
        self.to_combo.setSizePolicy(sizePolicy)
        self.to_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.to_combo)

        self.amount_label = QLabel(MakeATransfer)
        self.amount_label.setObjectName("amount_label")
        sizePolicy.setHeightForWidth(self.amount_label.sizePolicy().hasHeightForWidth())
        self.amount_label.setSizePolicy(sizePolicy)
        self.amount_label.setFont(font1)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.amount_label)

        self.amount = QLineEdit(MakeATransfer)
        self.amount.setObjectName("amount")
        sizePolicy.setHeightForWidth(self.amount.sizePolicy().hasHeightForWidth())
        self.amount.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.amount)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(6, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.date_label = QLabel(MakeATransfer)
        self.date_label.setObjectName("date_label")
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.date_label)

        self.date = QDateEdit(MakeATransfer)
        self.date.setObjectName("date")
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.date)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer_5)

        self.memo_label = QLabel(MakeATransfer)
        self.memo_label.setObjectName("memo_label")
        sizePolicy.setHeightForWidth(self.memo_label.sizePolicy().hasHeightForWidth())
        self.memo_label.setSizePolicy(sizePolicy)
        self.memo_label.setFont(font1)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.memo_label)

        self.memo = QLineEdit(MakeATransfer)
        self.memo.setObjectName("memo")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.memo)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(8, QFormLayout.FieldRole, self.verticalSpacer_6)

        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QPushButton(MakeATransfer)
        self.ok_button.setObjectName("ok_button")
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.ok_button)

        self.cancel_button = QPushButton(MakeATransfer)
        self.cancel_button.setObjectName("cancel_button")
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cancel_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MakeATransfer)

        QMetaObject.connectSlotsByName(MakeATransfer)

    # setupUi

    def retranslateUi(self, MakeATransfer):
        MakeATransfer.setWindowTitle(QCoreApplication.translate("MakeATransfer", "Make a Transfer", None))
        self.title_label.setText(QCoreApplication.translate("MakeATransfer", "Make a Transfer", None))
        self.from_label.setText(QCoreApplication.translate("MakeATransfer", "From:", None))
        self.to_label.setText(QCoreApplication.translate("MakeATransfer", "To:", None))
        self.amount_label.setText(QCoreApplication.translate("MakeATransfer", "Amount:", None))
        self.date_label.setText(QCoreApplication.translate("MakeATransfer", "Date:", None))
        self.memo_label.setText(QCoreApplication.translate("MakeATransfer", "Memo:", None))
        self.ok_button.setText(QCoreApplication.translate("MakeATransfer", "OK", None))
        self.cancel_button.setText(QCoreApplication.translate("MakeATransfer", "Cancel", None))

    # retranslateUi
