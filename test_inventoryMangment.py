import pytest
from projEnums import orderStatus
from fieldCheck import *
from onlineOrderSystem import *
from pantry import *  
from main import Main   
from sides import Side 

import pytest
from projEnums import orderStatus
from fieldCheck import *
from onlineOrderSystem import *
from pantry import *  
from main import Main   
from sides import Side 
from Sundaes import Dessert

class Test_US15_CorrectOrderID():
    def setup_method(self):
        self.GourmetBurgers = onlineOrderSystem()
        #ingred1 = self.GourmetBurgers.pantry.createNewIngredient("1L Coke",4,20)
        #self.GourmetBurgers.pantry.addSideIngredient(ingred1)
        self.newOrder = Order()
        self.newSide = Side()

    # Ensures on system startup ID Generator is initialsed correctly.
    def test_IDGeneratorInitilised(self):
        assert(self.GourmetBurgers.orderID == 0)
        newID = self.GourmetBurgers.generateID()
        assert(newID == 1)
        assert(self.GourmetBurgers.orderID == 1)
        newID = self.GourmetBurgers.generateID()
        assert(newID == 2)
        assert(self.GourmetBurgers.orderID == 2)
        self.GourmetBurgers.orderIDReset()
        assert(self.GourmetBurgers.orderID == 0)

    # Ensures no orders can have the same orderID.
    def test_cannotAddDuplicate(self):
        newOrder1 = Order()
        newOrder2 = Order()
        newOrder1.orderID = 1
        newOrder2.orderID = 1
        assert(len(self.GourmetBurgers.activeOrders)==0)
        self.GourmetBurgers.addActiveOrder(newOrder1)
        assert(len(self.GourmetBurgers.activeOrders)==1)
        self.GourmetBurgers.addActiveOrder(newOrder2)
        assert(len(self.GourmetBurgers.activeOrders)==1)

    # Ensure an order exists before moving into completed orders. Avoiding duplicated.
    def test_orderMustBeActive(self):
        newOrder1 = Order()
        newOrder1.orderID = self.GourmetBurgers.generateID()
        assert(self.GourmetBurgers.orderID == 1)
        assert(len(self.GourmetBurgers.activeOrders)==0)
        self.GourmetBurgers.addActiveOrder(newOrder1)
        assert(len(self.GourmetBurgers.activeOrders)==1)
        self.GourmetBurgers.moveToCompleted(newOrder1.orderID)
        assert(len(self.GourmetBurgers.activeOrders)==0)
        assert(len(self.GourmetBurgers.completedOrders)==1) 
        self.GourmetBurgers.moveToCompleted(newOrder1.orderID)  
        assert(len(self.GourmetBurgers.activeOrders)==0)
        assert(len(self.GourmetBurgers.completedOrders)==1)     

'''
    # Ensures that a confirmed order will have an order ID
    def test_IDExistsInOrder(self):
        assert(self.GourmetBurgers.orderID == 0)
        side = self.GourmetBurgers.pantry.findSide("1L Coke")
        self.newSide.confirmSide(side,1)
        self.newOrder.addOrderSides(self.newSide)
        self.newOrder.confirmOrderDefault()
        self.newOrder.orderID = self.newSystem.generateID()
        assert(self.GourmetBurgers.orderID == 1)

    # Ensures that mutliple orders will have unique IDs
    def test_IDUniqueMultipleOrders(self):
        pass
'''


class Test_US16_UpdateOrderProgression():
    def setup_method(self):
        self.GourmetBurgers = onlineOrderSystem()
        self.newOrder = Order()
        self.newOrder.orderID = self.GourmetBurgers.generateID()

    # This test ensures the order has been initialised correctly to not include any status.
    def test_initilisedCorrectly(self):
        assert(self.newOrder.status == None)

    # This test is to ensure that an order is set to active once confirmed.
    def test_confirmedOrder(self):
        assert(self.newOrder.status == None)
        self.newOrder.confirmOrderDefault()
        assert(self.newOrder.status == orderStatus.CONFIRMED)
        assert(self.newOrder.status != orderStatus.ACTIVE)
        self.GourmetBurgers.addActiveOrder(self.newOrder)
        assert(self.newOrder.status == orderStatus.ACTIVE)
        assert(self.newOrder.status != orderStatus.COMPLETED)
        self.GourmetBurgers.moveToCompleted(self.newOrder.orderID)
        assert(self.newOrder.status == orderStatus.COMPLETED)

class Test_US17_LogCompletedOrders():
    def setup_method(self):
        self.GourmetBurgers = onlineOrderSystem()
        self.newOrder1 = Order()
        self.newOrder1.orderID = self.GourmetBurgers.generateID()
        self.newOrder2 = Order()
        self.newOrder2.orderID = self.GourmetBurgers.generateID()
        self.newOrder3 = Order()
        self.newOrder3.orderID = self.GourmetBurgers.generateID()
        self.newOrder4 = Order()
        self.newOrder4.orderID = self.GourmetBurgers.generateID()
        self.randomSide1 = Side()
        self.randomSide1._quantity = 1
        self.newOrder1.addOrderSides(self.randomSide1)
        self.randomSide2 = Side()
        self.randomSide2._quantity = 2
        self.newOrder2.addOrderSides(self.randomSide2)

    # This test no past orders should exist when system is initialised
    def test_pastLogInitilisedCorrectly(self):
        assert(len(self.GourmetBurgers.completedOrders) == 0)

    # This test ensures all orders exist once moved. 
    def test_completeBackLog(self):
        self.GourmetBurgers.addActiveOrder(self.newOrder1)
        self.GourmetBurgers.addActiveOrder(self.newOrder2)
        self.GourmetBurgers.addActiveOrder(self.newOrder3)
        self.GourmetBurgers.addActiveOrder(self.newOrder4)
        assert(len(self.GourmetBurgers.activeOrders) == 4)
        assert(len(self.GourmetBurgers.completedOrders) == 0)
        self.GourmetBurgers.moveToCompleted(self.newOrder1.orderID)
        self.GourmetBurgers.moveToCompleted(self.newOrder2.orderID)
        self.GourmetBurgers.moveToCompleted(self.newOrder3.orderID)
        self.GourmetBurgers.moveToCompleted(self.newOrder4.orderID)
        assert(len(self.GourmetBurgers.activeOrders) == 0)
        assert(len(self.GourmetBurgers.completedOrders) == 4)

    def test_maintainsAttributes(self):
        self.GourmetBurgers.addActiveOrder(self.newOrder1)
        self.GourmetBurgers.addActiveOrder(self.newOrder2)
        assert(len(self.GourmetBurgers.activeOrders) == 2)
        assert(len(self.GourmetBurgers.completedOrders) == 0)
        assert(len(self.newOrder1.orderSides) == 1)
        assert(len(self.newOrder2.orderSides) == 1)
        self.GourmetBurgers.moveToCompleted(self.newOrder1.orderID)
        self.GourmetBurgers.moveToCompleted(self.newOrder2.orderID)
        assert(len(self.GourmetBurgers.activeOrders) == 0)
        assert(len(self.GourmetBurgers.completedOrders) == 2)
        assert(len(self.newOrder1.orderSides) == 1)
        assert(len(self.newOrder2.orderSides) == 1)