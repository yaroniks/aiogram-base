import app.utils as utils
import app.keyboards as kb
from config import settings

import logging
from aiogram import types, F, Router

logger = logging.getLogger(__name__)
router = Router(name='Messages')


@router.message(F.text.lower().startswith('привет'))
async def message_handler(message: types.Message):
    ...
