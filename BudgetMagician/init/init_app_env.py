from PySide6.QtWidgets import QApplication
from endstech_shared.environment_utils import IS_WINDOWS

from BudgetMagician.version import __app_id__, __app_name__, __author_name__, __display_name__, __version__


def init_app_env_id():
    QApplication.setApplicationName(__app_name__)
    QApplication.setApplicationDisplayName(__display_name__)
    QApplication.setOrganizationName(__author_name__)
    QApplication.setApplicationVersion(__version__)


def init_app_env():
    if IS_WINDOWS:
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(__app_id__)

    init_app_env_id()
