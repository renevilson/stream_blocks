import requests

from asyncio import sleep

from src.models import Domain, TelegramUser
from src.settings import CHECK_PERIOD, Session, IS_BLOCK_IN_RUSSIA_DOMAIN, bot


async def checker():
    """
    Корутина для проверки доменов
    """
    while True:
        session = Session()
        domains = session.query(Domain, TelegramUser).join(TelegramUser,
                                                           Domain.user_id == TelegramUser.id).with_for_update()
        s = requests.Session()
        for domain in domains:
            if not domain.Domain.block_date:
                response = s.post(
                    url="https://isitblockedinrussia.com/",
                    json={"host": domain.Domain.url}
                )
                response_dict = response.json()
                ips_blocked = response_dict.get("ips")[-1].get("blocked") if response_dict.get("ips") else None
                urls_blocked = response_dict.get("domain", {}).get("blocked")
                text = ""

                #  Проверка на блокировку по домену
                if urls_blocked:
                    decision_date = urls_blocked[-1].get("decision_date")
                    text += f"Домен {domain.Domain.url} заблокирован от {decision_date} \n"
                    domain.Domain.block_date = decision_date

                # Проверка на блокировку по ip адресу
                if ips_blocked:
                    decision_date = ips_blocked[-1].get("decision_date")
                    text += f"ip адрес домена {domain.Domain.url} заблокирован от {decision_date} \n"

                    if not domain.Domain.block_date:
                        domain.Domain.block_date = decision_date

                # Отсылаем пользователю уведомление о блокировке
                if text:
                    await bot.send_message(chat_id=domain.TelegramUser.chat_id, text=text)

                session.commit()
            await sleep(CHECK_PERIOD)  # Проверка будет производиться раз в CHECK_PERIOD
