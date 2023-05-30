import sys
import uberService
import fileUtils

def main(command):
    try:
        if "-create_map" == command[0]:
            uberService.createMap(command[1])
            print("map created successfully")
        elif "-load_fix_element" == command[0]:
            uberService.loadFixedElement(command[1])
        elif "-load_movil_element" == command[0]:
            uberService.loadMobileElement(command[1])
        elif "-create_trip" == command[0]:
            uberService.createTrip(command[1])
        # Sólo para testeo
        elif "-setupFiles" == command[0]:
            fileUtils.setupFiles()
        elif "-printFixedElems" == command[0]:
            print(fileUtils.loadFixedElems()["A1"].dir)
        elif "-printMobileElems" == command[0]:
            print(fileUtils.loadMobileElems()["P1"].amount)
    except Exception as a:
        print("Error", a.args)

command = sys.argv[1:]
main(command)
#uberService.createMap("resources/map.txt")
#uberService.loadFixedElement("<H0, {<e1, 100>, <e2, 1>}>")