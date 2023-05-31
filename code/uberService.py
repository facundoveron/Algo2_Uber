from ownLibraries import graphUtils
import fileUtils
import re

class Elem:
    def __init__(self, dir):
        self.dir = dir

class User(Elem):
    def __init__(self, dir, amount):
        super().__init__(dir)
        self.balance = amount

class Driver(Elem):
    def __init__(self, dir, amount):
        super().__init__(dir)
        self.rate = amount

def setup(route):
    try:
        coordinates = open(route)
        if coordinates != None:
            vertices = coordinates.readline()
            edges = coordinates.readline()
            coordinates.close()
            graph = graphUtils.createGraph(vertices, edges)
            fileUtils.save("map", graph)
            fileUtils.setupDicts()
            print("Map succesfully saved")
        else:
            print("El archivo está vacío")
    except Exception as a:
        print("Error al crear el mapa", a.args)

def saveElem(params):
    # params = <nombre, dirección, monto>
    # params = AX, {<e1, 10>, <e2, 5>}
    # params = PX, {<e1, 10>, <e2, 5>}, saldo
    # params = CX, {<e1, 10>, <e2, 5>}, tarifa
    parts = re.findall("\w+", params)
    # name -> part 0
    # dir -> parts 1-4
    # amount -> part 5
    if len(parts) <= 1 or (len(parts) > 1 and len(parts) < 5):
        print("Missing required arguments")
        return
    name = parts[0]
    dir = parts[1:-1] if len(parts) == 6 else parts[1:]
    # todo: add dir validation
    if name[0] == "P":
        balance = parts[5]
        dic = fileUtils.load("users")
        dic[name] = User(dir, balance)
        fileUtils.save("users", dic)
        print("User succesfully saved")
    elif name[0] == "C":
        rate = parts[5]
        dic = fileUtils.load("drivers")
        dic[name] = Driver(dir, rate)
        fileUtils.save("drivers", dic)
        print("Driver succesfully saved")
    else:
        dic = fileUtils.load("fixed")
        dic[name] = Elem(dir)
        fileUtils.save("fixed", dic)
        print("Fixed location succesfully saved")

def printList(L):
    for i in L:
        node = i.head
        print(i.head.value, end=" ")
        while node.nextNode != None:
            node = node.nextNode
            print(node.value, end=" ")
        print("")

def createTrip(params):
    # params = PX, <dirección>/<elemento>
    parts = re.findall("\w+", params)
    userName = parts[0]
    originDir = fileUtils.load("users")[userName].dir
    if parts[1][0] == "e":
        destinationDir = parts[1:]
    else:
        fixedLocation = parts[1]
        destinationDir = fileUtils.load("fixed")[fixedLocation].dir
    origVert1 = originDir[0]
    origDist1 = originDir[1]
    origVert2 = originDir[2]
    origDist2 = originDir[3]
    destVert1 = destinationDir[0]
    destDist1 = destinationDir[1]
    destVert2 = destinationDir[2]
    destDist2 = destinationDir[3]
    graph = fileUtils.load("map")
    shortestPath = graphUtils.dijkstra(graph, origVert1[1:], destVert1[1:])
    printList(shortestPath)