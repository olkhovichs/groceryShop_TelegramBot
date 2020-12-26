import os

class Product:
    def __init__(self, name, price, src_img):
        self.name = name
        self.price = price
        self.src_img = src_img

    @property
    def sale(init_price, procent):
        pass

class Drinks(Product):
    def __init__(self, name, price, src_img, volume):
        super().__init__(name, price, src_img)
        self.volume = volume

class VegFruit(Product):
    def __init__(self, name, price, src_img, weight):
        super().__init__(name, price, src_img)
        self.weight = weight

class Milk(Product, [Drinks]):
    def __init__(self, name, price, src_img, volume):
        super().__init__(name, price, src_img, volume)

class Bread(Product):
    def __init__(self, name, price, src_img):
        super().__init__(name, price, src_img)

class Meat(Product):
    def __init__(self, name, price, src_img, weight):
        super().__init__(name, price, src_img)
        self.weight = weight

class Fish(Product, [Meat]):
    def __init__(self, name, price, src_img, weight):
        super().__init__(name, price, src_img, weight)

class Cereal(Product):
    def __init__(self, name, price, src_img, weight):
        super().__init__(name, price, src_img)
        self.weight = weight