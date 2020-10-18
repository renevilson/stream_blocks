from aiogram import types


async def get_domain(message: types.Message):
    """
    Получение домена из сообщения
    """

    url = message.text.replace("/add", "").replace(" ", "")
    if url:
        return url
