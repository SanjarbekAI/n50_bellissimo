from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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


async def inside_menu_kb():
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Deliver"),
            KeyboardButton(text="Pick up"),
        ],
        [
            KeyboardButton(text="Back")
        ]
    ])
    return markup


async def inside_deliver_kb():
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Send your location")
        ],
        [
            KeyboardButton(text="My all locations")
        ]
    ], resize_keyboard=True)
    return markup


async def category_kb():
    categories = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5', 'Cat 6']
    builder = ReplyKeyboardBuilder()

    first_row = [
        KeyboardButton(text="Back"),
        KeyboardButton(text="Discounts"),
        KeyboardButton(text="Basket")
    ]
    builder.row(*first_row)

    temp_buttons = list()
    for cat in categories:
        temp_buttons.append(KeyboardButton(text=cat))
        if len(temp_buttons) == 2:
            builder.row(*temp_buttons)
            temp_buttons.clear()

    builder.row(*temp_buttons)
    keyboard = builder.as_markup(resize_keyboard=True)
    return keyboard
