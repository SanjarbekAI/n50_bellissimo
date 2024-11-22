from aiogram import F
from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from keyboards.default.user import inside_menu_kb, category_kb

router = Router()


@router.message(F.text.in_(['Menu 🍕', 'Menyu 🍕']))
async def menu_handler(message: types.Message, state: FSMContext):
    text = "Get your order by yourself 🙋‍♂️ or use delivering service 🚙"
    await message.answer(text=text, reply_markup=await category_kb())




