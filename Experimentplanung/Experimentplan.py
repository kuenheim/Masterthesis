import numpy as np
import matplotlib.pyplot as plt
from ast import literal_eval
import pandas as pd

mylist = [1, 2, 3, 4, 5, 6]
result = np.prod(np.array(mylist))

# domains
count_vorschubgeschwindigkeiten = 1
count_materialien = 3
count_querschnette = 1
count_klassen = 5  # TODO how many? 27 mit 1x steinsägen sind zu kleine abstände, 1/100mm pro klasse

count_schnitte_pro_Klasse = 150  # TODO how may are needed to get a good result? erstmal ausprobieren with small pre_datasatz?
count_testscnitte = 20
schnittdicke_mm = 9
aufschlag_zerspanung_mm = 1.5

count_steinschnitt_pro_klasse = 1
count_messvorgaenge_pro_klassee = 1
count_bandwechsel = 1
dauer_bandwechsel = 600

faktor_verschleiss_zeit = 1  #  durch Puffer abgedeckt
faktor_messhaeufigkeit = 0.5  # TODO wie oft messen? nach jeder zweiten domain?

dauer_alu_60 = 50 # a6
dauer_edelstahl_60 = 35 # a4
dauer_alu_30 = 35

dauer_schnitt_Metall_mean = (dauer_alu_60 + dauer_edelstahl_60 + dauer_alu_30) / 3  # TODO UPDATE test. Prozessdauer in Thesis angegeben mit 20 Sekunden
dauer_einstellung_vorschub = 10
dauer_materialwechsel = 120
dauer_counter = 20
dauer_steinschnitt = 90  # TODO evlt unnötig, das genug gesägt wird um Band zu verschleissen!
dauer_messung = 600

puffer = 1.1

domains = count_vorschubgeschwindigkeiten * count_materialien * count_querschnette
schnittzeit = count_klassen * (domains * count_schnitte_pro_Klasse * dauer_schnitt_Metall_mean * faktor_verschleiss_zeit)
steinzeit = count_klassen * (dauer_steinschnitt * count_steinschnitt_pro_klasse)
handhabungszeit = count_klassen * (dauer_materialwechsel * count_materialien * count_querschnette)
einstellzeit = count_klassen * domains * (dauer_einstellung_vorschub + dauer_counter)
bandwechselzeit = count_bandwechsel * dauer_bandwechsel
messzeit = count_klassen * domains * dauer_messung * faktor_messhaeufigkeit

daten_pro_domain = count_klassen * count_schnitte_pro_Klasse
dauer_domain_mean = np.round(daten_pro_domain * dauer_schnitt_Metall_mean / 3600, 1)
domaindauer_alu_40 = np.round(daten_pro_domain * dauer_alu_30 / 3600, 1)
domaindauer_alu_60 = np.round(daten_pro_domain * dauer_alu_60 / 3600, 1)
domaindauer_st_60 = np.round(daten_pro_domain * dauer_edelstahl_60 / 3600, 1)

anzahl_schnitte = domains * daten_pro_domain
schnittdauer_pro_klasse = np.round(count_schnitte_pro_Klasse * dauer_schnitt_Metall_mean / 3600, 1)
material_laenge_m = anzahl_schnitte * (schnittdicke_mm + aufschlag_zerspanung_mm) / 1000

sekunden = (schnittzeit + steinzeit + handhabungszeit + einstellzeit + bandwechselzeit + messzeit) * puffer
stunden = sekunden / 3600

h_day_10 = int(stunden / 10)
h_day_08 = int(stunden / 8)
h_day_06 = int(stunden / 6)
h_day_04 = int(stunden / 4)



def gesamtzeit_h(list_in):
    return np.round(np.sum(list_in) / 3600, 1)


parts_long = [steinzeit, handhabungszeit, einstellzeit, bandwechselzeit, messzeit, schnittzeit]
longlist = [x * puffer for x in parts_long]
longlist_h = [x / 3600 for x in longlist]
longlist_percent = [x / np.sum(longlist) for x in longlist]
long_labels = ['Steinzeit', 'Handhabungszeit', 'Einstellzeit', 'Bandwechselzeit', 'Messzeit', 'Schnittzeit']

parts_short = parts_long[:-1]
shortlist = [x * puffer for x in parts_short]
shortlist_h = [x / 3600 for x in shortlist]
shortlist_percent = [x / np.sum(shortlist) for x in shortlist]
short_labels = long_labels[:-1]


def vis():
    fontsize = 15

    plt.figure(figsize=(12, 8))
    plt.bar(long_labels, longlist_h, color='red')
    plt.ylabel('studen', fontsize=fontsize)
    #plt.ylabel('%', fontsize=fontsize)
    plt.xlabel('gesamtzeit h : {:.1f}'.format(gesamtzeit_h(longlist)), fontsize=fontsize)
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.bar(short_labels, shortlist_h, color='orange')
    #plt.ylabel('%', fontsize=fontsize)
    plt.ylabel('studen', fontsize=fontsize)
    plt.xlabel('gesamtzeit h : {:.1f}'.format(gesamtzeit_h(shortlist)), fontsize=fontsize)
    plt.show()
#vis()

print('\n')
print('Material 7 Schnitt mm:   ', schnittdicke_mm + aufschlag_zerspanung_mm, '  in:    ', dauer_schnitt_Metall_mean, '  s')
print('Domains:                  ', domains)
print('Klassen:                 ', count_klassen)
print('Schnitte pro Klasse mean  :    ', count_schnitte_pro_Klasse, '    in:     ', schnittdauer_pro_klasse, 'h')
print('Schnitte pro Domain Alu 60:   ', daten_pro_domain, '    min.:  ', domaindauer_alu_60, 'h')
print('Schnitte pro Domain Alu 40:   ', daten_pro_domain, '    min.:  ', domaindauer_alu_40, 'h')
print('Schnitte pro Domain Stahl :   ', daten_pro_domain, '    min.:  ', domaindauer_st_60, 'h')


schnittdauer_pro_klasse_a6 = np.round(count_schnitte_pro_Klasse * dauer_alu_60 / 3600, 1)
schnittdauer_pro_klasse_a4 = np.round(count_schnitte_pro_Klasse * dauer_alu_30 / 3600, 1)
schnittdauer_pro_klasse_s6 = np.round(count_schnitte_pro_Klasse * dauer_edelstahl_60 / 3600, 1)

print('Schnitte Alu 60 pro Klasse:   ', count_schnitte_pro_Klasse, '    min.:  ', schnittdauer_pro_klasse_a6, 'h')
print('Schnitte Alu 40 pro Klasse:   ', count_schnitte_pro_Klasse, '    min.:  ', schnittdauer_pro_klasse_a4, 'h')
print('Schnitte Stahl  pro Klasse:   ', count_schnitte_pro_Klasse, '    min.:  ', schnittdauer_pro_klasse_s6, 'h')

print('Dauer pro Klasse          :   ', schnittdauer_pro_klasse_a6 + schnittdauer_pro_klasse_a4 + schnittdauer_pro_klasse_s6)
print('Gesamtzahl Schnitte:  ', anzahl_schnitte, '    in:   ', gesamtzeit_h(longlist), 'h')

print('Gesamtlänge Material:   ', material_laenge_m, 'm')
print('\n')
print('h/d    7/7      5/7    4/7')
print('10:   ', h_day_10, '     ', int(h_day_10*7/5), '   ', int(h_day_10*7/4))
print('08:   ', h_day_08, '     ', int(h_day_08*7/5), '   ', int(h_day_08*7/4))
print('06:   ', h_day_06, '     ', int(h_day_06*7/5), '   ', int(h_day_06*7/4))
print('04:   ', h_day_04, '     ', int(h_day_04*7/5), '   ', int(h_day_04*7/4))



header = ['Klasse', 'Anzahl', 'Aktivität', '\'Material\'', 'Durchmesser [mm]', 'Einzeldauer [s]', 'Dauer [min]', 'Dauer [h]']
ablauf = np.full((89, len(header)), 'X', dtype=np.dtype('U30')) # set string lenght to eg 25
k0 = 'Einlauf'
k1 = 'Neu'
kk = 'Nullpunkt'

s0 = 'Verschlissene Sägebänder'
s00 = 'Neues Sägeband'
s1 = 'Eingelaufenes Trainingsband'
s11 = 'Eingelaufenes Testband'
s2 = 'Trainingsband'
s22 = 'Testsband'

M = 'Messen'
S = 'Schnitt'
W = 'Band wechseln'

se = 'Stein'
a = 'Aluminium'
sa = 'Edelstahl'

row = 0
ablauf[row, :] = [kk, '1', M, s0, '26.8', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
row += 1
ablauf[row, :] = [k1, '1', W, s00, '-', dauer_bandwechsel, int(dauer_bandwechsel / 60), np.round(dauer_bandwechsel / 3600, 1)]
row += 1
ablauf[row, :] = [k1, '1', M, s00, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
row += 1
ablauf[row, :] = [k0, '10', S, a, '60', dauer_alu_60, 10 * int(dauer_alu_60 / 60), 10 * np.round(dauer_alu_60 / 3600, 1)]
row += 1
ablauf[row, :] = [k0, '1', M, s1, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
row += 1

for i in range(5):
    ablauf[row, :] = [1 + i, count_schnitte_pro_Klasse, S, a, '30', dauer_alu_30, int(dauer_alu_30 * count_schnitte_pro_Klasse / 60), np.round(dauer_alu_30 * count_schnitte_pro_Klasse / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', M, s2, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, count_schnitte_pro_Klasse, S, a, '60', dauer_alu_60, int(dauer_alu_60 * count_schnitte_pro_Klasse / 60), np.round(dauer_alu_60 * count_schnitte_pro_Klasse / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', M, s2, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, count_schnitte_pro_Klasse, S, sa, '60', dauer_edelstahl_60, int(dauer_edelstahl_60 * count_schnitte_pro_Klasse / 60), np.round(dauer_edelstahl_60 * count_schnitte_pro_Klasse / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', M, s2, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', S, se, '-> tbd', dauer_steinschnitt, int(dauer_steinschnitt / 60), np.round(dauer_steinschnitt / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', M, s2, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
    row += 1

ablauf[row, :] = [k1, '1', M, s00, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
row += 1
ablauf[row, :] = [k1, '1', W, s00, '-', dauer_bandwechsel, int(dauer_bandwechsel / 60), np.round(dauer_bandwechsel / 3600, 1)]
row += 1
ablauf[row, :] = [k0, '10', S, a, '60', dauer_alu_60, 10 * int(dauer_alu_60 / 60), 10 * np.round(dauer_alu_60 / 3600, 1)]
row += 1
ablauf[row, :] = [k0, '1', M, s11, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
row += 1

for i in range(5):
    ablauf[row, :] = [1 + i, count_testscnitte, S, a, '30', dauer_alu_30, int(dauer_alu_30 * count_testscnitte / 60), np.round(dauer_alu_30 * count_testscnitte / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', M, s2, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, count_testscnitte, S, a, '60', dauer_alu_60, int(dauer_alu_60 * count_testscnitte / 60), np.round(dauer_alu_60 * count_testscnitte / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', M, s2, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, count_testscnitte, S, sa, '60', dauer_edelstahl_60, int(dauer_edelstahl_60 * count_testscnitte / 60), np.round(dauer_edelstahl_60 * count_testscnitte / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', M, s22, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', S, se, '-> tbd', dauer_steinschnitt, int(dauer_steinschnitt / 60), np.round(dauer_steinschnitt / 3600, 1)]
    row += 1
    ablauf[row, :] = [1 + i, '1', M, s22, '-> todo', dauer_messung, int(dauer_messung / 60), np.round(dauer_messung / 3600, 1)]
    row += 1




aa = pd.DataFrame(data=ablauf, columns=header)
aa.to_csv('ablauf_testband.csv', index=False)

training_dur = ablauf[0:33, 6].astype(float).sum()
test_dur = ablauf[33:, 6].astype(float).sum()
print('Duration Training: ', int(training_dur), 'min, ', int(training_dur / 60), 'h')
print('Duration Test: ', int(test_dur),  'min, ',int(test_dur / 60), 'h')
print('Sum: ', int(training_dur + test_dur),  'min, ', int((training_dur + test_dur)/ 60), 'h')

"""
Band Messen
Band einlaufen lassen
Band messen
Klasse 1: x Schnitte
Band Messen
Stein
Band Messen
"""

Messdauer_in_Stunden = aa.loc[aa['Aktivität'] == 'Messen'].shape[0] * dauer_messung / 60
