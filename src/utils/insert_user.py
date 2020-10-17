from src.models import TelegramUser
from src.settings import engine


async def insert_domain(username: str, telegram_id: str) -> bool:
    """
    Добавление домена для отслеживания
    """

    async with engine.acquire() as conn:
        result = await conn.execute(TelegramUser.insert(username=username, tg_id=telegram_id))

    return True
