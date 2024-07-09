import re
from datetime import date
from typing import List, Optional

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls):
        return re.sub(r"([A-Z])", r" \1", cls.__name__).strip().replace(" ", "_").lower()

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)


class Budget(Base):
    date: Mapped[date] = mapped_column(Date)
    budget_subcategory_id: Mapped[int] = mapped_column(ForeignKey("budget_subcategory.id"), index=True)
    budget_subcategory: Mapped["BudgetSubcategory"] = relationship(back_populates="budget")
    budgeted: Mapped[Optional[float]] = mapped_column(default=0.0)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, date={self.date!r})"


class BudgetCategory(Base):
    name: Mapped[str] = mapped_column(unique=True)
    budget_subcategories: Mapped[List["BudgetSubcategory"]] = relationship(back_populates="budget_category", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r})"


class BudgetSubcategory(Base):
    name: Mapped[str] = mapped_column(unique=True)
    budget_category_id: Mapped[int] = mapped_column(ForeignKey("budget_category.id"), index=True)
    budget_category: Mapped["BudgetCategory"] = relationship(back_populates="budget_subcategories")
    budget: Mapped[List["Budget"]] = relationship(back_populates="budget_subcategory", cascade="all, delete-orphan")
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="budget_subcategory")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r})"


class Account(Base):
    name: Mapped[str] = mapped_column(unique=True)
    type: Mapped[int]
    on_budget: Mapped[bool]
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="account", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, type={self.type!r}, on_budget={self.on_budget!r})"


class Transaction(Base):
    date: Mapped[date] = mapped_column(Date)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"), index=True)
    account: Mapped["Account"] = relationship(back_populates="transactions")
    payee_id: Mapped[Optional[int]] = mapped_column(ForeignKey("payee.id"), index=True)
    payee: Mapped["Payee"] = relationship(back_populates="transactions")
    budget_subcategory_id: Mapped[Optional[int]] = mapped_column(ForeignKey("budget_subcategory.id"), index=True)
    budget_subcategory: Mapped["BudgetSubcategory"] = relationship(back_populates="transactions")
    memo: Mapped[Optional[str]]
    amount: Mapped[float]
    cleared: Mapped[bool]
    reconciled: Mapped[bool]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id!r}, date={self.date!r}, memo={self.memo!r}, amount={self.amount!r}, cleared={self.cleared!r}, reconciled={self.reconciled!r})"
        )


class Payee(Base):
    name: Mapped[str] = mapped_column(unique=True)
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="payee")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r})"
