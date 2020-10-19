import requests

from asyncio import sleep

from src.models import Domain, TelegramUser
from src.settings import CHECK_PERIOD, Session, IS_BLOCK_IN_RUSSIA_DOMAIN


async def checker():
    """
    Корутина для проверки доменов
    """
    while True:
        session = Session()
        domains = session.query(Domain).join(TelegramUser).with_for_update()

        # TODO: надо использовать прокси сервисы, чтоб не улететь в бан
        for domain in domains:
            try:
                pass
                # response = requests.post(url=IS_BLOCK_IN_RUSSIA_DOMAIN, data={"host": domain.url})
                # response
        #         pass
        #         # await sleep(100)
            except Exception as err:
                pass
        session.commit()
        await sleep(CHECK_PERIOD)  # Проверка будет производиться раз в CHECK_PERIOD
