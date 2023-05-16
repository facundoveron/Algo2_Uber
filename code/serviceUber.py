
def createMap(route):
    try:
        coordinates = open(route)
        if coordinates != None:
            vertices = coordinates.readline()
            edges = coordinates.readline()
            coordinates.close()
        else:
            print("El archivo se encuentra el Null")
    except:
        print("error")


def loadFixElement(route):
    print("God")

def loadMovilElement(route):
    print("God")

def createTrip(route):
    print("God")