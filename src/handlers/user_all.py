from aiogram import types

from src.settings import dp, bot, Session
from src.models import Domain, TelegramUser


@dp.message_handler(commands=["all"])
async def all_domain(message: types.Message):
    """
    Отображение всех доменов, которые добавил пользователь
    """
    user_id = message.from_user.id
    chat_id = message["chat"]["id"]
    session = Session()

    response = list()
    results = session.query(Domain).join(TelegramUser).filter_by(tg_id=user_id).values("url", "block_date")
    for result in results:
        if result[1]:
            response.append(f"{result[0]} заблокирован от {result[1]}")
        else:
            response.append(f"{result[0]} доступен")

    res = "\n".join(response)
    text = f"""
Вы следите за следующими доменами:
{res}
"""
    await bot.send_message(chat_id=chat_id, text=text)
