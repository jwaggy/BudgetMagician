import logging

from qt_material import list_themes

from BudgetMagician.parameters.Language import LANGUAGES
from BudgetMagician.utils import logging as logging_utils
from BudgetMagician.utils.qt import translate

LOG_LEVELS = {
    logging_utils.DISABLED: translate("ErrorLevel", "Disabled"),
    logging.CRITICAL: translate("ErrorLevel", "Critical"),
    logging.ERROR: translate("ErrorLevel", "Error"),
    logging.WARNING: translate("ErrorLevel", "Warning"),
    logging.INFO: translate("ErrorLevel", "Info"),
    logging.DEBUG: translate("ErrorLevel", "Debug"),
}

MONTHS = {
    1: translate("Month", "January"),
    2: translate("Month", "February"),
    3: translate("Month", "March"),
    4: translate("Month", "April"),
    5: translate("Month", "May"),
    6: translate("Month", "June"),
    7: translate("Month", "July"),
    8: translate("Month", "August"),
    9: translate("Month", "September"),
    10: translate("Month", "October"),
    11: translate("Month", "November"),
    12: translate("Month", "December"),
}

ABBREVIATED_MONTHS = {
    1: translate("Month", "Jan"),
    2: translate("Month", "Feb"),
    3: translate("Month", "Mar"),
    4: translate("Month", "Apr"),
    5: translate("Month", "May"),
    6: translate("Month", "Jun"),
    7: translate("Month", "Jul"),
    8: translate("Month", "Aug"),
    9: translate("Month", "Sept"),
    10: translate("Month", "Oct"),
    11: translate("Month", "Nov"),
    12: translate("Month", "Dec"),
}

ACCOUNT_TYPES = {
    1: translate("AccountType", "Checking"),
    2: translate("AccountType", "Savings"),
    3: translate("AccountType", "Credit Card"),
    4: translate("AccountType", "Cash"),
    5: translate("AccountType", "Line of Credit or Other Credit"),
    6: translate("AccountType", "Paypal"),
    7: translate("AccountType", "Merchant Account"),
    8: translate("AccountType", "Investment Account"),
    9: translate("AccountType", "Mortgage"),
    10: translate("AccountType", "Other Asset (House, Car, etc)"),
    11: translate("AccountType", "Other Loan or Liability"),
}


def get_language_combo_dict() -> dict:
    return {k.code: {"title": k.title_native, "icon": f":icons/flags/{k.code}.svg"} for k in LANGUAGES}


def get_theme_combo_dict() -> dict:
    theme_list = list_themes()
    theme_dict = {}

    for theme in theme_list:
        theme_dict[theme] = theme.split(".")[0].replace("_", " ")

    return theme_dict
