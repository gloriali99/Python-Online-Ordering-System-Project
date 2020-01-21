from pantry import inventoryManager
 

class Main(): 

    def __init__(self): 
        self._burgerIngredients = {}
        self._wrapIngredients = {}
        self._totalMainPrice = 0.0 
        self._quantity = None 
    
    def mainInterface(self, pantry): 
        print("Mains:")
        while True: 
            print("========================================")
            print("Type B for a Burger")
            print("Type W for a Wrap")            
            print("Type C to cancel order")
            print("========================================")
            command = input("What would you like to do? ")

            if command.upper() == "C": 
                break 
            elif command.upper() == "W":
                if self.createBaseWrap(pantry) == True:
                    self.addExtraIngredient(pantry)
                    print(self.reviewBurger())
                    return None
            elif command.upper() == "B":
                if self.createBaseBurger(pantry) == True:
                    self.addExtraIngredient(pantry)
                    print(self.reviewBurger())
                    return None
    '''
    ### MAIN CREATOR
    '''

    def createBaseBurger(self, pantry):
        input_string = input("Type B if you would like a base burger and C to create your own?")
        baseOption = input_string.upper()
        if baseOption == "B":
            pantry.listBaseBurger()
            burgerChoice = input("Which burger would you like?:")
            quantity = input("How many burgers would you like?:")
            validOrder = pantry.getBaseBurger(burgerChoice,-int(amount))
            
            if validOrder != True:
                Print("Sorry, there is not enough ingredients to make a burger!")
                return None
            else: 
                burger = pantry.checkBaseBurgerMain(burgerChoice)
                for ingredient in burger:
                    self._totalMainPrice = self._totalMainPrice + self.calcNetMainPrice(ingredient,amount)       
        
        elif baseOption== "C": 
            pantry.listAllBuns()
            orderBun = input("What buns would you like?:")
            bquantity = input("Bun Quantity:")
            if pantry.checkInCategory(buns,orderBun) == True:
                pantry.getMain(orderBun, -int(bquantity))

            pantry.listAllPattys()
            orderPatty = input("What patty would you like?:")
            pquantity = input("Patty quantity:")
            if pantry.checkInCategory(patty,orderPatty) == True:
                pantry.getMain(orderPatty, -int(pquantity))

            pantry.listAllExtras()
            orderExtra = input("What extras would you like?:")
            while orderExtra != "exit":
                if pantry.checkInCategory(extras,orderExtra) == True:
                    equantity = input("Extras Quantity:")
                    pantry.getMain(orderExtra,-int(equantity))

            Buns = pantry.findMain(orderBun)
            Patty = pantry.findMain(orderPatty)
            Extras = pantry.findMain(orderExtra)
            #HAVE TO FIX MAIN PRICE
            self._totalMainPrice = self._totalMainPrice + self.calcNetMainPrice(baseIngred1, 2)
            self._totalMainPrice = self._totalMainPrice + self.calcNetMainPrice(baseIngred1, 1)

    def createBaseWrap(self, pantry):
        input_string = input("Type B if you would like a base wrap and C to create your own?")
        baseOption = input_string.upper()
        if baseOption == "B":
            pantry.listBaseWrap()
            wrapChoice = input("Which wrap would you like?:")
            quantity = input("How many wraps would you like?:")
            validOrder = pantry.getBaseWrap(wrapChoice,-int(amount))
            
            if validOrder != True:
                Print("Sorry, there is not enough ingredients to make a wrap!")
                return None
            else: 
                wrap = pantry.checkBaseWrapMain(wrapChoice)
                for ingredient in wrap:
                    self._totalMainPrice = self._totalMainPrice + self.calcNetMainPrice(ingredient,amount)       
        
        elif baseOption== "C": 
            pantry.listAllTortillas()
            orderTortilla = input("What Tortilla would you like?:")
            if pantry.checkInCategory(tortillas,orderTortilla) == True:
                pantry.getMain(orderTortilla, -1)

            pantry.listAllWrapFillings()
            orderFilling = input("What Filling would you like?:")
            fquantity = input("Filling quantity:")
            if pantry.checkInCategory(wrapFillings,orderFilling) == True:
                pantry.getMain(orderFilling, -int(fquantity))

            pantry.listAllExtras()
            orderExtra = input("What extras would you like?:")
            while orderExtra != "exit":
                if pantry.checkInCategory(extras,orderExtra) == True:
                    equantity = input("Extras Quantity:")
                    pantry.getMain(orderExtra,-int(equantity))

            Tortilla = pantry.findMain(orderTortilla)
            Filling = pantry.findMain(orderFilling)
            Extras = pantry.findMain(orderExtra)
            #HAVE TO FIX MAIN PRICE
            self._totalMainPrice = self._totalMainPrice + self.calcNetMainPrice(baseIngred1, 2)
            self._totalMainPrice = self._totalMainPrice + self.calcNetMainPrice(baseIngred1, 1)

   
    def calcNetMainPrice(self, ingredient, quantity):
        return ingredient.pricePerUnit * int(quantity)

    #HAVE TO FIX THIS AS WELL
    def reviewBurger(self):
        ingredList = ""
        for name in self.baseIngredients.keys():
            ingredList = ingredList + ", " + name
        price = self._totalMainPrice 
        return f"Main containing {ingredList} totalling ${price}"
    

    @property
    def burgerIngredients(self):
        return self._burgerIngredients

    @property
    def wrapIngredients(self):
        return self._wrapIngredients

    @property 
    def quantity(self):
        return self._quantity 

    @property 
    def netMainPrice(self):
        return self._totalMainPrice 

    def __str__(self):
        return self.reviewBurger()
