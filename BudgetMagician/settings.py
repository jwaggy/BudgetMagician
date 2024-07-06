from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parent

MIGRATIONS_DIR = MODULE_DIR / "migrations"

IS_DEV = True

DATABASE_DRIVER = "sqlite"