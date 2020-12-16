import os

def hideToken():
    with open('token.txt') as file:
        for line in file:
            token = line
    return token

TOKEN = hideToken()