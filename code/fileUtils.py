import pickle

routes = {
    "map": "resources/map",
    "fixed": "resources/fixed",
    "users": "resources/users",
    "drivers": "resources/drivers"
}

def setupDicts():
    dictionary = {}
    with open(routes["fixed"], "bw") as file:
        pickle.dump(dictionary, file)
    with open(routes["users"], "bw") as file:
        pickle.dump(dictionary, file)
    with open(routes["drivers"], "bw") as file:
        pickle.dump(dictionary, file)

def save(type, obj):
    with open(routes[type], "bw") as file:
        pickle.dump(obj, file)
def load(type):
    with open(routes[type], "br") as file:
        return pickle.load(file)    