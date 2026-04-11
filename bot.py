from config import settings

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession


async def create_bot():
    # session = AiohttpSession(proxy="")
    bot = Bot(settings.BOT_TOKEN)  # , session=session
    dp = Dispatcher(storage=MemoryStorage())
    return bot, dp


bot, dp = asyncio.run(create_bot())
