import os

def token():
    with open('token.txt') as file:
        for line in file:
            token = line
    return token