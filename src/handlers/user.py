import logging

from aiogram import types

from src.settings import dp, bot


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """
    Получаем временную почту
    """
    user_id = message.from_user.id
    chat_id = message["chat"]["id"]
    logging.info(filename="user_handler.log")
    await bot.send_message(chat_id=chat_id, text="hello")
