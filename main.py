import asyncio
import logging
from app import *
from bot import bot, dp
from app.utils import *
from aiogram import types, F
from app.database.base import async_main

logging.basicConfig(level=logging.INFO)


@bot.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: types.PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


@bot.message(F.successful_payment)
async def successful_payment(message: types.Message):
    await message.answer(f'Успешно произведена оплата {message.successful_payment.total_amount} ⭐\n'
                         f'ID операции: `{message.successful_payment.telegram_payment_charge_id}`',
                         parse_mode='MARKDOWN')


# async def TestLoop():
#     while True:
#         try:
#             ...
#         except Exception as err:
#             log(f'TestLoop error: {err}')
#
#         await asyncio.sleep(60)


async def main():
    await async_main()

    # loop = asyncio.get_event_loop()
    # task = loop.create_task(TestLoop())

    dp.include_routers(
        commands_router, main_state_router, main_buttons_router, messages_router
    )
    try:
        await dp.start_polling(bot)
    except:
        pass


if __name__ == '__main__':
    asyncio.run(main())
