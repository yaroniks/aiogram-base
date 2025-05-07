import asyncio
import logging
from app import *
from bot import bot, dp
from app.database.base import async_main

logging.basicConfig(level=logging.INFO)


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
