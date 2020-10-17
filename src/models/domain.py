import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey

from src.settings import Base


class Domain(Base):
    __tablename__ = "domain"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    add_date = Column(Date, default=datetime.datetime.now)
    block_date = Column(Date, nullable=True)
    user_id = Column(Integer, ForeignKey("telegram_user.id"))

    def __init__(self, url: str, user_id: int):
        self.url = url
        self.user_id = user_id

    def __str__(self):
        return self.url
