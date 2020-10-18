from aiogram import types

from src.models import TelegramUser
from src.settings import dp, bot
from src.utils import get_or_create


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """
    Получаем временную почту
    """
    user_id = message.from_user.id
    username = message.from_user.username
    chat_id = message["chat"]["id"]
    get_or_create(TelegramUser, username=username, tg_id=user_id, chat_id=chat_id)

    response = f"""
Для отслеживания домена напишите /add domain.
Для удаления домена используйте /remove domain
Для получения списка доменов введите /all
"""
    await bot.send_message(chat_id=chat_id, text=response)
