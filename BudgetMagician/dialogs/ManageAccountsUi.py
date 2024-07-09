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
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_ManageAccounts(object):
    def setupUi(self, ManageAccounts):
        if not ManageAccounts.objectName():
            ManageAccounts.setObjectName("ManageAccounts")
        ManageAccounts.resize(500, 452)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManageAccounts.sizePolicy().hasHeightForWidth())
        ManageAccounts.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ManageAccounts)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manage_accounts_label = QLabel(ManageAccounts)
        self.manage_accounts_label.setObjectName("manage_accounts_label")
        sizePolicy.setHeightForWidth(self.manage_accounts_label.sizePolicy().hasHeightForWidth())
        self.manage_accounts_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.manage_accounts_label.setFont(font)

        self.verticalLayout.addWidget(self.manage_accounts_label, 0, Qt.AlignHCenter)

        self.line = QFrame(ManageAccounts)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delete_existing_account_label = QLabel(ManageAccounts)
        self.delete_existing_account_label.setObjectName("delete_existing_account_label")
        sizePolicy.setHeightForWidth(self.delete_existing_account_label.sizePolicy().hasHeightForWidth())
        self.delete_existing_account_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.delete_existing_account_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.delete_existing_account_label)

        self.delete_combo_box = QComboBox(ManageAccounts)
        self.delete_combo_box.setObjectName("delete_combo_box")
        sizePolicy.setHeightForWidth(self.delete_combo_box.sizePolicy().hasHeightForWidth())
        self.delete_combo_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.delete_combo_box)

        self.delete_button = QPushButton(ManageAccounts)
        self.delete_button.setObjectName("delete_button")
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.delete_button)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_6 = QFrame(ManageAccounts)
        self.line_6.setObjectName("line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.name_label = QLabel(ManageAccounts)
        self.name_label.setObjectName("name_label")
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setFont(font1)

        self.verticalLayout.addWidget(self.name_label)

        self.name = QLineEdit(ManageAccounts)
        self.name.setObjectName("name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.name)

        self.line_2 = QFrame(ManageAccounts)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.current_balance_label = QLabel(ManageAccounts)
        self.current_balance_label.setObjectName("current_balance_label")
        sizePolicy.setHeightForWidth(self.current_balance_label.sizePolicy().hasHeightForWidth())
        self.current_balance_label.setSizePolicy(sizePolicy)
        self.current_balance_label.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.current_balance_label)

        self.date_of_current_balance_label = QLabel(ManageAccounts)
        self.date_of_current_balance_label.setObjectName("date_of_current_balance_label")
        sizePolicy.setHeightForWidth(self.date_of_current_balance_label.sizePolicy().hasHeightForWidth())
        self.date_of_current_balance_label.setSizePolicy(sizePolicy)
        self.date_of_current_balance_label.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.date_of_current_balance_label)

        self.current_balance = QLineEdit(ManageAccounts)
        self.current_balance.setObjectName("current_balance")
        sizePolicy.setHeightForWidth(self.current_balance.sizePolicy().hasHeightForWidth())
        self.current_balance.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.current_balance)

        self.current_balance_date = QDateEdit(ManageAccounts)
        self.current_balance_date.setObjectName("current_balance_date")
        sizePolicy.setHeightForWidth(self.current_balance_date.sizePolicy().hasHeightForWidth())
        self.current_balance_date.setSizePolicy(sizePolicy)
        self.current_balance_date.setCalendarPopup(True)
        self.current_balance_date.setDate(QDate(2023, 9, 1))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.current_balance_date)

        self.verticalLayout.addLayout(self.formLayout)

        self.line_3 = QFrame(ManageAccounts)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.type_label = QLabel(ManageAccounts)
        self.type_label.setObjectName("type_label")
        sizePolicy.setHeightForWidth(self.type_label.sizePolicy().hasHeightForWidth())
        self.type_label.setSizePolicy(sizePolicy)
        self.type_label.setFont(font1)

        self.verticalLayout.addWidget(self.type_label)

        self.type_combo = QComboBox(ManageAccounts)
        self.type_combo.setObjectName("type_combo")
        sizePolicy.setHeightForWidth(self.type_combo.sizePolicy().hasHeightForWidth())
        self.type_combo.setSizePolicy(sizePolicy)
        self.type_combo.setMinimumSize(QSize(160, 0))
        font2 = QFont()
        font2.setBold(False)
        self.type_combo.setFont(font2)
        self.type_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout.addWidget(self.type_combo)

        self.line_5 = QFrame(ManageAccounts)
        self.line_5.setObjectName("line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.budget_account_radio = QRadioButton(ManageAccounts)
        self.budget_account_radio.setObjectName("budget_account_radio")
        sizePolicy.setHeightForWidth(self.budget_account_radio.sizePolicy().hasHeightForWidth())
        self.budget_account_radio.setSizePolicy(sizePolicy)
        self.budget_account_radio.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.budget_account_radio)

        self.off_budget_radio = QRadioButton(ManageAccounts)
        self.off_budget_radio.setObjectName("off_budget_radio")
        sizePolicy.setHeightForWidth(self.off_budget_radio.sizePolicy().hasHeightForWidth())
        self.off_budget_radio.setSizePolicy(sizePolicy)
        self.off_budget_radio.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.off_budget_radio)

        self.budget_account_recommend_label = QLabel(ManageAccounts)
        self.budget_account_recommend_label.setObjectName("budget_account_recommend_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.budget_account_recommend_label.sizePolicy().hasHeightForWidth())
        self.budget_account_recommend_label.setSizePolicy(sizePolicy2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.budget_account_recommend_label)

        self.off_budget_recommend_label = QLabel(ManageAccounts)
        self.off_budget_recommend_label.setObjectName("off_budget_recommend_label")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.off_budget_recommend_label)

        self.verticalLayout.addLayout(self.formLayout_2)

        self.line_4 = QFrame(ManageAccounts)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QPushButton(ManageAccounts)
        self.ok_button.setObjectName("ok_button")
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.ok_button)

        self.cancel_button = QPushButton(ManageAccounts)
        self.cancel_button.setObjectName("cancel_button")
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cancel_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ManageAccounts)

        QMetaObject.connectSlotsByName(ManageAccounts)

    # setupUi

    def retranslateUi(self, ManageAccounts):
        ManageAccounts.setWindowTitle(QCoreApplication.translate("ManageAccounts", "Manage Accounts", None))
        self.manage_accounts_label.setText(QCoreApplication.translate("ManageAccounts", "Manage Your Accounts", None))
        self.delete_existing_account_label.setText(QCoreApplication.translate("ManageAccounts", "Delete an existing account:", None))
        self.delete_button.setText(QCoreApplication.translate("ManageAccounts", "Delete", None))
        self.name_label.setText(QCoreApplication.translate("ManageAccounts", "Name:", None))
        self.current_balance_label.setText(QCoreApplication.translate("ManageAccounts", "Current Balance:", None))
        self.date_of_current_balance_label.setText(QCoreApplication.translate("ManageAccounts", "Date of Current Balance", None))
        self.type_label.setText(QCoreApplication.translate("ManageAccounts", "Type:", None))
        self.type_combo.setPlaceholderText(QCoreApplication.translate("ManageAccounts", "Select an Account Type", None))
        self.budget_account_radio.setText(QCoreApplication.translate("ManageAccounts", "Budget Account", None))
        self.off_budget_radio.setText(QCoreApplication.translate("ManageAccounts", "Off Budget", None))
        self.budget_account_recommend_label.setText("")
        self.off_budget_recommend_label.setText("")
        self.ok_button.setText(QCoreApplication.translate("ManageAccounts", "OK", None))
        self.cancel_button.setText(QCoreApplication.translate("ManageAccounts", "Cancel", None))

    # retranslateUi
