from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

def init_menu():
    btn_categ = InlineKeyboardButton('Категории', callback_data='categ') # 1
    btn_cart = InlineKeyboardButton('Корзина', callback_data='cart') # 2
    btn_about = InlineKeyboardButton('Информация', callback_data='about') # 3
    btn_exit = InlineKeyboardButton('Выход', callback_data='exit') # 4
    markup_menu = InlineKeyboardMarkup(row_width = 2)
    markup_menu.add(btn_categ, btn_cart, btn_about, btn_exit)
    return markup_menu

def categ_menu():
    btn_water = InlineKeyboardButton('Вода', callback_data='water') # 5
    btn_beer = InlineKeyboardButton('Пиво', callback_data='beer') # 6
    markup_product = InlineKeyboardMarkup(row_width=2)
    markup_product.add(btn_water, btn_beer)
    return markup_product