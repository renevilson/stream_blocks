from src.models import *
from src.settings import Base, engine


def create_tables():
    """
    Создаем таблицы для сохранения отслеживаемых ресурсов
    """
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
