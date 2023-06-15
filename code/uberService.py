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
    startNode = dir[0][1:]
    endNode = dir[2][1:]
    adjListS = graph[startNode]
    adjListE = graph[endNode]
    for node in adjListS:
        if node.val == endNode and dirLen == int(node.len):
            return node

    for node in adjListE:
        if node.val == startNode and dirLen == int(node.len):
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
    # params = PX <dirección>/<elemento>
    graph = fileUtils.load("map")
    userName = params[0]
    user = fileUtils.load("users").get(userName, False)
    if not user:
        print("Entered user does not yet exist")
        return
    originDir = user.dir
    if params[1][0] == "<":
        destinationDir = re.findall("\w+", params[1])
    else:
        params = params.split()
        fixedLocationName = params[1]
        fixedLocation = fileUtils.load("fixed").get(fixedLocationName, False)
        if not fixedLocation:
            print("Entered fixed location does not yet exist")
            return
        destinationDir = fixedLocation.dir
    # At this point isValid should always returns a node,
    # as direction was previously checked at save time
    originNode = isValid(graph, originDir)
    destinationNode = isValid(graph, destinationDir)
    if not destinationNode:
        print("Entered direction is not a valid direction in the map")
        return
    parents = {}
    graphUtils.dijkstra(graph, originNode, parents)
    shortestPath = graphUtils.shortestPath(originNode, destinationNode, parents)
    driversNearUser = graphUtils.findDrivers(graph, originNode)
    # driversNearUser[x][0] = minimun distance car <-> user (int)
    # driversNearUser[x][1] = driver name (str)
    # driversNearUser[x][2] = trip price (float)
    driversNearUser.sort(key = lambda x: x[0])
    chosenDriver = requestUserInput(user, driversNearUser)
    # Move driver location to destinationDir
    driversDic = fileUtils.load("drivers")
    driverName = driversNearUser[chosenDriver][1]
    driversDic[driverName].dir = destinationDir
    fileUtils.save("drivers", driversDic)
    # Move user location to destinationDir and update it's balance accordingly
    usersDic = fileUtils.load("users")
    user.balance = int(user.balance) - driversNearUser[chosenDriver][2]
    user.dir = destinationDir
    usersDic[userName] = user
    fileUtils.save("users", usersDic)
    print("El camino hacia destino es: ", shortestPath, "\n")
    print("El viaje ha concluido.\n")

def requestUserInput(user, drivers):
    index = 0
    inputMessage = "\n"
    for driver in drivers:
        if driver[2] <= int(user.balance):
            inputMessage += f"{index+1}. {driver[1]} cobra ${driver[2]} y está a {driver[0]}m de tu ubicación actual.\n"
            index +=1
    inputMessage += "\n¿Con qué conductor te gustaría realizar el viaje?\n"
    inputMessage += "Ingresar a continuación el número de la opción deseada:\n"
    option = int(input(inputMessage))
    while option < 1 or option > len(drivers):
        print("La opción ingresada es incorrecta.\n")
        print("Por favor, vuelva a ingresar la opción deseada a continuación:\n")
        option = input(inputMessage)
    print("Su elección ha sido guardada satisfactoriamente.\n")
    return option-1

def test():
    graph = fileUtils.load("map")
    users = fileUtils.load("users")
    drivers = fileUtils.load("drivers")
    print(vars(graph["3"][0]))