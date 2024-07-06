from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QDialog

from BudgetMagician.dialogs.PrivacyPolicyUi import Ui_PrivacyPolicy


class PrivacyPolicy(QDialog, Ui_PrivacyPolicy):
    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        url = QUrl.fromLocalFile(":misc/PRIVACY.md")
        self.text_box.setSource(url)
        self.ok.clicked.connect(self.close)