from typing import Union
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def create_reply_markup(data: Union[list[str], tuple[str]], resize: bool = True, one_time: bool = False) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=i) for i in data]], resize_keyboard=resize, one_time_keyboard=one_time)


# main_reply = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='1')],
# ], resize_keyboard=True)
#
# main_inline = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='2', callback_data='3')],
# ])
