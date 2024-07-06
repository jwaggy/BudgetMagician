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
    QAbstractButton,
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QSpacerItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName("Settings")
        Settings.resize(800, 600)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QTabWidget(Settings)
        self.tabs.setObjectName("tabs")
        self.tabs.setFocusPolicy(Qt.TabFocus)
        self.Theme = QWidget()
        self.Theme.setObjectName("Theme")
        self.horizontalLayoutWidget_3 = QWidget(self.Theme)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(200, 0, 361, 201))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.theme_combo = QComboBox(self.horizontalLayoutWidget_3)
        self.theme_combo.setObjectName("theme_combo")
        sizePolicy.setHeightForWidth(self.theme_combo.sizePolicy().hasHeightForWidth())
        self.theme_combo.setSizePolicy(sizePolicy)
        self.theme_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_4.addWidget(self.theme_combo)

        self.tabs.addTab(self.Theme, "")
        self.language = QWidget()
        self.language.setObjectName("language")
        self.horizontalLayoutWidget_2 = QWidget(self.language)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(200, 0, 361, 201))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.language_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.language_combo.setObjectName("language_combo")
        sizePolicy.setHeightForWidth(self.language_combo.sizePolicy().hasHeightForWidth())
        self.language_combo.setSizePolicy(sizePolicy)
        self.language_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_3.addWidget(self.language_combo)

        self.tabs.addTab(self.language, "")
        self.logging = QWidget()
        self.logging.setObjectName("logging")
        self.horizontalLayout_2 = QHBoxLayout(self.logging)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(self.logging)
        self.label.setObjectName("label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.logging_combo = QComboBox(self.logging)
        self.logging_combo.setObjectName("logging_combo")
        sizePolicy.setHeightForWidth(self.logging_combo.sizePolicy().hasHeightForWidth())
        self.logging_combo.setSizePolicy(sizePolicy)
        self.logging_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.logging_combo)

        self.log_backups_line_edit = QLineEdit(self.logging)
        self.log_backups_line_edit.setObjectName("log_backups_line_edit")
        sizePolicy.setHeightForWidth(self.log_backups_line_edit.sizePolicy().hasHeightForWidth())
        self.log_backups_line_edit.setSizePolicy(sizePolicy)
        self.log_backups_line_edit.setFocusPolicy(Qt.ClickFocus)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.log_backups_line_edit)

        self.label_3 = QLabel(self.logging)
        self.label_3.setObjectName("label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.label_2 = QLabel(self.logging)
        self.label_2.setObjectName("label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.mb_line_edit = QLineEdit(self.logging)
        self.mb_line_edit.setObjectName("mb_line_edit")
        sizePolicy.setHeightForWidth(self.mb_line_edit.sizePolicy().hasHeightForWidth())
        self.mb_line_edit.setSizePolicy(sizePolicy)
        self.mb_line_edit.setFocusPolicy(Qt.ClickFocus)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.mb_line_edit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(6, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.horizontalLayout_2.addLayout(self.formLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.tabs.addTab(self.logging, "")

        self.verticalLayout.addWidget(self.tabs)

        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignHCenter)

        self.retranslateUi(Settings)

        self.tabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Settings)

    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", "Settings", None))
        self.label_5.setText(QCoreApplication.translate("Settings", "Theme Selection", None))
        self.tabs.setTabText(self.tabs.indexOf(self.Theme), QCoreApplication.translate("Settings", "Theme", None))
        self.label_4.setText(QCoreApplication.translate("Settings", "Language Selection", None))
        self.tabs.setTabText(self.tabs.indexOf(self.language), QCoreApplication.translate("Settings", "Language", None))
        self.label.setText(QCoreApplication.translate("Settings", "Logging Level", None))
        self.label_3.setText(QCoreApplication.translate("Settings", "Number of log backups", None))
        self.label_2.setText(QCoreApplication.translate("Settings", "MB per log file", None))
        self.tabs.setTabText(self.tabs.indexOf(self.logging), QCoreApplication.translate("Settings", "Logging", None))

    # retranslateUi
