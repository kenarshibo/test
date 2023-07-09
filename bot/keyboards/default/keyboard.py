from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('котлетки')
        ],
        [
            KeyboardButton('пюрешка'),
            KeyboardButton('макарошки'),
        ]
    ],
    resize_keyboard=True
)