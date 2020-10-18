from asyncio import sleep

from src.settings import CHECK_PERIOD


async def checker():
    """
    Корутина для проверки доменов
    """
    while True:
        print("hello")
        await sleep(CHECK_PERIOD)  # Проверка будет производиться раз в CHECK_PERIOD
