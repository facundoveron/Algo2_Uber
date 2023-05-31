from ownLibraries import graphUtils
import fileUtils

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
    # params = <AX, {<e1, 10>, <e2, 5>}>
    # params = <PX, {<e1, 10>, <e2, 5>}, saldo>
    # params = <CX, {<e1, 10>, <e2, 5>}, tarifa>
    parts = params.strip("<>\n").split(", ")
    name = parts[0]
    dir = parts[1].strip("{}").split(", ")
    # todo: add dir validation
    if name[0] == "P":
        balance = parts[2]
        dic = fileUtils.load("users")
        dic[name] = User(dir, balance)
        fileUtils.save("users", dic)
        print("User succesfully saved")
    elif name[0] == "C":
        rate = parts[2]
        dic = fileUtils.load("drivers")
        dic[name] = Driver(dir, rate)
        fileUtils.save("drivers", dic)
        print("Driver succesfully saved")
    else:
        dic = fileUtils.load("fixed")
        dic[name] = Elem(dir)
        fileUtils.save("fixed", dic)
        print("Fixed location succesfully saved")

def createTrip(params):
    # params = PX <dirección>/<elemento>
    print("")