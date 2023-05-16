import pickle

def saveMaps(graph):
    try:
        with open("../resources/newMap", "bw") as maps:
            pickle.dump(graph, maps)
    except Exception as a:
        print("Error al guardar el mapa", a.args)


def openGraph():
    try:
        with open("../resources/newMap", "br") as maps:
            f = pickle.load(maps)
            for i in f:
                print(i.head.value)

    except Exception as a:
        print("Error al guardar el mapa", a.args)