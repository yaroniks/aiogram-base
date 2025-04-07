from app.utils import *
import app.keyboards as kb
from config import settings
from app.database.models import *
from aiogram import types, F, Router
from aiogram.types import InlineKeyboardButton

router = Router(name='Buttons')


# @router.callback_query(F.data == '')
# async def main_page_query(callback: types.CallbackQuery):
#     await callback.answer()
#     ...
