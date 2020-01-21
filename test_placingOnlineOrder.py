import pytest
from projEnums import orderStatus
from fieldCheck import *
from onlineOrderSystem import *
from pantry import *  
from main import Main   
from sides import Side 



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

class TestUnableToOrderSundaeDueToStock():
    def setup_method(self):
        self.newSystem = onlineOrderSystem()
        ingred1 = self.newSystem.pantry.createNewIngredient("Chocolate Sundae",1,1)
        self.newSystem.pantry.addDessertIngredient(ingred1)
        self.newMain = Main()

    def test_checkStoredInMainIngredients(self):
        assert(len(self.newSystem.pantry.dessertIngredients) == 1)
    

    def unableToOrderSundae(self):
    assert(len(self.newMain.dessertIngredients) == 0)
    assert(self.newMain.calcNetDessertPrice == 0)
    assert(self.newSystem.pantry.findDessert.quantity == 1)
   




       


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

