import calendar
import statistics
from datetime import date
from typing import Optional

from PySide6 import QtPrintSupport
from PySide6.QtCore import Slot, Signal, QDate, QModelIndex
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPdfWriter, QPageSize, QPageLayout
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QHeaderView, QAbstractItemView
from dateutil.relativedelta import relativedelta
from sqlalchemy import select, and_
from sqlalchemy.orm import Session, scoped_session

from BudgetMagician.dialogs.About import About
from BudgetMagician.dialogs.BudgetNotFound import BudgetNotFound
from BudgetMagician.dialogs.MakeATransfer import MakeATransfer
from BudgetMagician.dialogs.ManageAccounts import ManageAccounts
from BudgetMagician.dialogs.ManageCategories import ManageCategories
from BudgetMagician.dialogs.NewTransaction import NewTransaction
from BudgetMagician.dialogs.PrivacyPolicy import PrivacyPolicy
from BudgetMagician.dialogs.ReconcileAccount import ReconcileAccount
from BudgetMagician.dialogs.ReleaseNotes import ReleaseNotes
from BudgetMagician.dialogs.SettingsDialog import SettingsDialog
from BudgetMagician.magician.MainWindowUi import Ui_MainWindow
from BudgetMagician.magician.models import Budget, Account, BudgetSubcategory, Payee, Transaction
from BudgetMagician.magician.queries import (
    get_years_plus_five_for_combobox,
    get_list_of_accounts_with_totals,
    get_names_list,
    get_budget_type_total,
    get_balances_dict_for_account,
)
from BudgetMagician.parameters.combobox_constants import MONTHS, ABBREVIATED_MONTHS
from BudgetMagician.settings import MIGRATIONS_DIR
from BudgetMagician.table_models.BudgetTableModel import BudgetTableModel, BudgetSubcategoryRow
from BudgetMagician.table_models.TransactionTableModel import TransactionTableModel, TransactionRow
from BudgetMagician.utils.Settings import Settings
from BudgetMagician.utils.chart_utils import get_pie_chart_from_dict, get_bar_char_from_dict
from BudgetMagician.utils.combox_utils import fill_combo_box, set_combo_box_by_data, get_combo_box_dict_from_list
from BudgetMagician.utils.db import run_migrations, get_magic_session
from BudgetMagician.utils.dir import get_desktop_dir
from BudgetMagician.utils.qt import translate
from BudgetMagician.utils.table_utils import fill_account_table


class MainWindow(QMainWindow, Ui_MainWindow):
    current_account = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.budget_file = Settings().get("budget/name")
        self.budget_not_found_window = BudgetNotFound(self)
        self.manage_accounts_window: Optional[ManageAccounts] = None
        self.manage_categories_window: Optional[ManageCategories] = None
        self.add_transactions_window: Optional[NewTransaction] = None
        self.make_a_transfer_window: Optional[MakeATransfer] = None
        self.reconcile_account_window: Optional[ReconcileAccount] = None
        self.file_menu = None
        self.view_menu = None
        self.help_menu = None
        self.reports_filters = {}
        self.reports_dates: tuple = ()
        self.current_account_name = ""
        self.current_report_function = self.fill_reports_spending_by_category

        self.setup_menu()
        self.setup_ui()
        self.setup_signals()

        if self.budget_file == "":
            self.budget_not_found_window.open()
        else:
            run_migrations(str(MIGRATIONS_DIR), self.budget_file)
            self.setup_windows_requiring_budget_file()
            self.fill_ui()

    def setup_windows_requiring_budget_file(self):
        if self.manage_accounts_window is not None:
            self.manage_accounts_button.clicked.disconnect()
            self.manage_accounts_window.account_created.disconnect()
            self.manage_accounts_window.account_deleted.disconnect()

        if self.manage_categories_window is not None:
            self.manage_categories_button.clicked.disconnect()
            self.manage_categories_window.categories_changed.disconnect()

        if self.add_transactions_window is not None:
            self.add_transaction_button.clicked.disconnect()
            self.add_transactions_window.transactions_changed.disconnect()
            self.add_transactions_window.payees_changed.disconnect()

        if self.make_a_transfer_window is not None:
            self.make_a_transfer_button.clicked.disconnect()
            self.make_a_transfer_window.transfer_added.disconnect()

        if self.reconcile_account_window is not None:
            self.reconcile_account_button.clicked.disconnect()
            self.reconcile_account_window.account_reconciled.disconnect()

        del self.manage_accounts_window
        del self.manage_categories_window
        del self.add_transactions_window
        del self.make_a_transfer_window
        del self.reconcile_account_window

        self.manage_accounts_window = ManageAccounts(self, self.budget_file)
        self.manage_categories_window = ManageCategories(self, self.budget_file)
        self.add_transactions_window = NewTransaction(self, self.budget_file, self.current_account)
        self.make_a_transfer_window = MakeATransfer(self, self.budget_file)
        self.reconcile_account_window = ReconcileAccount(self, self.budget_file, self.current_account)

        self.manage_accounts_button.clicked.connect(self.manage_accounts_window.open)
        self.manage_accounts_window.account_created.connect(self.account_created)
        self.manage_categories_button.clicked.connect(self.manage_categories_window.open)
        self.manage_categories_window.categories_changed.connect(self.categories_changed)
        self.add_transaction_button.clicked.connect(self.add_transactions_window.open)
        self.make_a_transfer_button.clicked.connect(self.make_a_transfer_window.open)
        self.make_a_transfer_window.transfer_added.connect(self.transfer_made)
        self.add_transactions_window.transactions_changed.connect(self.transaction_made)
        self.add_transactions_window.payees_changed.connect(self.payees_changed)
        self.manage_accounts_window.account_deleted.connect(self.account_deleted)
        self.reconcile_account_button.clicked.connect(self.reconcile_account_window.open)
        self.reconcile_account_window.account_reconciled.connect(self.transaction_made)

    def setup_menu(self):
        self.file_menu = self.menubar.addMenu(translate("Menu", "File"))
        open_budget = self.file_menu.addAction(translate("Menu", "Open Budget"), self.budget_not_found_window.open)
        open_budget.setShortcut("Ctrl+O")
        open_budget.setIcon(QIcon(":icons/lucide/folder-open.svg"))
        settings = self.file_menu.addAction(translate("Menu", "Settings"), SettingsDialog(self).open)
        settings.setShortcut("Ctrl+Alt+S")
        settings.setIcon(QIcon(":icons/lucide/settings.svg"))
        exit_action = self.file_menu.addAction(translate("Menu", "Exit"), self.close)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setIcon(QIcon(":icons/lucide/log-out.svg"))

        self.view_menu = self.menubar.addMenu(translate("Menu", "View"))
        self.view_menu.addAction(translate("Menu", "Go to Budget"), self.goto_budget)
        self.view_menu.addAction(translate("Menu", "Go to Accounts"), self.goto_accounts)
        self.view_menu.addAction(translate("Menu", "Go to Reports"), self.goto_reports)

        self.help_menu = self.menubar.addMenu(translate("Menu", "Help"))
        self.help_menu.addAction(translate("Menu", "Release Notes"), ReleaseNotes(self).open)
        self.help_menu.addAction(translate("Menu", "Privacy Policy"), PrivacyPolicy(self).open)
        about_action = self.help_menu.addAction(translate("Menu", "About"), About(self).open)
        about_action.setShortcut("F1")

    def setup_ui(self):
        self.print.setIcon(QIcon(":icons/feather/printer.svg"))
        self.pdf_export.setIcon(QIcon(":icons/lucide/arrow-right-circle.svg"))
        self.manage_accounts_button.setIcon(QIcon(":icons/lucide/settings.svg"))
        self.plus_label.setPixmap(QPixmap(":icons/lucide/plus.png"))
        self.equals_label.setPixmap(QPixmap(":icons/lucide/equal.png"))
        self.available_to_budget_equal.setPixmap(QPixmap(":icons/lucide/equal.png"))
        self.add_transaction_button.setIcon(QIcon(":icons/lucide/plus-circle.svg"))
        self.make_a_transfer_button.setIcon(QIcon(":icons/lucide/arrow-right-left.svg"))
        self.manage_categories_button.setIcon(QIcon(":icons/lucide/settings.svg"))

    def setup_signals(self):
        self.budget_not_found_window.budget_name_changed.connect(self.budget_changed)
        self.on_budget_accounts_table.itemClicked.connect(self.select_account)
        self.off_budget_accounts_table.itemClicked.connect(self.select_account)
        self.spending_by_category_button.clicked.connect(self.draw_report_spending_by_category)
        self.spending_by_payee_button.clicked.connect(self.draw_report_spending_by_payee)
        self.spending_trends_button.clicked.connect(self.draw_report_spending_trends)
        self.net_worth_button.clicked.connect(self.draw_report_net_worth)
        self.report_date_one.userDateChanged.connect(self.redraw_current_chart)
        self.report_date_two.userDateChanged.connect(self.redraw_current_chart)
        self.reports_categories_combo.currentTextChanged.connect(self.redraw_current_chart)
        self.reports_payees_combo.currentTextChanged.connect(self.redraw_current_chart)
        self.reports_accounts_combo.currentTextChanged.connect(self.redraw_current_chart)
        self.pdf_export.clicked.connect(self.export_chart_to_pdf)
        self.print.clicked.connect(self.print_preview_chart)
        self.income_v_expense_button.clicked.connect(self.draw_report_income_v_expense)
        self.budget_month_combo.currentTextChanged.connect(self.change_budget_tab_date)
        self.budget_year_combo.currentTextChanged.connect(self.change_budget_tab_date)

    def fill_ui(self):
        accounts_name_list = get_names_list(self.budget_file, Account)

        if len(accounts_name_list) > 0:
            today = date.today()
            self.current_account_name = accounts_name_list[0]

            self.fill_balances_bar(self.current_account_name)

            self.account_name_label.setText(self.tr("Current Account: {}").format(self.current_account_name))
            self.transactions_table.setModel(TransactionTableModel())
            self.preload_transactions_table(self.current_account_name)
            self.budget_table.setModel(BudgetTableModel())
            self.preload_budget_table(date(today.year, today.month, 1))
            self.current_account.emit(self.current_account_name)
        else:
            self.account_name_label.setText(self.tr("Create an account to continue."))
            self.transactions_table.setModel(TransactionTableModel())
            self.budget_table.setModel(BudgetTableModel())

        self.fill_date_combos()
        self.fill_date_edits()
        self.fill_report_categories_combo()
        self.fill_report_payees_combo()
        self.fill_report_account_combo()
        self.fill_account_tables()
        self.on_budget_total.setText(f"{get_budget_type_total(self.budget_file, True):.2f}")
        self.off_budget_total.setText(f"{get_budget_type_total(self.budget_file, False):.2f}")
        self.redraw_current_chart()
        self.transactions_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.budget_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.budget_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.budget_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.fill_budget_bar()

    def fill_date_combos(self):
        current_date = date.today()
        current_month = current_date.month
        current_year = current_date.year

        fill_combo_box(self.budget_month_combo, MONTHS)
        set_combo_box_by_data(self.budget_month_combo, current_month)

        budget_years_dict = get_years_plus_five_for_combobox(self.budget_file, Budget)
        fill_combo_box(self.budget_year_combo, budget_years_dict)
        set_combo_box_by_data(self.budget_year_combo, current_year)

    def fill_date_edits(self):
        current_date = date.today()

        self.report_date_one.setDate(QDate(current_date.year, 1, 1))
        self.report_date_two.setDate(QDate(current_date.year, current_date.month, current_date.day))

    def fill_report_categories_combo(self):
        categories_list = get_names_list(self.budget_file, BudgetSubcategory)
        categories_list.insert(0, "All")
        categories_list.remove("Income")
        fill_combo_box(self.reports_categories_combo, get_combo_box_dict_from_list(categories_list))
        set_combo_box_by_data(self.reports_categories_combo, 0)

    def fill_report_payees_combo(self):
        payees_list = get_names_list(self.budget_file, Payee)
        payees_list.insert(0, "All")
        fill_combo_box(self.reports_payees_combo, get_combo_box_dict_from_list(payees_list))
        set_combo_box_by_data(self.reports_payees_combo, 0)

    def fill_report_account_combo(self):
        accounts_list = get_names_list(self.budget_file, Account)
        if len(accounts_list) > 0:
            accounts_list.insert(0, "All")
            fill_combo_box(self.reports_accounts_combo, get_combo_box_dict_from_list(accounts_list))
            set_combo_box_by_data(self.reports_accounts_combo, 0)

    def fill_account_tables(self):
        headers = ["Acct", "Bal"]
        on_budget_table_data = get_list_of_accounts_with_totals(self.budget_file, True)
        off_budget_table_data = get_list_of_accounts_with_totals(self.budget_file, False)
        fill_account_table(self.on_budget_accounts_table, on_budget_table_data, headers)
        fill_account_table(self.off_budget_accounts_table, off_budget_table_data, headers)

    def fill_balances_bar(self, account_name):
        balances_dict = get_balances_dict_for_account(self.budget_file, account_name)
        self.cleared_balance.setText(f"{balances_dict['cleared']:.2f}")

        if balances_dict["cleared"] < 0:
            self.cleared_balance.setStyleSheet("color: red")
        else:
            self.cleared_balance.setStyleSheet("color: black")

        self.uncleared_transactions.setText(f"{balances_dict['uncleared']:.2f}")

        if balances_dict["uncleared"] < 0:
            self.uncleared_transactions.setStyleSheet("color: red")
        else:
            self.uncleared_transactions.setStyleSheet("color: black")

        self.working_balance.setText(f"{balances_dict['working']:.2f}")

        if balances_dict["working"] < 0:
            self.working_balance.setStyleSheet("color: red")
        else:
            self.working_balance.setStyleSheet("color: black")

    def clear_balances_bar(self):
        self.cleared_balance.setText("")
        self.uncleared_transactions.setText("")
        self.working_balance.setText("")

    def fill_budget_bar(self):
        todays_date = date.today()
        month = self.budget_month_combo.currentData()
        year = self.budget_year_combo.currentData()

        if month is None or year is None:
            year = todays_date.year
            month = todays_date.month

        max_day_in_current_month = calendar.monthrange(year, month)[1]
        current_month_date = date(year, month, 1)
        last_day_in_current_month_date = date(year, month, max_day_in_current_month)
        last_month_date = current_month_date - relativedelta(months=1)
        last_day_in_last_month_date = last_day_in_current_month_date - relativedelta(months=1)

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            income_budget_subcategory = db.execute(select(BudgetSubcategory.id).where(BudgetSubcategory.name == "Income")).first()

            if income_budget_subcategory is None:
                self.not_budgeted.setText("-")
                self.overspent.setText("-")
                self.income.setText("-")
                self.budgeted.setText("-")
                self.available_to_budget.setText("Error")
            else:
                income_transactions_for_this_month = db.execute(
                    select(Transaction.amount).where(
                        and_(
                            Transaction.budget_subcategory_id == income_budget_subcategory.id,
                            Transaction.date >= current_month_date,
                            Transaction.date <= last_day_in_current_month_date,
                        )
                    )
                ).all()
                income_for_this_month = sum((transaction.amount for transaction in income_transactions_for_this_month))
                income_transactions_for_last_month = db.execute(
                    select(Transaction.amount).where(
                        and_(
                            Transaction.budget_subcategory_id == income_budget_subcategory.id, Transaction.date >= last_month_date, Transaction.date <= last_day_in_last_month_date
                        )
                    )
                ).all()
                income_for_last_month = sum((transaction.amount for transaction in income_transactions_for_last_month))

                budgeted_amounts_this_month = db.execute(
                    select(Budget.budgeted).where(and_(Budget.date >= current_month_date, Budget.date <= last_day_in_current_month_date))
                ).all()
                budgeted_amount_this_month = sum((amount.budgeted for amount in budgeted_amounts_this_month))
                budgeted_amounts_last_month = db.execute(select(Budget.budgeted).where(and_(Budget.date >= last_month_date, Budget.date <= last_day_in_last_month_date))).all()
                budgeted_amount_last_month = sum((amount.budgeted for amount in budgeted_amounts_last_month))

                available_to_budget_this_month = income_for_this_month - budgeted_amount_this_month
                not_budgeted_last_month = income_for_last_month - budgeted_amount_last_month

                transactions_for_last_month = db.execute(
                    select(Transaction.amount).where(
                        and_(
                            Transaction.budget_subcategory_id != income_budget_subcategory.id, Transaction.date >= last_month_date, Transaction.date <= last_day_in_last_month_date
                        )
                    )
                ).all()
                expenses_for_last_month = sum((transaction.amount for transaction in transactions_for_last_month))

                if expenses_for_last_month >= 0:
                    overspent_for_last_month = 0
                else:
                    overspent_for_last_month = budgeted_amount_last_month - expenses_for_last_month

                self.not_budgeted.setText(f"{not_budgeted_last_month:.2f}")
                self.overspent.setText(f"{overspent_for_last_month:.2f}")
                self.income.setText(f"{income_for_this_month:.2f}")
                self.budgeted.setText(f"{budgeted_amount_this_month:.2f}")
                self.available_to_budget.setText(f"{available_to_budget_this_month:.2f}")

                if available_to_budget_this_month >= 0:
                    self.available_to_budget_label.setStyleSheet("color: black")
                    self.available_to_budget_label.setText(self.tr("Available to Budget"))
                else:
                    self.available_to_budget_label.setStyleSheet("color: red")
                    self.available_to_budget_label.setText(self.tr("Over Budgeted"))

    def get_reports_dates(self) -> None:
        starting_qdate = self.report_date_one.date()
        starting_date = date(starting_qdate.year(), starting_qdate.month(), starting_qdate.day())
        ending_qdate = self.report_date_two.date()
        ending_date = date(ending_qdate.year(), ending_qdate.month(), ending_qdate.day())

        self.reports_dates = (starting_date, ending_date)

    def redraw_current_chart(self):
        self.get_reports_dates()
        self.get_reports_filters()
        self.current_report_function()

    def get_reports_filters(self) -> None:
        return_kwargs = {}

        category_text = self.reports_categories_combo.currentText()
        payees_text = self.reports_payees_combo.currentText()
        accounts_text = self.reports_accounts_combo.currentText()

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            if category_text == "All":
                category = None
            else:
                category = db.execute(select(BudgetSubcategory.id).where(BudgetSubcategory.name == category_text)).first()

            if payees_text == "All":
                payee = None
            else:
                payee = db.execute(select(Payee.id).where(Payee.name == payees_text)).first()

            if accounts_text == "All":
                account = None
            else:
                account = db.execute(select(Account.id).where(Account.name == accounts_text)).first()

            if category is not None:
                return_kwargs["budget_subcategory_id"] = category.id

            if payee is not None:
                return_kwargs["payee_id"] = payee.id

            if account is not None:
                return_kwargs["account_id"] = account.id

        self.reports_filters = return_kwargs

    def fill_reports_income_v_expense(self):
        self.report_date_one.setEnabled(False)
        self.report_date_two.setEnabled(False)
        self.reports_categories_combo.setEnabled(True)
        self.reports_payees_combo.setEnabled(True)
        self.reports_accounts_combo.setEnabled(True)

        todays_date = date.today()

        kwargs = self.reports_filters

        x_axis_categories = [v for k, v in ABBREVIATED_MONTHS.items()]

        income_v_expense_dict: dict[str, list[float]] = {}
        total_income_text = translate("Reports", "Total Income")
        average_income_text = translate("Reports", "Average Income")
        total_expenses_text = translate("Reports", "Total Expenses")
        average_expenses_text = translate("Reports", "Average Expenses")
        net_income_text = translate("Reports", "Net Income")
        income_v_expense_dict[total_income_text] = []
        income_v_expense_dict[average_income_text] = []
        income_v_expense_dict[total_expenses_text] = []
        income_v_expense_dict[average_expenses_text] = []
        income_v_expense_dict[net_income_text] = []

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            for key in ABBREVIATED_MONTHS.keys():
                max_day = calendar.monthrange(todays_date.year, key)[1]
                rows = db.scalars(
                    select(
                        Transaction
                    ).where(and_(Transaction.date >= date(todays_date.year, key, 1), Transaction.date <= date(todays_date.year, key, max_day))).filter_by(**kwargs)
                ).all()

                income = [row.amount for row in rows if row.budget_subcategory is not None and row.budget_subcategory.name == "Income"]
                expenses = [abs(row.amount) for row in rows if row.budget_subcategory is not None and row.budget_subcategory.name != "Income"]
                income_sum = sum(income)
                expenses_sum = sum(expenses)
                net_income_sum = income_sum - expenses_sum

                if len(income) == 0:
                    income.append(0)

                if len(expenses) == 0:
                    expenses.append(0)

                average_income = statistics.mean(income)
                average_expenses = statistics.mean(expenses)

                income_v_expense_dict[total_income_text].append(income_sum)
                income_v_expense_dict[average_income_text].append(average_income)
                income_v_expense_dict[total_expenses_text].append(expenses_sum)
                income_v_expense_dict[average_expenses_text].append(average_expenses)
                income_v_expense_dict[net_income_text].append(net_income_sum)

        sums_list = []
        sums_list.extend(income_v_expense_dict[total_income_text])
        sums_list.extend(income_v_expense_dict[average_income_text])
        sums_list.extend(income_v_expense_dict[total_expenses_text])
        sums_list.extend(income_v_expense_dict[average_expenses_text])
        sums_list.extend(income_v_expense_dict[net_income_text])

        chart = get_bar_char_from_dict(
            translate("Reports", "Income Versus Expense"), translate("Reports", "No Data Found"), x_axis_categories, max(sums_list), min(sums_list), income_v_expense_dict
        )
        self.chart_viewer.setChart(chart)

    def fill_reports_net_worth(self):
        self.report_date_one.setEnabled(False)
        self.report_date_two.setEnabled(False)
        self.reports_categories_combo.setEnabled(False)
        self.reports_payees_combo.setEnabled(False)
        self.reports_accounts_combo.setEnabled(True)

        todays_date = date.today()

        kwargs = self.reports_filters

        if "budget_subcategory_id" in kwargs:
            del kwargs["budget_subcategory_id"]

        if "payee_id" in kwargs:
            del kwargs["payee_id"]

        x_axis_categories = [v for k, v in ABBREVIATED_MONTHS.items()]

        net_worth_dict: dict[str, list[float]] = {}
        debts_text = translate("Reports", "Debts")
        assets_text = translate("Reports", "Assets")
        net_worth_text = translate("Reports", "Net Worth")
        net_worth_dict[debts_text] = []
        net_worth_dict[assets_text] = []
        net_worth_dict[net_worth_text] = []

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            for key in ABBREVIATED_MONTHS.keys():
                max_day = calendar.monthrange(todays_date.year, key)[1]
                rows = db.scalars(
                    select(
                        Transaction
                    ).where(and_(Transaction.date >= date(todays_date.year, key, 1), Transaction.date <= date(todays_date.year, key, max_day))).filter_by(**kwargs)
                ).all()

                debts_sum = sum((abs(row.amount) for row in rows if row.budget_subcategory is not None and row.budget_subcategory.name != "Income"))
                assets_sum = sum((row.amount for row in rows if row.budget_subcategory is not None and row.budget_subcategory.name == "Income"))
                net_worth_sum = assets_sum - debts_sum

                net_worth_dict[debts_text].append(debts_sum)
                net_worth_dict[assets_text].append(assets_sum)
                net_worth_dict[net_worth_text].append(net_worth_sum)

        sums_list = []
        sums_list.extend(net_worth_dict[debts_text])
        sums_list.extend(net_worth_dict[assets_text])
        sums_list.extend(net_worth_dict[net_worth_text])

        chart = get_bar_char_from_dict(translate("Reports", "Net Worth"), translate("Reports", "No Data Found"), x_axis_categories, max(sums_list), min(sums_list), net_worth_dict)
        self.chart_viewer.setChart(chart)

    def fill_reports_spending_trends(self):
        self.report_date_one.setEnabled(False)
        self.report_date_two.setEnabled(False)
        self.reports_categories_combo.setEnabled(True)
        self.reports_payees_combo.setEnabled(True)
        self.reports_accounts_combo.setEnabled(True)

        todays_date = date.today()

        kwargs = self.reports_filters

        x_axis_categories = [v for k, v in ABBREVIATED_MONTHS.items()]

        spending_trends_dict: dict[str, list[float]] = {}
        spending_text = translate("Reports", "Spending")
        spending_trends_dict[spending_text] = []

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            for key in ABBREVIATED_MONTHS.keys():
                max_day = calendar.monthrange(todays_date.year, key)[1]
                rows = db.scalars(
                    select(
                        Transaction
                    ).where(and_(Transaction.date >= date(todays_date.year, key, 1), Transaction.date <= date(todays_date.year, key, max_day))).filter_by(**kwargs)
                ).all()

                month_sum = sum((abs(row.amount) for row in rows if row.budget_subcategory is not None and row.budget_subcategory.name != "Income"))
                spending_trends_dict[spending_text].append(month_sum)

        chart = get_bar_char_from_dict(
            translate("Reports", "Spending Trends"),
            translate("Reports", "No Data Found"),
            x_axis_categories,
            max(spending_trends_dict[spending_text]),
            min(spending_trends_dict[spending_text]),
            spending_trends_dict,
        )
        self.chart_viewer.setChart(chart)

    def fill_reports_spending_by_payee(self):
        self.report_date_one.setEnabled(True)
        self.report_date_two.setEnabled(True)
        self.reports_categories_combo.setEnabled(True)
        self.reports_payees_combo.setEnabled(True)
        self.reports_accounts_combo.setEnabled(True)

        starting_date, ending_date = self.reports_dates

        kwargs = self.reports_filters

        amounts_per_payee_dict = {}

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            rows = db.scalars(select(Transaction).where(and_(Transaction.date >= starting_date, Transaction.date <= ending_date)).filter_by(**kwargs)).all()

            for row in rows:
                if row.payee is None:
                    continue

                if row.budget_subcategory.name != "Income":
                    if row.payee.name not in amounts_per_payee_dict:
                        amounts_per_payee_dict[row.payee.name] = 0.00

                    amounts_per_payee_dict[row.payee.name] = sum((amounts_per_payee_dict[row.payee.name], abs(row.amount)))

        chart = get_pie_chart_from_dict(translate("Reports", "Spending By Payee"), translate("Reports", "No Expenses Found"), amounts_per_payee_dict)

        self.chart_viewer.setChart(chart)

    def fill_reports_spending_by_category(self):
        self.report_date_one.setEnabled(True)
        self.report_date_two.setEnabled(True)
        self.reports_categories_combo.setEnabled(True)
        self.reports_payees_combo.setEnabled(True)
        self.reports_accounts_combo.setEnabled(True)

        starting_date, ending_date = self.reports_dates

        kwargs = self.reports_filters

        amounts_per_category_dict = {}

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            rows = db.scalars(select(Transaction).where(and_(Transaction.date >= starting_date, Transaction.date <= ending_date)).filter_by(**kwargs)).all()

            for row in rows:
                if row.budget_subcategory is None:
                    continue

                if row.budget_subcategory.name != "Income":
                    if row.budget_subcategory.name not in amounts_per_category_dict:
                        amounts_per_category_dict[row.budget_subcategory.name] = 0.00

                    amounts_per_category_dict[row.budget_subcategory.name] = sum((amounts_per_category_dict[row.budget_subcategory.name], abs(row.amount)))

            chart = get_pie_chart_from_dict(translate("Reports", "Spending By Category"), translate("Reports", "No Expenses Found"), amounts_per_category_dict)

        self.chart_viewer.setChart(chart)

    def append_transaction_to_transaction_table(self, idd: int):
        model: TransactionTableModel = self.transactions_table.model()
        index = len(model.rows)
        transaction_row = TransactionRow(idd, self.budget_file, self.manage_categories_window.categories_changed, self.add_transactions_window.payees_changed)
        transaction_row.delete_button.clicked.connect(self.remove_transaction_from_transaction_table)
        transaction_row.cleared.stateChanged.connect(self.cleared_state_changed)
        model.insert_transaction_row(index, transaction_row)
        self.transactions_table.setIndexWidget(model.index(index, 0), transaction_row.date)
        self.transactions_table.setIndexWidget(model.index(index, 1), transaction_row.payee)
        self.transactions_table.setIndexWidget(model.index(index, 2), transaction_row.budget_subcategory)
        self.transactions_table.setIndexWidget(model.index(index, 3), transaction_row.memo)
        self.transactions_table.setIndexWidget(model.index(index, 4), transaction_row.amount)
        self.transactions_table.setIndexWidget(model.index(index, 5), transaction_row.cleared)
        self.transactions_table.setIndexWidget(model.index(index, 6), transaction_row.delete_button)

    def preload_transactions_table(self, account_name):
        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            account = db.scalars(select(Account).where(Account.name == account_name)).first()

            if account is not None:
                rows = db.execute(select(Transaction.id).where(Transaction.account == account).order_by(Transaction.date)).all()

                if len(rows) > 0:
                    for row in rows:
                        self.append_transaction_to_transaction_table(row.id)

    def append_budget_subcategory_to_budget_table(self, idd: int, date_to_search: date):
        model: BudgetTableModel = self.budget_table.model()
        index = len(model.rows)
        budget_subcategory_row = BudgetSubcategoryRow(idd, date_to_search, self.budget_file)
        budget_subcategory_row.amount.editingFinished.connect(self.fill_budget_bar)
        model.insert_budget_subcategory_row(index, budget_subcategory_row)
        self.budget_table.setIndexWidget(model.index(index, 0), budget_subcategory_row.amount)

    def preload_budget_table(self, date_to_search: date):
        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            budget_subcategory_ids = db.execute(select(BudgetSubcategory.id).where(BudgetSubcategory.name != "Income")).all()

        for budget_subcategory_id in budget_subcategory_ids:
            self.append_budget_subcategory_to_budget_table(budget_subcategory_id.id, date_to_search)

    @Slot()
    def change_budget_tab_date(self):
        todays_date = date.today()
        month = self.budget_month_combo.currentData()
        year = self.budget_year_combo.currentData()

        if month is None or year is None:
            date_to_search = date(todays_date.year, todays_date.month, 1)
        else:
            date_to_search = date(year, month, 1)

        self.budget_table.setModel(BudgetTableModel())
        self.preload_budget_table(date_to_search)
        self.fill_budget_bar()

    @Slot()
    def cleared_state_changed(self):
        self.fill_balances_bar(self.current_account_name)

    @Slot()
    def remove_transaction_from_transaction_table(self):
        model: TransactionTableModel = self.transactions_table.model()
        index = None
        transaction_row: TransactionRow

        for i, transaction_row in enumerate(model.rows):
            if transaction_row.delete_button is self.sender():
                index = i
                break

        if index is not None:
            db: scoped_session[Session]
            with get_magic_session(self.budget_file) as db:
                transaction = db.scalars(select(Transaction).where(Transaction.id == model.rows[index].id)).first()

                if transaction is not None:
                    db.delete(transaction)
                    db.commit()

            model.removeRow(index, QModelIndex())

            self.fill_account_tables()
            self.on_budget_total.setText(f"{get_budget_type_total(self.budget_file, True):.2f}")
            self.off_budget_total.setText(f"{get_budget_type_total(self.budget_file, False):.2f}")
            self.redraw_current_chart()
            self.fill_balances_bar(self.current_account_name)
            self.fill_budget_bar()

    @Slot()
    def export_chart_to_pdf(self):
        file_name = QFileDialog.getSaveFileName(self, translate("FileDialog", "Save to PDF"), str(get_desktop_dir()), translate("FileDialog", "PDF (*.pdf)"))

        pdf_writer = QPdfWriter(file_name[0])
        pdf_writer.setCreator("BudgetMagician")
        pdf_writer.setPageOrientation(QPageLayout.Orientation.Landscape)
        pdf_writer.setPageSize(QPageSize.PageSizeId.A4)

        painter = QPainter(pdf_writer)
        self.chart_viewer.render(painter)
        painter.end()

    @Slot()
    def print_preview_chart(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterMode.HighResolution)
        printer.setPageOrientation(QPageLayout.Orientation.Landscape)
        printer.setFullPage(False)

        dialog = QtPrintSupport.QPrintPreviewDialog(printer, self)
        dialog.paintRequested.connect(self.handle_print_preview_paint_request)
        dialog.showMaximized()
        dialog.exec()

    @Slot()
    def handle_print_preview_paint_request(self, printer):
        painter = QPainter(printer)
        self.chart_viewer.render(painter)
        painter.end()

    @Slot(int)
    def transaction_made(self, transaction_id: int):
        self.fill_balances_bar(self.current_account_name)
        self.fill_account_tables()
        self.on_budget_total.setText(f"{get_budget_type_total(self.budget_file, True):.2f}")
        self.off_budget_total.setText(f"{get_budget_type_total(self.budget_file, False):.2f}")
        self.redraw_current_chart()
        self.append_transaction_to_transaction_table(transaction_id)
        month = self.budget_month_combo.currentData()
        year = self.budget_year_combo.currentData()
        date_to_search = date(year, month, 1)
        self.budget_table.setModel(BudgetTableModel())
        self.preload_budget_table(date_to_search)
        self.fill_budget_bar()

    @Slot(tuple)
    def transfer_made(self, transfer_id_tuple: tuple):
        self.fill_balances_bar(self.current_account_name)
        self.fill_account_tables()
        self.on_budget_total.setText(f"{get_budget_type_total(self.budget_file, True):.2f}")
        self.off_budget_total.setText(f"{get_budget_type_total(self.budget_file, False):.2f}")
        self.redraw_current_chart()
        from_transaction_id, to_transaction_id = transfer_id_tuple
        self.append_transaction_to_transaction_table(from_transaction_id)
        self.append_transaction_to_transaction_table(to_transaction_id)
        month = self.budget_month_combo.currentData()
        year = self.budget_year_combo.currentData()
        date_to_search = date(year, month, 1)
        self.budget_table.setModel(BudgetTableModel())
        self.preload_budget_table(date_to_search)
        self.fill_budget_bar()

    @Slot(str)
    def account_created(self, account_name):
        month = self.budget_month_combo.currentData()
        year = self.budget_year_combo.currentData()
        date_to_search = date(year, month, 1)
        self.budget_table.setModel(BudgetTableModel())
        self.preload_budget_table(date_to_search)

        self.transactions_table.setModel(TransactionTableModel())
        self.preload_transactions_table(account_name)
        self.fill_balances_bar(account_name)

        self.on_budget_accounts_table.clearSelection()
        self.off_budget_accounts_table.clearSelection()
        self.fill_account_tables()
        self.account_name_label.setText(self.tr("Current Account: {}").format(account_name))
        self.on_budget_total.setText(f"{get_budget_type_total(self.budget_file, True):.2f}")
        self.off_budget_total.setText(f"{get_budget_type_total(self.budget_file, False):.2f}")
        self.fill_report_account_combo()
        self.redraw_current_chart()
        self.fill_budget_bar()
        self.current_account_name = account_name
        self.current_account.emit(account_name)

    @Slot(str)
    def account_deleted(self, account_name):
        self.on_budget_accounts_table.clearSelection()
        self.off_budget_accounts_table.clearSelection()
        self.fill_account_tables()
        self.on_budget_total.setText(f"{get_budget_type_total(self.budget_file, True):.2f}")
        self.off_budget_total.setText(f"{get_budget_type_total(self.budget_file, False):.2f}")
        self.fill_report_account_combo()
        self.redraw_current_chart()
        self.fill_budget_bar()

        if self.current_account_name == account_name:
            accounts_list = get_names_list(self.budget_file, Account)

            if len(accounts_list) > 0:
                month = self.budget_month_combo.currentData()
                year = self.budget_year_combo.currentData()
                date_to_search = date(year, month, 1)
                self.budget_table.setModel(BudgetTableModel())
                self.preload_budget_table(date_to_search)
                self.current_account_name = accounts_list[0]
                self.account_name_label.setText(self.tr("Current Account: {}").format(self.current_account_name))
                self.transactions_table.setModel(TransactionTableModel())
                self.preload_transactions_table(self.current_account_name)
                self.fill_balances_bar(self.current_account_name)
                self.current_account.emit(self.current_account_name)
            else:
                self.account_name_label.setText(self.tr("Create an account to continue."))
                self.transactions_table.setModel(TransactionTableModel())
                self.budget_table.setModel(BudgetTableModel())
                self.clear_balances_bar()
                self.current_account.emit("")

    @Slot()
    def categories_changed(self):
        month = self.budget_month_combo.currentData()
        year = self.budget_year_combo.currentData()
        date_to_search = date(year, month, 1)
        self.budget_table.setModel(BudgetTableModel())
        self.preload_budget_table(date_to_search)
        self.fill_report_categories_combo()
        self.redraw_current_chart()
        self.fill_budget_bar()

    @Slot()
    def payees_changed(self):
        self.fill_report_payees_combo()
        self.redraw_current_chart()

    @Slot(QTableWidgetItem)
    def select_account(self, table_widget_item: QTableWidgetItem):
        account_name = table_widget_item.text()

        try:
            float(account_name)
        except ValueError:
            self.fill_balances_bar(account_name)
            self.account_name_label.setText(self.tr("Current Account: {}").format(account_name))
            self.transactions_table.setModel(TransactionTableModel())
            self.preload_transactions_table(account_name)
            self.current_account_name = account_name
            self.current_account.emit(account_name)

    @Slot()
    def draw_report_spending_by_category(self):
        self.current_report_function = self.fill_reports_spending_by_category
        self.current_report_function()

    @Slot()
    def draw_report_spending_by_payee(self):
        self.current_report_function = self.fill_reports_spending_by_payee
        self.current_report_function()

    @Slot()
    def draw_report_spending_trends(self):
        self.current_report_function = self.fill_reports_spending_trends
        self.current_report_function()

    @Slot()
    def draw_report_net_worth(self):
        self.current_report_function = self.fill_reports_net_worth
        self.current_report_function()

    @Slot()
    def draw_report_income_v_expense(self):
        self.current_report_function = self.fill_reports_income_v_expense
        self.current_report_function()

    def goto_budget(self):
        self.tabWidget.setCurrentIndex(0)

    def goto_accounts(self):
        self.tabWidget.setCurrentIndex(1)

    def goto_reports(self):
        self.tabWidget.setCurrentIndex(2)

    @Slot()
    def budget_changed(self):
        self.budget_file = Settings().get("budget/name")

        run_migrations(str(MIGRATIONS_DIR), self.budget_file)

        self.setup_windows_requiring_budget_file()

        self.fill_ui()
