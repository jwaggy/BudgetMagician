import sys
from pathlib import Path

from PySide6.QtCore import QStandardPaths

from BudgetMagician.parameters.env import IS_WINDOWS, IS_FROZEN
from BudgetMagician.settings import IS_DEV, MODULE_DIR

PORTABLE_APP_DATA_DIR = "portable_data"


def is_portable() -> bool:
    if not (IS_WINDOWS and IS_FROZEN):
        return False

    portable_data_dir = Path(sys.executable).parent / PORTABLE_APP_DATA_DIR

    return portable_data_dir.is_dir()


def get_app_data_dir() -> Path:
    if is_portable():
        return Path(sys.executable).parent / PORTABLE_APP_DATA_DIR

    if not IS_DEV:
        app_dir = Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation))
    else:
        app_dir = MODULE_DIR.parent / PORTABLE_APP_DATA_DIR

    if not app_dir.is_dir():
        app_dir.mkdir(parents=True)

    return app_dir


def get_desktop_dir() -> Path:
    return Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation))
