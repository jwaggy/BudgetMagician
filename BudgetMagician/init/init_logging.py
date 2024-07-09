from PySide6.QtCore import qInstallMessageHandler

from BudgetMagician.utils.Settings import Settings
from BudgetMagician.utils.logging import configure_log, QtLogHandler
from BudgetMagician.utils.dir import get_app_data_dir
from BudgetMagician.version import __app_name__


def init_logging():
    log_path = get_app_data_dir() / f"{__app_name__.lower()}.log"

    max_log_size = max(Settings().get("logging/log_limit_size"), 1) * 1024 * 1024

    max_log_backups = max(Settings().get("logging/log_limit_backups"), 1)

    configure_log(log_path, Settings().get("logging/log_level"), max_log_size, max_log_backups)

    qt_logger = QtLogHandler()

    qInstallMessageHandler(qt_logger.handle)
