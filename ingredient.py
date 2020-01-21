from fieldCheck import negativeIngredientQuantity

class Ingredient():
    
    def __init__(self, ingredientName, pricePerUnit, initialQuantity):
        self._ingredientName = ingredientName
        self._pricePerUnit = pricePerUnit
        self._quantity = initialQuantity

    def updateQuantity(self, amount): # updates quantity. Raises and exception if quantity is negative. However this check should already done in findMain/findSide. 
        try:
            if int(self.quantity) + amount < 0:
                raise negativeIngredientQuantity(self.name,self.quantity,amount,self.quantity + amount)
        except negativeIngredientQuantity as error:
            print(error)
        else: 
            self._quantity = int(self.quantity) + amount

    @property #Getter
    def name(self):
        return self._ingredientName
    
    @property # gets PricePerUnit
    def pricePerUnit(self):
        return self._pricePerUnit
    
    @pricePerUnit.setter # Sets a new price
    def pricePerUnit(self, newPrice):
        self._pricePerUnit = newPrice
    
    @property # gets ingredient quantity
    def quantity(self):
        return self._quantity



    def __str__(self):
        return f"Ingredient {self.name} (@ ${self.pricePerUnit}/unit) has {self.quantity} remaining units."
        


