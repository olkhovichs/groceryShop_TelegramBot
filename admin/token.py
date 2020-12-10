def hideToken():
    with open('/Users/semenolhovic/Python_Projects/groceryShop/token.txt') as file:
        for line in file:
            token = line
    return token

print(hideToken())