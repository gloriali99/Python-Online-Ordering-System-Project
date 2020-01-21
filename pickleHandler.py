import pickle

def loadSystem():
    fileName = "EntireOrderSystem.pickle"

    try:
        pickle_input = open(fileName,"rb")
        currentSystem = pickle.load(pickle_input)
        pickle_input.close()
    except FileNotFoundError:
        print(f"Cannot open {fileName} as it cannot be located!")
    except EOFError:
        print(f"The end of {fileName} was reached without being able to load the previous GourmetBurger Ordering System.")
    except pickle.UnpicklingError:
        print(f"A problem was enocuntered loading the GourmetBurger Ordering System from {fileName}. Data may be corrupt.")
    else:
        return currentSystem

def saveSystem(systemToDump):
    fileName = "EntireOrderSystem.pickle"

    try:
        pickle_output = open(fileName,"wb")
        pickle.dump(systemToDump, pickle_output)
        pickle_output.close()
    except FileNotFoundError:
        print(f"Cannot open {fileName} as it cannot be located!")
