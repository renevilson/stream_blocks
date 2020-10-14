from sqlalchemy import create_engine, MetaData

from src.models import Domain, TelegramUser
from src.settings import DSN


def create_tables(engine):
    """
    Создаем таблицы для сохранения отслеживаемых ресурсов
    """

    if engine.dialect.has_table(engine, "domain") or engine.dialect.has_table(engine, "telegram_user"):
        return

    meta = MetaData()
    meta.create_all(bind=engine, tables=[Domain, TelegramUser])


if __name__ == "__main__":
    engine = create_engine(DSN)
    create_tables(engine)
