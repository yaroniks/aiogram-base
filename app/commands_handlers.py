from app.utils import *
import app.keyboards as kb
from config import settings
from aiogram import types, Router
from app.database.models import *
from aiogram.filters.command import Command, CommandStart

router = Router(name='Commands')


@router.message(CommandStart())
async def start_command(message: types.Message):
    await Chat.add_chat(message.chat.id)
    ...


@router.message(Command('help'))
async def help_command(message: types.Message):
    ...
