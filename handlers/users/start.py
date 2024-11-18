from aiogram import types
from loader import dp
from main.config import ADMINS


@dp.message_handler(commands="start", chat_id=ADMINS)
async def start_handler(message: types.Message):
    text = "Hello world"
    await message.answer(text=text)
