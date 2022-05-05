"""
Dieses File wird gestartet wenn an der Kasto die Geschwindigkeit verstellt wird, um die
Bandgeschwindigkeit direkt in m/min in der Konsole auszugeben
"""

from helpers.functions import OPCConnection
from helpers.lists import names, names_without_sig_raw_fft_hk


class SubHandlerLicht(object):
    """
    Subscription Handler. To receive events from server for a subscription
    This class is just a sample class. Whatever class having these methods can be used

    Diese ist da um die Lichtshrankenfrequenz im Terminal auszudrucken und zu checken, welche werte kommen.
    die Einstellung mit dem Stellrad an der Säge ist nicht mehr exakt nach dem beheben des Gewindedefekts.
    steht sie auf 90 vor dem defekt - war die F 161-164
    nachher hat sie nun:
    """

    def datachange_notification(self, node, val, data):
        """
        called for every datachange notification from server
        """

        print(node,  'Hz:', val, ' m/min:', val * 60 * 2.54 / (100 * 3.5))


    def event_notification(self, event):
        """
        called for every event notification from server
        """
        print('event_notification data:', event)

    def status_change_notification(self, status):
        """
        called for every status change notification from server
        """
        print('status_change_notification data:', status)

def lets_go_licht():
    opc = OPCConnection()
    client = opc.connect_client()

    all_nodes = [client.get_node(x) for x in names]
    nodes_without_sigs = [client.get_node(x) for x in names_without_sig_raw_fft_hk]
    licht_node = client.get_node(names[8])

    handler_licht = SubHandlerLicht()

    milliseconds_data = 5

    sub_licht = client.create_subscription(milliseconds_data, handler_licht)
    handle_licht = sub_licht.subscribe_data_change(licht_node)
    return sub_licht, handle_licht

def stop_licht():
    sub_licht.unsubscribe(handle_licht)


if __name__ == "__main__":

    sub_licht, handle_licht = lets_go_licht()

    #  stop_licht()


