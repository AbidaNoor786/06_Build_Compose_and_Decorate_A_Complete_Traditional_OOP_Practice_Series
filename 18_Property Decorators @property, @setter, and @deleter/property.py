class Product:
    def __init__(self, price):
        self._price = price  # Private attribute by convention

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage:
p = Product(100)

# Get the price
print(p.price)

# Set a new price
p.price = 150
print(p.price)

# Delete the price
del p.price
