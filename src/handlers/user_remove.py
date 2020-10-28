from aiogram import types

from src.settings import dp, bot
from src.utils import DatabaseWorker


@dp.message_handler(commands=["remove"])
async def remove_domain(message: types.Message):
    """
    Удаление домена из отслеживаемых
    """
    worker = DatabaseWorker(message)
    response = worker.remove_domain()
    await bot.send_message(**response)
