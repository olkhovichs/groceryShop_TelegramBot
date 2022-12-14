import os

import sqlite3
from sqlite3 import Error

def hide_token():
    with open('/Users/semenolhovic/Python_Projects/groceryShop/token.txt') as file:
        for line in file:
            token = line
    return token

TOKEN = hide_token()
about_path = 'https://github.com/olkhovichs/groceryShop_TelegramBot/blob/master/README.md'
path_db = '/Users/semenolhovic/Python_Projects/groceryShop/bot/data/products.db'
'''
def create_products_table():
    id = list()


    try:
        conn = sqlite3.connection('/Users/semenolhovic/Python_Projects/groceryShop/bot/sql/bot.db')
        cursor = conn.cursor()
        with conn:
            for i in range(1, 5):
                id.append(i)
                query = """
                INSERT INTO 'products'
                VALUES(?, ?)
                """, (id)
'''