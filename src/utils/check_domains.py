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
        domains = session.query(Domain).with_for_update()
        s = requests.Session()
        for domain in domains:

                response = s.post(url="https://isitblockedinrussia.com/", json={"host": domain.url})
                response_dict = response.json()
                ips = response_dict.get("ips")
                urls = response_dict.get("domain")
                text = ""

                if ips and len(ips):
                    blocked = ips[0].get('blocked')
                    if blocked:
                        block_date = blocked[0].get('decision_date')
                    # ip_address = ips[0].get('value')
                    # text += f"IP {ip_address} заблокирован от {block_date}"
                        if not domain.block_date:
                            domain.block_date = block_date
                # if domain:
                #     block_date = domain[0].get('blocked')[-1].get('decision_date')
                #     text += f"domain {domain.url} заблокирован от {block_date}"
                #     if not domain.block_date:
                #         domain.block_date = block_date
                print(domain.user)
                if text:
                    print(domain.user)
                    # await bot.send_message(chat_id=domain.)


        # except Exception as err:
            #     print(err)
            #     break
        session.commit()
        await sleep(CHECK_PERIOD)  # Проверка будет производиться раз в CHECK_PERIOD
