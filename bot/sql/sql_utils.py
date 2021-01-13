import sqlite3
#from datetime import datetime
#from dateutil import tz

def show_menu():
    try:
        conn = sqlite3.connect('bot.db')
        cursor = conn.cursor()
        query = """SELECT * FROM 'categories'"""
        cursor.execute(query)
        categories = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return categories
