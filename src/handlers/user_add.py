from aiogram import types

from src.settings import dp, bot
from src.utils import DatabaseWorker


@dp.message_handler(commands=["add"])
async def add_domain(message: types.Message):
    """
    Сохранение домена для отслеживания
    """
    worker = DatabaseWorker(message)
    response = worker.add_domain()
    await bot.send_message(**response)
