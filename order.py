from projEnums import orderStatus
from pantry import inventoryManager
from sides import Side 
from main import Main
from Sundaes import Dessert

class Order():

    def __init__(self):

        self._orderMains = {}
        self._orderSides = {}
        self._orderDesserts = {}     
        self._netOrderPrice = 0.0
        self._orderID = None
        self._status = None
    
    '''
    ### INTERFACE
    '''
    def welcomeInterface(self, pantry):
        print("========================================")
        print("Create an order with GourmetBurgers.com!")

        while True:
            print("========================================")
            print("Type 1 to add a main.")
            print("Type 2 to add a side.")
            print("Type 3 to review your order.")
            print("Type 4 to confirm order.")
            print("Type C to cancel your order.")
            print("========================================")
            command = input("What would you like to do? ")

            if command.upper() == "C":
                self.status = orderStatus.CANCELED
                break
            elif command.isdigit() == True:
                if int(command) == 1:
                    newMain = Main()          #GLORIA ADD MAINS LOGIC
                    newMain.mainInterface(pantry)
                    if newMain._totalMainPrice != 0.0:
                        self.addOrderMain(newMain)

                elif int(command) == 2:
                    newSide = Side()
                    newSide.sideInterface(pantry)
                    if newSide.side != None:
                        self.addOrderSides(newSide)
                elif int(command) == 3:
                    self.printEntireOrder()
                elif int(command) == 4:
                    self.confirmOrder()
                    if self.status == orderStatus.CONFIRMED:
                        break

    '''
    #### MAKE ORDER ####
    '''

    def addOrderMain(self, newMain):    #GLORIA
        order = "Main " + str(len(self.orderMains) + 1)
        self.orderMains[order] = newMain
        self.updateNetPrice(newMain.netMainPrice)

    def addOrderSides(self, newSide):
        self.orderSides[newSide.side] = newSide 
        self.updateNetPrice(newSide.netSidePrice)

    def addOrderDesserts(self, newDessert):
        self.orderDesserts[newDessert.dessert] = newDessert 
        self.updateNetPrice(newDessert.netDessertPrice)

    def updateNetPrice(self, price):
        self._netOrderPrice = self.netOrderPrice + float(price)

    '''
    ### REVIEW ORDER ###
    '''    

    def printEntireOrder(self):
        print("___ ORDER SUMMARY ___")
        self.printAllMains()
        self.printAllSides()
        print(f"Total: ${self.netOrderPrice}")

    def printAllMains(self):
        print("--- MAINS SUMMARY ---")
        if len(self.orderMains) == 0:
            print("There are currently no mains in this order.")
        else:
            for currMain in self.orderMains.keys():
                print(self.orderMains[currMain])

    def printAllSides(self):
        print("--- SIDE SUMMARY ---")
        if len(self.orderSides) == 0:
            print("There are currently no sides in this order.")
        else:
            for currSides in self.orderSides.keys():
                print(self.orderSides[currSides])

    def printAllDesserts(self):
        print("--- Dessert SUMMARY ---")
        if len(self.orderDesserts) == 0:
            print("There are currently no Desserts in this order.")
        else:
            for currDessert in self.orderDesserts.keys():
                print(self.orderDesserts[currDessert])


    '''
    ### CONFIRM ORDER ###
    '''

    def confirmOrderDefault(self):
        self.status = orderStatus.CONFIRMED

    def confirmOrder(self):
        if len(self.orderMains) == 0 and len(self.orderSides) == 0:
            print("No mains or sides have been ordered!")
        self.printEntireOrder
        answer = input("Are you happy with your order (Y/N)? ")
        if answer.upper() == "Y":
            self.status = orderStatus.CONFIRMED

    '''
    #properties :)
    '''

    @property 
    def netOrderPrice(self): 
        return self._netOrderPrice 
    @netOrderPrice.setter
    def netOrderPrice(self, price):
        self._netOrderPrice += price    

    @property 
    def orderID(self): 
        return self._orderID 
    @orderID.setter
    def orderID(self, id):
        self._orderID = id

    @property 
    def orderMains(self):
        return self._orderMains

    @property 
    def orderSides(self): 
        return self._orderSides

    @property 
    def orderDesserts(self): 
        return self._orderDesserts

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, statusVal):
        self._status = statusVal

    def __str__(self):
        return f"Order {self.orderID}, containing {len(self.orderMains)} mains, {len(self.orderSides)} sides. Totalling ${self.netOrderPrice}."

