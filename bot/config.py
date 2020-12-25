import os

def hide_token():
    with open('token.txt') as file:
        for line in file:
            token = line
    return token

TOKEN = hide_token()
about_path = 'https://github.com/olkhovichs/groceryShop_TelegramBot/blob/master/README.md'
all_categ = list()
all_categ = ['']