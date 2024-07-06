from datetime import date

import PySide6
from PySide6 import QtCore
from PySide6.QtCore import QDate, Signal, Qt, Slot
from PySide6.QtGui import QDoubleValidator, QIcon
from PySide6.QtWidgets import QDialog, QMessageBox
from sqlalchemy.orm import scoped_session, Session
from sqlalchemy import select

from BudgetMagician.dialogs.ManageAccountsUi import Ui_ManageAccounts
from BudgetMagician.magician.models import Account, Transaction, BudgetSubcategory
from BudgetMagician.magician.queries import get_names_list
from BudgetMagician.parameters.combobox_constants import ACCOUNT_TYPES
from BudgetMagician.utils.combox_utils import set_combo_box_by_data, fill_combo_box, get_combo_box_dict_from_list
from BudgetMagician.utils.db import get_magic_session
from BudgetMagician.utils.qt import translate


class ManageAccounts(QDialog, Ui_ManageAccounts):
    account_created = Signal(str)
    account_deleted = Signal(str)

    def __init__(self, parent, budget_file):
        super().__init__(parent)
        self.budget_file = budget_file
        self.setupUi(self)
        self.installEventFilter(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setup_ui()
        self.type_combo.currentIndexChanged.connect(self.combo_index_changed)
        self.cancel_button.clicked.connect(self.close)
        self.ok_button.clicked.connect(self.save_account)
        self.current_balance.textChanged.connect(self.check_disabled)
        self.name.textChanged.connect(self.check_disabled)
        self.delete_button.clicked.connect(self.delete_account)

    def setup_ui(self):
        self.budget_account_recommend_label.setText(self.tr("- This account should affect my budget (recommended)"))
        self.off_budget_recommend_label.setText(self.tr("- This account should not affect my budget"))

        fill_combo_box(self.type_combo, ACCOUNT_TYPES)
        set_combo_box_by_data(self.type_combo, 1)

        self.budget_account_radio.setChecked(True)
        self.off_budget_radio.setChecked(False)

        current_date = date.today()
        self.current_balance_date.setDate(QDate(current_date.year, current_date.month, current_date.day))

        float_validator = QDoubleValidator(self)
        float_validator.setDecimals(2)
        self.current_balance.setValidator(float_validator)
        self.current_balance.setText("")
        self.name.setText("")
        self.ok_button.setEnabled(False)
        self.delete_button.setIcon(QIcon(":icons/lucide/delete.svg"))
        fill_combo_box(self.delete_combo_box, get_combo_box_dict_from_list(get_names_list(self.budget_file, Account)))

    @Slot()
    def check_disabled(self):
        enabled = bool(self.current_balance.text() and self.name.text())
        self.ok_button.setEnabled(enabled)

    @Slot()
    def combo_index_changed(self):
        current_data = self.type_combo.currentData()

        if current_data is None:
            pass
        elif current_data <= 7:
            if self.off_budget_radio.isChecked():
                self.off_budget_radio.setChecked(False)

            self.budget_account_radio.setChecked(True)

            self.budget_account_recommend_label.setText(self.tr("- This account should affect my budget (recommended)"))
            self.off_budget_recommend_label.setText(self.tr("- This account should not affect my budget"))
        elif current_data > 7:
            if self.budget_account_radio.isChecked():
                self.budget_account_radio.setChecked(False)

            self.off_budget_radio.setChecked(True)

            self.budget_account_recommend_label.setText(self.tr("- This account should affect my budget"))
            self.off_budget_recommend_label.setText(self.tr("- This account should not affect my budget (recommended)"))

    @Slot()
    def save_account(self):
        account_names = get_names_list(self.budget_file, Account)
        new_account_name = self.name.text()

        if new_account_name in account_names:
            QMessageBox.warning(self, translate("Dialog", "Warning"), translate("Warning", "The account name that you provided already exists."), QMessageBox.StandardButton.Ok)
            return

        current_balance = float(self.current_balance.text())

        current_qdate = self.current_balance_date.date()
        current_date = date(current_qdate.year(), current_qdate.month(), current_qdate.day())

        account_type = self.type_combo.currentData()

        on_budget = self.budget_account_radio.isChecked()

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            budget_subcategory = db.execute(select(BudgetSubcategory.id).where(BudgetSubcategory.name == "Income")).first()

            if budget_subcategory is None:
                QMessageBox.critical(
                    self,
                    translate("Dialog", "Critical"),
                    translate("Critical", "The income budget category cannot be found and your budget file may be corrupt. Restart BudgetMagician and try again."),
                    QMessageBox.StandardButton.Ok,
                )
            else:
                account = Account()
                account.name = new_account_name
                account.type = account_type
                account.on_budget = on_budget

                transaction = Transaction()
                transaction.date = current_date
                transaction.account = account
                transaction.budget_subcategory_id = budget_subcategory.id
                transaction.memo = "Starting Balance"
                transaction.amount = current_balance
                transaction.cleared = True
                transaction.reconciled = False
                db.add(account)
                db.add(transaction)
                db.commit()

                self.account_created.emit(new_account_name)
                self.close()

    @Slot()
    def delete_account(self):
        account_to_delete = self.delete_combo_box.currentText()

        if len(account_to_delete) > 0:
            db: scoped_session[Session]
            with get_magic_session(self.budget_file) as db:
                account = db.scalars(select(Account).where(Account.name == account_to_delete)).first()
                if account is not None:
                    db.delete(account)
                    db.commit()

                    self.account_deleted.emit(account_to_delete)

                fill_combo_box(self.delete_combo_box, get_combo_box_dict_from_list(get_names_list(self.budget_file, Account)))

    def open(self):
        self.setup_ui()
        return super().open()

    def eventFilter(self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent) -> bool:
        if arg__1 is self and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Escape, Qt.Key.Key_Enter):
                return True
        return super().eventFilter(arg__1, arg__2)
