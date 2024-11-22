from aiogram import F
from aiogram import types, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from filters.is_admin import IsAdminFilter
from keyboards.common import phone_number_share_keyboard
from keyboards.default.user import languages, user_main_menu_keyboard_with_lang
from keyboards.default.user import user_main_menu_keyboard
from loader import _
from states.user import RegisterState
from utils.db_commands.user import get_user, add_user
from utils.get_lang_code import get_lang_by_text
from utils.get_location import get_full_address

router = Router()


@router.message(F.LOCATION)
async def get_full_location(message: types.Message):
    address = await get_full_address(latitude=message.location.latitude, longitude=message.location.longitude)
    await message.answer(text=address)


@router.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    await state.clear()
    user = await get_user(chat_id=message.chat.id)
    if user:
        text = _("Welcome back my hero 😊")
        await message.answer(text=text, reply_markup=await user_main_menu_keyboard())
    else:
        text = "Tilni tanlang\nSelect Language\nRu tilni tanlang"
        await message.answer(text=text, reply_markup=languages)
        await state.set_state(RegisterState.language)


@router.message(StateFilter(RegisterState.language))
async def language_handler(message: types.Message, state: FSMContext):
    language = await get_lang_by_text(language=message.text)
    await state.update_data(language=language)
    text = _("Sorry, you have to enter your full name", locale=language)
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegisterState.full_name)


@router.message(StateFilter(RegisterState.full_name))
async def get_full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    language = data.get('language')

    text = _("Please, enter your phone number by the button below 👇", locale=language)
    await message.answer(text=text, reply_markup=await phone_number_share_keyboard(language=language))
    await state.set_state(RegisterState.phone_number)


@router.message(StateFilter(RegisterState.phone_number), F.content_type == types.ContentType.CONTACT)
async def get_phone_number_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    language = data.get('language')

    new_user = await add_user(message=message, data=data)
    if new_user:
        text = _("You have successfully registered ✅", locale=language)
        await message.answer(text=text, reply_markup=await user_main_menu_keyboard_with_lang(language=language))
    else:
        text = _("Sorry, please try again later 😔", locale=language)
        await message.answer(text=text)
    await state.clear()
