from datetime import date

import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, QDate, Slot, Signal
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog, QMessageBox
from sqlalchemy import select
from sqlalchemy.orm import scoped_session, Session

from BudgetMagician.dialogs.NewTransactionUi import Ui_NewTransaction
from BudgetMagician.magician.models import BudgetSubcategory, Payee, Account, Transaction
from BudgetMagician.magician.queries import get_names_list
from BudgetMagician.utils.combox_utils import fill_combo_box, set_combo_box_by_data, get_combo_box_dict_from_list
from BudgetMagician.utils.db import get_magic_session
from BudgetMagician.utils.qt import translate


class NewTransaction(QDialog, Ui_NewTransaction):
    payees_changed = Signal()
    transactions_changed = Signal(int)

    def __init__(self, parent, budget_file: str, account_changed_signal):
        super().__init__(parent)
        self.budget_file = budget_file
        self.account_changed_signal = account_changed_signal
        self.current_account_name = None
        self.setupUi(self)
        self.installEventFilter(self)
        self.payee.installEventFilter(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.fill_ui()
        self.account_changed_signal.connect(self.account_changed)
        self.cancel_button.clicked.connect(self.close)
        self.ok_button.clicked.connect(self.transaction_added)
        self.amount.textChanged.connect(self.check_disabled)
        self.category.currentTextChanged.connect(self.check_disable_combo)

    def fill_ui(self):
        today = date.today()
        self.date.setDate(QDate(today.year, today.month, today.day))

        payees_combobox_dict = get_combo_box_dict_from_list(get_names_list(self.budget_file, Payee))
        fill_combo_box(self.payee, payees_combobox_dict)
        set_combo_box_by_data(self.payee, 0)

        budget_subcategory_combobox_dict = get_combo_box_dict_from_list(get_names_list(self.budget_file, BudgetSubcategory))
        fill_combo_box(self.category, budget_subcategory_combobox_dict)
        set_combo_box_by_data(self.category, 0)

        self.memo.setText("")
        self.amount.setText("")
        validator = QDoubleValidator(self)
        validator.setDecimals(2)
        self.amount.setValidator(validator)
        self.ok_button.setEnabled(False)

    @Slot()
    def check_disable_combo(self):
        budget_subcategory_text = self.category.currentText()

        if budget_subcategory_text == "Income":
            self.payee.setEnabled(False)
        else:
            self.payee.setEnabled(True)

    @Slot()
    def check_disabled(self):
        enabled = bool(self.amount.text())
        self.ok_button.setEnabled(enabled)

    def payee_added(self):
        payee_combo_text = self.payee.currentText()

        if payee_combo_text == "":
            QMessageBox.warning(self, translate("Dialog", "Warning"), translate("Warning", "You must provide a non-zero length payee name."), QMessageBox.StandardButton.Ok)
            return

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            possible_payee = db.scalars(select(Payee).where(Payee.name == payee_combo_text)).first()

            if possible_payee is None:
                new_payee = Payee()
                new_payee.name = payee_combo_text
                db.add(new_payee)
                db.commit()

                self.payees_changed.emit()
                self.fill_ui()
            else:
                QMessageBox.warning(self, translate("Dialog", "Warning"), translate("Warning", "The payee you have attempted to add already exists."), QMessageBox.StandardButton.Ok)

    @Slot()
    def transaction_added(self):
        qdate = self.date.date()
        new_datetime_date = date(qdate.year(), qdate.month(), qdate.day())
        assigned_payee = self.payee.currentText()
        assigned_category = self.category.currentText()
        new_memo = self.memo.text()
        new_amount = float(self.amount.text())

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            account_id = db.execute(select(Account.id).where(Account.name == self.current_account_name)).first()
            payee_id = db.execute(select(Payee.id).where(Payee.name == assigned_payee)).first()
            budget_subcategory = db.scalars(select(BudgetSubcategory).where(BudgetSubcategory.name == assigned_category)).first()

            if account_id is None:
                QMessageBox.warning(
                    self,
                    translate("Dialog", "Warning"),
                    translate("Warning", "The current account cannot be found. You must create an account before adding transactions."),
                    QMessageBox.StandardButton.Ok,
                )
                return
            if payee_id is None:
                QMessageBox.critical(
                    self, translate("Dialog", "Critical"), translate("Critical", "An error has occurred and the payee selected cannot be found."), QMessageBox.StandardButton.Ok
                )
                return
            if budget_subcategory is None:
                QMessageBox.critical(
                    self, translate("Dialog", "Critical"), translate("Critical", "An error has occurred and the category selected cannot be found."), QMessageBox.StandardButton.Ok
                )
                return

            transaction = Transaction()
            transaction.date = new_datetime_date
            transaction.account_id = account_id.id
            if budget_subcategory.name != "Income":
                transaction.payee_id = payee_id.id
            transaction.budget_subcategory = budget_subcategory
            transaction.memo = new_memo
            transaction.amount = new_amount
            transaction.cleared = False
            transaction.reconciled = False
            db.add(transaction)
            db.flush()
            transaction_id = transaction.id
            db.commit()

        self.transactions_changed.emit(transaction_id)
        self.close()

    @Slot(str)
    def account_changed(self, account_name):
        self.current_account_name = account_name

    def open(self) -> None:
        self.fill_ui()
        return super().open()

    def eventFilter(self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent) -> bool:
        if arg__1 is self.payee and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                self.payee_added()
                return True
        if arg__1 is self and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Escape, Qt.Key.Key_Enter):
                return True
        return super().eventFilter(arg__1, arg__2)
