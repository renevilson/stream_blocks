class TableAlreadyExists(Exception):
    """
    Исключение. Таблица, которую пытаетесь создать существует
    """

    def __init__(self):
        self.message = "Such table already exists"

    def __str__(self):
        return self.message
