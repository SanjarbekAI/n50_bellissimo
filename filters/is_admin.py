from aiogram.dispatcher.filters import BoundFilter


class IsAdminFilter(BoundFilter):
    async def check(self, message, *args) -> bool:
        if message.chat.id == 1358470521:
            return True
        return False
