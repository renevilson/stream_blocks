from aiogram import types

from src.settings import dp, bot
from src.utils import DatabaseWorker


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """
    Получаем временную почту
    """
    worker = DatabaseWorker(message)
    response = worker.start()
    await bot.send_message(**response)
