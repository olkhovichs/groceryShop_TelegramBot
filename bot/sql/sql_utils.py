import sqlite3
#from datetime import datetime
#from dateutil import tz

def show_menu():
    try:
        conn = sqlite3.connect('bot.db') # connection db
        cursor = conn.cursor() # creating cursor for executing requests
        query = """CREATE TABLE categories
                    (bread text, milk text, water text)""" # request
        cursor.execute(query) # executing request
        categories = cursor.fetchall() # saving in variable
    except Error:
        print(Error)
    finally:
        conn.close()

    return categories
