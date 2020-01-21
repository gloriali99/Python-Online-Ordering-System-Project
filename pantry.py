from ingredient import Ingredient
from fieldCheck import validNewIngredientCheck, IngredientFieldError, FieldTypeError

class inventoryManager():

    def __init__(self):
        self._mainIngredients = {}
        self._sideIngredients = {}
        self._dessertIngredients = {}
        self._mainBaseBurger = {}
        self._mainBaseWrap = {}
        self._buns = []
        self._tortillas = []
        self._patty = []
        self._extras = []        

    def inventoryInterface(self):
        print("========================================")
        print("GourmetBurgers invetory manager")

        while True:
            print("========================================")
            print("Type 1 to add an ingredient")
            print("Type 2 to add a base burger")
            print("Type 3 to add a base wrap")
            print("Type 4 to see all ingredients")
            print("Type 5 to see all main ingredients")
            print("Type 6 to see all side ingredients")
            print("Type C to cancel")
            print("========================================")
            command = input("What would you like to do? ")       

            if command.isdigit() == True:
                if int(command) == 1:
                    i = input("Please enter ingredient name: ")
                    j = input("Enter Price per unit: ")
                    k = input("Enter initial quantity: ")
                    #Gloria p.s - i adde this input to put ingredients into categories
                    l = input("Please enter category type >B for buns >T for tortillas >P for patty F> for wrap filling >E for extras:")
                    newIngred = self.createNewIngredient(i,float(j),int(k))
                    self.addtoCategory(i,l)
                    if newIngred != None:
                        self.storeIngredient(newIngred)
                elif int(command) == 2: 
                    self.ingredientsforBaseBurger()
                elif int (command) == 3:
                    self.ingredientsforBaseWrap()
                elif int(command) == 4:
                    self.listAllIngredients()
                elif int(command) == 5:
                    self.listMainIngredients()
                elif int(command) == 6:
                    self.listSideIngredients()
            elif command.upper() == "C":
                break

    '''
    ### INVENTORY MANAGER
    '''
    
    def createNewIngredient(self,ingredientName, pricePerUnit, initialQuantity):        #Creates a new instance of Ingredient. Does NOT assign it to any dictionaries.
        try:
             validNewIngredientCheck(ingredientName, pricePerUnit, initialQuantity)
        except FieldTypeError as error:
            print(error)
        except IngredientFieldError as error:
            print(error)
        else:
            self.storeIngredient(Ingredient(ingredientName, pricePerUnit, initialQuantity))

    #GLORIA EDITS 
    # HELPER FUNCTIONS TO HELP IN MAIN INTERFACE - pls check
    
    def addtoCategory(self,ingredientName,category):
        cat = category.upper()
        if cat == "B":
            self.addToBuns(ingredientName)
        elif cat == "T":
            self.addToTortillas(ingredientName)
        elif cat == "P":
            self.addToPatty(ingredientName)
        elif cat == "F":
            self.addToWrapFilling(ingredientName)
        elif cat == "E":
            self.addToExtra(ingredientName)

        self.listAllExtras()
    #FUNCTIONS TO ADD INGREDINT IN THEIR RESPECTIVE CATEGORY LIST

    def addToBuns(self,ingredientName):
        if ingredientName in self.buns:
            print(f"{ingredientName} already exists in inventory")
        elif ingredientName not in self.buns:
            self.buns.append(ingredientName)

    def addToTortillas(self,ingredientName):
        if ingredientName in self.tortillas:
            print(f"{ingredientName} already exists in inventory")
        elif ingredientName not in self.tortillas :
            self.tortillas.append(ingredientName)

    def addToPatty(self,ingredientName):
        if ingredientName in self.patty:
            print(f"{ingredientName} already exists in inventory")
        elif ingredientName not in self.buns:
            self.patty.append(ingredientName)

    def addToWrapFilling(self,ingredientName):
        if ingredientName in self.wrapFilling:
            print(f"{ingredientName} already exists in inventory")
        elif ingredientName not in self.wrapFilling:
            self.wrapFilling.append(ingredientName)

    def addToExtra(self,ingredientName):
        if ingredientName in self.extras:
            print(f"{ingredientName} already exists in inventory")
        elif ingredientName not in self.extras:
            self.extras.append(ingredientName)

    '''
    #FUNCTIONS TO LIST ALL INGREDIENTS IN THEIR CATEGORIES
    '''
    def listAllBuns(self): 
        title = "ALL BUNS"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.buns) == 0:
            print("There are currently no buns stored on record")
        else: 
            for i in buns: 
                print(i)
        print("-" * len(title))

    def listAllTortillas(self): 
        title = "ALL TORTILLAS"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.tortillas) == 0:
            print("There are currently no tortillas stored on record")
        else: 
            for i in self.tortillas: 
                print(i)
        print("-" * len(title))

    def listAllPattys(self): 
        title = "ALL PATTIES"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.patty) == 0:
            print("There are currently no patties stored on record")
        else: 
            for i in self.patty: 
                print(i)
        print("-" * len(title))

    def listAllWrapFillings(self): 
        title = "ALL WRAP FILLINGS"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.wrapFilling) == 0:
            print("There are currently no wrap fillings stored on record")
        else: 
            for i in self.wrapFilling: 
                print(i)
        print("-" * len(title))

    def listAllExtras(self): 
        title = "ALL EXTRAS"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.extras) == 0:
            print("There are currently no wrap fillings stored on record")
        else: 
            for i in self.extras: 
                print(i)
        print("-" * len(title))

    #FUNCTION TO CHECK IF INGREDIENT EXISTS IN ITS CATEGORY 
    def checkInCategory(catList,ingredientName): 
        if ingredientName in catList: 
            return True
        elif ingredientName not in catList:
            return False

    # function to create a list of ingredients that will be in base burger
    def ingredientsforBaseBurger(self): 
        # need to create tests for this, user input error , LOWER CASE FOR FIND FUNCTION, GET RID OF WHITE SPACE 
        baseList = []
        input_string = input("Enter a list of ingredients for a base burger with a coma after each ingredient:")
        # MIGHT HAVE TO USE A COMAAA TO SPLIT 
        baseList = input_string.split(",")
        print(baseList)
        
        # iterating through list to check validity of ingredients 
        for i in baseList:
        # if the ingredient does not exist already, create it 
            exist = self.findMain(i)
            if exist == None: 
                print("Follow instructions below to create.")
                i = input("Please enter ingredient name: ")
                j = input("Enter Price per unit: ")
                k = input("Enter initial quantity: ")
                self.createNewIngredient(i,float(j),int(k))
            else:
                print(i)
                print(" found test")
        #stores the base burger as a dict       
        self.addBaseBurger(baseList)

    #function to create a list of ingredients for wraps
    def ingredientsforBaseWrap(self): 
        baseList = []
        input_string = input("Enter a list of ingredients for a base burger with a space between each ingredient:")
        # MIGHT HAVE TO USE A COMAAA TO SPLIT 
        baseList = input_string.split()
        # iterating through list to check validity of ingredients 
        for i in baseList:
        # if the ingredient does not exist already, create it 
            exist = self.findMain(i)
            if exist == None: 
                print("Follow instructions below to create.")
                i = input("Please enter ingredient name: ")
                j = input("Enter Price per unit: ")
                k = input("Enter initial quantity: ")
                self.createNewIngredient(i,float(j),int(k))

        #stores the base burger as a dict       
        self.addBaseWrap(baseList)

    #END GLORIA EDITS

    def storeIngredient(self, Ingredient):
        print(f"New ingredient created [{Ingredient}]")
        print("Enter >M to store in mains, >S to store in sides, >R to return, >C to cancel.")
        while True:
            answer = input(">")
            if answer.upper() == "M":
                self.addMainIngredient(Ingredient)
                break
            elif answer.upper() == "S": 
                self.addSideIngredient(Ingredient)
                break
            elif answer.upper() == "R":
                return Ingredient
            elif answer.upper() == "C":
                break
            else:
                print("Invalid input. Please try again.")

    def addMainIngredient(self, Ingredient):                     # Given an ingredient, it will add it to the Mains dictionary if one does not already exist.
        if self.mainIngredients.get(Ingredient.name) == None:
            self.mainIngredients[Ingredient.name] = Ingredient
        else: 
            #REPLACE WITH EXCEPTION?
            print(f"Unable to add {Ingredient.name}, as {Ingredient.name} already exists in the system.")

    def addSideIngredient(self, Ingredient):                    # Adds to side dict if does not already exist.
        if self.sideIngredients.get(Ingredient.name) == None:
            self.sideIngredients[Ingredient.name] = Ingredient
        else:
            #REPLACE WITH EXCEPTION?
            print(f"Unable to add {Ingredient.name}, as {Ingredient.name} already exists in the system.")

    def addDessertIngredient(self, Ingredient):                    # Adds to side dict if does not already exist.
        if self.dessertIngredients.get(Ingredient.name) == None:
            self.dessertIngredients[Ingredient.name] = Ingredient
        else:
            #REPLACE WITH EXCEPTION?
            print(f"Unable to add {Ingredient.name}, as {Ingredient.name} already exists in the system.")

    def deleteMainIngredient(self, Ingredient):
        if self.mainIngredients.get(Ingredient.name) == None:
            return None
        else:
            del self.mainIngredients[Ingredient.name]
            return True

    def deleteSideIngredient(self, Ingredient):
        if self.sideIngredients.get(Ingredient.name) == None:
            return None
        else:
            del self.sideIngredients[Ingredient.name]
            return True

    def deleteDessertIngredient(self, Ingredient):
        if self.dessertIngredients.get(Ingredient.name) == None:
            return None
        else:
            del self.dessertIngredients[Ingredient.name]
            return True

    #GLORIA'S EDITS 

    #adds the base burger into the dictionary mainBaseBurger{}
    def addBaseBurger(self, baseList): 
        print("Entered addbaseburger")
        print(baseList)
        burgerName = input("Enter the name of the burger:")
        #checking if burger exists already 
        
        key = burgerName
        if self.checkBaseBurgerMain(key) == True:
            print("Base Burger already exists")
        else: 
            self.mainBaseBurger[burgerName] = baseList 
            print(f"Base burger created with name {burgerName} and ingredients {baseList} has been created")

    #adds the base burger into the dictionary mainBaseBurger{}
    def addBaseWrap(self, baseList): 
        wrapName = input("Enter the name of the wrap:")
        #checking if burger exists already 
        
        key = wrapName
        if self.checkBaseBurgerMain(key) == True:
            print("Base wrap already exists")
        else:
            self.mainBaseWrap[wrapName] = baseList 
            print(f"Base wrap created with name {wrapName} and ingredients {baseList} has been created")


    # END GLORIA EDITS

    # separate function to check if base already exists  
    def addBaseWrap(self, baseList): 
        i = self.mainBaseBurger.get(nameOfBurger)
        if i == None:
            return i 
        else:
            print(f"{nameOfBurger} already exists as a base burger")
            return None

    def addBaseWrap(self, baseList): 
        i = self.mainBaseWrap.get(nameOfWrap)
        if i == None:
            return i 
        else:
            print(f"{nameOfWrap} already exists as a base burger")
            return None
    

    def findMain(self, nameOfIngredient):           # FindMain/FindSide finds said OBJECT and returns an OBJECT
        i = self.mainIngredients.get(nameOfIngredient)
        if i == None:
            print(f"{nameOfIngredient} does not exist as a main ingredient.")
            return None
        else:
            return i

    def findSide(self, nameOfIngredient):
        i = self.sideIngredients.get(nameOfIngredient)
        if i == None:
            print(f"{nameOfIngredient} does not exist as a side ingredient.")
            return None
        else:
            return i

    def findDessert(self, nameOfIngredient):
        i = self.dessertIngredients.get(nameOfIngredient)
        if i == None:
            print(f"{nameOfIngredient} does not exist as a side ingredient.")
            return None
        else:
            return i

    def getMain(self, nameOfIngredient, amount):    # GetMAINS/GetSIDES is responsible for first checking sufficient quantity, and if avalible, decrement the quantity. Otherwise will raise an exception.
        cmain = self.findMain(nameOfIngredient)
        if cmain != None:
            if int(cmain.quantity) + amount >= 0:
                cmain.updateQuantity(amount)
                print(f"Added {nameOfIngredient} to your order!")
                return True
            else:
                print("There is unfortuantly insufficient stock to complete your order. Please try something else.")
                return None

    def getSide(self,nameOfIngredient, amount): 
        cside = self.findSide(nameOfIngredient)
        if cside != None:
            if int(cside.quantity) + amount >= 0:
                cside.updateQuantity(amount)
                print(f"Added {nameOfIngredient} to your order!")
                return True
            else:
                print("There is unfortuantly insufficient stock to complete your order. Please try something else.")
                return None

    def getDessert(self,nameOfIngredient, amount): 
        cdessert = self.findDessert(nameOfIngredient)
        if cdessert != None:
            if int(cdessert.quantity) + amount >= 0:
                cdessert.updateQuantity(amount)
                print(f"Added {nameOfIngredient} to your order!")
                return True
            else:
                print("There is unfortuantly insufficient stock to complete your order. Please try something else.")
                return None

    def getBaseBurger(self,nameOfBurger,amount):
        cbase = self.checkBaseBurgerMain(nameOfBurger)
        if cbase != None: 
            for ingredient in cbase:
                if ingredient.quantity + amount >= 0:
                    ingredient.updateQuantity(amount)
                    print(f"Added {ingredient} to your order!")
                    return True 
                else:
                    print("There is unfortuantly insufficient stock to complete your order. Please try something else.")
                    return None

    def getBaseWrap(self,nameOfWrap,amount):
        cbase = self.checkBaseWrapMain(nameOfWrap)
        if cbase != None: 
            for ingredient in cbase:
                if ingredient.quantity + amount >= 0:
                    ingredient.updateQuantity(amount)
                    print(f"Added {ingredient} to your order!")
                    return True 
                else:
                    print("There is unfortuantly insufficient stock to complete your order. Please try something else.")
                    return None

    def returnEmptyMains(self):
        if len(self.mainIngredients) == 0:
            return []
        emptyList = []
        for currIngred in self.mainIngredients.values():
            if int(currIngred.quantity) == 0:
                emptyList.append(currIngred)
        return emptyList        

    def returnEmptySides(self):
        if len(self.sideIngredients) == 0:
            return []
        emptyList = []
        for currIngred in self.sideIngredients.values():
            if int(currIngred.quantity) == 0:
                emptyList.append(currIngred)
        return emptyList

    def returnEmptyDesserts(self):
        if len(self.dessertIngredients) == 0:
            return []
        emptyList = []
        for currIngred in self.dessertIngredients.values():
            if int(currIngred.quantity) == 0:
                emptyList.append(currIngred)
        return emptyList
    '''
    ### INVENTORY STOCKTAKE
    '''

    def listAllIngredients(self):
        self.listMainIngredients()
        self.listSideIngredients()

    def listMainIngredients(self):
        title = "MAIN INGREDIENTS SUMMARY"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.mainIngredients) == 0:
            print("There are currently no Main ingredients stored on record.")
        else:
            for currIngredient in self.mainIngredients.keys():
                print(self.mainIngredients[currIngredient])
        print("-" * len(title))

    # displays list of all burgers 
    def listBaseBurger(self): 
        title = "BASE BURGER SUMMARY"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.mainBaseBurger) == 0:
            print("There are currently no Base burgers stored on record.")
        else: 
            for currBurger in self.mainBaseBurger.keys(): 
                print(self.mainBaseBurger[currBurger])
        print("-" * len(title))

    def listSideIngredients(self):
        title = "SIDE INGREDIENTS SUMMARY"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.sideIngredients) == 0:
            print("There are currently no Side ingredients stored on record.")
        else:
            for currIngredient in self.sideIngredients.keys():
                print(self.sideIngredients[currIngredient])
        print("-" * len(title))

    def listEmptyIngredients(self):
        title = "EMPTY INGREDIENTS SUMMARY"
        print("-" * len(title))
        print(title)
        print("-" * len(title))
        print("<FROM MAINS>")
        for currIngredient in self.mainIngredients.keys():
            if self.mainIngredients[currIngredient].quantity == 0:
                print(self.mainIngredients[currIngredient])
        print("<FROM SIDES>")
        for currIngredient in self.sideIngredients.keys():
            if self.sideIngredients[currIngredient].quantity == 0:
                print(self.sideIngredients[currIngredient])
        print("\n" + "-" * len(title))


    '''
    ### Properties ###
    '''
 
    @property
    def mainIngredients(self):
        return self._mainIngredients

    @property
    def sideIngredients(self):
        return self._sideIngredients

    @property
    def dessertIngredients(self):
        return self._dessertIngredients

    @property
    def mainBaseBurger(self): 
        return self._mainBaseBurger

    @property 
    def mainBaseWrap(self): 
        return self._mainBaseWrap

    @property
    def buns(self):
        return self._buns

    @property 
    def tortillas(self):
        return self._tortillas 

    @property
    def patty(self):
        return self._patty

    @property
    def wrapFilling(self):
        return self._wrapFilling

    @property 
    def extras(self):
        return self._extras

    def __str__(self):
        return (f"I have {len(self.sideIngredients)} sides bitties")