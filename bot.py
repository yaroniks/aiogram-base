from config import settings
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
