def hide_token(path):
    with open(path) as file:
        for line in file:
            token = line
    return token

about_path = 'https://github.com/olkhovichs/groceryShop_TelegramBot/blob/master/README.md'
path_db = '/Users/semenolhovic/Python_Projects/groceryShop/data/products.db'