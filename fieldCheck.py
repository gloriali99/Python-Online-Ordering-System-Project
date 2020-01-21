
class negativeIngredientQuantity(Exception):
    def __init__(self, ingredientName, currQuantity, quantityToAdd, afterQuantity):
        errorMsg = f"{ingredientName} currently has {currQuantity} units remaining. The request for {quantityToAdd} units will result in a negative quantity ({afterQuantity}) which is not allowed"

        self._errorMsg = errorMsg

    @property
    def errorMsg(self):
        return self._errorMsg

    def __str__(self):
        return self.errorMsg

class IngredientFieldError(Exception):

    def __init__(self, errorField = None, errorMsg = None):
        if errorMsg == None:
            if errorField == None:
                errorMsg = "One or more fields has invalid input incorrectly. Please carefully review each field to ensure everything is correct before proceeding."
            else:
                errorMsg = f"{errorField} has invalid input. Please ensure this field is correct before proceeding."
        self._errorMsg = errorMsg

    @property
    def errorMsg(self):
        return self._errorMsg

    def __str__(self):
        return self.errorMsg

class DuplicateOrder(Exception):

    def __init__(self, errorMsg = "An order seems to exist with the exact order ID."):
        self._errorMsg = errorMsg

    @property
    def errorMsg(self):
        return self._errorMsg

    def __str__(self):
        return self.errorMsg

class MissingOrder(Exception):

    def __init__(self, errorMsg = "No order exists with give order ID"):
        self._errorMsg = errorMsg

    @property
    def errorMsg(self):
        return self._errorMsg

    def __str__(self):
        return self.errorMsg

class FieldTypeError(Exception):

    def __init__(self, errorField = None, recievedType = None, expectedType = None, errorMsg = None):
        if errorMsg == None and errorField != None:
            if recievedType == None or expectedType == None:
                errorMsg = f"{errorField} has been input incorrectly. Please ensure {errorField} is filled in correctly before proceeding."
            else:
                errorMsg = f"{errorField} has been input incorrectly. Please ensure {errorField} recieves an {expectedType} instead of a {recievedType}."
        elif errorMsg == None:
            errorMsg = "One or more fields is recieveing the wrong type of information! Please ensure all fields are filled out correctly before proceeding."
        self._errorMsg = errorMsg

    @property
    def errorMsg(self):
        return self._errorMsg

    def __str__(self):
        return self.errorMsg

def validNewIngredientCheck(ingredientName, pricePerUnit, initialQuantity):
    if type(ingredientName) != str:
        raise FieldTypeError("Ingredient Name",str(type(ingredientName)),"String")
    if type(initialQuantity) != int:
        raise FieldTypeError("Initial Quantity",str(type(initialQuantity)),"Integer")
    if type(pricePerUnit) != int and type(pricePerUnit) != float:
        raise FieldTypeError("Price per Unit",str(type(pricePerUnit)),"Integer or Decimal") 

    if len(ingredientName) == 0:
        raise IngredientFieldError(None,"It does not appear this ingredient has been given a name. Please try again")
    if pricePerUnit < 0:
        raise IngredientFieldError(None,"Price can not be negative. Please try again.")
    if initialQuantity < 0:
        raise IngredientFieldError(None,"Initial Quantity can not be negative. Please try again.")

def checkValidOrder(orderID):
    if self.activeOrders.get(orderID) == None:
        raise MissingOrder(f"Order {orderID} currently does not exist as an active order.")
    if self.completedOrders.get(orderID) != None:
        raise DuplicateOrder(f"Order {orderID} already exists in completedOrders list. Please check to ensure no duplicate orders are present and try again.")

# valid ingredient for burger 

# valid ingredient for wrap 


