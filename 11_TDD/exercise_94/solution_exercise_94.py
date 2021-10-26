class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if isinstance(price, (int, float)):
            self.price = price
        else:
            raise TypeError
