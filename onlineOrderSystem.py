from order import Order
from pantry import inventoryManager
from fieldCheck import DuplicateOrder, MissingOrder, checkValidOrder
from projEnums import orderStatus


class onlineOrderSystem():

    def __init__(self):
        self._activeOrders = {}
        self._completedOrders = {}
        self._pantry = inventoryManager()
        self._orderIDIndex = 0

    '''
    ## ORDER MANAGER ##
    '''

    def mainInterface(self):
        print("========================================")
        print("GourmetBurgers onlineSystem Overview")

        while True:
            print("========================================")
            print("Type 1 to go to Inventory Manager")
            print("Type 2 to add an order")
            print("Type 3 to see all orders")
            print("Type C to cancel")
            print("Type S to save system")
            print("========================================")
            command = input("What would you like to do? ")    

            if command.isdigit() == True:
                if int(command) == 1:
                    self.pantry.inventoryInterface()
                elif int(command) == 2:
                    self.createNewOrder()
                elif int(command) == 3:
                    self.listAllOrders()
            elif command.upper() == "C":
                break
            elif command.upper() == "S":
                systemShutdown(self)


    def createNewOrder(self):
        newOrder = Order()
        newOrder.welcomeInterface(self.pantry)
        if newOrder.status == orderStatus.CONFIRMED:
            newOrder.orderID = self.generateID()
            self.addActiveOrder(newOrder)
            newOrder.status = orderStatus.ACTIVE
        elif newOrder.status == orderStatus.CANCELED:
            self.handleCanceled(newOrder)
            print("Order canceled. Please come again!")
        else:
            print("No order to add.")
    
    def handleCanceled(self,newOrder):
        '''
        if len(newOrder.orderMains) > 0:
            for currMain in newOrder.orderMains.keys():
                for currIngred in currMain.baseIngredients.keys():
                    currQuant = currMain.baseIngredients[currIngred].quantity
                for currIngred in currMain.extraIngredients.keys():
                    currQuant = currMain.extraIngredients[currIngred].quantity
                self.pantry.getMain(currMain, currQuant)
        '''
        if len(newOrder.orderSides) > 0:
            for currSide in newOrder.orderSides.keys():
                currQuant = newOrder.orderSides[currSide].quantity
                self.pantry.getSide(currSide, currQuant)


    def addActiveOrder(self, order):            # adds a new order to ActiveOrders dictionary
        try:
            if self.activeOrders.get(order.orderID) != None:
                raise DuplicateOrder(f"Unable to add order {order.orderID} as an order with ID {order.orderID} already exists.")
        except DuplicateOrder as error:
            print(error)
        else:
            order.status = orderStatus.ACTIVE
            self.activeOrders[order.orderID] = order

    def moveToCompleted(self, orderID):         # moves an order from activeOrders list to completedOrders list.
        try:
            if self.activeOrders.get(orderID) == None:
                raise MissingOrder(f"Order {orderID} currently does not exist as an active order.")
            if self.completedOrders.get(orderID) != None:
                raise DuplicateOrder(f"Order {orderID} already exists in completedOrders list. Please check to ensure no duplicate orders are present and try again.")
        except MissingOrder as error:
            print(error)
            return None
        except DuplicatOrder as error:
            print(error)
            return None
        else:
            orderToAdd = self.activeOrders.pop(orderID)
            orderToAdd.status = orderStatus.COMPLETED
            self.completedOrders[orderID] = orderToAdd

    '''
    ## ORDER SEARCH ##
    '''

    def getActiveOrder(self, orderID):          # returns specific order from ActiveOrders list
        i = self.activeOrders.get(orderID)
        if i == None:
            print (f"Order {orderID} does not exist as an active order.")
            return None
        else:
            return i

    def getCompletedOrders(self, orderID):      # returns specific order from completedOrders List
        i = self.completedOrders.get(orderID)
        if i == None:
            print (f"Order {orderID} does not exist as a completed order.")
            return None
        else:
            return i

    '''
    ### ORDER PRINT ###
    '''
    def listAllOrders(self):
        self.listActiveOrders()
        self.listCompletedOrders()

    def listActiveOrders(self):
        title = "CURRENT ACTIVE ORDERS"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.activeOrders) == 0:
            print("There are currently no active orders at this moment.")
        else:
            for currOrder in self.activeOrders.keys():
                print(self.activeOrders[currOrder])
        print("-" * len(title))

    def listCompletedOrders(self):
        title = "COMPLETED ORDERS"
        print("-" * len(title))
        print(title)
        print("=" * len(title))
        if len(self.completedOrders) == 0:
            print("There are currently no completed orders.")
        else:
            for currOrder in self.completedOrders.keys():
                print(self.completedOrders[currOrder])
        print("-" * len(title))

    '''
    ### OrderID Logic ###
    '''
    def generateID(self): 
        self.orderID = 1
        return self.orderID

    def orderIDReset(self):
        self.orderID = 0

    '''
    ### Properties ###
    '''
    @property                           # returns dictionary of all Active Orders
    def activeOrders(self):
        return self._activeOrders

    @property                           # returned dictionary of all Completed Orders
    def completedOrders(self):
        return self._completedOrders

    @property
    def pantry(self):
        return self._pantry

    @property
    def orderID(self):
        return self._orderIDIndex
    @orderID.setter
    def orderID(self, i):
        if i == 1:
            self._orderIDIndex += i 
        if i == 0:
            self._orderIDIndex = 0

#if __name__ == "__main__":
#    main()
