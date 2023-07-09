import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers.echo import dp, send_to_admin
    from handlers.menu import dp
    from handlers.items import *
    executor.start_polling(dp, on_startup=send_to_admin)