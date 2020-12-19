from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

btn_categ = KeyboardButton('Категории') # 1
btn_cart = KeyboardButton('Корзина') # 2
btn_about = KeyboardButton('Информация') # 3
btn_exit = KeyboardButton('Выход') # 4
markup_menu = ReplyKeyboardMarkup()
markup_menu.add(btn_categ).add(btn_cart).add(btn_about).add(btn_exit)
#markup_menu.row(btn_categ, btn_cart)
#markup_menu.row(btn_about, btn_exit)