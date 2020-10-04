import datetime

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey

from src.Validations import TableAlreadyExists
from src.settings import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def create_tables(engine):
    """
    Создаем таблицы для сохранения отслеживаемых ресурсов
    """

    if engine.dialect.has_table(engine, "domain") or engine.dialect.has_table(engine, "telegram_user"):
        raise TableAlreadyExists

    meta = MetaData()

    domain = Table(
        "domain", meta,
        Column("id", Integer, primary_key=True),
        Column("url", String),
        Column("add_date", Date, default=datetime.datetime.now),
        Column("block_date", Date, nullable=True),
    )

    telegram_user = Table(
        "telegram_user", meta,
        Column("id", Integer, primary_key=True),
        Column("domain_id", Integer, ForeignKey("domain.id")),
        Column("username", String),
        Column("tg_id", String),
    )

    meta.create_all(bind=engine, tables=[domain, telegram_user])


if __name__ == "__main__":
    engine = create_engine(DSN)
    create_tables(engine)
