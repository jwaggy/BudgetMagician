import calendar
from datetime import date
from functools import cached_property
from typing import Union, Any

import PySide6
from PySide6.QtCore import Slot, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QDoubleValidator, QColor
from PySide6.QtWidgets import QLineEdit
from sqlalchemy import select, and_
from sqlalchemy.orm import scoped_session, Session

from BudgetMagician.magician.models import Budget, Transaction, BudgetSubcategory
from BudgetMagician.utils.db import get_magic_session


class BudgetSubcategoryRow:
    def __init__(self, idd, date_to_search, budget_file):
        self.budget_file: str = budget_file
        self.id: int = idd
        self.date: date = date_to_search

        self.budgeted_amount = "0.00"
        self.budget_subcategory_name = ""

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            budget = db.scalars(select(Budget).where(and_(Budget.budget_subcategory_id == self.id, Budget.date == self.date))).first()

            if budget is None:
                budget_subcategory = db.scalars(select(BudgetSubcategory).where(BudgetSubcategory.id == self.id)).first()

                if budget_subcategory is not None:
                    new_budget = Budget()
                    new_budget.date = self.date
                    new_budget.budget_subcategory = budget_subcategory
                    new_budget.budgeted = 0.00

                    self.budgeted_amount = "0.00"
                    self.budget_subcategory_name = budget_subcategory.name
                    db.add(new_budget)
                    db.commit()
                else:
                    self.budgeted_amount = "0.00"
                    self.budget_subcategory_name = "ERROR"
            else:
                self.budgeted_amount = f"{budget.budgeted:.2f}"
                self.budget_subcategory_name = budget.budget_subcategory.name

        self.amount = QLineEdit()
        validator = QDoubleValidator()
        validator.setDecimals(2)
        self.amount.setValidator(validator)
        self.amount.setText(self.budgeted_amount)

        self.amount.editingFinished.connect(self.change_budgeted_amount)

    def get_budgeted_amount(self):
        return float(self.budgeted_amount)

    @cached_property
    def get_budget_subcategory_name(self):
        return self.budget_subcategory_name

    @cached_property
    def get_outflows(self):
        max_day = calendar.monthrange(self.date.year, self.date.month)[1]
        max_date = date(self.date.year, self.date.month, max_day)

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            transactions = db.execute(
                select(Transaction.amount).where(and_(Transaction.budget_subcategory_id == self.id, Transaction.date >= self.date, Transaction.date <= max_date))
            ).all()

            outflows_generator = (transaction.amount for transaction in transactions)

        return sum(outflows_generator)

    @Slot()
    def change_budgeted_amount(self):
        self.budgeted_amount = self.amount.text()

        db: scoped_session[Session]
        with get_magic_session(self.budget_file) as db:
            budget = db.scalars(select(Budget).where(and_(Budget.budget_subcategory_id == self.id, Budget.date == self.date))).first()

            if budget is not None:
                budget.budgeted = float(self.budgeted_amount)
                db.commit()


class BudgetTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.column_names = ["Budgeted", "Outflows", "Balance"]
        self.rows: list[BudgetSubcategoryRow] = []

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.rows)

    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.column_names)

    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.column_names[section]
            if orientation == Qt.Orientation.Vertical:
                return self.rows[section].get_budget_subcategory_name

    def insert_budget_subcategory_row(self, row, budget_subcategory_row):
        self.beginInsertRows(QModelIndex(), row, row)
        self.rows.append(budget_subcategory_row)
        self.endInsertRows()

    def removeRows(self, row: int, count: int, parent=QModelIndex()) -> bool:
        self.beginRemoveRows(parent, row, row + count - 1)

        for r in range(count):
            del self.rows[row]

        self.endRemoveRows()
        return True

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role: int = ...) -> Any:
        row = index.row()
        column = index.column()
        budget_subcategory_row = self.rows[row]
        outflows = budget_subcategory_row.get_outflows
        balance = budget_subcategory_row.get_budgeted_amount() - outflows

        if role == Qt.ItemDataRole.DisplayRole:
            if column == 1:
                return f"{outflows:.2f}"
            if column == 2:
                return f"{balance:.2f}"

        if role == Qt.ItemDataRole.BackgroundRole and column == 2:
            if balance >= 0:
                return QColor("white")
            if balance < 0:
                return QColor("red")
