"""initial

Revision ID: 3ae1ef9f5030
Revises: 
Create Date: 2023-08-29 16:20:25.832659

"""
from datetime import date
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3ae1ef9f5030"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "account",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
        sa.Column("name", sa.String, unique=True, nullable=False),
        sa.Column("type", sa.Integer, nullable=False),
        sa.Column("on_budget", sa.Boolean, nullable=False),
    )

    budget_category = op.create_table(
        "budget_category",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
        sa.Column("name", sa.String, unique=True, nullable=False),
    )

    budget = op.create_table(
        "budget",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
        sa.Column("date", sa.Date, nullable=False),
        sa.Column("budget_subcategory_id", sa.Integer, sa.ForeignKey("budget_subcategory.id"), index=True, nullable=False),
        sa.Column("budgeted", sa.Float, nullable=False),
    )

    budget_subcategory = op.create_table(
        "budget_subcategory",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
        sa.Column("name", sa.String, unique=True, nullable=False),
        sa.Column("budget_category_id", sa.Integer, sa.ForeignKey("budget_category.id"), index=True, nullable=False),
    )

    op.create_table(
        "payee",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
        sa.Column("name", sa.String, unique=True, nullable=False)
    )

    op.create_table(
        "transaction",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
        sa.Column("date", sa.Date, nullable=False),
        sa.Column("account_id", sa.Integer, sa.ForeignKey("account.id"), nullable=False, index=True),
        sa.Column("payee_id", sa.Integer, sa.ForeignKey("payee.id"), nullable=True, index=True),
        sa.Column("budget_subcategory_id", sa.Integer, sa.ForeignKey("budget_subcategory.id"), nullable=True, index=True),
        sa.Column("memo", sa.String),
        sa.Column("amount", sa.Float, nullable=False),
        sa.Column("cleared", sa.Boolean, nullable=False),
        sa.Column("reconciled", sa.Boolean, nullable=False),
    )

    op.bulk_insert(
        budget_category,
        [
            {"name": "SYSTEM"},
            {"name": "Giving"},
            {"name": "Monthly Bills"},
            {"name": "Everyday Expenses"},
            {"name": "Rainy Day Funds"},
            {"name": "Savings Goals"},
            {"name": "Debt"}
        ]
    )

    op.bulk_insert(
        budget_subcategory,
        [
            {"name": "Income", "budget_category_id": 1, "budgeted": 0.0},
            {"name": "Tithing", "budget_category_id": 2, "budgeted": 0.0},
            {"name": "Charitable", "budget_category_id": 2, "budgeted": 0.0},
            {"name": "Rent/Mortgage", "budget_category_id": 3, "budgeted": 0.0},
            {"name": "Phone", "budget_category_id": 3, "budgeted": 0.0},
            {"name": "Internet", "budget_category_id": 3, "budgeted": 0.0},
            {"name": "Cable", "budget_category_id": 3, "budgeted": 0.0},
            {"name": "Electricity", "budget_category_id": 3, "budgeted": 0.0},
            {"name": "Water", "budget_category_id": 3, "budgeted": 0.0},
            {"name": "Natural Gas/Propane/Oil", "budget_category_id": 2, "budgeted": 0.0},
            {"name": "Groceries", "budget_category_id": 4, "budgeted": 0.0},
            {"name": "Fuel", "budget_category_id": 4, "budgeted": 0.0},
            {"name": "Spending Money", "budget_category_id": 4, "budgeted": 0.0},
            {"name": "Restaurants", "budget_category_id": 4, "budgeted": 0.0},
            {"name": "Medical", "budget_category_id": 4, "budgeted": 0.0},
            {"name": "Clothing", "budget_category_id": 4, "budgeted": 0.0},
            {"name": "Household Goods", "budget_category_id": 4, "budgeted": 0.0},
            {"name": "Emergency Fund", "budget_category_id": 5, "budgeted": 0.0},
            {"name": "Car Repairs", "budget_category_id": 5, "budgeted": 0.0},
            {"name": "Life Insurance", "budget_category_id": 5, "budgeted": 0.0},
            {"name": "Health Insurance", "budget_category_id": 5, "budgeted": 0.0},
            {"name": "Birthdays", "budget_category_id": 5, "budgeted": 0.0},
            {"name": "Christmas", "budget_category_id": 5, "budgeted": 0.0},
            {"name": "Vacation", "budget_category_id": 6, "budgeted": 0.0},
            {"name": "Car Replacement", "budget_category_id": 6, "budgeted": 0.0},
            {"name": "Car Payment", "budget_category_id": 7, "budgeted": 0.0},
            {"name": "Student Loan Payment", "budget_category_id": 7, "budgeted": 0.0},
            {"name": "Personal Loan Payment", "budget_category_id": 7, "budgeted": 0.0},
        ]
    )

    this_year = date.today().year
    budget_dict_list = []

    for month in range(1, 13):
        for category_id in range(2, 29):
            budget_dict_list.append({"date": date(this_year, month, 1), "budget_subcategory_id": category_id, "budgeted": 0.00})

    op.bulk_insert(budget, budget_dict_list)


def downgrade() -> None:
    op.drop_table("transaction")

    op.drop_table("payee")

    op.drop_table("budget_subcategory")

    op.drop_table("budget_category")

    op.drop_table("budget")

    op.drop_table("account")
