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
from PySide6.QtWidgets import QApplication, QComboBox, QDialog, QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget


class Ui_ManageCategories(object):
    def setupUi(self, ManageCategories):
        if not ManageCategories.objectName():
            ManageCategories.setObjectName("ManageCategories")
        ManageCategories.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManageCategories.sizePolicy().hasHeightForWidth())
        ManageCategories.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ManageCategories)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QLabel(ManageCategories)
        self.title_label.setObjectName("title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.title_label.setFont(font)

        self.verticalLayout.addWidget(self.title_label, 0, Qt.AlignHCenter)

        self.line = QFrame(ManageCategories)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.category_delete_label = QLabel(ManageCategories)
        self.category_delete_label.setObjectName("category_delete_label")
        sizePolicy1.setHeightForWidth(self.category_delete_label.sizePolicy().hasHeightForWidth())
        self.category_delete_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setBold(True)
        self.category_delete_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.category_delete_label)

        self.category_combobox = QComboBox(ManageCategories)
        self.category_combobox.setObjectName("category_combobox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.category_combobox.sizePolicy().hasHeightForWidth())
        self.category_combobox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.category_combobox)

        self.delete_category_button = QPushButton(ManageCategories)
        self.delete_category_button.setObjectName("delete_category_button")
        sizePolicy1.setHeightForWidth(self.delete_category_button.sizePolicy().hasHeightForWidth())
        self.delete_category_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.delete_category_button)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.master_category_label = QLabel(ManageCategories)
        self.master_category_label.setObjectName("master_category_label")
        sizePolicy1.setHeightForWidth(self.master_category_label.sizePolicy().hasHeightForWidth())
        self.master_category_label.setSizePolicy(sizePolicy1)
        self.master_category_label.setFont(font1)

        self.horizontalLayout.addWidget(self.master_category_label)

        self.master_category_combo = QComboBox(ManageCategories)
        self.master_category_combo.setObjectName("master_category_combo")
        self.master_category_combo.setFocusPolicy(Qt.ClickFocus)
        self.master_category_combo.setEditable(True)
        self.master_category_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout.addWidget(self.master_category_combo)

        self.delete_button = QPushButton(ManageCategories)
        self.delete_button.setObjectName("delete_button")
        sizePolicy1.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy1)
        self.delete_button.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout.addWidget(self.delete_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.category_label = QLabel(ManageCategories)
        self.category_label.setObjectName("category_label")
        sizePolicy1.setHeightForWidth(self.category_label.sizePolicy().hasHeightForWidth())
        self.category_label.setSizePolicy(sizePolicy1)
        self.category_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.category_label)

        self.category_line_edit = QLineEdit(ManageCategories)
        self.category_line_edit.setObjectName("category_line_edit")

        self.horizontalLayout_2.addWidget(self.category_line_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ok_button = QPushButton(ManageCategories)
        self.ok_button.setObjectName("ok_button")
        sizePolicy1.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.ok_button)

        self.cancel_button = QPushButton(ManageCategories)
        self.cancel_button.setObjectName("cancel_button")
        sizePolicy1.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.cancel_button)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(ManageCategories)

        QMetaObject.connectSlotsByName(ManageCategories)

    # setupUi

    def retranslateUi(self, ManageCategories):
        ManageCategories.setWindowTitle(QCoreApplication.translate("ManageCategories", "Manage Categories", None))
        self.title_label.setText(QCoreApplication.translate("ManageCategories", "Manage Categories", None))
        self.category_delete_label.setText(QCoreApplication.translate("ManageCategories", "Delete a Category:", None))
        self.delete_category_button.setText(QCoreApplication.translate("ManageCategories", "Delete", None))
        self.master_category_label.setText(QCoreApplication.translate("ManageCategories", "Master Category:", None))

        self.master_category_combo.setToolTip(QCoreApplication.translate("ManageCategories", "Type here and press enter to add a category", None))

        self.delete_button.setText(QCoreApplication.translate("ManageCategories", "Delete", None))
        self.category_label.setText(QCoreApplication.translate("ManageCategories", "Category:", None))
        self.ok_button.setText(QCoreApplication.translate("ManageCategories", "OK", None))
        self.cancel_button.setText(QCoreApplication.translate("ManageCategories", "Cancel", None))

    # retranslateUi
