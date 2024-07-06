from datetime import date

import PySide6
from PySide6 import QtCore
from PySide6.QtCore import Qt, Signal, QDate, Slot
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDialog, QMessageBox
from sqlalchemy import select
from sqlalchemy.orm import scoped_session, Session

from BudgetMagician.dialogs.MakeATransferUi import Ui_MakeATransfer
from BudgetMagician.magician.models import Transaction, Account
from BudgetMagician.magician.queries import get_names_list
from BudgetMagician.utils.combox_utils import fill_combo_box, get_combo_box_dict_from_list
from BudgetMagician.utils.db import get_magic_session
from BudgetMagician.utils.qt import translate


class MakeATransfer(QDialog, Ui_MakeATransfer):
    transfer_added = Signal(tuple)

    def __init__(self, parent, budget_file):
        super().__init__(parent)
        self.budget_file = budget_file
        self.setupUi(self)
        self.installEventFilter(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.fill_ui()
        self.cancel_button.clicked.connect(self.close)
        self.ok_button.clicked.connect(self.ok_clicked)
        self.amount.textChanged.connect(self.check_disabled)

    def fill_ui(self):
        current_date = date.today()
        self.date.setDate(QDate(current_date.year, current_date.month, current_date.day))
        self.amount.setText("")
        validator = QDoubleValidator(self)
        validator.setDecimals(2)
        validator.setBottom(0.00)
        self.amount.setValidator(validator)
        self.ok_button.setEnabled(False)

        accounts_dict = get_combo_box_dict_from_list(get_names_list(self.budget_file, Account))
        fill_combo_box(self.from_combo, accounts_dict)
        fill_combo_box(self.to_combo, accounts_dict)

    @Slot()
    def check_disabled(self):
        enabled = bool(self.amount.text())
        self.ok_button.setEnabled(enabled)

    @Slot()
    def ok_clicked(self):
        acquired_qdate = self.date.date()
        acquired_date = date(acquired_qdate.year(), acquired_qdate.month(), acquired_qdate.day())
        from_account_text = self.from_combo.currentText()
        to_account_text = self.to_combo.currentText()
        amount_text = self.amount.text()
        memo_text = self.memo.text()

        if from_account_text == "" or to_account_text == "":
            QMessageBox.warning(self, translate("Dialog", "Warning"), translate("Warning", "You must select a to and from account."))
            return

        if "-" in amount_text:
            QMessageBox.warning(self, translate("Dialog", "Warning"), translate("Warning", "You must provide a positive amount to transfer."))
            return

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            from_account_id = db.execute(select(Account.id).where(Account.name == from_account_text)).first()
            to_account_id = db.execute(select(Account.id).where(Account.name == to_account_text)).first()

            if from_account_id is None:
                QMessageBox.critical(
                    self,
                    translate("Dialog", "Critical"),
                    translate("Critical", "The from account in question was not found and your budget file may be corrupted. Please restart the application and try again."),
                )
                return

            if to_account_id is None:
                QMessageBox.critical(
                    self,
                    translate("Dialog", "Critical"),
                    translate("Critical", "The to account in question was not found and your budget file may be corrupted. Please restart the application and try again."),
                )
                return

            from_transaction = Transaction()
            from_transaction.date = acquired_date
            from_transaction.account_id = from_account_id.id
            from_transaction.memo = memo_text
            from_transaction.amount = float(f"-{amount_text}")
            from_transaction.cleared = False
            from_transaction.reconciled = False

            to_transaction = Transaction()
            to_transaction.date = acquired_date
            to_transaction.account_id = to_account_id.id
            to_transaction.memo = memo_text
            to_transaction.amount = float(amount_text)
            to_transaction.cleared = False
            to_transaction.reconciled = False

            db.add(from_transaction)
            db.add(to_transaction)
            db.flush()
            from_transaction_id = from_transaction.id
            to_transaction_id = to_transaction.id
            db.commit()

        self.transfer_added.emit((from_transaction_id, to_transaction_id))
        self.close()

    def open(self) -> None:
        self.fill_ui()
        return super().open()

    def eventFilter(self, arg__1: PySide6.QtCore.QObject, arg__2: PySide6.QtCore.QEvent) -> bool:
        if arg__1 is self and arg__2.type() == QtCore.QEvent.Type.KeyPress:
            if arg__2.key() in (Qt.Key.Key_Return, Qt.Key.Key_Escape, Qt.Key.Key_Enter):
                return True
        return super().eventFilter(arg__1, arg__2)
