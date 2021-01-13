import sqlite3

from sqlite3 import Error

def show_categories():
    try:
        conn = sqlite3.connect('/Users/semenolhovic/Python_Projects/groceryShop/bot/sql/bot.db')
        cursor = conn.cursor()
        query = """SELECT * FROM 'categories'"""
        cursor.execute(query)
        categories = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return categories