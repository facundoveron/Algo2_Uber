from ownLibraries import graphUtils
import fileUtils

def createMap(route):
    try:
        coordinates = open(route)
        if coordinates != None:
            vertices = coordinates.readline()
            edges = coordinates.readline()
            coordinates.close()
            graph = graphUtils.createGraph(vertices, edges)
            fileUtils.saveMap(graph)
            fileUtils.openMap()
        else:
            print("El archivo está vacío")
    except:
        print("Error al crear el mapa")

def loadFixElement(route):
    print("God")

def loadMobileElement(route):
    print("God")

def createTrip(route):
    print("God")