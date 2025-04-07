from app.utils import *
import app.keyboards as kb
from config import settings
from aiogram import types, F, Router

router = Router(name='Messages')


@router.message()
async def messages(message: types.Message):
    ...
