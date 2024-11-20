from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

async def user_main_menu_keyboard_with_lang(language: str):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Menu 🍕", locale=language))
            ],
            [
                KeyboardButton(text=_("My orders 📖", locale=language)),
                KeyboardButton(text=_("Our branches 🏚", locale=language)),
            ],
            [
                KeyboardButton(text=_("Contact ☎️", locale=language)),
                KeyboardButton(text=_("Settings ⚙️", locale=language)),
            ]
        ], resize_keyboard=True
    )

    return markup


async def user_main_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Menu 🍕"))
            ],
            [
                KeyboardButton(text=_("My orders 📖")),
                KeyboardButton(text=_("Our branches 🏚")),
            ],
            [
                KeyboardButton(text=_("Contact ☎️")),
                KeyboardButton(text=_("Settings ⚙️")),
            ]
        ], resize_keyboard=True
    )

    return markup


languages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzbek 🇺🇿"),
            KeyboardButton(text="Russian 🇷🇺"),
            KeyboardButton(text="English 🇺🇸"),
        ]
    ], resize_keyboard=True
)
