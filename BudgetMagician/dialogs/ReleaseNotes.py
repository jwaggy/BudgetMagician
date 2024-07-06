from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QDialog

from BudgetMagician.dialogs.ReleaseNotesUi import Ui_ReleaseNotes


class ReleaseNotes(QDialog, Ui_ReleaseNotes):
    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        url = QUrl.fromLocalFile(":misc/CHANGELOG.md")
        self.text_box.setSource(url)
        self.ok.clicked.connect(self.close)
