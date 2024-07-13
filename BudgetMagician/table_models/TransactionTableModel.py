from datetime import date
from functools import cached_property
from typing import Union, Any

import PySide6
from PySide6.QtCore import QDate, QAbstractTableModel, Qt, QModelIndex, Slot
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QDateEdit, QComboBox, QLineEdit, QCheckBox, QPushButton
from endstech_shared.qt_combo_box_utils import fill_combo_box, get_combo_box_dict_from_list, set_combo_box_by_text
from endstech_shared.sqlalchemy_utils import get_magic_session
from sqlalchemy import select
from sqlalchemy.orm import scoped_session, Session

from BudgetMagician.magician.models import Payee, BudgetSubcategory, Transaction
from BudgetMagician.magician.queries import get_names_list
from BudgetMagician.settings import DATABASE_DRIVER


class TransactionRow:
    def __init__(self, idd, budget_file, categories_changed_signal, payees_changed_signal):
        self.id = idd
        self.categories_changed_signal = categories_changed_signal
        self.payees_changed_signal = payees_changed_signal
        self.budget_file = budget_file
        self.transaction_date = date.today()
        self.transaction_payee_name = ""
        self.transaction_budget_subcategory_name = ""
        self.transaction_memo = ""
        self.transaction_amount = "0.00"
        self.transaction_cleared = False
        self.transaction_reconciled = False

        if self.id is not None:
            db: scoped_session[Session]
            with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
                row = db.scalars(select(Transaction).where(Transaction.id == self.id)).first()

                if row is not None:
                    self.transaction_date = row.date
                    self.transaction_payee_name = "" if row.payee is None else row.payee.name
                    self.transaction_budget_subcategory_name = "" if row.budget_subcategory is None else row.budget_subcategory.name
                    self.transaction_memo = "" if row.memo is None else row.memo
                    self.transaction_amount = f"{row.amount:.2f}"
                    self.transaction_cleared = row.cleared
                    self.transaction_reconciled = row.reconciled

        self.date = QDateEdit()
        self.date.setCalendarPopup(True)
        self.date.setDate(QDate(self.transaction_date.year, self.transaction_date.month, self.transaction_date.day))

        self.payee = QComboBox()
        fill_combo_box(self.payee, get_combo_box_dict_from_list(get_names_list(self.budget_file, Payee)))
        set_combo_box_by_text(self.payee, self.transaction_payee_name)

        self.budget_subcategory = QComboBox()
        fill_combo_box(self.budget_subcategory, get_combo_box_dict_from_list(get_names_list(self.budget_file, BudgetSubcategory)))
        set_combo_box_by_text(self.budget_subcategory, self.transaction_budget_subcategory_name)

        self.memo = QLineEdit()
        memo_enabled = self.transaction_memo != "Starting Balance"
        self.memo.setText(self.transaction_memo)
        self.memo.setEnabled(memo_enabled)

        self.amount = QLineEdit()
        validator = QDoubleValidator()
        validator.setDecimals(2)
        self.amount.setText(self.transaction_amount)
        self.amount.setValidator(validator)

        self.cleared = QCheckBox("Cleared")
        cleared_enabled = not self.transaction_reconciled and self.transaction_memo != "Starting Balance"
        self.cleared.setEnabled(cleared_enabled)
        self.cleared.setChecked(self.transaction_cleared)

        self.delete_button = QPushButton("Delete")
        delete_enabled = self.transaction_memo != "Starting Balance"
        self.delete_button.setEnabled(delete_enabled)

        self.date.userDateChanged.connect(self.change_transaction_date)
        self.payee.currentTextChanged.connect(self.change_transaction_payee)
        self.budget_subcategory.currentTextChanged.connect(self.change_transaction_category)
        self.memo.editingFinished.connect(self.change_transaction_memo)
        self.amount.editingFinished.connect(self.change_transaction_amount)
        self.cleared.stateChanged.connect(self.change_transaction_cleared)
        self.categories_changed_signal.connect(self.transaction_categories_changed)
        self.payees_changed_signal.connect(self.transaction_payees_changed)

    @Slot(QDate)
    def change_transaction_date(self, qdate: QDate):
        fetched_date = date(qdate.year(), qdate.month(), qdate.day())
        self.transaction_date = fetched_date

        db: scoped_session[Session]
        with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
            transaction = db.scalars(select(Transaction).where(Transaction.id == self.id)).first()

            if transaction is not None:
                transaction.date = fetched_date
                db.commit()

    @Slot(str)
    def change_transaction_payee(self, payee_name: str):
        self.transaction_payee_name = payee_name

        db: scoped_session[Session]
        with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
            payee = db.scalars(select(Payee).where(Payee.name == payee_name)).first()

            if payee is not None:
                transaction = db.scalars(select(Transaction).where(Transaction.id == self.id)).first()

                if transaction is not None:
                    transaction.payee = payee
                    db.commit()

    @Slot(str)
    def change_transaction_category(self, category_name: str):
        self.transaction_budget_subcategory_name = category_name

        db: scoped_session[Session]
        with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
            category = db.scalars(select(BudgetSubcategory).where(BudgetSubcategory.name == category_name)).first()
    
            if category is not None:
                transaction = db.scalars(select(Transaction).where(Transaction.id == self.id)).first()
    
                if transaction is not None:
                    transaction.budget_subcategory = category
                    db.commit()

    @Slot()
    def change_transaction_memo(self):
        new_memo = self.memo.text()
        self.transaction_memo = new_memo

        db: scoped_session[Session]
        with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
            transaction = db.scalars(select(Transaction).where(Transaction.id == self.id)).first()

            if transaction is not None:
                transaction.memo = new_memo
                db.commit()

    @Slot()
    def change_transaction_amount(self):
        new_amount = float(self.amount.text())
        self.transaction_amount = f"{new_amount:.2f}"

        db: scoped_session[Session]
        with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
            transaction = db.scalars(select(Transaction).where(Transaction.id == self.id)).first()

            if transaction is not None:
                transaction.amount = new_amount
                db.commit()

    @Slot()
    def change_transaction_cleared(self):
        checked = self.cleared.isChecked()
        self.transaction_cleared = checked

        db: scoped_session[Session]
        with get_magic_session(self.budget_file, DATABASE_DRIVER) as db:
            transaction = db.scalars(select(Transaction).where(Transaction.id == self.id)).first()

            if transaction is not None:
                transaction.cleared = checked
                db.commit()

    @Slot()
    def transaction_categories_changed(self):
        self.budget_subcategory.currentTextChanged.disconnect()
        fill_combo_box(self.budget_subcategory, get_combo_box_dict_from_list(get_names_list(self.budget_file, BudgetSubcategory)))
        set_combo_box_by_text(self.budget_subcategory, self.transaction_budget_subcategory_name)
        self.budget_subcategory.currentTextChanged.connect(self.change_transaction_category)

    @Slot()
    def transaction_payees_changed(self):
        self.payee.currentTextChanged.disconnect()
        fill_combo_box(self.payee, get_combo_box_dict_from_list(get_names_list(self.budget_file, Payee)))
        set_combo_box_by_text(self.payee, self.transaction_payee_name)
        self.payee.currentTextChanged.connect(self.change_transaction_payee)

    @cached_property
    def get_id(self):
        return self.id

    @property
    def get_date(self):
        qdate = self.date.date()
        return date(qdate.year(), qdate.month(), qdate.day())


class TransactionTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.column_names = ["Date", "Payee", "Category", "Memo", "Amount", "Cleared", "Delete"]
        self.rows: list[TransactionRow] = []

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.rows)

    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.column_names)

    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.column_names[section]
            if orientation == Qt.Orientation.Vertical:
                return self.rows[section].get_id

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int = ...) -> Any:
        ...

    def insert_transaction_row(self, row, transaction_row):
        self.beginInsertRows(QModelIndex(), row, row)
        self.rows.append(transaction_row)
        self.endInsertRows()

    def removeRows(self, row: int, count: int, parent=QModelIndex()) -> bool:
        self.beginRemoveRows(parent, row, row + count - 1)

        for r in range(count):
            del self.rows[row]

        self.endRemoveRows()
        return True
