import utils
import repository

def createMap(route):
    try:
        coordinates = open(route)
        if coordinates != None:
            vertices = coordinates.readline()
            edges = coordinates.readline()
            coordinates.close()
            graph = utils.createGraph(vertices, edges)
            repository.saveMaps(graph)
            repository.openGraph()
        else:
            print("El archivo se encuentra el Null")
    except:
        print("Error al crear el mapa")


def loadFixElement(route):
    print("God")

def loadMovilElement(route):
    print("God")

def createTrip(route):
    print("God")