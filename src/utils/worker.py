from aiogram import types
from sqlalchemy.sql import ClauseElement

from src.models import Domain, TelegramUser
from src.settings import Session, Base


class DatabaseWorker:
    """
    Класс для работы с базой данных
    """

    def __init__(self, message: types.Message):
        self.session = Session()
        self.chat_id = message["chat"]["id"]
        self.user_id = message.from_user.id
        self.username = message.from_user.username
        self.text = message.text

    def get_all(self) -> dict:
        """
        Получение спика всех доменов
        """
        response = list()
        results = self.session.query(Domain).join(TelegramUser). \
            filter_by(tg_id=self.user_id).values("url", "block_date")
        for result in results:
            if result[1]:
                response.append(f"{result[0]} заблокирован от {result[1]}")
            else:
                response.append(f"{result[0]} доступен")

        res = "\n".join(response)
        text = f"Вы следите за следующими доменами:\n{res}"
        return {"chat_id": self.chat_id, "text": text}

    def add_domain(self) -> dict:
        """
        Метод для добавления домена к списку отслеживаемых.
        """

        user, _ = self._get_or_create(TelegramUser, tg_id=self.user_id, username=self.username, chat_id=self.chat_id)
        url = self._get_domain(self.text)

        if not url:
            return {"chat_id": self.chat_id, "text": "Домен для отслеживания введен некорректно"}

        _, created = self._get_or_create(Domain, url=url, user_id=user.id)
        text = f"Домен {url} добавлен."
        if not created:
            text = f"Вы уже следите за доменом {url}"
        return {"chat_id": self.chat_id, "text": text}

    def remove_domain(self) -> dict:
        """
        Метод для удаления отслеживаемого домена
        """

        url = self._get_domain(self.text)
        if not url:
            return {"chat_id": self.chat_id, "text": "Некорректный домен"}

        obj = self.session.query(Domain).filter_by(url=url).first()
        if not obj:
            return {"chat_id": self.chat_id, "text": "Такой домен не отслеживается"}
        self.session.delete(obj)
        self.session.commit()
        response = f"Домен {url} удален"
        return {"chat_id": self.chat_id, "text": response}

    def start(self) -> dict:
        """
        Начало работы с ботом. Добавление пользователя в базу данных.
        """
        self._get_or_create(TelegramUser, username=self.username, tg_id=self.user_id, chat_id=self.chat_id)
        response = f"Для отслеживания домена напишите /add domain.\n" \
                   f"Для удаления домена используйте /remove domain. \n" \
                   f"Для получения списка доменов введите /all"
        return {"chat_id": self.chat_id, "text": response}

    @staticmethod
    def _get_domain(text: str) -> str or None:
        """
        Выделение домена из сообщения
        """
        try:
            return text.split(" ")[-1]
        except Exception as err:
            return None

    def _get_or_create(self, model: Base, defaults=None, **kwargs) -> (Base, bool):
        instance = self.session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, False
        else:
            params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
            params.update(defaults or {})
            instance = model(**params)
            self.session.add(instance)
            self.session.commit()
            return instance, True
