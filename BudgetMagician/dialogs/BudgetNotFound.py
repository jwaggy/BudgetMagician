from pathlib import Path
from typing import Union

import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox

from BudgetMagician.dialogs.BudgetNotFoundUi import Ui_BudgetNotFound
from BudgetMagician.utils.Settings import Settings
from BudgetMagician.utils.dir import get_app_data_dir
from BudgetMagician.utils.qt import translate


class BudgetNotFound(QDialog, Ui_BudgetNotFound):
    budget_name_changed = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.file_name: Union[tuple[str, str], tuple[str]] = ("", "")
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.installEventFilter(self)
        self.new_button.clicked.connect(self.open_new_budget_file_dialog)
        self.open_button.clicked.connect(self.open_old_budget_file_dialog)
        self.ok_button.clicked.connect(self.ok_budget_file_button)
        self.cancel_button.clicked.connect(self.close)
        self.file_text.textChanged.connect(self.check_enabled)

    @Slot()
    def open_old_budget_file_dialog(self):
        open_dir = get_app_data_dir()
        self.file_name = QFileDialog.getOpenFileName(self, translate("FileDialog", "Open Existing Budget"), str(open_dir), translate("FileDialog", "Budgets (*.bgt)"))
        self.file_text.setText(self.file_name[0])

    @Slot()
    def open_new_budget_file_dialog(self):
        open_dir = get_app_data_dir()
        self.file_name = QFileDialog.getSaveFileName(self, translate("FileDialog", "Open New Budget"), str(open_dir), translate("FileDialog", "Budgets (*.bgt)"))
        self.file_text.setText(self.file_name[0])

    @Slot()
    def ok_budget_file_button(self):
        file_path = Path(self.file_text.text())
        if len(str(file_path)) > 4 and file_path.name.split(".")[1] == "bgt":
            self.file_name = (str(file_path),)

            if file_path.parent.is_dir():
                Settings().set("budget/name", str(file_path))
                self.budget_name_changed.emit()
                self.close()
            else:
                QMessageBox.warning(
                    self, translate("Dialog", "Warning"), translate("Warning", "The file directory provided doesn't exist or is invalid."), QMessageBox.StandardButton.Ok
                )
        else:
            QMessageBox.information(
                self,
                translate("Dialog", "Information"),
                translate("Information", "You must provide a file name before continuing ending with .bgt."),
                QMessageBox.StandardButton.Ok,
            )
            
    @Slot()
    def check_enabled(self):
        enabled = bool(self.file_text.text())
        self.ok_button.setEnabled(enabled)

    def open(self) -> None:
        self.file_text.setText("")
        self.ok_button.setEnabled(False)
        return super().open()

    def eventFilter(self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent) -> bool:
        if arg__1 is self and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Escape, Qt.Key.Key_Enter):
                return True
        return super().eventFilter(arg__1, arg__2)
