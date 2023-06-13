import graphUtils
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
    coordinates = open(route)
    if coordinates != None:
        vertices = coordinates.readline()
        vertices = re.findall("\d+", vertices)
        edges = coordinates.readline()
        edges = re.findall("<.+?>", edges)
        coordinates.close()
        graph = graphUtils.createGraph(vertices, edges)
        fileUtils.save("map", graph)
        fileUtils.setupDicts()
        print("Map succesfully saved")
    else:
        print("Initialization error")

def isValid(graph, dir):
    # ej: dir = ["e0", "10", "e1", "20"]
    dirLen = int(dir[1]) + int(dir[3])
    startNode = dir[0][1]
    adjList = graph[startNode]
    for node in adjList:
        if node.val == dir[2][1] and dirLen == int(node.len):
            return node
    return False

def saveElem(params):
    # params = <nombre, dirección, monto>
    # params = AX "<e1, 10>, <e2, 5>"
    # params = PX "<e1, 10>, <e2, 5>" saldo
    # params = CX "<e1, 10>, <e2, 5>" tarifa
    # name -> params[0]
    # dir -> params[1]
    # amount -> params[2]
    if len(params) < 2:
        print("Missing required arguments")
        return
    name = params[0]
    dir = re.findall("\w+", params[1])
    graph = fileUtils.load("map")
    destinationNode = isValid(graph, dir)
    if not destinationNode:
        print("Entered direction is not a valid direction in the map")
        return
    if name[0] == "P":
        balance = params[2]
        dic = fileUtils.load("users")
        dic[name] = User(dir, balance)
        fileUtils.save("users", dic)
        print("User succesfully saved")
    elif name[0] == "C":
        rate = params[2]
        dic = fileUtils.load("drivers")
        dic[name] = Driver(dir, rate)
        destinationNode.driver = name
        fileUtils.save("drivers", dic)
        fileUtils.save("map", graph)
        print("Driver succesfully saved")
    else:
        dic = fileUtils.load("fixed")
        dic[name] = Elem(dir)
        fileUtils.save("fixed", dic)
        print("Fixed location succesfully saved")

def createTrip(params):
    # params = PX, <dirección>/<elemento>
    graph = fileUtils.load("map")
    parts = re.findall("\w+", params)
    userName = parts[0]
    user = fileUtils.load("users").get(userName, False)
    if not user:
        print("Entered user does not yet exist")
        return
    originDir = user.dir
    if parts[1][0] == "e":
        destinationDir = parts[1:]
    else:
        fixedLocationName = parts[1]
        destinationDir = fileUtils.load("fixed")[fixedLocationName].dir
    # At this point isValid should always returns a node,
    # as direction was previously checked at save time
    originNode = isValid(graph, originDir)
    destinationNode = isValid(graph, destinationDir)
    if not destinationNode:
        print("Entered direction is not a valid direction in the map")
        return
    parents = {}
    graphUtils.dijkstra(graph, originNode, parents)
    #shortestPath = graphUtils.shortestPath(originNode, destinationNode, parents)
    driversNearUser = graphUtils.findDrivers(graph, originNode)

def test():
    graph = fileUtils.load("map")
    users = fileUtils.load("users")
    drivers = fileUtils.load("drivers")
    print(vars(graph["3"][0]))