from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

btn_categ = InlineKeyboardButton('Категории', callback_data='categ') # 1
btn_cart = InlineKeyboardButton('Корзина', callback_data='cart') # 2
btn_about = InlineKeyboardButton('Информация', callback_data='about') # 3
btn_exit = InlineKeyboardButton('Выход', callback_data='exit') # 4
markup_menu = InlineKeyboardMarkup(row_width = 2)
markup_menu.add(btn_categ, btn_cart, btn_about, btn_exit)