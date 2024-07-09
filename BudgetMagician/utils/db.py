from contextlib import contextmanager
from typing import Generator, Any

from alembic import command
from alembic.config import Config
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session

from BudgetMagician.exceptions import BudgetMagicianException
from BudgetMagician.settings import DATABASE_DRIVER


@contextmanager
def get_magic_session(path: str) -> Generator[scoped_session[Session], Any, None]:
    if path == "":
        raise BudgetMagicianException("Path must not be an empty string")

    url = URL.create(DATABASE_DRIVER, database=path)

    engine = create_engine(url)

    connection = engine.connect()

    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))

    yield db_session

    db_session.close()
    connection.close()


def run_migrations(script_location: str, path: str) -> None:
    url = URL.create(DATABASE_DRIVER, database=path)
    alembic_config = Config()
    alembic_config.set_main_option("script_location", script_location)
    alembic_config.set_main_option("sqlalchemy.url", str(url))
    command.upgrade(alembic_config, "head")
