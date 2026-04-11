import app.utils as utils
import app.keyboards as kb
from config import settings
from app.database.models import *

import logging
from aiogram import types, F, Router
from aiogram.types import InlineKeyboardButton

logger = logging.getLogger(__name__)
router = Router(name='Buttons')


# @router.callback_query(F.data == '')
# async def main_page_query(callback: types.CallbackQuery):
#     await callback.answer()
#     ...
