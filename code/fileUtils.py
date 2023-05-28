import pickle

''' Métodos principales '''
''' (requeridos por el proyecto) '''

def saveMap(graph):
    try:
        with open("../resources/newMap", "bw") as file:
            pickle.dump(graph, file)
    except Exception as a:
        print("Error al guardar el mapa", a.args)
def loadMap():
    try:
        with open("../resources/newMap", "br") as file:
            f = pickle.load(file)
            for i in f:
                print(i.head.value)
    except Exception as a:
        print("Error al guardar el mapa", a.args)
def saveFixedElem(elem):
    try:
        with open("../resources/fixedElems", "bw") as file:
            pickle.dump(elem, file)
    except:
        print("Error al guardar elemento fijo")
def loadFixedElems():
    try:
        with open("../resources/fixedElems", "br") as file:
            return pickle.load(file)
    except:
        print("Error al cargar elemento fijo")
def saveMobileElem(elem):
    try:
        with open("../resources/mobileElems", "bw") as file:
            pickle.dump(elem, file)
    except:
        print("Error al guardar elemento móvil")
def loadMobileElems():
    try:
        with open("../resources/mobileElems", "br") as file:
            return pickle.load(file)
    except:
        print("Error al cargar elemento móvil")

''' Métodos temporales para testeo de funciones del programa '''
''' (no deberían ser necesarios una vez terminada la aplicación) '''

def setupFiles():
    dictionary = {}
    with open("../resources/fixedElems", "bw") as file:
        pickle.dump(dictionary, file)
    with open("../resources/mobileElems", "bw") as file:
        pickle.dump(dictionary, file)
