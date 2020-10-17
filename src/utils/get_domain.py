from aiogram import types


async def get_domain(message: types.Message):
    """
    Получение домена из сообщения
    """

    url = message.text.split("/add")
    if url:
        return url
