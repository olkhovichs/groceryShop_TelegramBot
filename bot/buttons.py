from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

#def but():
button_hi = KeyboardButton('Привет! 👋')
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

#greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
