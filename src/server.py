from aiogram.utils import executor
from aiogram.utils.exceptions import NetworkError

from src.settings import dp
from src.handlers import *
from src.utils import checker

try:
    dp.loop.create_task(checker())
    executor.start_polling(dp, skip_updates=True)

except NetworkError as err:
    print(err)
