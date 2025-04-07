from app.utils import *
import app.keyboards as kb
from config import settings
from app.database.models import *
from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router(name='State')


# class MainState(StatesGroup):
#     first = State()
#     second = State()
#
#
# @router.message(MainState.first)
# async def mainstate_first(message: types.Message, state: FSMContext):
#     await state.set_state(MainState.second)
#     await state.update_data(first=message.text)
#     ...
