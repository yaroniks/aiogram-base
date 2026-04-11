import app.utils as utils
import app.keyboards as kb
from config import settings
from app.database.models import Chat

import logging
from aiogram import types, Router
from aiogram.filters.command import Command, CommandStart

logger = logging.getLogger(__name__)
router = Router(name='Commands')


@router.message(CommandStart())
async def start_command(message: types.Message):
    if not Chat.get_chat(message.chat.id):
        await Chat.add_chat(message.chat.id)

    logger.info(f'/start - @{message.from_user.username} ({message.chat.id})')


@router.message(Command('help'))
async def help_command(message: types.Message):

    logger.info(f'/help - @{message.from_user.username} ({message.chat.id})')
