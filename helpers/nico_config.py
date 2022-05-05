from opcua import ua, Client

from helpers.functions import OPCConnection, Logger, IdCollector

import time
from numpy import genfromtxt
import re
import matplotlib.pyplot as plt
#from opcua.tools import SubHandler
from opcua import ua
from datetime import datetime





if __name__ == "__main__":

    #url = "opc.tcp://192.168.125.186:48012"
    url = "opc.tcp://192.168.125.52: 4840"

    client = Client(url)
    client.connect()

    #  Preperations:
    col = IdCollector()



    #Global_PV_nodes = col.get_process_variables_nico(client)[1:] # der erste eintrag hat kein s=
    Global_PV_nodes = col.get_Global_PV_nodes(client)

    names = col.flatten_list()

    identifiers = [x.nodeid.Identifier for x in Global_PV_nodes]
    #create_header(client)
    #langsames schreiben
    #log_lines_via_get_node(2)
    #visualize_raw_and_HK_data([42, 51, 57], names)
    #single variable
    #var = client.get_node(names[50])

    #value = client.get_node(node_ids[14]).get_data_value().Value.Value


#und da dann eine config erzeugen für den telegraf die so aussieht:
##{name="bCutActive", namespace="6", identifier_type="s", identifier="::AsGlobalPV:bCutActive"},
#{name="CPU_Kuehler_Temp", namespace="6", identifier_type="s", identifier="::AsGlobalPV:CPU_Kuehler_Temp"},
"""
nodes = [
{name="DMC_Ruestzeit", namespace="5", identifier_type="s", identifier="DMC_Ruestzeit"},
{name="TriggerFraese", namespace="5", identifier_type="s", identifier="TriggerFraese"},
{name="DMC_Zykluszeit", namespace="5", identifier_type="s", identifier="DMC_Zykluszeit"},
{name="Saege_Zykluszeit", namespace="5", identifier_type="s", identifier="Saege_Zykluszeit"},
{name="Kaercher_Zykluszeit", namespace="5", identifier_type="s", identifier="Kaercher_Zykluszeit"},
{name="DMC_Energieverbrauch", namespace="5", identifier_type="s", identifier="DMC_Energieverbrauch"},
{name="Saege_Barcodescanner", namespace="5", identifier_type="s", identifier="Saege_Barcodescanner"},
{name="DMC_Startzeit_Auftrag", namespace="5", identifier_type="s", identifier="DMC_Startzeit_Auftrag"},
{name="DMC_Stueckzaehler_Tag", namespace="5", identifier_type="s", identifier="DMC_Stueckzaehler_Tag"},
{name="DMC_Stueckzaehler_Jahr", namespace="5", identifier_type="s", identifier="DMC_Stueckzaehler_Jahr"},
{name="DMC_Zykluszeit_Auftrag", namespace="5", identifier_type="s", identifier="DMC_Zykluszeit_Auftrag"},
{name="Saege_Energieverbrauch", namespace="5", identifier_type="s", identifier="Saege_Energieverbrauch"},
{name="DMC_Stueckzaehler_Monat", namespace="5", identifier_type="s", identifier="DMC_Stueckzaehler_Monat"},
{name="Saege_Startzeit_Auftrag", namespace="5", identifier_type="s", identifier="Saege_Startzeit_Auftrag"},
{name="Kaercher_Energieverbrauch", namespace="5", identifier_type="s", identifier="Kaercher_Energieverbrauch"},
{name="DMC_Ruestzeit_Durchschnitt", namespace="5", identifier_type="s", identifier="DMC_Ruestzeit_Durchschnitt"},
{name="DMC_Zykluszeit_Durchscnitt", namespace="5", identifier_type="s", identifier="DMC_Zykluszeit_Durchscnitt"},
{name="Kaercher_Startzeit_Auftrag", namespace="5", identifier_type="s", identifier="Kaercher_Startzeit_Auftrag"},
{name="Saege_Bauteilkennzeichnung", namespace="5", identifier_type="s", identifier="Saege_Bauteilkennzeichnung"},
{name="DMC_Bauteilkennzeichnung_D25", namespace="5", identifier_type="s", identifier="DMC_Bauteilkennzeichnung_D25"},
{name="DMC_Bauteilkennzeichnung_D40", namespace="5", identifier_type="s", identifier="DMC_Bauteilkennzeichnung_D40"},
{name="DMC_Energieverbrauch_Auftrag", namespace="5", identifier_type="s", identifier="DMC_Energieverbrauch_Auftrag"},
{name="Montagelinie_AP4_Montagezeit", namespace="5", identifier_type="s", identifier="Montagelinie_AP4_Montagezeit"},
{name="Montagelinie_AP5_Montagezeit", namespace="5", identifier_type="s", identifier="Montagelinie_AP5_Montagezeit"},
{name="Saege_Stueckzaehler_Gutteile", namespace="5", identifier_type="s", identifier="Saege_Stueckzaehler_Gutteile"},
{name="Kaercher_Bauteilkennzeichnung", namespace="5", identifier_type="s", identifier="Kaercher_Bauteilkennzeichnung"},
{name="Montagelinie_Energieverbrauch", namespace="5", identifier_type="s", identifier="Montagelinie_Energieverbrauch"},
{name="Saege_Energieverbrauch_Auftrag", namespace="5", identifier_type="s", identifier="Saege_Energieverbrauch_Auftrag"},
{name="DMC_Bauteilkennzeichnung_Auftrag", namespace="5", identifier_type="s", identifier="DMC_Bauteilkennzeichnung_Auftrag"},
{name="Messstation_Bauteilkennzeichnung", namespace="5", identifier_type="s", identifier="Messstation_Bauteilkennzeichnung"},
{name="Montagelinie_AP1_Montagezeit_D25", namespace="5", identifier_type="s", identifier="Montagelinie_AP1_Montagezeit_D25"},
{name="Montagelinie_AP1_Montagezeit_D40", namespace="5", identifier_type="s", identifier="Montagelinie_AP1_Montagezeit_D40"},
{name="Montagelinie_AP2_Montagezeit_D25", namespace="5", identifier_type="s", identifier="Montagelinie_AP2_Montagezeit_D25"},
{name="Montagelinie_AP2_Montagezeit_D40", namespace="5", identifier_type="s", identifier="Montagelinie_AP2_Montagezeit_D40"},
{name="Montagelinie_AP3_Montagezeit_D25", namespace="5", identifier_type="s", identifier="Montagelinie_AP3_Montagezeit_D25"},
{name="Montagelinie_AP3_Montagezeit_D40", namespace="5", identifier_type="s", identifier="Montagelinie_AP3_Montagezeit_D40"},
{name="Kaercher_Energieverbrauch_Auftrag", namespace="5", identifier_type="s", identifier="Kaercher_Energieverbrauch_Auftrag"},
{name="Saege_K_Prozessdaten_Leistung_Watt", namespace="5", identifier_type="s", identifier="Saege_K_Prozessdaten_Leistung_Watt"},
{name="DMC_ProzessIntMess_RauheitBodenD40_1", namespace="5", identifier_type="s", identifier="DMC_ProzessIntMess_RauheitBodenD40_1"},
{name="DMC_ProzessIntMess_RauheitBodenD40_2", namespace="5", identifier_type="s", identifier="DMC_ProzessIntMess_RauheitBodenD40_2"},
{name="DMC_ProzessIntMess_RauheitBodenD40_3", namespace="5", identifier_type="s", identifier="DMC_ProzessIntMess_RauheitBodenD40_3"},
{name="DMC_ProzessIntMess_RauheitBodenD40_4", namespace="5", identifier_type="s", identifier="DMC_ProzessIntMess_RauheitBodenD40_4"},
{name="LaseBox_K_Prozessdaten_Leistung_Watt", namespace="5", identifier_type="s", identifier="LaseBox_K_Prozessdaten_Leistung_Watt"},
{name="Waschen_K_Prozessdaten_Leistung_Watt", namespace="5", identifier_type="s", identifier="Waschen_K_Prozessdaten_Leistung_Watt"},
{name="HaasST10_K_Prozessdaten_Leistung_Watt", namespace="5", identifier_type="s", identifier="HaasST10_K_Prozessdaten_Leistung_Watt"},
{name="HaasST10_PS_Prozessdaten_Trigger_Bool", namespace="5", identifier_type="s", identifier="HaasST10_PS_Prozessdaten_Trigger_Bool"},
{name="Saege_Waage_Stueckzaehler_TeileGesamt", namespace="5", identifier_type="s", identifier="Saege_Waage_Stueckzaehler_TeileGesamt"},
{name="Emco_K_Prozessdaten_Stueckzaehler_Bool", namespace="5", identifier_type="s", identifier="Emco_K_Prozessdaten_Stueckzaehler_Bool"},
{name="HaasMill2_K_Prozessdaten_Leistung_Watt", namespace="5", identifier_type="s", identifier="HaasMill2_K_Prozessdaten_Leistung_Watt"},
{name="HaasMill2_PS_Prozessdaten_Trigger_Bool", namespace="5", identifier_type="s", identifier="HaasMill2_PS_Prozessdaten_Trigger_Bool"},
{name="DMC_K_Prozessdaten_Trigger_Saege_on_Bool", namespace="5", identifier_type="s", identifier="DMC_K_Prozessdaten_Trigger_Saege_on_Bool"},
{name="Saege_K_Prozessdaten_Luftverbrauch_Liter", namespace="5", identifier_type="s", identifier="Saege_K_Prozessdaten_Luftverbrauch_Liter"},
{name="Saege_Waage_Stueckzaehler_Ausschussteile", namespace="5", identifier_type="s", identifier="Saege_Waage_Stueckzaehler_Ausschussteile"},
{name="Saege_Waage_Teilegewicht_TeilegewichtGut", namespace="5", identifier_type="s", identifier="Saege_Waage_Teilegewicht_TeilegewichtGut"},
{name="Saege_K_Prozessdaten_Energieverbrauch_Watt", namespace="5", identifier_type="s", identifier="Saege_K_Prozessdaten_Energieverbrauch_Watt"},
{name="Saege_Waage_Teilegewicht_TeilegewichtGesamt", namespace="5", identifier_type="s", identifier="Saege_Waage_Teilegewicht_TeilegewichtGesamt"},
{name="LaseBox_K_Prozessdaten_Energieverbrauch_Watt", namespace="5", identifier_type="s", identifier="LaseBox_K_Prozessdaten_Energieverbrauch_Watt"},
{name="Waschen_K_Prozessdaten_Energieverbrauch_Watt", namespace="5", identifier_type="s", identifier="Waschen_K_Prozessdaten_Energieverbrauch_Watt"},
{name="HaasST10_K_Prozessdaten_Energieverbrauch_Watt", namespace="5", identifier_type="s", identifier="HaasST10_K_Prozessdaten_Energieverbrauch_Watt"},
{name="DMC_K_Prozessdaten_Trigger_Automatikmodus_Bool", namespace="5", identifier_type="s", identifier="DMC_K_Prozessdaten_Trigger_Automatikmodus_Bool"},
{name="HaasMill2_K_Prozessdaten_Energieverbrauch_Watt", namespace="5", identifier_type="s", identifier="HaasMill2_K_Prozessdaten_Energieverbrauch_Watt"},
{name="Saege_K_Prozessdaten_Saege_Schnittzaehler_DINT", namespace="5", identifier_type="s", identifier="Saege_K_Prozessdaten_Saege_Schnittzaehler_DINT"},
{name="Messstation_Digmar_Qualitaetskontrolle_Nuttiefe", namespace="5", identifier_type="s", identifier="Messstation_Digmar_Qualitaetskontrolle_Nuttiefe"},
{name="HaasST10_K_Prozessdaten_Druckluftverbrauch_Liter", namespace="5", identifier_type="s", identifier="HaasST10_K_Prozessdaten_Druckluftverbrauch_Liter"},
{name="Saege_PS_Prozessdaten_Saege_Anheben_Trigger_Bool", namespace="5", identifier_type="s", identifier="Saege_PS_Prozessdaten_Saege_Anheben_Trigger_Bool"},
{name="HaasMill2_K_Prozessdaten_Druckluftverbrauch_Liter", namespace="5", identifier_type="s", identifier="HaasMill2_K_Prozessdaten_Druckluftverbrauch_Liter"},
{name="DMC_K_Prozessdaten_Trigger_Saege_Saegeblatt_on_Bool", namespace="5", identifier_type="s", identifier="DMC_K_Prozessdaten_Trigger_Saege_Saegeblatt_on_Bool"},
{name="DMC_K_Prozessdaten_Trigger_Bearbeitungsprogramm_Bool", namespace="5", identifier_type="s", identifier="DMC_K_Prozessdaten_Trigger_Bearbeitungsprogramm_Bool"},
{name="DMC_Spindel_OelBehaelter_Materialspeicher_Fuellstand", namespace="5", identifier_type="s", identifier="DMC_Spindel_OelBehaelter_Materialspeicher_Fuellstand"},
{name="Messstation_Messuhr2_Qualitaetskontrolle_Durchmesser", namespace="5", identifier_type="s", identifier="Messstation_Messuhr2_Qualitaetskontrolle_Durchmesser"},
{name="Emco_K_Prozessdaten_Trigger_Bearbeitungsprogramm_Bool", namespace="5", identifier_type="s", identifier="Emco_K_Prozessdaten_Trigger_Bearbeitungsprogramm_Bool"},
{name="DMC_Bettbahn_FettBehaelter_Materialspeicher_Fuellstand", namespace="5", identifier_type="s", identifier="DMC_Bettbahn_FettBehaelter_Materialspeicher_Fuellstand"},
{name="Messstation_Messuhr1_Qualitaetskontrolle_Parallelitaet", namespace="5", identifier_type="s", identifier="Messstation_Messuhr1_Qualitaetskontrolle_Parallelitaet"},
{name="Saege_K_Prozessdaten_Saege_Schnittzaehler_Arepron_DINT", namespace="5", identifier_type="s", identifier="Saege_K_Prozessdaten_Saege_Schnittzaehler_Arepron_DINT"},
{name="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_1_Bool", namespace="5", identifier_type="s", identifier="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_1_Bool"},
{name="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_2_Bool", namespace="5", identifier_type="s", identifier="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_2_Bool"},
{name="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_3_Bool", namespace="5", identifier_type="s", identifier="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_3_Bool"},
{name="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_4_Bool", namespace="5", identifier_type="s", identifier="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_4_Bool"},
{name="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_5_Bool", namespace="5", identifier_type="s", identifier="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_5_Bool"},
{name="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_6_Bool", namespace="5", identifier_type="s", identifier="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_6_Bool"},
{name="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_7_Bool", namespace="5", identifier_type="s", identifier="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_7_Bool"},
{name="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_8_Bool", namespace="5", identifier_type="s", identifier="Montagelinie_K_Prozessdaten_Junbiki_Trigger_Sensor_8_Bool"},
{name="DMC_KSSVersorgung_KSSBehaelter_Materialspeicher_Fuellstand", namespace="5", identifier_type="s", identifier="DMC_KSSVersorgung_KSSBehaelter_Materialspeicher_Fuellstand"},
{name="DMC_KSSVersorgung_SpanBehaelter_Materialspeicher_Fuellstand", namespace="5", identifier_type="s", identifier="DMC_KSSVersorgung_SpanBehaelter_Materialspeicher_Fuellstand"},
{name="DMC_Werkzeug_Werkzeugwechsler_Werkzeugwechsel_Triggersignal", namespace="5", identifier_type="s", identifier="DMC_Werkzeug_Werkzeugwechsler_Werkzeugwechsel_Triggersigna"}]

"""