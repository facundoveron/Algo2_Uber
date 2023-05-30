from ownLibraries import graphUtils
import fileUtils
import re

class FixedElem:
    def __init__(self, dir):
        self.dir = dir

class MobileElem:
    def __init__(self, dir, amount):
        self.dir = dir
        self.amount = amount

def createMap(route):
    try:
        coordinates = open(route)
        if coordinates != None:
            vertices = coordinates.readline()
            edges = coordinates.readline()
            coordinates.close()
            graph = graphUtils.createGraph(vertices, edges)
            fileUtils.saveMap(graph)
        else:
            print("El archivo está vacío")
    except Exception as a:
        print("Error al crear el mapa", a.args)

def loadFixedElement(route):
    '''
    route = <nombre, dirección>
    route = <AX, {<e1, 10>, <e2, 5>}>
    '''
    name = re.search("\w{2}", route).group()
    direction = re.search("(?<={).+(?=})", route).group()
    direction = re.findall(r'\w+', direction)
    graph = fileUtils.loadMap()
    error = graphUtils.validator(direction, graph)
    if error == None:
        currentDict = fileUtils.loadFixedElems()
        currentDict[name] = FixedElem(direction)
        fileUtils.saveFixedElem(currentDict)
        print("Done! FE")
    else:
        print(error)

def loadMobileElement(route):
    '''
    route = <nombre, dirección, monto>
    route = <PX, {<e1, 10>, <e2, 5>}, saldo>
    route = <CX, {<e1, 10>, <e2, 5>}, tarifa>
    '''
    name = re.search("\w{2}", route).group()
    direction = re.search("(?<={).+(?=})", route).group()
    amount = re.search("\d{1,5}(?=>$)", route).group()
    error = graphUtils.validator("","")
    if error == None:
        currentDict = fileUtils.loadMobileElems()
        currentDict[name] = MobileElem(direction, amount)
        fileUtils.saveMobileElem(currentDict)
        print("Done! ME")
    else:
        print(error)

def createTrip(route):
    '''
    route = PX/CX <dirección>/<elemento>
    '''
    print("CT")