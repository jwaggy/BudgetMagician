import logging
from contextlib import suppress
from enum import Enum
from pathlib import Path

from PySide6.QtCore import QSettings

from BudgetMagician.parameters.Language import get_system_language
from BudgetMagician.utils.dir import get_app_data_dir

_default_settings = {
    "window/language": get_system_language(),
    "window/maximized": True,
    "window/theme": "light_blue.xml",
    "budget/name": "",
    "logging/log_level": logging.DEBUG,
    "logging/log_limit_size": 10,
    "logging/log_limit_backups": 1,
}

SETTINGS = None


class _Settings:
    def __init__(self):
        settings_path = get_app_data_dir() / "settings.ini"

        self.settings = QSettings(str(settings_path), QSettings.IniFormat)

        logging.getLogger("Settings").debug(f"Settings path: {settings_path}")

    def _parse_enum(self, setting_type, setting):
        setting_value = self.settings.value(setting)

        if isinstance(setting_value, str):
            with suppress(ValueError):
                return setting_type(setting_value)

        return _default_settings[setting]

    @staticmethod
    def _get_storage_value(setting_value):
        if isinstance(setting_value, Enum):
            return setting_value.value

        if isinstance(setting_value, (Path, str)):
            return str(setting_value)

        return setting_value

    def get(self, setting):
        setting_type = type(_default_settings[setting])

        if issubclass(setting_type, Enum):
            return self._parse_enum(setting_type, setting)

        return self.settings.value(setting, _default_settings[setting], type=setting_type)

    def set(self, setting_name, setting_value):
        setting_type = type(_default_settings[setting_name])

        if setting_type != type(setting_value):
            raise ValueError(f"Setting {setting_name} is of type {setting_type} but value is of type {type(setting_value)}.")

        setting_value = self._get_storage_value(setting_value)

        self.settings.setValue(setting_name, setting_value)

    def reset(self, setting_name):
        self.set(setting_name, _default_settings[setting_name])

    def get_all(self) -> dict:
        return {k: self.get(k) for k in _default_settings}

    def sync(self):
        self.settings.sync()

    def sync_get(self, setting):
        self.sync()
        return self.get(setting)

    @property
    def filename(self):
        return self.settings.fileName()


def Settings():
    global SETTINGS

    if not SETTINGS:
        SETTINGS = _Settings()

    return SETTINGS


def default_field(setting_name):
    return Field(default_factory=lambda: Settings().get(setting_name))
