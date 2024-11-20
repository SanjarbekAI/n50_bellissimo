from aiogram import types

from loader import dp, _


@dp.message_handler(text=["Contact ☎️", "Aloqa ☎️"])
async def contact_handler(message: types.Message):
    text = _("📲 Call center: 1174 or (71) 203-66-66")
    await message.answer(text=text)
