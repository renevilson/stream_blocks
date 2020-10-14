import datetime

from sqlalchemy import Table, Column, Integer, String, Date

from src.settings import meta

Domain = Table(
    "domain", meta,
    Column("id", Integer, primary_key=True),
    Column("url", String),
    Column("add_date", Date, default=datetime.datetime.now),
    Column("block_date", Date, nullable=True),
)
