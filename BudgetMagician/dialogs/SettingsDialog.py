import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog, QMessageBox

from BudgetMagician.dialogs.SettingsUi import Ui_Settings
from BudgetMagician.parameters.combobox_constants import LOG_LEVELS, get_language_combo_dict, get_theme_combo_dict
from BudgetMagician.utils.Settings import Settings
from BudgetMagician.utils.combox_utils import fill_combo_box, fill_combo_box_with_icon, set_combo_box_by_data
from BudgetMagician.utils.qt import translate


class SettingsDialog(QDialog, Ui_Settings):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.installEventFilter(self)
        self.fill_ui()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.save_settings)

    def fill_ui(self):
        self.fill_backup_line()
        self.fill_log_limit_line()
        self.fill_log_levels()
        self.fill_languages()
        self.fill_themes()

    def fill_log_levels(self):
        fill_combo_box(self.logging_combo, LOG_LEVELS)

        current_log_level = Settings().get("logging/log_level")

        set_combo_box_by_data(self.logging_combo, current_log_level)

    def fill_languages(self):
        fill_combo_box_with_icon(self.language_combo, get_language_combo_dict())

        current_language = Settings().get("window/language")

        set_combo_box_by_data(self.language_combo, current_language)

    def fill_themes(self):
        fill_combo_box(self.theme_combo, get_theme_combo_dict())

        current_theme = Settings().get("window/theme")

        set_combo_box_by_data(self.theme_combo, current_theme)

    def fill_backup_line(self):
        backup_limit = Settings().get("logging/log_limit_backups")

        self.log_backups_line_edit.setText(str(backup_limit))

        int_validator = QIntValidator(1, 10, self)
        self.log_backups_line_edit.setValidator(int_validator)

    def fill_log_limit_line(self):
        log_limit = Settings().get("logging/log_limit_size")

        self.mb_line_edit.setText(str(log_limit))

        int_validator = QIntValidator(1, 1024, self)
        self.mb_line_edit.setValidator(int_validator)

    def save_settings(self):
        old_settings = Settings().get_all()
        settings_changed = False

        log_backups = int(self.log_backups_line_edit.text())
        if log_backups != old_settings["logging/log_limit_backups"]:
            settings_changed = True
            Settings().set("logging/log_limit_backups", log_backups)

        log_size = int(self.mb_line_edit.text())
        if log_size != old_settings["logging/log_limit_size"]:
            settings_changed = True
            Settings().set("logging/log_limit_size", log_size)

        log_level = self.logging_combo.currentData()
        if log_level != old_settings["logging/log_level"]:
            settings_changed = True
            Settings().set("logging/log_level", log_level)

        language = self.language_combo.currentData()
        if language != old_settings["window/language"]:
            settings_changed = True
            Settings().set("window/language", language)

        theme = self.theme_combo.currentData()
        if theme != old_settings["window/theme"]:
            settings_changed = True
            Settings().set("window/theme", theme)

        if settings_changed:
            QMessageBox.information(
                self, translate("Dialog", "Information"), translate("Information", "Please restart the application for the settings to take effect."), QMessageBox.StandardButton.Ok
            )

        self.close()

    def eventFilter(self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent) -> bool:
        if arg__1 is self and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Escape, Qt.Key.Key_Enter):
                return True
        return super().eventFilter(arg__1, arg__2)
