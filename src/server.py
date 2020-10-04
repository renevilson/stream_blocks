from aiogram.utils import executor
from aiogram.utils.exceptions import NetworkError

from src.settings import dp
import src.handlers

try:
    executor.start_polling(dp, skip_updates=True)
except NetworkError as err:
    print(err)
