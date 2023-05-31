import sys
import uberService
import fileUtils

def main(command):
    try:
        if command[0] == "-create_map":
            uberService.setup(command[1])
        elif command[0] in ("-load_fix_element", "-load_movil_element"):
            uberService.saveElem(command[1])
        elif command[0] == "-create_trip":
            uberService.createTrip(command[1])
    except Exception as a:
        print("Error", a.args)

command = sys.argv[1:]
main(command)
#uberService.createMap("resources/map.txt")
#uberService.loadFixedElement("<H0, {<e1, 100>, <e2, 1>}>")