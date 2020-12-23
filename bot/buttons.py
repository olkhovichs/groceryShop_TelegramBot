from bot.config import about_path as gh_rm

from aiogram.types import ReplyKeyboardRemove, \
        ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    btn_categ = InlineKeyboardButton(text = 'Категории', callback_data='categ') # 1
    btn_cart = InlineKeyboardButton(text = 'Корзина', callback_data='cart') # 2
    btn_about = InlineKeyboardButton(text = 'Информация', url = gh_rm, callback_data='about') # 3
    btn_exit = InlineKeyboardButton(text = 'Выход', callback_data='exit') # 4
    markup_menu = InlineKeyboardMarkup()
    markup_menu.row(btn_categ).row(btn_cart)
    markup_menu.row(btn_about, btn_exit)
    return markup_menu


def categ_menu():
    btn_sales = InlineKeyboardButton('Скидки!', callback_data='sales') # 5
    btn_drinks = InlineKeyboardButton('Напитки', callback_data='drinks') # 6
    btn_veg = InlineKeyboardButton('Овощи', callback_data='veg')
    btn_fruits = InlineKeyboardButton('Фрукты', callback_data='fruits')
    btn_milk = InlineKeyboardButton('Молоко', callback_data='milk')
    btn_bread = InlineKeyboardButton('Хлеб', callback_data='water')
    btn_meat = InlineKeyboardButton('Мясо', callback_data='meat')
    btn_fish = InlineKeyboardButton('Рыба', callback_data='fish')
    btn_cereal = InlineKeyboardButton('Бакалея', callback_data='cereal')
    markup_categ = InlineKeyboardMarkup(row_width=3)
    markup_categ.add(btn_bread, btn_cereal)
    return markup_categ
