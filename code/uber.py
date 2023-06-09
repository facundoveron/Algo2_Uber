import sys
import uberService
import traceback

def main(command):
    try:
        if command[0] == "-create_map":
            uberService.setup(command[1])
        elif command[0] in ("-load_fix_element", "-load_movil_element"):
            uberService.saveElem(command[1:])
        elif command[0] == "-create_trip":
            uberService.createTrip(command[1:])
        elif command[0] == "-test":
            uberService.test()
    except:
        traceback.print_exc()

command = sys.argv[1:]
main(command)
#uberService.setup("resources/map.txt")
#uberService.createTrip("P2 H1")