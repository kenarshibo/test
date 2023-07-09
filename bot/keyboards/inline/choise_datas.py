from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.keyboards.inline.callback_datas import buy_callback


choise = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='Купить грушу', callback_data=buy_callback.new(
            item_name='pear', quantity=2
        )),
        InlineKeyboardButton(text='Купить яблоко', callback_data=buy_callback.new(
            item_name='apple', quantity=2
        ))
    ],
    [
        InlineKeyboardButton(text='Отмена', callback_data='cancel')
    ]
])