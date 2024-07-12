import logging
from pathlib import Path

from endstech_shared.languages import get_system_language

from BudgetMagician.parameters.Language import LANGUAGES

MODULE_DIR = Path(__file__).resolve().parent

MIGRATIONS_DIR = MODULE_DIR / "migrations"

IS_DEV = False

DATABASE_DRIVER = "sqlite"

default_settings = {
    "window/language": get_system_language(LANGUAGES),
    "window/maximized": True,
    "window/theme": "light_blue.xml",
    "budget/name": "",
    "logging/log_level": logging.INFO,
    "logging/log_limit_size": 10,
    "logging/log_limit_backups": 1,
}
