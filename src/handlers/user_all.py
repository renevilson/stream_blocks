from aiogram import types

from src.settings import dp, bot
from src.utils import DatabaseWorker


@dp.message_handler(commands=["all"])
async def all_domain(message: types.Message):
    """
    Отображение всех доменов, которые добавил пользователь
    """
    worker = DatabaseWorker(message)
    response = worker.get_all()
    await bot.send_message(**response)
