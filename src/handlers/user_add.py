from aiogram import types

from src.settings import dp, bot, Session
from src.models import Domain, TelegramUser
from src.utils import get_or_create, get_domain


@dp.message_handler(commands=["add"])
async def add_domain(message: types.Message):
    """
    Сохранение домена для отслеживания
    """

    user_id = message.from_user.id
    chat_id = message["chat"]["id"]
    url = await get_domain(message)
    session = Session()
    user = session.query(TelegramUser).filter_by(tg_id=user_id).first()
    if not user:
        return
    response = "Укажите домен"
    if url:
        get_or_create(Domain, url=url, user_id=user.id)
        response = f"Домен {url} добавлен."
    await bot.send_message(chat_id=chat_id, text=response)
