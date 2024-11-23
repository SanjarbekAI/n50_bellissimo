import asyncio

from handlers.users import start, contact, menu
from loader import dp, bot
from loader import i18n
from main.database import database
from middlewares.language import LanguageMiddleware
from middlewares.subscribe import SubscribeMiddleware
from utils.notify_devs import send_notification_to_devs
from utils.set_bot_commands import set_default_commands

# test
async def main():
    dp.include_router(router=start.router)
    dp.include_router(router=contact.router)
    dp.include_router(router=menu.router)

    dp.message.middleware(middleware=LanguageMiddleware(i18n=i18n))
    dp.message.middleware(middleware=SubscribeMiddleware())

    await database.connect()
    await set_default_commands(bot=bot)
    await send_notification_to_devs(bot=bot)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
