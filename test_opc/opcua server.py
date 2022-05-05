from opcua import Server
import random
from time import sleep
from IPython import embed

server = Server()
url = 'opc.tcp://127.0.0.1:12345'
server.set_endpoint(url)
name = 'Room1'
namespace = server.register_namespace(name)
# why did it print out 2? everytime?
objects = server.get_objects_node()
tempsens = objects.add_object('ns=2;s="TS1"', 'Temperature Sensor 1')
name = tempsens.add_variable('ns=2;s="TS1_VendorName"', 'TS1 Vendor Name', "Sensor King")
serial = tempsens.add_variable('ns=2;s="TS1_SerialNumber"', 'TS1 Serial Number', 12345678)
temp = tempsens.add_variable('ns=2;s="TS1_Temperature"', 'TS1 Temperature', 20)

# 2 is the number of the namespace
# namespace, browsename
bulb = objects.add_object(2, "Light Bulb")
# bulb
# creates a numerical node id

state = bulb.add_variable(2, "State of Light Bulb", False)
state.set_writable()  # writeable from the client side
name.set_writable()
serial_number = 0
temperature = 20
try:
    print("Start Server")
    server.start()
    print("Server online")

    counter = 0
    while True:
        counter += 1
        #sel = int(input('Please make a selection\n'))
        #if sel == 99:
        #    break
        #elif sel == 88:
        #    print('this')
        #else:
        if counter % 5 == 0:
            if name.get_value() == 'lets_go':
                name.set_value('Sensor_King')
                print(name.get_value())
            else:
                name.set_value('lets_go')
                print(name.get_value())

        temperature += random.uniform(0, 2)
        serial_number += 1
        serial.set_value(serial_number)
        #temp.set_value(temperature)
        print("new Temp: " + str(temp.get_value()),"new serial: " + str(serial.get_value()))

        #print("State of Light Bulb" + str(state.get_value()))
        sleep(1)

finally:
    server.stop()
    print("server offline")
    print('!')
