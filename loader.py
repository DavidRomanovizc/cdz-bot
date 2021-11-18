from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config
from utils.db_api.database import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode="Markdown")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()