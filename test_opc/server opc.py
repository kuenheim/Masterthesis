from opcua import Server
from random import randint
import datetime
import time

server = Server()

#url = "opt.tcp://127.0.0.1:4840"   # this works!!  https://stackoverflow.com/questions/23857942/winerror-10049-the-requested-address-is-not-valid-in-its-context
#url = "opt.tcp://192.168.0.8:4840"
url = "opt.tcp://127.0.0.1:12345"
server.set_endpoint(url)

name = "OPCUA_SIM_SERVER"
addspace = server.register_namespace(name)

# Rootnode
node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Press", 0)
Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()


server.start()
print("server started at" + str(url))

while True:
    Temperature = randint(10, 50)
    Pressure = randint(200, 999)
    TIME = datetime.datetime.now()

    print(Temperature, Pressure, TIME)
    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(0.1)


