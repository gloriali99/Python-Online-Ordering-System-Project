from pantry import inventoryManager

class Side():

    def __init__(self):
        self._netSidePrice = 0.0
        self._side = None
        self._quantity = None

    def sideInterface(self, pantry):
        print("Sides:")
        while True:
            print("========================================")
            print("Type 1 to review all sides.")
            print("Type C to cancel your order.")
            print("========================================")
            command = input("Which side would you like? ")

            if command.upper() == "C":
                break
            elif command.isdigit() == True:
                if int(command) == 1:
                    pantry.listSideIngredients()
            else:
                cside = pantry.findSide(command)
                if cside != None:
                    quantity = input("How many would you like? ")
                    if quantity.isdigit() == True:
                        if int(quantity) > 0:
                            valid = pantry.getSide(command, -int(quantity))
                            if valid == True:
                                self.confirmSide(cside,int(quantity))
                                print(self)
                                return None 
                    else:
                        print("Please enter a valid amount!")

    def confirmSide(self, cside, amount):
        self._netSidePrice = self.calcNetSidePrice(cside, amount)
        self._side = cside.name
        self._quantity = amount

    def calcNetSidePrice(self, ingredient, quantity):
        return ingredient.pricePerUnit * int(quantity)

    @property
    def side(self):
        return self._side
    
    @property
    def quantity(self):
        return self._quantity

    @property
    def netSidePrice(self):
        return self._netSidePrice

    def __str__(self):
        return f"{self.quantity} x {self.side}. Totalling: ${self.netSidePrice}"