import sys
import serviceUber

def main(command):
    try:
        if "-create_map" == command[0]:
            serviceUber.createMap(command[1])
            print("map created successfully")
        elif "-load_fix_element" == command[0]:
            serviceUber.loadFixElement(command[1])
        elif "-load_movil_element" == command[0]:
            serviceUber.loadMovilElement(command[1])
        elif "-create_trip" == command[0]:
            serviceUber.createTrip(command[1])
    except:
        print("Error de sistema o parametros")

command = sys.argv[1:]
main(command)