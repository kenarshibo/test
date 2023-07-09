from bot.keyboards.default.keyboard import kboard
from bot.main import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text


@dp.message_handler(Command('menu'))
async def send_menu(message: Message):
    await message.answer("Chose smth from this menu-tablet, please",
                         reply_markup=kboard)
    # await message.answer(reply_markup=)


@dp.message_handler(Text(equals=['макарошки', 'пюрешка', 'котлетки']))
async def respond(message: Message):
    result = message.text
    await message.answer(f'u have chosen {result}',
                         reply_markup=ReplyKeyboardRemove())
