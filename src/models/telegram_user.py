from sqlalchemy import Column, Integer, String

from src.settings import Base


class TelegramUser(Base):
    __tablename__ = "telegram_user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    tg_id = Column(String, unique=True)

    def __init__(self, username: str, tg_id: str):
        self.username = username
        self.tg_id = tg_id

    def __str__(self):
        return self.username
