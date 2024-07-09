import logging
import os
import platform
import pprint
import sys
from logging.config import dictConfig
from pathlib import Path

from PySide6.QtCore import QtMsgType
from PySide6.QtCore import __version__ as qt_version

from BudgetMagician.parameters.env import IS_FROZEN
from BudgetMagician.utils.qt import is_qt_log_ignored
from BudgetMagician.version import __display_name__, __version__

DISABLED = logging.CRITICAL + 1


class QtLogHandler:
    log_level_map = {
        QtMsgType.QtDebugMsg: logging.DEBUG,
        QtMsgType.QtInfoMsg: logging.INFO,
        QtMsgType.QtWarningMsg: logging.WARNING,
        QtMsgType.QtCriticalMsg: logging.ERROR,
        QtMsgType.QtFatalMsg: logging.CRITICAL,
    }

    def __init__(self):
        self._log = logging.getLogger("QT")

    def handle(self, mode, context, message):
        if is_qt_log_ignored(message):
            return

        log_level = self.log_level_map[mode]

        if context.file is not None:
            log_message_head = f"qt_message_handler: line: {context.line}, func: {context.function},file: {context.file}."

            self._log.log(log_level, log_message_head)

        self._log.log(log_level, message.strip())


def configure_log(log_path: Path, log_level: int, max_log_size: int, max_log_backups: int):
    config = {
        "version": 1,
        "formatters": {"magic_formatter": {"format": "%(asctime)s (%(process)d) | %(name)s | %(levelname)s | %(message)s"}},
        "handlers": {
            "console": {"class": "logging.StreamHandler", "level": "DEBUG", "formatter": "magic_formatter", "stream": sys.__stderr__},
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "magic_formatter",
                "filename": str(log_path),
                "encoding": "utf8",
                "maxBytes": max_log_size,
                "backupCount": max_log_backups,
            },
        },
        "root": {"level": log_level, "handlers": ["console", "file"]},
    }

    dictConfig(config)


def set_root_level(log_level):
    logging.root.setLevel(log_level)


def log_environment():
    log = logging.getLogger("ENV")

    log.info(f"{__display_name__} v{__version__} starting")

    if log.getEffectiveLevel() != logging.DEBUG:
        return

    pretty_environment = pprint.pformat(dict(os.environ))[1:-1]

    environment_log = [
        "Environment info",
        "================",
        f"OS: {platform.platform()}",
        f"OS Version: {platform.version()}",
        f"OS Release: {platform.release()}",
        f"Python: {platform.python_version()}",
        f"Qt: {qt_version}",
        f"is_pyinstaller_frozen: {IS_FROZEN}",
        f"_MEIPASS: {sys._MEIPASS}" if IS_FROZEN else "",
        f"sys.argv: {sys.argv}",
        f"sys.executable: {sys.executable}",
        f"sys.path: {sys.path}",
        f"os.getcwd: {os.getcwd()}",
        "================",
        f"ENV\n {pretty_environment}",
        "================",
    ]

    for e in filter(None, environment_log):
        log.debug(e)
