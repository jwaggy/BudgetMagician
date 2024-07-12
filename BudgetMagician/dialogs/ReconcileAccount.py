from datetime import date

import PySide6
from PySide6 import QtCore
from PySide6.QtCore import QDate, Signal, Qt, Slot
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog, QMessageBox
from endstech_shared.qt_translation_utils import translate
from endstech_shared.sqlalchemy_utils import get_magic_session
from sqlalchemy import select, and_
from sqlalchemy.orm import scoped_session, Session

from BudgetMagician.dialogs.ReconcileAccountUi import Ui_ReconcileAccount
from BudgetMagician.magician.models import Account, Transaction, BudgetSubcategory
from BudgetMagician.settings import DATABASE_DRIVER


class ReconcileAccount(QDialog, Ui_ReconcileAccount):
    account_reconciled = Signal(int)

    def __init__(self, parent, budget_file: str, account_changed_signal):
        super().__init__(parent)
        self.budget_file = budget_file
        self.account_changed_signal = account_changed_signal
        self.current_account_name = ""
        self.setupUi(self)
        self.installEventFilter(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.fill_ui()

        self.account_changed_signal.connect(self.account_changed)
        self.amount.textChanged.connect(self.check_disabled)
        self.cancel_button.clicked.connect(self.close)
        self.ok_button.clicked.connect(self.reconcile_account)

    def fill_ui(self):
        validator = QDoubleValidator(self)
        validator.setDecimals(2)
        self.amount.setValidator(validator)
        self.amount.setText("")

        current_date = date.today()
        self.date.setDate(QDate(current_date.year, current_date.month, current_date.day))

        db: scoped_session[Session]
        with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
            account = db.execute(select(Account.id).where(Account.name == self.current_account_name)).first()

            if account is not None:
                transactions = db.execute(select(Transaction.amount).where(and_(Transaction.account_id == account.id, Transaction.cleared == True))).all()

                amount_sum = sum((transaction.amount for transaction in transactions))

                self.cleared_balance.setText(f"{amount_sum:.2f}")

        self.ok_button.setEnabled(False)

    @Slot()
    def reconcile_account(self):
        current_qdate = self.date.date()
        current_date = date(current_qdate.year(), current_qdate.month(), current_qdate.day())

        current_amount = float(self.amount.text())

        db: scoped_session[Session]
        with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
            account_id = db.execute(select(Account.id).where(Account.name == self.current_account_name)).first()

            budget_subcategory_id = db.execute(select(BudgetSubcategory.id).where(BudgetSubcategory.name == "Income")).first()

            if budget_subcategory_id is None:
                QMessageBox.critical(
                    self,
                    translate("Dialog", "Critical"),
                    translate("Critical", "The income budget category cannot be found and your budget file may be corrupt. Restart BudgetMagician and try again."),
                    QMessageBox.StandardButton.Ok,
                )
            else:
                if account_id is None:
                    QMessageBox.warning(
                        self,
                        translate("Dialog", "Warning"),
                        translate("Warning", "The current account cannot be found. You must create an account before reconciling an account."),
                        QMessageBox.StandardButton.Ok,
                    )
                else:
                    cleared_transactions = db.execute(select(Transaction.amount).where(and_(Transaction.account_id == account_id.id, Transaction.cleared == True))).all()

                    cleared_amount_sum = sum((transaction.amount for transaction in cleared_transactions))

                    new_amount = current_amount - cleared_amount_sum

                    if new_amount > 0 or new_amount < 0:
                        new_transaction = Transaction()
                        new_transaction.date = current_date
                        new_transaction.account_id = account_id.id
                        new_transaction.budget_subcategory_id = budget_subcategory_id.id
                        new_transaction.memo = "Reconciliation Transaction"
                        new_transaction.amount = new_amount
                        new_transaction.cleared = True
                        new_transaction.reconciled = True

                        db.add(new_transaction)
                        db.flush()
                        new_transaction_id = new_transaction.id
                        db.commit()
                        self.account_reconciled.emit(new_transaction_id)
                        self.close()

    @Slot()
    def check_disabled(self):
        enabled = bool(self.amount.text())
        self.ok_button.setEnabled(enabled)

    @Slot(str)
    def account_changed(self, account_name: str):
        self.current_account_name = account_name

    def open(self) -> None:
        self.fill_ui()
        return super().open()

    def eventFilter(self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent) -> bool:
        if arg__1 is self and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Escape, Qt.Key.Key_Enter):
                return True
        return super().eventFilter(arg__1, arg__2)
