#import os
#os.chdir('C:\\Users\\Kuni\\PycharmProjects\\Übung')

from helpers.functions import OPCConnection, Logger, IdCollector
from helpers.lists import names, names_without_sig_raw_fft_hk
import time
from numpy import genfromtxt
import re
import matplotlib.pyplot as plt
#from opcua.tools import SubHandler
from opcua import ua
from datetime import datetime


def set_cut_counter_zero(to_number):
    dv = ua.DataValue(ua.Variant(to_number, ua.VariantType.UInt16))
    client.get_node(names[3]).set_value(dv)

def set_obereMaterialkante(to_number):
    dv = ua.DataValue(ua.Variant(to_number, ua.VariantType.Float))
    client.get_node(names[12]).set_value(dv)


class SubHandlerCutCounter(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        """
        called for every datachange notification from server
        """

        global cut_counter
        cut_counter = val

        print(node, val)

    def event_notification(self, event):
        """
        called for every event notification from server
        """
        print('event_notification of CutCounter:', event, 'type: ', type(event))

    def status_change_notification(self, status):
        """
        called for every status change notification from server
        """
        print('status_change_notification of CutCounter:', status, 'type: ', type(status))


class SubHandlerSigRaw(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        """
        called for every datachange notification from server
        """

        logger_sig_raw.write_line([data.monitored_item.Value.SourceTimestamp,
                                   datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                           data.monitored_item.Value.StatusCode.name,
                           node.nodeid.Identifier[13:],
                           val])
        # add datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


    def event_notification(self, event):
        """
        called for every event notification from server
        """
        print('event_notification sig_raw:', event)
        #logger_sig_raw.write_line([datetime.now().strftime("%d-%m-%Y_%H-%M-%S"), 'time=received_time', 'event_change', event])
        logger_event_status.write_line([datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                                    'time= received_time', 'event_change_sigraw', event])

    def status_change_notification(self, status):
        """
        called for every status change notification from server
        """
        print('status_change_notification sig_raw:', status)
        #logger_sig_raw.write_line([datetime.now().strftime("%d-%m-%Y_%H-%M-%S"), 'time=received_time', 'status_change', status])
        logger_event_status.write_line([datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                                    'times= received_time', 'event_change_sigraw', status])


class SubHandlerData(object):
    """
    Subscription Handler. To receive events from server for a subscription
    This class is just a sample class. Whatever class having these methods can be used
    """

    def datachange_notification(self, node, val, data):
        """
        called for every datachange notification from server
        """
        logger_all_data.write_line([data.monitored_item.Value.SourceTimestamp,
                                    datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                           data.monitored_item.Value.StatusCode.name,
                           node.nodeid.Identifier[13:],
                           val])


    def event_notification(self, event):
        """
        called for every event notification from server
        """
        print('event_notification data:', event)
        logger_event_status.write_line([datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), 'time=received_time', 'event_change_data', event])

    def status_change_notification(self, status):
        """
        called for every status change notification from server
        """
        print('status_change_notification data:', status)
        logger_event_status.write_line([datetime.now().strftime("%d-%m-%Y_%H-%M-%S"), 'time=received_time', 'status_change_data', status])


if __name__ == "__main__":
    opc = OPCConnection()
    client = opc.connect_client()

    #  Preperations:
    # col = IdCollector()
    # Global_PV_nodes = col.get_Global_PV_nodes(client)
    # names = col.flatten_list()
    # create_header(client)
    # langsames schreiben
    # log_lines_via_get_node(2)
    # visualize_raw_and_HK_data([42, 51, 57], names)
    # single variable
    # var = client.get_node(names[50])

    all_nodes = [client.get_node(x) for x in names]
    nodes_without_sigs = [client.get_node(x) for x in names_without_sig_raw_fft_hk]
    sig_node_list = [client.get_node(names[x]) for x in range(33, 38)]

    handler_data = SubHandlerData()
    handler_sig_raw = SubHandlerSigRaw()

    milliseconds_data = 5

    sub_data = client.create_subscription(milliseconds_data, handler_data)
    sub_raw = client.create_subscription(milliseconds_data, handler_sig_raw)

    #handle_licht = sub_raw.subscribe_data_change(sig_node_list)
    #material = 'Stahl-60'
    #set_obereMaterialkante(60)# Todo select Material

    a000 = """
    material = 'keinMaterial'
    vorschub = '0'
    bandgeschwindigkeit = '0'
    set_obereMaterialkante(60)# Todo select Material
    # """
    # Todo select Material
    #a699 = """
    material = 'Alu-60'
    set_obereMaterialkante(60)# Todo select Material
    vorschub = '90'
    bandgeschwindigkeit = '90'
    # """
    # Todo select Material
    a499 = """
    material = 'Alu-40'
    vorschub = '90'
    bandgeschwindigkeit = '90'
    set_obereMaterialkante(40)
    #"""
    # Todo select Material
    a479 = """
    material = 'Alu-40'
    vorschub = '90'
    bandgeschwindigkeit = '75'
    set_obereMaterialkante(40)# Todo select Material
    #"""
    # Todo select Material
    ast = """
    material = 'Stein'
    set_obereMaterialkante(120)# Todo select Material
    vorschub = '5'
    bandgeschwindigkeit = '75'
    #"""
    # TODO
    # Todo fit filenamepart_1 Klasse  (1,2,3,4,5)
    filenamestart = 'Schluss_neuesBandEinlauf_' + str(material) + '_Vors-' + str(vorschub) + '_Bandv-' + str(bandgeschwindigkeit) + '_' + str(milliseconds_data) + '-ms_' + '_'
    #filenamestart = 'Test_alu_100m-min_vorschub_10_' + material + '_' + str(milliseconds_data) + '-ms_' + '_'

    #Klasse_1
    # TODO select path (Trainingsband, Testband)
    csv_path = 'data/Trainingsband/5'


    # TODO 1. material/quer/v/ob
    #      2. klasse filename
    #      3. path


    logger_all_data = Logger()
    logger_sig_raw = Logger()
    logger_event_status = Logger()
    logger_all_data.create_csv(filenamestart, '_data', csv_path, with_header=False)
    logger_sig_raw.create_csv(filenamestart, '_SigRaw', csv_path, with_header=False)
    logger_event_status.create_csv(filenamestart, '_event_status', csv_path, with_header=False)

    handle_data = sub_data.subscribe_data_change(nodes_without_sigs)
    handle_raw = sub_raw.subscribe_data_change(sig_node_list)

    # fft anfordern
    dv = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))
    sig_raw_anforderung_seconds = 0.3

    while True:
        time.sleep(sig_raw_anforderung_seconds)
        client.get_node(names[5]).set_value(dv)




"""


    sub_data.unsubscribe(handle_data)
    
    sub_raw.unsubscribe(handle_raw)

    sub_cut_counter.unsubscribe(handle_cuts)






 # für nico in influxdata
    #for i in names:
    #    print('{name = "' + i[0][20:] + '", namespace = "6", identifier_type = "s", identifier = "' + i[7:] +'"},')

    sub_data.unsubscribe(handle_data)
    while True:
        if cut_active:
            logger = Logger()
            csv_name_start = 'testing_profil_' + str(milliseconds_data) + '-ms_' + str(cut_counter) + '-cutcounter'
            logger.create_csv(csv_name_start, with_header=False)
            print('csv created')
            handle_data = sub_data.subscribe_data_change(all_nodes)
            while cut_active: # müsste genauso gehen wenn ich es rauslasse, oder?
                pass

        elif not cut_active:
            try:
                sub_data.unsubscribe(handle_data)
                print('unsubscribed')
            except:
                pass
"""

    #sub_on_off.unsubscribe(handle_on_off)
    #sub_data.unsubscribe(handle_data)

# todo zeiten sind nicht sortiert!

"""
# print terminal ausgabe
import sys
sys.stdout = open('testing\\file30_10min.csv', 'w')
time.sleep(600)
#close after if

sys.stdout.close()
# back to normal:
sys.stdout = sys.__stdout__
print('done')


"""

# TODO set value of node
#  so hat es nicht geklappt:
#  opcua.ua.uaerrors._auto.BadWriteNotSupported: "The server does not support writing the combination of value,
#  status and timestamps provided."(BadWriteNotSupported)
"""
#works:
dv = ua.DataValue(ua.Variant(1300, ua.VariantType.UInt16), ua.StatusCode(1))
dv.SourceTimestamp = datetime.now()
# deosnt:
all_nodes[3].set_data_value()
all_nodes[3].set_value(dv)

#  maybe with uawrite?
#  no documentation...
#  https://github.com/FreeOpcUa/python-opcua/blob/master/opcua/tools.py#L234
"""

#change_value_of_cut_counter
#dv = ua.DataValue(ua.Variant(11389, ua.VariantType.UInt16))

#client.get_node(names[3]).set_value(dv)


# change FS-Modes {'Rohsignal', 'FFT Rohsignal', 'FFT Hüllkurve'};
"""
from opcua import ua
dv = ua.DataValue(ua.Variant(1, ua.VariantType.Int16))
client.get_node(names[9]).set_value(dv)

# fft anfordern
dv = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))
client.get_node(names[5]).set_value(dv)
"""
