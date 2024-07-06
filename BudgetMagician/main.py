import sys

from BudgetMagician.init.init_app import init_app
from BudgetMagician.init.init_app_env import init_app_env
from BudgetMagician.init.init_logging import init_logging
from BudgetMagician.magician.MainWindow import MainWindow
from BudgetMagician.utils.logging import log_environment


def main():
    init_app_env()

    init_logging()

    log_environment()

    app = init_app()

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
