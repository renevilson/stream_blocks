from sqlalchemy import Column, Integer, String

from src.settings import Base


class TelegramUser(Base):
    __tablename__ = "telegram_user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    tg_id = Column(Integer, unique=True)
    chat_id = Column(Integer, unique=True)

    def __init__(self, username: str, tg_id: int, chat_id: int):
        self.username = username
        self.tg_id = tg_id
        self.chat_id = chat_id

    def __str__(self):
        return self.username
