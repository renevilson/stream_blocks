import os
import asyncio

from environs import Env
from aiogram import Bot, Dispatcher

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.getenv("ENV_PATH", os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"), )
env = Env()
Env.read_env(ENV_PATH)

IS_BLOCK_IN_RUSSIA_DOMAIN = env.str("IS_BLOCK_IN_RUSSIA_DOMAIN", "https://isitblockedinrussia.com/")
API_TOKEN = env.str("API_TOKEN")

# PSQL
POSTGRES_HOST = env.str("POSTGRES_HOST", "0.0.0.0")
POSTGRES_PORT = env.int("POSTGRES_PORT", 5433)
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", "")
POSTGRES_USER = env.str("POSTGRES_USER", "")
POSTGRES_DB = env.str("POSTGRES_DB", "")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# loop = asyncio.get_event_loop()
