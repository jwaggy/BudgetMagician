import sys

from PySide6.QtWidgets import QApplication
from endstech_shared.Settings import Settings
from endstech_shared.directory_utils import get_app_data_dir
from endstech_shared.environment_utils import IS_WINDOWS, IS_FROZEN
from qt_material import apply_stylesheet

from BudgetMagician.init.init_translator import init_translator
from BudgetMagician.settings import IS_DEV, MODULE_DIR, default_settings


def init_app() -> QApplication:
    app = QApplication(sys.argv)

    from BudgetMagician import resources_bin

    style_sheet_setting = Settings(get_app_data_dir(IS_WINDOWS, IS_FROZEN, IS_DEV, MODULE_DIR) / "settings.ini", default_settings).get("window/theme")

    light_or_dark = style_sheet_setting.split("_")[0]

    apply_stylesheet(app, theme=style_sheet_setting, invert_secondary=True if light_or_dark == "light" else False)

    init_translator(app)

    return app
