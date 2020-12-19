import os

def hide_token():
    with open('token.txt') as file:
        for line in file:
            token = line
    return token

TOKEN = hide_token()