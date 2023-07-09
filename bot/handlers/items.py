from aiogram.dispatcher.filters import Command

from bot.keyboards.inline.choise_datas import choise
from bot.main import dp
from aiogram.types import Message


@dp.message_handler(Command('items'))
async def chow_items(message: Message):
    await message.answer(text='We have two selling goods: five apples and one banana,'
                              ' if u dont need in smth, please klick on "Cancel"',
                         reply_markup=choise)