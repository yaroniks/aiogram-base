import asyncio
import logging
from app import *
from config import settings
from aiogram import Bot, Dispatcher
from app.database.base import async_main
from aiogram.fsm.storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    await async_main()

    dp.include_routers(
        commands_router, main_state_router, main_buttons_router, messages_router
    )
    try:
        await dp.start_polling(bot)
    except:
        pass


if __name__ == '__main__':
    asyncio.run(main())
