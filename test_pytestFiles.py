import pytest
from projEnums import orderStatus
from fieldCheck import *
from onlineOrderSystem import *
from pantry import *  
from main import Main   
from sides import Side 

def test_correctlyInitialisedStartUp():
    newSystem = onlineOrderSystem()
    assert(newSystem.orderID == 0)
    assert(len(newSystem.activeOrders) == 0)
    assert(len(newSystem.completedOrders) == 0)
    assert(len(newSystem.pantry.sideIngredients) == 0)
    assert(len(newSystem.pantry.mainIngredients) == 0)

def test_IDGenerator():
    newSystem = onlineOrderSystem()
    assert(newSystem.orderID == 0)
    newID = newSystem.generateID()
    assert(newID == 1)
    assert(newSystem.orderID == 1)
    newID = newSystem.generateID()
    assert(newID == 2)
    assert(newSystem.orderID == 2)
    newSystem.orderIDReset()
    assert(newSystem.orderID == 0)

def test_createBasicIngredient():
    newPantry = inventoryManager()
    ingred1 = newPantry.createNewIngredient("Burger Bun",1,100)
    ingred2 = newPantry.createNewIngredient("Chicken Nugget",0.5,150)

    assert(ingred1.name == "Burger Bun")
    assert(ingred1.pricePerUnit == 1.0)
    assert(ingred1.quantity == 100)
    assert(ingred2.name == "Chicken Nugget")
    assert(ingred2.pricePerUnit == 0.5)
    assert(ingred2.quantity == 150)

# TESTS FOR EXCEPTION HANDLING
def test_createBasicIngredientWithNegativePrice():
    with pytest.raises(IngredientFieldError):
        validNewIngredientCheck("Burger Bun",-1,100)    

def test_createBasicIngredientWithNegativeQuantity():
    with pytest.raises(IngredientFieldError):
        validNewIngredientCheck("Burger Bun",1,-100)    

def test_createBasicIngredientWithNoName():
    with pytest.raises(IngredientFieldError):
        validNewIngredientCheck("",1,100)   

def test_createBasicIngredientWrongPriceType():
    with pytest.raises(FieldTypeError):
        validNewIngredientCheck("Burger Bun","1",100)  

def test_createBasicIngredientWrongNameType():
    with pytest.raises(FieldTypeError):
        validNewIngredientCheck(False,1,100)  

def test_createBasicIngredientWrongQuantityType():
    with pytest.raises(FieldTypeError):
        validNewIngredientCheck("Burger Bun",1,"100")

class TestBasicPantry():
    def setup_method(self):
        self.newPantry = inventoryManager()
        ingred1 = self.newPantry.createNewIngredient("Buns",1,100)
        ingred2 = self.newPantry.createNewIngredient("Beef Patty",1,100)
        ingred3 = self.newPantry.createNewIngredient("Cheese",0.5,100)
        ingred4 = self.newPantry.createNewIngredient("Lettuce",0.5,100)
        ingred5 = self.newPantry.createNewIngredient("375ml Fanta",2,10)
        ingred6 = self.newPantry.createNewIngredient("1L Coke",4,20)
        self.newPantry.addMainIngredient(ingred1)
        self.newPantry.addMainIngredient(ingred2)
        self.newPantry.addMainIngredient(ingred3)
        self.newPantry.addMainIngredient(ingred4)
        self.newPantry.addSideIngredient(ingred5)
        self.newPantry.addSideIngredient(ingred6)
  
    def test_checkCorrectlyAddedToDicts(self):
        assert(len(self.newPantry.mainIngredients) == 4)
        assert(len(self.newPantry.sideIngredients) == 2)
        
        getIngred1 = self.newPantry.findMain("Buns")
        assert(getIngred1.name == "Buns")
        assert(getIngred1.pricePerUnit == 1)
        assert(getIngred1.quantity == 100)
        getIngred2 = self.newPantry.findMain("Beef Patty")
        assert(getIngred2.name == "Beef Patty")
        assert(getIngred2.pricePerUnit == 1)
        assert(getIngred2.quantity == 100)
        getIngred3 = self.newPantry.findMain("Cheese")
        assert(getIngred3.name == "Cheese")
        assert(getIngred3.pricePerUnit == 0.5)
        assert(getIngred3.quantity == 100)
        getIngred4 = self.newPantry.findMain("Lettuce")
        assert(getIngred4.name == "Lettuce")
        assert(getIngred4.pricePerUnit == 0.5)
        assert(getIngred4.quantity == 100)

        getIngred1 = self.newPantry.findSide("375ml Fanta")
        assert(getIngred1.name == "375ml Fanta")
        assert(getIngred1.pricePerUnit == 2)
        assert(getIngred1.quantity == 10)
        getIngred2 = self.newPantry.findSide("1L Coke")
        assert(getIngred2.name == "1L Coke")
        assert(getIngred2.pricePerUnit == 4)
        assert(getIngred2.quantity == 20)

    def test_ingredientDoesNotExist(self):
        getIngred1 = self.newPantry.findMain("Shrek 2")
        assert(getIngred1 == None)
        getIngred2 = self.newPantry.findSide("Donuts")
        assert(getIngred2 == None)

    def test_removeIngredient(self):
        assert(len(self.newPantry.mainIngredients) == 4)
        self.newPantry.deleteIngredient("Lettuce",self.newPantry.mainIngredients)
        assert(len(self.newPantry.mainIngredients) == 3)
        getIngred1 = self.newPantry.findMain("Lettuce")
        assert(getIngred1 == None)
    
    def test_cannotAddExistingIngredient(self):
        assert(len(self.newPantry.sideIngredients) == 2)
        ingred1 = self.newPantry.createNewIngredient("375ml Fanta",2,10)
        self.newPantry.addSideIngredient(ingred1)
        assert(len(self.newPantry.sideIngredients) == 2)     

class TestMakeBasicBurger():
    def setup_method(self):
        self.newSystem = onlineOrderSystem()
        ingred1 = self.newSystem.pantry.createNewIngredient("Buns",1,100)
        ingred2 = self.newSystem.pantry.createNewIngredient("Beef Patty",1,100)
        self.newSystem.pantry.addMainIngredient(ingred1)
        self.newSystem.pantry.addMainIngredient(ingred2)
        self.newMain = Main()

    def test_checkStoredInMainIngredients(self):
        assert(len(self.newSystem.pantry.mainIngredients) == 2)

    def test_correctlyInitialisedMain(self):
        newMain = Main()
        assert(self.newMain.netMainPrice == 0.0)
        assert(self.newMain.quantity == None)
        assert(len(self.newMain.baseIngredients) == 0)
        assert(len(self.newMain.extraIngredients) == 0)

    def test_createBaseBurger(self):
        assert(self.newMain.createBaseBurger(self.newSystem.pantry) == True)
        assert(len(self.newMain.baseIngredients) == 2)
        assert(self.newMain.netMainPrice == 3)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Buns").quantity == 98)
        assert(self.newSystem.pantry.findMain("Beef Patty").quantity == 99)

class TestMakeComplexBurger():
    def setup_method(self):
        self.newSystem = onlineOrderSystem()
        ingred1 = self.newSystem.pantry.createNewIngredient("Buns",1,100)
        ingred2 = self.newSystem.pantry.createNewIngredient("Beef Patty",1,100)
        ingred3 = self.newSystem.pantry.createNewIngredient("Cheese",0.5,100)
        ingred4 = self.newSystem.pantry.createNewIngredient("Lettuce",0.5,100)
        self.newSystem.pantry.addMainIngredient(ingred1)
        self.newSystem.pantry.addMainIngredient(ingred2)
        self.newSystem.pantry.addMainIngredient(ingred3)
        self.newSystem.pantry.addMainIngredient(ingred4)
        self.newMain = Main()

    def test_checkStoredInMainIngredients(self):
        assert(len(self.newSystem.pantry.mainIngredients) == 4)

    def test_createBurgerWithExtras(self):
        assert(self.newMain.createBaseBurger(self.newSystem.pantry) == True)
        assert(len(self.newMain.baseIngredients) == 2)
        assert(self.newMain.netMainPrice == 3)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Buns").quantity == 98)
        assert(self.newSystem.pantry.findMain("Beef Patty").quantity == 99)

        assert(self.newMain.addExtraIngredientBasic(self.newSystem.pantry,"Cheese",2)==True)
        assert(len(self.newMain.extraIngredients) == 1)
        assert(self.newSystem.pantry.findMain("Cheese").quantity == 98)
        assert(self.newMain.netMainPrice == 4)

        assert(self.newMain.addExtraIngredientBasic(self.newSystem.pantry,"Lettuce",1)==True)
        assert(len(self.newMain.extraIngredients) == 2)
        assert(self.newSystem.pantry.findMain("Lettuce").quantity == 99)
        assert(self.newMain.netMainPrice == 4.5)

    def test_cannotAddExtraInsufficientStock(self):
        assert(self.newMain.createBaseBurger(self.newSystem.pantry) == True)
        assert(len(self.newMain.baseIngredients) == 2)
        assert(self.newMain.netMainPrice == 3)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Buns").quantity == 98)
        assert(self.newSystem.pantry.findMain("Beef Patty").quantity == 99)

        assert(self.newMain.addExtraIngredientBasic(self.newSystem.pantry,"Cheese",200)==False)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Cheese").quantity == 100)
        assert(self.newMain.netMainPrice == 3)

    def test_cannotAddNonExistingIngredients(self):
        assert(self.newMain.createBaseBurger(self.newSystem.pantry) == True)
        assert(len(self.newMain.baseIngredients) == 2)
        assert(self.newMain.netMainPrice == 3)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Buns").quantity == 98)
        assert(self.newSystem.pantry.findMain("Beef Patty").quantity == 99)

        assert(self.newMain.addExtraIngredientBasic(self.newSystem.pantry,"Eggs",200)==False)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newMain.netMainPrice == 3)


class TestMakeBasicWrap():
    def setup_method(self):
        self.newSystem = onlineOrderSystem()
        ingred1 = self.newSystem.pantry.createNewIngredient("Tortillas",1,100)
        ingred2 = self.newSystem.pantry.createNewIngredient("Chicken",1.5,100)
        self.newSystem.pantry.addMainIngredient(ingred1)
        self.newSystem.pantry.addMainIngredient(ingred2)
        self.newMain = Main()

    def test_checkStoredInMainIngredients(self):
        assert(len(self.newSystem.pantry.mainIngredients) == 2)

    def test_correctlyInitialisedMain(self):
        newMain = Main()
        assert(self.newMain.netMainPrice == 0.0)
        assert(self.newMain.quantity == None)
        assert(len(self.newMain.baseIngredients) == 0)
        assert(len(self.newMain.extraIngredients) == 0)

    def test_createBaseWrap(self):
        assert(self.newMain.createBaseWrap(self.newSystem.pantry) == True)
        assert(len(self.newMain.baseIngredients) == 2)
        assert(self.newMain.netMainPrice == 2.5)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Tortillas").quantity == 99)
        assert(self.newSystem.pantry.findMain("Chicken").quantity == 99)


class TestMakeComplexWrap():
    def setup_method(self):
        self.newSystem = onlineOrderSystem()
        ingred1 = self.newSystem.pantry.createNewIngredient("Tortillas",1,100)
        ingred2 = self.newSystem.pantry.createNewIngredient("Chicken",1.5,100)
        ingred3 = self.newSystem.pantry.createNewIngredient("Onions",0.1,100)
        ingred4 = self.newSystem.pantry.createNewIngredient("Hommus",2.5,30)
        self.newSystem.pantry.addMainIngredient(ingred1)
        self.newSystem.pantry.addMainIngredient(ingred2)
        self.newSystem.pantry.addMainIngredient(ingred3)
        self.newSystem.pantry.addMainIngredient(ingred4)
        self.newMain = Main()

    def test_checkStoredInMainIngredients(self):
        assert(len(self.newSystem.pantry.mainIngredients) == 4)

    def test_createWrapWithExtras(self):
        assert(self.newMain.createBaseWrap(self.newSystem.pantry) == True)
        assert(len(self.newMain.baseIngredients) == 2)
        assert(self.newMain.netMainPrice == 2.5)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Tortillas").quantity == 99)
        assert(self.newSystem.pantry.findMain("Chicken").quantity == 99)

        assert(self.newMain.addExtraIngredientBasic(self.newSystem.pantry,"Onions",10)==True)
        assert(len(self.newMain.extraIngredients) == 1)
        assert(self.newSystem.pantry.findMain("Onions").quantity == 90)
        assert(self.newMain.netMainPrice == 3.5)

        assert(self.newMain.addExtraIngredientBasic(self.newSystem.pantry,"Hommus",1)==True)
        assert(len(self.newMain.extraIngredients) == 2)
        assert(self.newSystem.pantry.findMain("Hommus").quantity == 29)
        assert(self.newMain.netMainPrice == 6)

    def test_cannotAddExtraInsufficientStock(self):
        assert(self.newMain.createBaseWrap(self.newSystem.pantry) == True)
        assert(len(self.newMain.baseIngredients) == 2)
        assert(self.newMain.netMainPrice == 2.5)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Tortillas").quantity == 99)
        assert(self.newSystem.pantry.findMain("Chicken").quantity == 99)

        assert(self.newMain.addExtraIngredientBasic(self.newSystem.pantry,"Hommus",200)==False)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Hommus").quantity == 30)
        assert(self.newMain.netMainPrice == 2.5)



class TestUnableToMakeBasicBurgerDueToStock():
    def setup_method(self):
        self.newSystem = onlineOrderSystem()
        ingred1 = self.newSystem.pantry.createNewIngredient("Buns",1,1)
        ingred2 = self.newSystem.pantry.createNewIngredient("Beef Patty",1,1)
        self.newSystem.pantry.addMainIngredient(ingred1)
        self.newSystem.pantry.addMainIngredient(ingred2)
        self.newMain = Main()

    def test_checkStoredInMainIngredients(self):
        assert(len(self.newSystem.pantry.mainIngredients) == 2)

    def test_unableToCreateBaseBurger(self):
        assert(self.newMain.createBaseBurger(self.newSystem.pantry) == None)
        assert(len(self.newMain.baseIngredients) == 0)
        assert(self.newMain.netMainPrice == 0)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Buns").quantity == 1)
        assert(self.newSystem.pantry.findMain("Beef Patty").quantity == 1)

class TestUnableToMakeBasicWrapDueToStock():
    def setup_method(self):
        self.newSystem = onlineOrderSystem()
        ingred1 = self.newSystem.pantry.createNewIngredient("Tortillas",1,1)
        ingred2 = self.newSystem.pantry.createNewIngredient("Chicken",1,0)
        self.newSystem.pantry.addMainIngredient(ingred1)
        self.newSystem.pantry.addMainIngredient(ingred2)
        self.newMain = Main()

    def test_checkStoredInMainIngredients(self):
        assert(len(self.newSystem.pantry.mainIngredients) == 2)

    def test_unableToCreateBaseWrap(self):
        assert(self.newMain.createBaseWrap(self.newSystem.pantry) == None)
        assert(len(self.newMain.baseIngredients) == 0)
        assert(self.newMain.netMainPrice == 0)
        assert(len(self.newMain.extraIngredients) == 0)
        assert(self.newSystem.pantry.findMain("Tortillas").quantity == 1)
        assert(self.newSystem.pantry.findMain("Chicken").quantity == 0)

class TestOrderSystem():
    def setup_method(self):
        self.newSystem = onlineOrderSystem()
        ingred1 = self.newSystem.pantry.createNewIngredient("Buns",1,100)
        ingred2 = self.newSystem.pantry.createNewIngredient("Beef Patty",1,100)
        ingred3 = self.newSystem.pantry.createNewIngredient("1L Coke",4,20)
        self.newSystem.pantry.addMainIngredient(ingred1)
        self.newSystem.pantry.addMainIngredient(ingred2)
        self.newSystem.pantry.addSideIngredient(ingred3)
        self.newOrder = Order()
        self.newMain = Main()
        self.newSide = Side()


    def test_correctlyInitialisedOrder(self):
        assert(self.newOrder._netOrderPrice == 0.0)
        assert(self.newOrder._orderID == None)
        assert(self.newOrder._status == None)
        assert(len(self.newOrder._orderMains)==0)
        assert(len(self.newOrder._orderSides)==0)

    def test_addMainsToOrder(self):
        assert(self.newMain._totalMainPrice == 0)
        self.newMain.createBaseBurger(self.newSystem.pantry)
        assert(self.newMain._totalMainPrice == 3)
        assert(len(self.newOrder.orderMains)==0)
        assert(self.newOrder.netOrderPrice == 0.0)
        self.newOrder.addOrderMain(self.newMain)
        assert(len(self.newOrder.orderMains)==1)   
        assert(self.newOrder.netOrderPrice == 3.0)     

    def test_addSidesToOrder(self):
        assert(self.newSide.netSidePrice == 0)
        side= self.newSystem.pantry.findSide("1L Coke")
        assert(side != None)
        self.newSide.confirmSide(side, 2)
        assert(self.newSide._netSidePrice == 8)
        assert(len(self.newOrder.orderSides)==0)
        assert(self.newOrder.netOrderPrice == 0.0)
        self.newOrder.addOrderSides(self.newSide)
        assert(len(self.newOrder.orderSides)==1)   
        assert(self.newOrder.netOrderPrice == 8.0)     

    def test_AddOrderToActiveList(self):
        self.newMain.createBaseBurger(self.newSystem.pantry)
        self.newOrder.addOrderMain(self.newMain)
        self.newOrder.confirmOrderDefault()
        self.newOrder.orderID = self.newSystem.generateID()
        assert(len(self.newSystem.activeOrders) == 0)
        self.newSystem.addActiveOrder(self.newOrder)
        assert(len(self.newSystem.activeOrders) == 1)      

    def test_searchForOrders(self):
        self.newMain.createBaseBurger(self.newSystem.pantry)
        self.newOrder.addOrderMain(self.newMain)
        self.newOrder.confirmOrderDefault()
        self.newOrder.orderID = self.newSystem.generateID()
        self.newSystem.addActiveOrder(self.newOrder)
        assert(len(self.newSystem.activeOrders) == 1) 
        assert(self.newSystem.getActiveOrder(1) != None) 

    def test_searchForNonExistantOrders(self):
        assert(self.newSystem.getActiveOrder(1) == None)
        assert(self.newSystem.getCompletedOrders(1)==None)

    def test_moveOrderActiveToCompleted(self):
        self.newMain.createBaseBurger(self.newSystem.pantry)
        self.newOrder.addOrderMain(self.newMain)
        self.newOrder.confirmOrderDefault()
        self.newOrder.orderID = self.newSystem.generateID()
        self.newSystem.addActiveOrder(self.newOrder)
        assert(len(self.newSystem.activeOrders) == 1) 
        assert(self.newSystem.getActiveOrder(1) != None) 
        assert(len(self.newSystem.completedOrders) == 0) 
        assert(self.newSystem.getCompletedOrders(1) == None) 

        self.newSystem.moveToCompleted(1)
        assert(len(self.newSystem.activeOrders) == 0) 
        assert(self.newSystem.getActiveOrder(1) == None) 
        assert(len(self.newSystem.completedOrders) == 1) 
        assert(self.newSystem.getCompletedOrders(1) != None) 