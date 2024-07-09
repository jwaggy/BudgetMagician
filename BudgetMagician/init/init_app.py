import sys

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from BudgetMagician.init.init_translator import init_translator
from BudgetMagician.utils.Settings import Settings


def init_app() -> QApplication:
    app = QApplication(sys.argv)

    from BudgetMagician import resources_bin

    style_sheet_setting = Settings().get("window/theme")

    light_or_dark = style_sheet_setting.split("_")[0]

    apply_stylesheet(app, theme=style_sheet_setting, invert_secondary=True if light_or_dark == "light" else False)

    init_translator(app)

    return app
