from opcua import Client
from opcua import ua
import random
import time

url = "opc.tcp://127.0.0.1:12345"
global onoffsignal
onoffsignal = None
client = Client(url)
client.connect()
root = client.get_root_node()

available_namespaces = client.get_namespace_array()
objects = client.get_objects_node()
children_of_node = objects.get_children()




class SubHandler_onoff(object):
    """
    Subscription Handler. To receive events from server for a subscription
    This class is just a sample class. Whatever class having these methods can be used
    """

    def datachange_notification(self, val, node):
        """
        called for every datachange notification from server
        """
        print('signal changed!', val)
        global onoffsignal
        if val == 'lets_go':
            onoffsignal = True
        else:
            onoffsignal = False

        #print(val)


    def event_notification(self, event):
        """
        called for every event notification from server
        """
        print('event_notification:', event)

    def status_change_notification(self, status):
        """
        called for every status change notification from server
        """
        print('status_change_notification:', status, ' type: ', type(status))



class SubHandler_data(object):
    """
    Subscription Handler. To receive events from server for a subscription
    This class is just a sample class. Whatever class having these methods can be used
    """

    def datachange_notification(self, node, val, data):
        """
        called for every datachange notification from server
        """
        print(node, val)


    def event_notification(self, event):
        """
        called for every event notification from server
        """
        print('event_notification:', event)

    def status_change_notification(self, status):
        """
        called for every status change notification from server
        """
        print('status_change_notification:', status, ' type: ', type(status))



nodes_ids = ['ns=2;s="TS1"',
'ns=2;s="TS1_VendorName"',
'ns=2;s="TS1_SerialNumber"',
'ns=2;s="TS1_Temperature"']



handler_data = SubHandler_data()
handler_onoff = SubHandler_onoff

milliseconds = 30
sub_on = client.create_subscription(milliseconds, handler_onoff)
sub_data = client.create_subscription(milliseconds, handler_data)


# Cutactive subscription
nodes = [client.get_node(x) for x in nodes_ids]



handle_onoff = sub_on.subscribe_data_change(nodes[1])

while True:
    if onoffsignal:
        handle_data = sub_data.subscribe_data_change(nodes[-2:])
        while onoffsignal:
            pass

    elif not onoffsignal:
        try:
            sub_data.unsubscribe(handle_data)
        except:
            pass
