import pickle
from pickleHandler import loadSystem, saveSystem
from onlineOrderSystem import onlineOrderSystem 
from flask import Flask 

app = Flask(__name__,template_folder="Templates")

### Terminal Management ###
def systemLoad():
    print("Loading previous system.")
    system = loadSystem()
    if system != None:
        print("Successfully loaded past system.")
        return system

def systemShutdown(systemToSave):
    print("Shutting down")
    saveSystem(systemToSave)
    exit()

def updateToLatest(oldSystem):
    newSystem = onlineOrderSystem()
    newSystem.pantry._mainIngredients = oldSystem.pantry._mainIngredients
    newSystem.pantry._sideIngredients = oldSystem.pantry._sideIngredients
    newSystem.pantry._dessertIngredients = oldSystem.pantry._dessertIngredients
    return newSystem