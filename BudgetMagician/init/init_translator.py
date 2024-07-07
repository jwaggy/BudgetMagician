import logging

from PySide6.QtCore import QLibraryInfo, QLocale, QTranslator
from PySide6.QtWidgets import QApplication

from BudgetMagician.parameters.env import IS_WINDOWS, IS_FROZEN, PYINSTALLER_LIB_ROOT
from BudgetMagician.utils.Settings import Settings


def init_translator(app: QApplication):
    log = logging.getLogger(__name__)

    language = Settings().get("window/language")

    if language == "en_US":
        return

    log.debug(f"Loading translation for {language}")

    if IS_FROZEN and IS_WINDOWS:
        qt_translations_path = str(PYINSTALLER_LIB_ROOT / "PySide6" / "Qt6" / "translations")
    else:
        qt_translations_path = QLibraryInfo.location(QLibraryInfo.LibraryPath.TranslationsPath)

    log.debug(f"Qt translations path: {qt_translations_path}")

    qt_translator = QTranslator(app)

    if qt_translator.load(QLocale(language), "qtbase_", "", qt_translations_path):
        app.installTranslator(qt_translator)
    else:
        log.warning(f"Failed to load Qt translations for {language}.")

    translator = QTranslator(app)

    if translator.load(language, ":/translations/"):
        app.installTranslator(translator)
    else:
        log.warning(f"Failed to load translations for {language}.")
