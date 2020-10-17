from sqlalchemy import Table, Column, Integer, String, ForeignKey

from src.settings import meta

TelegramUser = Table(
    "telegram_user", meta,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("tg_id", String),
)
