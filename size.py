import os


sig1a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__13-58-30_28-02-2022_SigRaw.csv']
sig1a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__16-21-47_28-02-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__11-10-27_01-03-2022_SigRaw.csv']
sig2a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-01-59_01-03-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__16-49-50_01-03-2022_SigRaw.csv']
sig2a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__12-57-39_01-03-2022_SigRaw.csv']
sig3a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_SigRaw.csv']
sig3a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__15-30-29_19-03-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__17-35-40_19-03-2022_SigRaw.csv',
]
sig4a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-10-19_21-03-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__14-45-28_21-03-2022_SigRaw.csv']
sig4a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-58-22_31-03-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__16-48-04_31-03-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-24-51_31-03-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-36-01_01-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__09-13-12_01-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__12-18-38_01-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-21-33_01-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__15-12-05_01-04-2022_SigRaw.csv',]
sig5a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__10-57-16_02-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__14-30-07_02-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-09-48_05-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-13-10_05-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__11-41-57_07-04-2022_SigRaw.csv']
sig5a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__14-24-55_07-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-28-33_08-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-43-54_08-04-2022_SigRaw.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__12-34-31_08-04-2022_SigRaw.csv']


tsig1a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__12-55-50_26-02-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__12-37-20_26-02-2022_SigRaw.csv']
tsig1a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__12-16-37_26-02-2022_SigRaw.csv']
tsig2a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__14-01-38_26-02-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__13-46-22_26-02-2022_SigRaw.csv']
tsig2a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__13-26-13_26-02-2022_SigRaw.csv']
tsig3a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__15-07-14_26-02-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__14-52-59_26-02-2022_SigRaw.csv']
tsig3a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__14-33-45_26-02-2022_SigRaw.csv']
tsig4a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-01-04_28-02-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__10-37-23_28-02-2022_SigRaw.csv']
tsig4a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__10-08-36_28-02-2022_SigRaw.csv']
tsig5a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__12-38-29_28-02-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__12-17-52_28-02-2022_SigRaw.csv']
tsig5a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__11-45-02_28-02-2022_SigRaw.csv']



all_paths = [sig1a6, sig1a4, sig2a4, sig2a6, sig3a6, sig3a4, sig4a4, sig4a6, sig5a4, sig5a6, tsig1a4, tsig1a6,tsig2a4, tsig2a6,tsig3a4,   tsig3a6,tsig4a4,     tsig4a6,tsig5a4,     tsig5a6]
sizes = []
for i in all_paths:
    for j in i:
        #print(j)
        sizes.append(int(os.path.getsize(j)/(1000 ** 2)))





col = 3
fig, axs = plt.subplots(3,1, figsize=(19,10), sharey=True, sharex=True)
plt.suptitle(ids[new_ids[col-1]])
for i, j in enumerate(ends):
    if i == 0:
        row = 0
    else:
        row = ends[i-1]
    axs[0].scatter(range(row, j[0]), arr_6[row:j[0], col], label='a6', color=colors[i])
    axs[0].legend()
    axs[1].scatter(range(row, j[1]), arr_47[row:j[1], col], label='a47', color=colors[i])
    axs[1].legend()
    axs[2].scatter(range(row, j[2]), arr_49[row:j[2], col], label='a49', color=colors[i])
    axs[2].legend()