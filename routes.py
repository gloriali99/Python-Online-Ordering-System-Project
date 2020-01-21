from flask import render_template, url_for, abort, request, redirect
from fieldCheck import validNewIngredientCheck,  IngredientFieldError, FieldTypeError
from ingredient import Ingredient
from SystemManager import app, systemShutdown
from order import Order
from sides import Side
from Sundaes import Dessert
from run import GourmetBurgers
import copy

newOrder = Order()
orderSubmit = Order()

@app.route('/404')
@app.errorhandler(404)
def page_note_found(e=None):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/orderConfirmation/<orderID>")
def orderConfirmation(orderID):
    return render_template('confirmation.html', orderID=orderID)


# CODE FOR CUSTOMER INTERFACE
@app.route("/orderReview", methods=["GET","POST"])
def finalOrder():
    if request.method == "POST":
        newOrder.confirmOrderDefault()
        newOrder.orderID = GourmetBurgers.generateID()
        orderSubmit= copy.deepcopy(newOrder)
        GourmetBurgers.addActiveOrder(orderSubmit)
        newOrder.orderID = None
        newOrder.netOrderPrice=0.0
        newOrder.status = None
        newOrder.orderDesserts.clear()
        newOrder.orderMains.clear()
        newOrder.orderSides.clear()
        return redirect(url_for("orderConfirmation", orderID = orderSubmit.orderID))
    return render_template("finalOrder.html", order=newOrder)

@app.route("/desserts", methods=["GET","POST"])
def desserts():
    allDesserts = GourmetBurgers.pantry.dessertIngredients
    if request.method=="POST":
        for dictIterKeys, dictIterValues in request.form.items():
            if dictIterValues.isdigit() == True:
                if int(dictIterValues)>0:
                    if GourmetBurgers.pantry.getDessert(dictIterKeys,-int(dictIterValues)) == True: 
                        newDessert = Dessert()
                        newDessert.confirmDessert(GourmetBurgers.pantry.findDessert(dictIterKeys),int(dictIterValues))
                        newOrder.addOrderDesserts(newDessert)
                        print(newDessert)
                        print(len(newOrder.orderDesserts))
    return render_template("desserts.html", allDesserts = allDesserts)

@app.route("/sides", methods=["GET","POST"])
def sides():
    allSides = GourmetBurgers.pantry.sideIngredients
    if request.method=="POST":
        for dictIterKeys, dictIterValues in request.form.items():
            if dictIterValues.isdigit() == True:
                if int(dictIterValues)>0:
                    if GourmetBurgers.pantry.getSide(dictIterKeys,-int(dictIterValues)) == True: 
                        newSide = Side()
                        newSide.confirmSide(GourmetBurgers.pantry.findSide(dictIterKeys),int(dictIterValues))
                        newOrder.addOrderSides(newSide)
                        print(newSide)
    return render_template("sides.html", allSides = allSides)

#DONE
@app.route("/main")
def chooseBurgerorWrap():
    return render_template("mainBase.html")

@app.route("/main/burger")
def burger():
    return render_template("burger.html")

@app.route("/main/wrap")
def wrap():
    return render_template("wrap.html")

@app.route("/main/burger/baseburger")
def baseBurger():
    burgers = GourmetBurgers.pantry.mainBaseBurger
    return render_template("baseburger.html", baseburger = burgers)

@app.route("/main/wrap/customise")
def customiseBurger():
    return render_template("customiseburger.html")

@app.route("/order", methods=["GET","POST"])
def order():
    if request.method=="POST":
        orderID = request.form.get("orderID")
        if orderID == "":
            error = "Please enter your Unique Order ID!"
            return render_template("orderSearch.html", error=error)           
        elif orderID.isdigit() == False:
            error = "Your Order ID must be a number!"
            return render_template("orderSearch.html", error=error)           
        else:
            order = GourmetBurgers.getActiveOrder(int(orderID))
            if order == None:
                order = GourmetBurgers.getCompletedOrders(int(orderID))
                if order == None:
                    error = f"Uh oh! Order {orderID} does not exist in the system!"
                    return render_template("orderSearch.html", error=error)
        return redirect(url_for("orderID", orderID=orderID))
    return render_template("orderSearch.html")

@app.route("/order/<orderID>")
def orderID(orderID):
    order = GourmetBurgers.getActiveOrder(int(orderID))
    if order == None:
        order = GourmetBurgers.getCompletedOrders(int(orderID))
        if order == None:
            abort(404)
    return render_template("customerOrder.html", order=order)


'''    
####### STAFF ROUTES #######
'''


@app.route("/staff", methods=["GET", "POST"])
def staff():
    emptyMains = GourmetBurgers.pantry.returnEmptyMains()
    emptySides = GourmetBurgers.pantry.returnEmptySides()
    emptyDesserts = GourmetBurgers.pantry.returnEmptyDesserts()
    if request.method == "POST":
        if request.form.get("btnSystemShutDown"):
            return render_template("indexStaffDashboard.html", activeOrders=GourmetBurgers.activeOrders,mainEmpty=emptyMains,sideEmpty=emptySides, dessertEmpty=emptyDesserts, systemShutdown=True)
        if request.form.get("btnShutdownConfirm"):
            systemShutdown(GourmetBurgers)
    return render_template("indexStaffDashboard.html", activeOrders=GourmetBurgers.activeOrders,mainEmpty=emptyMains,sideEmpty=emptySides, dessertEmpty=emptyDesserts)

@app.route("/staff/pantry")
def inventoryCheck():
    return render_template("inventoryManager.html", mainIngredients=GourmetBurgers.pantry.mainIngredients, sideIngredients=GourmetBurgers.pantry.sideIngredients, dessertIngredients=GourmetBurgers.pantry.dessertIngredients)

@app.route("/staff/pantry/<ingredName>", methods=["GET", "POST"])
def pantryIngredient(ingredName):
    ingred = GourmetBurgers.pantry.findMain(ingredName)     #EITHER FIND ALL INGRED OR KEEP AS IS
    if ingred == None:
        ingred = GourmetBurgers.pantry.findSide(ingredName)
        if ingred == None:
            ingred = GourmetBurgers.pantry.findDessert(ingredName)
            if ingred == None:
                abort(404)
    if request.method == "POST":
        #print("Recieved post")
        if request.form.get("btnDeletedConfirm"):
            ingred = GourmetBurgers.pantry.findMain(ingredName)     #EITHER FIND ALL INGRED OR KEEP AS IS
            if ingred != None:
                GourmetBurgers.pantry.deleteMainIngredient(ingred)
            else:
                ingred = GourmetBurgers.pantry.findSide(ingredName)
                if ingred != None:
                    GourmetBurgers.pantry.deleteSideIngredient(ingred)
                else:
                    ingred = GourmetBurgers.pantry.findDessert(ingredName)
                    GourmetBurgers.pantry.deleteDessertIngredient(ingred)
            return redirect(url_for("inventoryCheck"))
        if request.form.get("btnDeleteIngredient"):
            return render_template("ingredient.html", ingredient = ingred, ingredDelete=True)
        elif request.form.get("btnUpdatePriceQuantity"):
            newPrice = request.form.get("priceField")
            if newPrice == "":
                newPrice = ingred.pricePerUnit
            newQuantity = request.form.get("quantityField")
            if newQuantity == "":
                newQuantity = ingred.quantity
            try:
                validNewIngredientCheck("CorrectName", float(newPrice), int(newQuantity))
            except FieldTypeError as error:
                #print(error)
                return render_template("ingredient.html", ingredient = ingred, error=error)
            except IngredientFieldError as error:
                #print(error)
                return render_template("ingredient.html", ingredient = ingred, error=error)
            except ValueError as error:
                try:
                    validNewIngredientCheck("CorrectName", newPrice, newQuantity)
                except FieldTypeError as error:
                    #print(error)
                    return render_template("ingredient.html", ingredient = ingred, error=error)
            else:
                ingred.pricePerUnit = newPrice
                ingred._quantity = newQuantity
                return render_template("ingredient.html", ingredient = ingred, error="Successfully updated Fields")
          
    return render_template("ingredient.html", ingredient = ingred)



@app.route("/staff/pantry/createIngredient", methods=["GET", "POST"])
def createIngredient():
    if request.method == "POST":
        if request.form.get("createIngredient"):
            ingredName = request.form.get("nameField")
            quantity = request.form.get("quantityField")
            price = request.form.get("priceField")
            ingredDict = request.form.get("dictSelect")

            try:
                validNewIngredientCheck(ingredName, float(price), int(quantity))
            except FieldTypeError as error:
                print(error)
                return render_template("createIngredient.html", error=error)
            except IngredientFieldError as error:
                print(error)
                return render_template("createIngredient.html", error=error)
            except ValueError as error:
                print(error)
            else:
                newIngred = Ingredient(ingredName,price,quantity)
                if ingredDict == "Main":
                    print("About to add to mains ")
                    GourmetBurgers.pantry.addMainIngredient(newIngred)
                elif ingredDict == "Side":
                    print("About to add to sides")
                    GourmetBurgers.pantry.addSideIngredient(newIngred)
                elif ingredDict == "Dessert":
                    GourmetBurgers.pantry.addDessertIngredient(newIngred)
                return render_template("createIngredient.html", ingred=newIngred)

        elif request.form.get("cancel"):
            return redirect(url_for("inventoryCheck"))

    return render_template("createIngredient.html")

@app.route("/staff/activeorders")
def activeOrders():
    return render_template("activeOrders.html", activeOrders=GourmetBurgers.activeOrders)

@app.route("/staff/completedorders")
def completedOrders():
    return render_template("completedOrders.html", completedOrders=GourmetBurgers.completedOrders)

@app.route("/staff/order/activeorders/<orderID>", methods=["GET", "POST"])
def orderStaffActive(orderID):

    if request.method == "POST":
        if request.form.get("btnOrderComplete"):
            GourmetBurgers.moveToCompleted(int(orderID))
            print("trying to redirect")
            return redirect(url_for("orderStaffCompleted",orderID=orderID))
    try:
        order = GourmetBurgers.getActiveOrder(int(orderID))
        if order == None:
            abort(404)
    except ValueError:
        abort(404)
    return render_template("order.html", order=order)


@app.route("/staff/order/completedorders/<orderID>")
def orderStaffCompleted(orderID):
    print("Entered orderStaff Complete with order id" + str(orderID))
    try:
        order = GourmetBurgers.getCompletedOrders(int(orderID))
        if order == None:
            abort(404)
    except ValueError:
        abort(404)
    else:
        return render_template("order.html", order=order)