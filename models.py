class Dessert:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def calculate_total(self, quantity):
        return self.price * quantity
