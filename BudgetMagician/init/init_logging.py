from PySide6.QtCore import qInstallMessageHandler
from endstech_shared.Settings import Settings
from endstech_shared.directory_utils import get_app_data_dir
from endstech_shared.environment_utils import IS_WINDOWS, IS_FROZEN
from endstech_shared.logging_utils import configure_log, QtLogHandler

from BudgetMagician.settings import IS_DEV, MODULE_DIR, default_settings
from BudgetMagician.version import __app_name__


def init_logging():
    log_path = get_app_data_dir(IS_WINDOWS, IS_FROZEN, IS_DEV, MODULE_DIR) / f"{__app_name__.lower()}.log"

    max_log_size = max(Settings(get_app_data_dir(IS_WINDOWS, IS_FROZEN, IS_DEV, MODULE_DIR) / "settings.ini", default_settings).get("logging/log_limit_size"), 1) * 1024 * 1024

    max_log_backups = max(Settings(get_app_data_dir(IS_WINDOWS, IS_FROZEN, IS_DEV, MODULE_DIR) / "settings.ini", default_settings).get("logging/log_limit_backups"), 1)

    configure_log(log_path, Settings(get_app_data_dir(IS_WINDOWS, IS_FROZEN, IS_DEV, MODULE_DIR) / "settings.ini", default_settings).get("logging/log_level"), max_log_size, max_log_backups)

    qt_logger = QtLogHandler()

    qInstallMessageHandler(qt_logger.handle)
