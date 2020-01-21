from pantry import inventoryManager

class Dessert():

    def __init__(self):
        self._netDessertPrice = 0.0
        self._dessert = None
        self._quantity = None

    def confirmDessert(self, cdessert, amount):
        self.dessert = cdessert
        self.netDessertPrice = self.calcNetDessertPrice(cdessert, amount)
        self.quantity = amount

    def calcNetDessertPrice(self, ingredient, quantity):
        return ingredient.pricePerUnit * int(quantity)

    @property
    def dessert(self):
        return self._dessert
    @dessert.setter
    def dessert(self, dessert):
        self._dessert = dessert

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def netDessertPrice(self):
        return self._netSidePrice
    @netDessertPrice.setter
    def netDessertPrice(self, price):
        self._netSidePrice = price

    def __str__(self):
        return f"{self.quantity} x {self.dessert}. Totalling: ${self.netDessertPrice}"
