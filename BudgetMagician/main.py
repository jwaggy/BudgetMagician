import sys

from endstech_shared.environment_utils import IS_FROZEN
from endstech_shared.logging_utils import log_environment

from BudgetMagician.init.init_app import init_app
from BudgetMagician.init.init_app_env import init_app_env
from BudgetMagician.init.init_logging import init_logging
from BudgetMagician.magician.MainWindow import MainWindow
from BudgetMagician.version import __display_name__, __version__


def main():
    init_app_env()

    init_logging()

    log_environment(__display_name__, __version__, IS_FROZEN)

    app = init_app()

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
