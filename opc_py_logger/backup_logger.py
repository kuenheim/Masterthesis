from opcua import ua, Client
from datetime import datetime
import os
import csv
from helpers import node_ids_without_fftraw_ffthk_sigrawtime, node_ids, ids, Logger
import time




class SubHandlerData(object):
    """
    Subscription Handler. To receive events from server for a subscription
    This class is just a sample class. Whatever class having these methods can be used
    """

    def datachange_notification(self, node, val, data):
        """
        called for every datachange notification from server
        """
        logger_subscribed_data.write_line([data.monitored_item.Value.SourceTimestamp,
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

    url = "opc.tcp://192.168.125.52:4840"
    client = Client(url)
    client.connect()

    # subscription intervall
    milliseconds_intervall = 100

    all_nodes = [client.get_node(x) for x in node_ids]
    nodes_without_fftraw_ffthk_sigrawtime = [client.get_node(x) for x in node_ids_without_fftraw_ffthk_sigrawtime]

    # save data at
    folder = 'data'

    # TODO: choose beginning of your csv filename
    csv_name_start = 'choose a name' + '_'

    # create a csv
    logger_subscribed_data = Logger()
    logger_event_status = Logger()
    logger_subscribed_data.create_csv(folder, csv_name_start)
    logger_event_status.create_csv(folder, csv_name_start)

    # the handler receives the change notifications and saves each one to a line in csv
    # instanciate:
    handler_data = SubHandlerData()

    # now the subscription is created
    sub_data = client.create_subscription(milliseconds_intervall, handler_data)

    # ab dieser Zeile kommen Werte im Subhandler and
    #handle_data = sub_data.subscribe_data_change(nodes_without_fftraw_ffthk_sigrawtime)

    # zu Beginn werden immer alle Werte einmal abgerufen, danach nur noch die, die sich ändern


    # um sig_raw anzufordern, muss in der SPS der Wert FFT_Anforderung auf True,
    # wird von SPS nach jeder Übertragung wieder auf False gesetzt. ist der
    # Wert auf True, beginnt eine neue Aufzeichnung usw
    data_value_form_die_die_sps_versteht = ua.DataValue(ua.Variant(True, ua.VariantType.Boolean))
    sig_raw_anforderung_interval_seconds = 0.3


    # TODO kennst du evtl. einen besseren weg, alle paar sekunden etwas anzufordern als mit while True und sleep?
    """
    while True:
        # warten wir ein bisschen
        time.sleep(sig_raw_anforderung_interval_seconds)

        # all_nodes[5] ist die node von FFT_Anforderung
        all_nodes[5].set_value(data_value_form_die_die_sps_versteht)
        # print('angefordert')
    """

    # mit unsubscribe kannst du den unermüdlichen Datenstrom unterbrechen - manchmal geht es nicht, weis noch nicht warum,
    # vor allem wenn mehrere Subscriptions laufen.
    # dann einfach den ganzen Prozess killen. Strg+C geht auch nicht immer, erst recht wenn mehrere Subhandler
    # gleichzeitig laufen

    # -->   sub_data.unsubscribe(handle_data)


    # oder einzeln, sieh in node_ids nach welchen wet du nimmst

    value = client.get_node(node_ids[14]).get_data_value().Value.Value




