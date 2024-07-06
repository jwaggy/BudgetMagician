from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session, scoped_session

from BudgetMagician.magician.models import Account, Transaction
from BudgetMagician.utils.db import get_magic_session


def get_years_plus_five_for_combobox(path: str, model) -> dict[int, str]:
    current_year = datetime.now().year
    years_dict = {}

    db: scoped_session[Session]
    with get_magic_session(path) as db:
        rows = db.execute(select(model.date).order_by(model.date).distinct()).all()
        years_set = set()
        years_set.add(current_year)

        for row in rows:
            years_set.add(row.date.year)

        year = current_year
        for _ in range(5):
            year += 1
            years_set.add(year)

        for year in sorted(years_set):
            years_dict[year] = str(year)

    return years_dict


def get_names_list(path: str, model, on_budget: bool | None = None) -> list[str]:
    db: scoped_session[Session]
    with get_magic_session(path) as db:
        if model.__name__ == "BudgetCategory":
            rows = db.execute(select(model.name).where(model.name != "SYSTEM").order_by(model.name)).all()
        elif model.__name__ == "Account" and on_budget is not None:
            rows = db.execute(select(model.name).where(model.on_budget == on_budget).order_by(model.name)).all()
        else:
            rows = db.execute(select(model.name).order_by(model.name)).all()
    
        return [row.name for row in rows]


def get_ids_list(path: str, model, on_budget: bool | None = None) -> list[int]:
    db: scoped_session[Session]
    with get_magic_session(path) as db:
        if model.__name__ == "BudgetCategory":
            rows = db.execute(select(model.id).where(model.name != "SYSTEM").order_by(model.name)).all()
        elif model.__name__ == "Account" and on_budget is not None:
            rows = db.execute(select(model.id).where(model.on_budget == on_budget).order_by(model.name)).all()
        else:
            rows = db.execute(select(model.id).order_by(model.name)).all()

        return [row.id for row in rows]


def get_list_of_accounts_with_totals(path: str, on_budget: bool) -> list[list[str | float]]:
    accounts_list = get_names_list(path, Account, on_budget)
    table_data = []

    db: scoped_session[Session]
    with get_magic_session(path) as db:
        for account in accounts_list:
            fetched_account = db.scalars(select(Account).where(Account.name == account)).first()

            if fetched_account is None:
                continue

            data = [account, sum((transaction.amount for transaction in fetched_account.transactions))]
            table_data.append(data)

    return table_data


def get_budget_type_total(path: str, on_budget: bool) -> float:
    accounts_list = get_ids_list(path, Account, on_budget)
    totals = []

    db: scoped_session[Session]
    with get_magic_session(path) as db:
        for account_id in accounts_list:
            rows = db.execute(select(Transaction.amount).where(Transaction.account_id == account_id)).all()

            totals.append(sum((transaction.amount for transaction in rows)))

    return sum(totals)


def get_balances_dict_for_account(path: str, account_name: str) -> dict[str, float]:
    balance_dict = {}

    db: scoped_session[Session]
    with get_magic_session(path) as db:
        fetched_account = db.scalars(select(Account).where(Account.name == account_name)).first()

        if fetched_account is None:
            return {"cleared": 0.00, "uncleared": 0.00, "working": 0.00}

        cleared_total = sum((transaction.amount for transaction in fetched_account.transactions if transaction.cleared is True))

        uncleared_total = sum((transaction.amount for transaction in fetched_account.transactions if transaction.cleared is False))

    balance_dict["cleared"] = cleared_total
    balance_dict["uncleared"] = uncleared_total
    balance_dict["working"] = sum([cleared_total, uncleared_total])

    return balance_dict
