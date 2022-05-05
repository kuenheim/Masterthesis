from helpers.functions import dfs_for_timetest_csv, sort_per_id, sort_per_id_vib
from helpers.lists import ids, val_id_type_dict, paths, short_labels, rel_ids
import helpers.lists as lists
import matplotlib.pyplot as plt
import numpy as np
import vis
import pandas as pd
import os
import pickle
from scipy.signal import find_peaks


def concat_dfs_sep_ids(pahts, sig=False):
    """
    load all data in pathlist
    concatenate
    then sort ALL per id
    :param pahts:
    :return: list of dataframes, one per sensor
    """
    data = [dfs_for_timetest_csv(x) for x in pahts]
    data = pd.concat(data)
    if sig:
        temp = sort_per_id_vib(data)
    else:
        temp = sort_per_id(data)
    return temp


def add_feature_seeds(data):
    if len(data) == 0:
        pass
    try:
        roll_big = 20
        roll_small = 5

        # rolling means
        data['roll'] = data['val'].rolling(roll_big).mean()
        data['roll333'] = data['val'].rolling(roll_small).mean()
        data['roll333'] = data['roll333'].rolling(roll_small).mean()
        data['roll333'] = data['roll333'].rolling(roll_small).mean()
        data['roll333'] = data['roll333'].rolling(roll_small).mean()
        data['std'] = data['val'].rolling(roll_big).std()

        # ableitung
        data['slope'] = pd.Series(np.gradient(data['roll']), data['roll'].index, name='slope')
        data['slope2'] = pd.Series(np.gradient(data['roll333']), data['roll333'].index, name='slope2')
        print('features added')
    except ValueError:
        print('ValueError')
    return data
"""
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
#-------------------------

k1a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__13-58-30_28-02-2022_data.csv']
k1a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__16-21-47_28-02-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__11-10-27_01-03-2022_data.csv']
k2a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-01-59_01-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__16-49-50_01-03-2022_data.csv']
k2a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__12-57-39_01-03-2022_data.csv']
k3a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_data.csv']
k3a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__15-30-29_19-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__17-35-40_19-03-2022_data.csv',
]
k4a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-10-19_21-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__14-45-28_21-03-2022_data.csv']
k4a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-58-22_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__16-48-04_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-24-51_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-36-01_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__09-13-12_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__12-18-38_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-21-33_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__15-12-05_01-04-2022_data.csv',]
k5a4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__10-57-16_02-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__14-30-07_02-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-09-48_05-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-13-10_05-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__11-41-57_07-04-2022_data.csv']
k5a6 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__14-24-55_07-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-28-33_08-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-43-54_08-04-2022_data     Lücke in sig.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__12-34-31_08-04-2022_data.csv']

tk1a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__12-55-50_26-02-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__12-37-20_26-02-2022_data.csv']
tk1a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__12-16-37_26-02-2022_data.csv']
tk2a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__14-01-38_26-02-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__13-46-22_26-02-2022_data.csv']
tk2a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__13-26-13_26-02-2022_data.csv']
tk3a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__15-07-14_26-02-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__14-52-59_26-02-2022_data.csv']
tk3a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__14-33-45_26-02-2022_data.csv']
tk4a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-01-04_28-02-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__10-37-23_28-02-2022_data.csv']
tk4a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__10-08-36_28-02-2022_data.csv']
tk5a4 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__12-38-29_28-02-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__12-17-52_28-02-2022_data.csv']
tk5a6 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__11-45-02_28-02-2022_data.csv']
"""



#-----------------------------
# data paths     -    sensoren
#-----------------------------
k1a6  = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__13-58-30_28-02-2022_data.csv']
k1a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__16-21-47_28-02-2022_data.csv']
k1a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__11-10-27_01-03-2022_data.csv']

k2a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-01-59_01-03-2022_data.csv']
k2a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__16-49-50_01-03-2022_data.csv']
k2a6 =  ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__12-57-39_01-03-2022_data.csv']

k3a6 =  [      'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_data.csv']
k3a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__15-30-29_19-03-2022_data.csv']
k3a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__17-35-40_19-03-2022_data.csv']

k4a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-10-19_21-03-2022_data.csv']
k4a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__14-45-28_21-03-2022_data.csv']
k4a6 =  ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-58-22_31-03-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__16-48-04_31-03-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-24-51_31-03-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-36-01_01-04-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__09-13-12_01-04-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__12-18-38_01-04-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-21-33_01-04-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__15-12-05_01-04-2022_data.csv']

k5a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__10-57-16_02-04-2022_data.csv']
k5a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__14-30-07_02-04-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-09-48_05-04-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-13-10_05-04-2022_data.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__11-41-57_07-04-2022_data.csv']

k5a6 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__14-24-55_07-04-2022_data.csv',
        'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-28-33_08-04-2022_data.csv',
        'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-43-54_08-04-2022_data     Lücke in sig.csv',
        'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__12-34-31_08-04-2022_data.csv']

# TODO check als sigraw
tk1a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__12-55-50_26-02-2022_data.csv']
tk1a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__12-37-20_26-02-2022_data.csv']
tk1a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__12-16-37_26-02-2022_data.csv']

tk2a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__14-01-38_26-02-2022_data.csv']
tk2a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__13-46-22_26-02-2022_data.csv']
tk2a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__13-26-13_26-02-2022_data.csv']

tk3a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__15-07-14_26-02-2022_data.csv']
tk3a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__14-52-59_26-02-2022_data.csv']
tk3a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__14-33-45_26-02-2022_data.csv']

tk4a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-01-04_28-02-2022_data.csv']
tk4a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__10-37-23_28-02-2022_data.csv']
tk4a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__10-08-36_28-02-2022_data.csv']

tk5a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__12-38-29_28-02-2022_data.csv']
tk5a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__12-17-52_28-02-2022_data.csv']
tk5a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__11-45-02_28-02-2022_data.csv']


#-----------------------------
# data paths     -    SIG RAW
#-----------------------------
sig1a6  = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__13-58-30_28-02-2022_SigRaw.csv']
sig1a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__16-21-47_28-02-2022_SigRaw.csv']
sig1a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__11-10-27_01-03-2022_SigRaw.csv']

sig2a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-01-59_01-03-2022_SigRaw.csv']
sig2a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__16-49-50_01-03-2022_SigRaw.csv']
sig2a6 =  ['E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__12-57-39_01-03-2022_SigRaw.csv']

sig3a6 =  [      'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_SigRaw.csv',
        'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_SigRaw.csv']
sig3a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__15-30-29_19-03-2022_SigRaw.csv']
sig3a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__17-35-40_19-03-2022_SigRaw.csv']

sig4a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-10-19_21-03-2022_SigRaw.csv']
sig4a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__14-45-28_21-03-2022_SigRaw.csv']
sig4a6 =  ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-58-22_31-03-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__16-48-04_31-03-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-24-51_31-03-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-36-01_01-04-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__09-13-12_01-04-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__12-18-38_01-04-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-21-33_01-04-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__15-12-05_01-04-2022_SigRaw.csv']


sig5a47 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__10-57-16_02-04-2022_SigRaw.csv']
sig5a49 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__14-30-07_02-04-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-09-48_05-04-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-13-10_05-04-2022_SigRaw.csv',
         'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__11-41-57_07-04-2022_SigRaw.csv']

sig5a6 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__14-24-55_07-04-2022_SigRaw.csv',
        'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-28-33_08-04-2022_SigRaw.csv',
        'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-43-54_08-04-2022_SigRaw.csv',
        'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__12-34-31_08-04-2022_SigRaw.csv']


# TODO check als sigraw
tsig1a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__12-55-50_26-02-2022_SigRaw.csv']
tsig1a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__12-37-20_26-02-2022_SigRaw.csv']
tsig1a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__12-16-37_26-02-2022_SigRaw.csv']

tsig2a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__14-01-38_26-02-2022_SigRaw.csv']
tsig2a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__13-46-22_26-02-2022_SigRaw.csv']
tsig2a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__13-26-13_26-02-2022_SigRaw.csv']

tsig3a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__15-07-14_26-02-2022_SigRaw.csv']
tsig3a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__14-52-59_26-02-2022_SigRaw.csv']
tsig3a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__14-33-45_26-02-2022_SigRaw.csv']

tsig4a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-01-04_28-02-2022_SigRaw.csv']
tsig4a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__10-37-23_28-02-2022_SigRaw.csv']
tsig4a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__10-08-36_28-02-2022_SigRaw.csv']

tsig5a47 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__12-38-29_28-02-2022_SigRaw.csv']
tsig5a49 = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__12-17-52_28-02-2022_SigRaw.csv']
tsig5a6  = ['E:\\ausgelagert thesis daten\\Testband\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__11-45-02_28-02-2022_SigRaw.csv']


pahts_sigs = [sig1a6, sig2a6, sig3a6, sig4a6, sig5a6, sig1a47, sig2a47, sig3a47, sig4a47, sig5a47, sig1a49, sig2a49, sig3a49, sig4a49, sig5a49]
tpahts_sigs = [tsig1a6, tsig2a6, tsig3a6, tsig4a6, tsig5a6, tsig1a47, tsig2a47, tsig3a47, tsig4a47, tsig5a47, tsig1a49, tsig2a49, tsig3a49, tsig4a49, tsig5a49]
pahts_data = [k1a6 , k2a6 , k3a6 , k4a6 , k5a6 , k1a47, k2a47, k3a47, k4a47, k5a47, k1a49, k2a49, k3a49, k4a49, k5a49]
tpahts_data = [tk1a6 , tk2a6 , tk3a6 , tk4a6 , tk5a6 , tk1a47, tk2a47, tk3a47, tk4a47, tk5a47, tk1a49, tk2a49, tk3a49, tk4a49, tk5a49]

short_class1 = """
k1a6_id = concat_dfs_sep_ids(k1a6)
k1a4_id = concat_dfs_sep_ids(k1a4)
k1a6_id[13] = add_feature_seeds(k1a6_id[13])
k1a4_id[13] = add_feature_seeds(k1a4_id[13])
cutactive_true1a6, cutactive_false1a6 = vis.get_bCutActives(k1a6_id)
cutactive_true1a4, cutactive_false1a4 = vis.get_bCutActives(k1a4_id)
"""


#"""


load_precut_class_data_47_49_69 = """
k1a6_id = concat_dfs_sep_ids( k1a6 );print('1a6')
k2a6_id = concat_dfs_sep_ids( k2a6 );print('2a6')
k3a6_id = concat_dfs_sep_ids( k3a6 );print('3a6')
k4a6_id = concat_dfs_sep_ids( k4a6 );print('4a6')
k5a6_id = concat_dfs_sep_ids( k5a6 );print('5a6')
k1a47_id = concat_dfs_sep_ids(k1a47);print('1a47')
k2a47_id = concat_dfs_sep_ids(k2a47);print('2a47')
k3a47_id = concat_dfs_sep_ids(k3a47);print('3a47')
k4a47_id = concat_dfs_sep_ids(k4a47);print('4a47')
k5a47_id = concat_dfs_sep_ids(k5a47);print('5a47')
k1a49_id = concat_dfs_sep_ids(k1a49);print('1a49')
k2a49_id = concat_dfs_sep_ids(k2a49);print('2a49')
k3a49_id = concat_dfs_sep_ids(k3a49);print('3a49')
k4a49_id = concat_dfs_sep_ids(k4a49);print('4a49')
k5a49_id = concat_dfs_sep_ids(k5a49);print('5a49')

#[k1a6_id , k2a6_id , k3a6_id , k4a6_id , k5a6_id , k1a47_id, k2a47_id, k3a47_id, k4a47_id, k5a47_id, k1a49_id, k2a49_id,
# k3a49_id, k4a49_id, k5a49_id] = [concat_dfs_sep_ids(x) for x in pahts_data]
#k_id = [concat_dfs_sep_ids(x) for x in pahts_data]

#tk1a6_id = concat_dfs_sep_ids(tk1a6);print('tk1a6')
#tk2a6_id = concat_dfs_sep_ids(tk2a6);print('tk2a6')
#tk3a6_id = concat_dfs_sep_ids(tk3a6);print('tk3a6')
#tk4a6_id = concat_dfs_sep_ids(tk4a6);print('tk4a6')
#tk5a6_id = concat_dfs_sep_ids(tk5a6);print('tk5a6')
#tk1a47_id = concat_dfs_sep_ids(tk1a47);print('tk1a47')
#tk2a47_id = concat_dfs_sep_ids(tk2a47);print('tk2a47')
#tk3a47_id = concat_dfs_sep_ids(tk3a47);print('tk3a47')
#tk4a47_id = concat_dfs_sep_ids(tk4a47);print('tk4a47')
#tk5a47_id = concat_dfs_sep_ids(tk5a47);print('tk5a47')
#tk1a49_id = concat_dfs_sep_ids(tk1a49);print('tk1a49')
#tk2a49_id = concat_dfs_sep_ids(tk2a49);print('tk2a49')
#tk3a49_id = concat_dfs_sep_ids(tk3a49);print('tk3a49')
#tk4a49_id = concat_dfs_sep_ids(tk4a49);print('tk4a49')
#tk5a49_id = concat_dfs_sep_ids(tk5a49);print('tk5a49')
#tk1a6_id , tk2a6_id , tk3a6_id , tk4a6_id , tk5a6_id , tk1a47_id, tk2a47_id, tk3a47_id, tk4a47_id, tk5a47_id,\
#tk1a49_id, tk2a49_id, tk3a49_id, tk4a49_id, tk5a49_id = [concat_dfs_sep_ids(x) for x in tpahts_data]

#tk_id = [concat_dfs_sep_ids(x) for x in tpahts_data]




#"""
def sep_cuts(start, stop, data, index, timecol1, timecol2, sig=False):
     #start = cutactive_true1a6
     #stop = cutactive_false1a6
     #data = sig1a6_id
    # select only values between cuta true false
    assert len(start) == len(stop)
    if sig:
        """Damit das ende der Aufnahme auch innerhalb des Schnittes ist, wird die aufnahmezeit vom Ende abgezogen"""
        #stop['shifted'] = stop['shifted'] - pd.Timedelta(seconds=1.5885576009750366)
        stop = cut_end_substract_sig(stop, 1.5885576009750366)
    active_cut_data = []
    #for i in range(len(ids)):
    cuts_per_id = []
    for j in range(len(start)):
        cuts_per_id.append(data[index][data[index]['source'].between(start.iloc[0 + j, timecol1], stop.iloc[0 + j, timecol2])])
    #active_cut_data.append(cuts_per_id)
    return cuts_per_id

def sep_cuts_all_sensors(start, stop, data, idx=None, timecol1=None, timecol2=None):
    # start = cutactive_true1a6
    # stop = cutactive_false1a6
    # data = k4a6_id

    # select only values between cuta true false
    assert len(start) == len(stop)

    active_cut_data = []
    for index in idx:
        cuts_per_id = []
        for j in range(len(start)):
            cuts_per_id.append((data[index][data[index]['source'].between(start.iloc[0 + j, timecol1], stop.iloc[0 + j, timecol2])])[['source', 'val']])
            #print(data[index]['source'])
        active_cut_data.append(cuts_per_id)
    return active_cut_data



#import json
#with open("test", "w", encoding='utf-8') as fp:
#    json.dump(active_cut_data1, fp, ensure_ascii=False)

def plot_all_cuts_overlapping(data, index, title):
    plt.figure()
    for i, j in enumerate(data[index]):
        plt.plot(j['val'].values)
    plt.title(title)
    plt.xlabel('Messungen')
    plt.ylabel('P_Vorschub')

#plot_all_cuts_overlapping(active_cut_data5, 13)

# TODO mache erst die ganzen roll und slopes, speichere dann erst die cutas und
# TODO später nur relenvante daten????
#  aa = [vis.get_cuts(k1_id, x, 10) for x in vis.important_sensors]

def plot_roll_windows(data, roll_windows, cutactive_true, cutactive_false):
    fig, axs = plt.subplots(3, 1, figsize=(19, 12), sharex=True)
    #fig.suptitle(str(roll_windows))

    #straight line
    axs[1].plot(data['source'], np.full(len(data['source']), 0), 'k')

    #plt.scatter(range(len(data['val'].values)), data['val'].values, s =3)
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
    for col, roll_window in enumerate(roll_windows):
        #data['roll'] = data['val'].rolling(roll_window).mean()
        #data['roll333'] = data['val'].rolling(5).mean()
        #data['roll333'] = data['roll333'].rolling(5).mean()
        #data['roll333'] = data['roll333'].rolling(5).mean()
        #data['roll333'] = data['roll333'].rolling(5).mean()

        #data['std'] = data['val'].rolling(roll_window).std()
        #data['slope'] = pd.Series(np.gradient(data['roll']), data['roll'].index, name='slope')
        #data['slope2'] = pd.Series(np.gradient(data['roll333']), data['roll333'].index, name='slope2')

        axs[0].plot(data['source'], data['roll'], color=colors[col], label='roll 20')
        axs[0].plot(data['source'], data['roll333'], color='r', label='roll 4x5')

        axs[1].plot(data['source'], data['slope'], color=colors[col], label='d/dt r20')
        axs[1].plot(data['source'], data['slope2'], color='r', label='d/dt r4x5')

        axs[2].plot(data['source'], data['roll333'], color='r')
        axs[2].plot(data['source'], data['roll'], color=colors[col], label='roll 20')
        axs[2].plot(data['source'], data['val'], color='k', label='raw')


        #axs[2].plot(data['source'], data['std'], color=colors[col])
    axs[1].scatter(cutactive_true['source'], np.full(len(cutactive_true['source']), 0), c='g', s=35)
    axs[1].scatter(cutactive_false['source'], np.full(len(cutactive_false['source']), 0), c='r', s=35)
    axs[0].scatter(cutactive_true['source'], np.full(len(cutactive_true['source']), 10), c='g', s=35)
    axs[0].scatter(cutactive_false['source'], np.full(len(cutactive_false['source']), 10), c='r', s=35)

#plot_roll_windows(k1a4_id[13], [21, 29], cutactive_true1a4, cutactive_false1a4)
#plot_roll_windows(k2a6_id[13], [21, 29], cutactive_true2a6, cutactive_false2a6)

#plot_roll_windows(data, [10,12,15])

def plot_sensors_and_cutactive(input_data, cutactive_true, cutactive_false, column):
    #input_data = k5_id
    #cutactive_true = cutactive_true5
    #cutactive_false = cutactive_false5

    important_for_clean = [13, 8, 14, 39, 40, 64]
    fig, axs = plt.subplots(len(important_for_clean)-4, 1, figsize=(19, 16), sharex=True)

    for i,j in enumerate(important_for_clean):
        try:
            data = input_data[j]
            #axs[i].scatter(data['source'], data['val'], s=15, color='grey')
            axs[i].plot(data['source'], data['val'], label=lists.short_labels[j])
            axs[i].legend()
            if j == 13 or j == 16:
                axs[i].scatter(cutactive_true['source'], np.full(len(cutactive_true['source']), 10), c='g', s=25)
                axs[i].scatter(cutactive_false['source'], np.full(len(cutactive_false['source']), 10), c='r', s=25)
        except:
            print('agaljzgfjfgf')
            pass
        axs[1].scatter(cutactive_true[column], np.full(len(cutactive_true[column]), 10), c='g', s=25)
        axs[1].scatter(cutactive_false[column], np.full(len(cutactive_false[column]), 10), c='r', s=25)
#plot_sensors_and_cutactive(k2a47_id, cutactive_true2a47, cutactive_false2a47)
#plot_sensors_and_cutactive(k2a49_id, cutactive_true2a49, cutactive_false2a49)


"""
# gets where smaller than 10 sign = k1_a699[13].loc[k1_a699[13]['sign'] <= 10]

# create col where pvorschub changes singn at end of cut
data['sign'] = data['val'] - 10

# # get all indices where the sign changes - sign changes because i substract 10
changing_sings = data.loc[(np.sign(data['sign']).diff().ne(0))]

abc0 = changing_sings[changing_sings['sign'] == 0]
signneg = changing_sings[changing_sings['sign'] < 0]
signpos = changing_sings[changing_sings['sign'] > 0]


list_enddeltas = []
for i in range(len(cutactive_false)):
    list_enddeltas.append((cutactive_false.iloc[i, 0] - signneg.iloc[i, 0]).total_seconds())
plt.figure()
plt.plot(cutactive_false['source'], list_enddeltas)


# TODO wtf was ist mit dem stufigem verlauf wenn die liste sortiert wird?????

## TODO wir könnten auch die maxima minima bestimmen wie in cwru
 # da ja eh nur die bereiche zwischen curatvie interessant sind

Schnittende: von Cutactive False Rückwärts hinzu dem ersten mal wo das vorzeichen der ableitung des roll 29 >0 ist - hier schnittende
Schnittbeginn:

wenn ich ein schmales fenser öfter anwende, dann bekomme ich sinusähnliche verläufe und gehe sicher, dass mein graph die 0 linie nicht sehr oft kreuztz

with open('active_cut_data1.pkl', 'wb') as outp:
    pickle.dump(active_cut_data1, outp, pickle.HIGHEST_PROTOCOL)
with open('active_cut_data2.pkl', 'wb') as outp:
    pickle.dump(active_cut_data2, outp, pickle.HIGHEST_PROTOCOL)
with open('active_cut_data3.pkl', 'wb') as outp:
    pickle.dump(active_cut_data3, outp, pickle.HIGHEST_PROTOCOL)
with open('active_cut_data4.pkl', 'wb') as outp:
    pickle.dump(active_cut_data4, outp, pickle.HIGHEST_PROTOCOL)
with open('active_cut_data5.pkl', 'wb') as outp:
    pickle.dump(active_cut_data5, outp, pickle.HIGHEST_PROTOCOL)

with open('active_cut_data1.pkl', 'rb') as inp:
    active_cut_data1 = pickle.load(inp)
with open('active_cut_data2.pkl', 'rb') as inp:
    active_cut_data2 = pickle.load(inp)
with open('active_cut_data3.pkl', 'rb') as inp:
    active_cut_data3 = pickle.load(inp)
with open('active_cut_data4.pkl', 'rb') as inp:
    active_cut_data4 = pickle.load(inp)
with open('active_cut_data5.pkl', 'rb') as inp:
    active_cut_data5 = pickle.load(inp)
"""
#vis.plot_timedeltas_datachange(cutactive_true1, 0, 'Class 1 true')
#vis.plot_timedeltas_datachange(cutactive_true2, 0, 'Class 2 true')
#vis.plot_timedeltas_datachange(cutactive_true3, 0, 'Class 3 true')
#vis.plot_timedeltas_datachange(cutactive_true4, 0, 'Class 4 true')
#vis.plot_timedeltas_datachange(cutactive_true5, 0, 'Class 5 true')
#vis.plot_timedeltas_datachange(cutactive_false1, 0, 'Class 1 false')
#vis.plot_timedeltas_datachange(cutactive_false2, 0, 'Class 2 false')
#vis.plot_timedeltas_datachange(cutactive_false3, 0, 'Class 3 false')
#vis.plot_timedeltas_datachange(cutactive_false4, 0, 'Class 4 false')
#vis.plot_timedeltas_datachange(cutactive_false5, 0, 'Class 5 false')



#cuta_true = [cutactive_true1, cutactive_true2, cutactive_true3, cutactive_true4, cutactive_true5]
#cuta_false = [cutactive_false1, cutactive_false2, cutactive_false3, cutactive_false4, cutactive_false5]
#cutas =[cuta_true, cuta_false]

# TODO this is only the time between each tures and each falses, better between ture-false
#fig, axs = plt.subplots(5, 2, sharey=True)
#for i, j in enumerate(cutas):
#    print('i: ', i)
#    for k, l in enumerate(j):
#        print('k: ', k)
#        #y = vis.faster_timedetla_datachange(l)
#        x = range(len(y))
#        axs[k, i].scatter(x, y, s=3)
#        axs[k, i].set_ylim(0, 120)

def calc_true_false_timedelta(data):
    #data = k1_id[0]

    trues = []
    falses = []

    current = False
    truefalselist = data['val'].values
    timeslist = data['source'].values
    true_times = []
    false_times = []
    for j in range(data.shape[0]):
        if j % 2 == 0:
            trues.append(truefalselist[j])
            true_times.append(timeslist[j])
        elif j % 2 == 1:
            falses.append(truefalselist[j])
            false_times.append(timeslist[j])
        else:
            print('oopsy false')

    print('sum trues: ' + str(sum(trues)))
    print('sum falses: ' + str(sum(falses)))

    true_false_timedelta = (np.array(false_times) - np.array(true_times))/ np.timedelta64(1, 's')
    return true_false_timedelta

def plot_all_cutactive_truefalse_between_times(all_class_list):
    fig, axs = plt.subplots(5, sharey=True)
    for i, j in enumerate(all_class_list):
        #y = vis.faster_timedetla_datachange(l)
        y = calc_true_false_timedelta(j[0])
        x = range(len(y))
        #x = j[i]['source']
        print(len(x), len(y))
        axs[i].scatter(x, y, s=3)
        axs[i].set_ylim(-5, 120)
        axs[i].set_ylabel('class ' + str(i+1))
    plt.suptitle('cuttimes between cutactive True and False')
#plot_all_cutactive_truefalse_between_times(all_class_list)

def plot_slope_delta(df, title, cutlist):
    # von, bis
    for cut_number in cutlist:
        #cut_number = 0
        #df = active_cut_data1a6

        data = df[0][cut_number]
        changing_sings_of_slope = data.loc[(np.sign(data['slope2']).diff().ne(0))]

        abc0 = changing_sings_of_slope[changing_sings_of_slope['slope2'] == 0]
        signneg = changing_sings_of_slope[changing_sings_of_slope['slope2'] < 0]
        signpos = changing_sings_of_slope[changing_sings_of_slope['slope2'] > 0]

        #parts_between_pos = vis.faster_timedetla_datachange(signpos)
        #parts_between_neg = vis.faster_timedetla_datachange(signneg)


        #aaa = vis.faster_timedetla_datachange(changing_sings_of_slope)
        #plt.figure()
        #plt.scatter(changing_sings_of_slope['source'][1:], aaa)
        #plt.title('timedeltas between sign changes - biggest one shows start')

        from scipy.signal import find_peaks
        peaks, _ = find_peaks(data['slope2'])


        fig, axs = plt.subplots(3, sharex=True)
        plt.suptitle(title + '  cutnumber/index: ' + str(cut_number))
        axs[0].plot(data['source'], data['roll333'])
        axs[0].plot(data['source'], data['val'])
        #axs[0].scatter(cutactive_true1a4['source'], np.full(len(cutactive_true1a4['source']), 10), c='g', s=25)
        #axs[0].scatter(cutactive_false1a4['source'], np.full(len(cutactive_false1a4['source']), 10), c='r', s=25)
        #axs[0].set_ylim(15.6, 18)


        axs[1].plot(data['source'], data['slope2'])
        axs[1].scatter(signneg['source'], np.full(len(signneg['source']), 0), color='r')
        axs[1].scatter(signpos['source'], np.full(len(signpos['source']), 0), color='g')
        #axs[1].plot(data['slope2'].iloc[peaks], 'x')

        axs[2].scatter(changing_sings_of_slope['source'][1:], vis.faster_timedetla_datachange(changing_sings_of_slope))

#plot_slope_delta(active_cut_data1a6, '1a6 raw', [93])

def cut_end_substract(df_cuta_false, seconds):
    df_cuta_false['shifted'] = df_cuta_false['new stop'] - pd.Timedelta(seconds=seconds)
    return df_cuta_false

def cut_end_substract_sig(df_cuta_false, seconds):
    df_cuta_false['shifted'] = df_cuta_false['shifted'] - pd.Timedelta(seconds=seconds)
    return df_cuta_false

def calc_end_time_p_drop(data, last_rows, threshold):
    """
    ende von cut wird erstmal damit festgelegt, dass P_vorschub unter Schwelle sinkt
    danach wird dann je nach Querschnitt eine Zeit abgezogen
    betrachte das letzte viertel - um bei langen daten den anfang zu vermeiden
    dann suche letzten indize der unter 15 ist
    """

    df = data[0]
    p_threshold = 15
    end_times = []
    indices = []
    empty = []
    for h, i in enumerate(df):

        print(h)
        # nimm die letzten last_rows Werte
        i = i.iloc[-last_rows:, :]

        # und nimm den ersten wert (aus den letzen) der unter 15 geht - der moment in den P droppt ist das Ende des schnitts
        #p_dropping = i[i['val'] <= 15].iloc[0, 0]

        # ein wert befor es auf threshold droppt
        if i['val'].min() <= threshold:
            end_time = i[i['source'] < i[i['val'] <= threshold].iloc[0, 0]].iloc[-1, 0]
            end_times.append(end_time)
            indices.append(h)
        else:
            # unterscheidung weil in manchen schnitten die letzten werte zu hoch sind, bzw der p Abfall ert nach cuta false liegt
            print('index ', h, 'was below threshold')
            end_times.append(0)
            empty.append(h)
    return end_times

def update_cut_end_time(df_cuta_true, new_start):
    timelist = []
    cutalist = df_cuta_true['source'].values
    for i, j in enumerate(new_start):
        if j == 0:
            timelist.append(df_cuta_true.iloc[i, 0])
        else:
            timedelta = cutalist[i] - j
            timelist.append(j)

    df_cuta_true['new stop'] = timelist
    return df_cuta_true

def update_cut_begin_time(df_cuta_true, new_start, col_name):
    df_cuta_true[col_name] = new_start
    return df_cuta_true

def calc_start_time_per_max_timedelta(df_already_cut):
    """ the moment where the blade meets the metal happens at the time, the derivative is positive for the longes time
    check, that the slope is above 0
    """
    #cut_number = 0
    #df = active_cut_data1a6
    counter = 0
    dataset_listindex = 0
    df = df_already_cut[dataset_listindex]
    start_times = []
    for h, i in enumerate(df):
        # data of one cut
        #data = df[i]
        changing_sings_of_slope = i.loc[(np.sign(i['slope2']).diff().ne(0))]
        # calc times between nulldurchgänge
        zero_crossings_timedelta = vis.faster_timedetla_datachange(changing_sings_of_slope)
        # index of biggest timedelda
        first_metal_contact_timestamp_index = np.argmax(zero_crossings_timedelta)

        cut_begin = changing_sings_of_slope.iloc[first_metal_contact_timestamp_index + 1, 0]
        start_times.append(cut_begin)

    return start_times

def calc_start_time_per_third_after_max_slope(df_already_cut, cutoff, peak_number, step_two=False):
    """ the moment where the blade meets the metal happens at the time, the derivative is positive for the longes time
    check, that the slope is above 0
    """
    #cut_number = 0
    #df_already_cut = active_cut_data1a4_new

    dataset_listindex = 0
    df = df_already_cut[dataset_listindex]
    start_times = []
    for h, i in enumerate(df):
        # data of one cut
        print(h)
        i = i.iloc[:-cutoff, :]
        #data = df[i]
        changing_sings_of_slope = i.loc[(np.sign(i['slope2']).diff().ne(0))]
        signneg = changing_sings_of_slope[changing_sings_of_slope['slope2'] < 0]
        signpos = changing_sings_of_slope[changing_sings_of_slope['slope2'] > 0]

        # calc times between nulldurchgänge
        #zero_crossings_timedelta = vis.faster_timedetla_datachange(changing_sings_of_slope)
        # index of biggest timedelda
        #first_metal_contact_timestamp_index = np.argmax(zero_crossings_timedelta)

        #cut_begin = changing_sings_of_slope.iloc[first_metal_contact_timestamp_index + 1, 0]
        #
        #when has the slope the max value?

        #data = active_cut_data1a4[0][1]
        peaks, _ = find_peaks(i['slope2'])
        #plt.figure()
        #plt.plot(data['slope2'])
        #plt.plot(data['slope2'].iloc[peaks], 'x')
        #drop all

        # workaround for big maxima at the end of the cut, just look at the first 3/4 or so

        sorted_peaks = i['slope2'].iloc[peaks].sort_values(ascending=False)
        relevant_peak_time_index = sorted_peaks.index[peak_number]
        cut_begin = (signneg[signneg['source'] > i['source'].loc[relevant_peak_time_index]]).iloc[0, 0]
        start_times.append(cut_begin)

        #if step_two == False:
    return start_times
        #else:

def qnd_outlier_indices(data, offset_percent, class_):
    median = np.median(data)
    mean = np.mean(data)
    lower = median * (1 - offset_percent)
    upper = median * (1 + offset_percent)
    #indices = np.where((data > upper) | (data < lower))[0]
    lowindices = np.where((data < lower))[0]
    highindices = np.where((data > upper))[0]
    indices = list(lowindices) + list(highindices)
    print(class_, '(count :', len(data), ')', '\tkicked:', len(indices), '\t low-high: ', '\t(', len(lowindices), '/', len(highindices),')',
          '\trest: ', len(data) - len(indices), ' \t(', np.round(len(indices)/len(data), 2), '%)', '\tmean: ', int(mean), '\tmedian: ', int(median))
    return indices

def qnd_bandpass_per_class(data, index, highpass, lowpass):
    #indices = np.where((data > upper) | (data < lower))[0]
    high_out = []
    low_out = []
    data = data[index]
    for i in range(len(data)):
        if (data[i]['val'] > highpass).any():
            high_out.append(i)
        elif (data[i]['val'] < lowpass).any():
            low_out.append(i)


    indices = list(low_out) + list(high_out)
    print('kicked indices (low_bound-high_bound): ', len(indices), '\t\t(',len(low_out), '/', len(high_out),')', '\t of ',
          len(data), ' \t(', np.round(100 * len(indices)/len(data), 1), '%),\t \trest: ',
          (len(data) - len(indices)))
    return indices

def cut_concat_save_sig(class_, cuta_true, cuta_false, id_data):
    """
    seperate with the brandnew cutactives
    for each of the 3 axis
    keep ID column
    concat 3 axis
    save to file, one per class
    """
    path_final_sig = 'E:\\ausgelagert thesis daten\\final_data\\sigraw'

    dfs = []
    for i in [0, 1, 2]:
        dfs.append(pd.concat(sep_cuts(cuta_true, cuta_false, id_data, i, 0, 0, sig=True)))

    data = pd.concat(dfs)
    data.to_csv(os.path.join(path_final_sig, 'sig' + class_ + '.csv'), index_label='idx')

new_cutactives_and_cut_data = """
k1a6_id[13] = add_feature_seeds(k1a6_id[13])
k2a6_id[13] = add_feature_seeds(k2a6_id[13])
k3a6_id[13] = add_feature_seeds(k3a6_id[13])
k4a6_id[13] = add_feature_seeds(k4a6_id[13])
k5a6_id[13] = add_feature_seeds(k5a6_id[13])
k1a47_id[13] = add_feature_seeds(k1a47_id[13])
k2a47_id[13] = add_feature_seeds(k2a47_id[13])
k3a47_id[13] = add_feature_seeds(k3a47_id[13])
k4a47_id[13] = add_feature_seeds(k4a47_id[13])
k5a47_id[13] = add_feature_seeds(k5a47_id[13])
k1a49_id[13] = add_feature_seeds(k1a49_id[13])
k2a49_id[13] = add_feature_seeds(k2a49_id[13])
k3a49_id[13] = add_feature_seeds(k3a49_id[13])
k4a49_id[13] = add_feature_seeds(k4a49_id[13])
k5a49_id[13] = add_feature_seeds(k5a49_id[13])


tk1a6_id[13] = add_feature_seeds(tk1a6_id[13])
tk2a6_id[13] = add_feature_seeds(tk2a6_id[13])
tk3a6_id[13] = add_feature_seeds(tk3a6_id[13])
tk4a6_id[13] = add_feature_seeds(tk4a6_id[13])
tk5a6_id[13] = add_feature_seeds(tk5a6_id[13])
tk1a47_id[13] = add_feature_seeds(tk1a47_id[13])
tk2a47_id[13] = add_feature_seeds(tk2a47_id[13])
tk3a47_id[13] = add_feature_seeds(tk3a47_id[13])
tk4a47_id[13] = add_feature_seeds(tk4a47_id[13])
tk5a47_id[13] = add_feature_seeds(tk5a47_id[13])
tk1a49_id[13] = add_feature_seeds(tk1a49_id[13])
tk2a49_id[13] = add_feature_seeds(tk2a49_id[13])
tk3a49_id[13] = add_feature_seeds(tk3a49_id[13])
tk4a49_id[13] = add_feature_seeds(tk4a49_id[13])
tk5a49_id[13] = add_feature_seeds(tk5a49_id[13])

# get original cutas
cutactive_true1a6, cutactive_false1a6 = vis.get_bCutActives(k1a6_id)
cutactive_true2a6, cutactive_false2a6 = vis.get_bCutActives(k2a6_id)
cutactive_true3a6, cutactive_false3a6 = vis.get_bCutActives(k3a6_id)
cutactive_true4a6, cutactive_false4a6 = vis.get_bCutActives(k4a6_id)
cutactive_true5a6, cutactive_false5a6 = vis.get_bCutActives(k5a6_id)
cutactive_true1a47, cutactive_false1a47 = vis.get_bCutActives(k1a47_id)
cutactive_true2a47, cutactive_false2a47 = vis.get_bCutActives(k2a47_id)
cutactive_true3a47, cutactive_false3a47 = vis.get_bCutActives(k3a47_id)
cutactive_true4a47, cutactive_false4a47 = vis.get_bCutActives(k4a47_id)
cutactive_true5a47, cutactive_false5a47 = vis.get_bCutActives(k5a47_id)
cutactive_true1a49, cutactive_false1a49 = vis.get_bCutActives(k1a49_id)
cutactive_true2a49, cutactive_false2a49 = vis.get_bCutActives(k2a49_id)
cutactive_true3a49, cutactive_false3a49 = vis.get_bCutActives(k3a49_id)
cutactive_true4a49, cutactive_false4a49 = vis.get_bCutActives(k4a49_id)
cutactive_true5a49, cutactive_false5a49 = vis.get_bCutActives(k5a49_id)


tcutactive_true1a6, tcutactive_false1a6 = vis.get_bCutActives(tk1a6_id)
tcutactive_true2a6, tcutactive_false2a6 = vis.get_bCutActives(tk2a6_id)
tcutactive_true3a6, tcutactive_false3a6 = vis.get_bCutActives(tk3a6_id)
tcutactive_true4a6, tcutactive_false4a6 = vis.get_bCutActives(tk4a6_id)
tcutactive_true5a6, tcutactive_false5a6 = vis.get_bCutActives(tk5a6_id)
tcutactive_true1a47, tcutactive_false1a47 = vis.get_bCutActives(tk1a47_id)
tcutactive_true2a47, tcutactive_false2a47 = vis.get_bCutActives(tk2a47_id)
tcutactive_true3a47, tcutactive_false3a47 = vis.get_bCutActives(tk3a47_id)
tcutactive_true4a47, tcutactive_false4a47 = vis.get_bCutActives(tk4a47_id)
tcutactive_true5a47, tcutactive_false5a47 = vis.get_bCutActives(tk5a47_id)
tcutactive_true1a49, tcutactive_false1a49 = vis.get_bCutActives(tk1a49_id)
tcutactive_true2a49, tcutactive_false2a49 = vis.get_bCutActives(tk2a49_id)
tcutactive_true3a49, tcutactive_false3a49 = vis.get_bCutActives(tk3a49_id)
tcutactive_true4a49, tcutactive_false4a49 = vis.get_bCutActives(tk4a49_id)
tcutactive_true5a49, tcutactive_false5a49 = vis.get_bCutActives(tk5a49_id)

# seperate data with original cutas
active_cut_data1a6 = sep_cuts(cutactive_true1a6, cutactive_false1a6, k1a6_id, 13, 0, 0)
active_cut_data2a6 = sep_cuts(cutactive_true2a6, cutactive_false2a6, k2a6_id, 13, 0, 0)
active_cut_data3a6 = sep_cuts(cutactive_true3a6, cutactive_false3a6, k3a6_id, 13, 0, 0)
active_cut_data4a6 = sep_cuts(cutactive_true4a6, cutactive_false4a6, k4a6_id, 13, 0, 0)
active_cut_data5a6 = sep_cuts(cutactive_true5a6, cutactive_false5a6, k5a6_id, 13, 0, 0)
active_cut_data1a47 = sep_cuts(cutactive_true1a47, cutactive_false1a47, k1a47_id, 13, 0, 0)
active_cut_data2a47 = sep_cuts(cutactive_true2a47, cutactive_false2a47, k2a47_id, 13, 0, 0)
active_cut_data3a47 = sep_cuts(cutactive_true3a47, cutactive_false3a47, k3a47_id, 13, 0, 0)
active_cut_data4a47 = sep_cuts(cutactive_true4a47, cutactive_false4a47, k4a47_id, 13, 0, 0)
active_cut_data5a47 = sep_cuts(cutactive_true5a47, cutactive_false5a47, k5a47_id, 13, 0, 0)
active_cut_data1a49 = sep_cuts(cutactive_true1a49, cutactive_false1a49, k1a49_id, 13, 0, 0)
active_cut_data2a49 = sep_cuts(cutactive_true2a49, cutactive_false2a49, k2a49_id, 13, 0, 0)
active_cut_data3a49 = sep_cuts(cutactive_true3a49, cutactive_false3a49, k3a49_id, 13, 0, 0)
active_cut_data4a49 = sep_cuts(cutactive_true4a49, cutactive_false4a49, k4a49_id, 13, 0, 0)
active_cut_data5a49 = sep_cuts(cutactive_true5a49, cutactive_false5a49, k5a49_id, 13, 0, 0)


tactive_cut_data1a6 = sep_cuts(tcutactive_true1a6, tcutactive_false1a6, tk1a6_id, 13, 0, 0)
tactive_cut_data2a6 = sep_cuts(tcutactive_true2a6, tcutactive_false2a6, tk2a6_id, 13, 0, 0)
tactive_cut_data3a6 = sep_cuts(tcutactive_true3a6, tcutactive_false3a6, tk3a6_id, 13, 0, 0)
tactive_cut_data4a6 = sep_cuts(tcutactive_true4a6, tcutactive_false4a6, tk4a6_id, 13, 0, 0)
tactive_cut_data5a6 = sep_cuts(tcutactive_true5a6, tcutactive_false5a6, tk5a6_id, 13, 0, 0)
tactive_cut_data1a47 = sep_cuts(tcutactive_true1a47, tcutactive_false1a47, tk1a47_id, 13, 0, 0)
tactive_cut_data2a47 = sep_cuts(tcutactive_true2a47, tcutactive_false2a47, tk2a47_id, 13, 0, 0)
tactive_cut_data3a47 = sep_cuts(tcutactive_true3a47, tcutactive_false3a47, tk3a47_id, 13, 0, 0)
tactive_cut_data4a47 = sep_cuts(tcutactive_true4a47, tcutactive_false4a47, tk4a47_id, 13, 0, 0)
tactive_cut_data5a47 = sep_cuts(tcutactive_true5a47, tcutactive_false5a47, tk5a47_id, 13, 0, 0)
tactive_cut_data1a49 = sep_cuts(tcutactive_true1a49, tcutactive_false1a49, tk1a49_id, 13, 0, 0) 
tactive_cut_data2a49 = sep_cuts(tcutactive_true2a49, tcutactive_false2a49, tk2a49_id, 13, 0, 0) 
tactive_cut_data3a49 = sep_cuts(tcutactive_true3a49, tcutactive_false3a49, tk3a49_id, 13, 0, 0) 
tactive_cut_data4a49 = sep_cuts(tcutactive_true4a49, tcutactive_false4a49, tk4a49_id, 13, 0, 0) 
tactive_cut_data5a49 = sep_cuts(tcutactive_true5a49, tcutactive_false5a49, tk5a49_id, 13, 0, 0) 


# one list with all from each diameter
data_6 = [active_cut_data1a6[0] + active_cut_data2a6[0] + active_cut_data3a6[0] + active_cut_data4a6[0] + active_cut_data5a6[0]]
data_47 = [active_cut_data1a47[0] + active_cut_data2a47[0] + active_cut_data3a47[0] + active_cut_data4a47[0] + active_cut_data5a47[0]]
data_49 = [active_cut_data1a49[0] + active_cut_data2a49[0] + active_cut_data3a49[0] + active_cut_data4a49[0] + active_cut_data5a49[0]]


# better endpoint of cut
end_points_1a6 = calc_end_time_p_drop(active_cut_data1a6, 100, 15.6)
end_points_2a6 = calc_end_time_p_drop(active_cut_data2a6, 100, 15.6)
end_points_3a6 = calc_end_time_p_drop(active_cut_data3a6, 100, 15.6)
end_points_4a6 = calc_end_time_p_drop(active_cut_data4a6, 100, 15.6)
end_points_5a6 = calc_end_time_p_drop(active_cut_data5a6, 100, 15.6)
end_points_1a47 = calc_end_time_p_drop(active_cut_data1a47, 100, 15.6)
end_points_2a47 = calc_end_time_p_drop(active_cut_data2a47, 100, 15.6)
end_points_3a47 = calc_end_time_p_drop(active_cut_data3a47, 100, 15.6)
end_points_4a47 = calc_end_time_p_drop(active_cut_data4a47, 100, 15.6)
end_points_5a47 = calc_end_time_p_drop(active_cut_data5a47, 100, 15.6)
end_points_1a49 = calc_end_time_p_drop(active_cut_data1a49, 100, 15.6)
end_points_2a49 = calc_end_time_p_drop(active_cut_data2a49, 100, 15.6)
end_points_3a49 = calc_end_time_p_drop(active_cut_data3a49, 100, 15.6)
end_points_4a49 = calc_end_time_p_drop(active_cut_data4a49, 100, 15.6)
end_points_5a49 = calc_end_time_p_drop(active_cut_data5a49, 100, 15.6)

tend_points_1a6 = calc_end_time_p_drop(tactive_cut_data1a6, 100, 15.6)
tend_points_2a6 = calc_end_time_p_drop(tactive_cut_data2a6, 100, 15.6)
tend_points_3a6 = calc_end_time_p_drop(tactive_cut_data3a6, 100, 15.6)
tend_points_4a6 = calc_end_time_p_drop(tactive_cut_data4a6, 100, 15.6)
tend_points_5a6 = calc_end_time_p_drop(tactive_cut_data5a6, 100, 15.6)
tend_points_1a47 = calc_end_time_p_drop(tactive_cut_data1a47, 100, 15.6)
tend_points_2a47 = calc_end_time_p_drop(tactive_cut_data2a47, 100, 15.6)
tend_points_3a47 = calc_end_time_p_drop(tactive_cut_data3a47, 100, 15.6)
tend_points_4a47 = calc_end_time_p_drop(tactive_cut_data4a47, 100, 15.6)
tend_points_5a47 = calc_end_time_p_drop(tactive_cut_data5a47, 100, 15.6)
tend_points_1a49 = calc_end_time_p_drop(tactive_cut_data1a49, 100, 15.6)
tend_points_2a49 = calc_end_time_p_drop(tactive_cut_data2a49, 100, 15.6)
tend_points_3a49 = calc_end_time_p_drop(tactive_cut_data3a49, 100, 15.6)
tend_points_4a49 = calc_end_time_p_drop(tactive_cut_data4a49, 100, 15.6)
tend_points_5a49 = calc_end_time_p_drop(tactive_cut_data5a49, 100, 15.6)

# update cuta with better endpoint
cutactive_false1a6 = update_cut_end_time(cutactive_false1a6, end_points_1a6)
cutactive_false2a6 = update_cut_end_time(cutactive_false2a6, end_points_2a6)
cutactive_false3a6 = update_cut_end_time(cutactive_false3a6, end_points_3a6)
cutactive_false4a6 = update_cut_end_time(cutactive_false4a6, end_points_4a6)
cutactive_false5a6 = update_cut_end_time(cutactive_false5a6, end_points_5a6)
cutactive_false1a47 = update_cut_end_time(cutactive_false1a47, end_points_1a47)
cutactive_false2a47 = update_cut_end_time(cutactive_false2a47, end_points_2a47)
cutactive_false3a47 = update_cut_end_time(cutactive_false3a47, end_points_3a47)
cutactive_false4a47 = update_cut_end_time(cutactive_false4a47, end_points_4a47)
cutactive_false5a47 = update_cut_end_time(cutactive_false5a47, end_points_5a47)
cutactive_false1a49 = update_cut_end_time(cutactive_false1a49, end_points_1a49)
cutactive_false2a49 = update_cut_end_time(cutactive_false2a49, end_points_2a49)
cutactive_false3a49 = update_cut_end_time(cutactive_false3a49, end_points_3a49)
cutactive_false4a49 = update_cut_end_time(cutactive_false4a49, end_points_4a49)
cutactive_false5a49 = update_cut_end_time(cutactive_false5a49, end_points_5a49)


tcutactive_false1a6 = update_cut_end_time(tcutactive_false1a6, tend_points_1a6)
tcutactive_false2a6 = update_cut_end_time(tcutactive_false2a6, tend_points_2a6)
tcutactive_false3a6 = update_cut_end_time(tcutactive_false3a6, tend_points_3a6)
tcutactive_false4a6 = update_cut_end_time(tcutactive_false4a6, tend_points_4a6)
tcutactive_false5a6 = update_cut_end_time(tcutactive_false5a6, tend_points_5a6)
tcutactive_false1a47 = update_cut_end_time(tcutactive_false1a47, tend_points_1a47)
tcutactive_false2a47 = update_cut_end_time(tcutactive_false2a47, tend_points_2a47)
tcutactive_false3a47 = update_cut_end_time(tcutactive_false3a47, tend_points_3a47)
tcutactive_false4a47 = update_cut_end_time(tcutactive_false4a47, tend_points_4a47)
tcutactive_false5a47 = update_cut_end_time(tcutactive_false5a47, tend_points_5a47)
tcutactive_false1a49 = update_cut_end_time(tcutactive_false1a49, tend_points_1a49)
tcutactive_false2a49 = update_cut_end_time(tcutactive_false2a49, tend_points_2a49)
tcutactive_false3a49 = update_cut_end_time(tcutactive_false3a49, tend_points_3a49)
tcutactive_false4a49 = update_cut_end_time(tcutactive_false4a49, tend_points_4a49)
tcutactive_false5a49 = update_cut_end_time(tcutactive_false5a49, tend_points_5a49)

# update cuta - detete same timespan from each diameter
cutactive_false1a6 = cut_end_substract(cutactive_false1a6, 4.4)
cutactive_false2a6 = cut_end_substract(cutactive_false2a6, 4.4)
cutactive_false3a6 = cut_end_substract(cutactive_false3a6, 4.4)
cutactive_false4a6 = cut_end_substract(cutactive_false4a6, 4.4)
cutactive_false5a6 = cut_end_substract(cutactive_false5a6, 4.4)
cutactive_false1a47 = cut_end_substract(cutactive_false1a47, 3)
cutactive_false2a47 = cut_end_substract(cutactive_false2a47, 3)
cutactive_false3a47 = cut_end_substract(cutactive_false3a47, 3)
cutactive_false4a47 = cut_end_substract(cutactive_false4a47, 3)
cutactive_false5a47 = cut_end_substract(cutactive_false5a47, 3)
cutactive_false1a49 = cut_end_substract(cutactive_false1a49, 3)
cutactive_false2a49 = cut_end_substract(cutactive_false2a49, 3)
cutactive_false3a49 = cut_end_substract(cutactive_false3a49, 3)
cutactive_false4a49 = cut_end_substract(cutactive_false4a49, 3)
cutactive_false5a49 = cut_end_substract(cutactive_false5a49, 3)


tcutactive_false1a6 = cut_end_substract(tcutactive_false1a6, 4.4)
tcutactive_false2a6 = cut_end_substract(tcutactive_false2a6, 4.4)
tcutactive_false3a6 = cut_end_substract(tcutactive_false3a6, 4.4)
tcutactive_false4a6 = cut_end_substract(tcutactive_false4a6, 4.4)
tcutactive_false5a6 = cut_end_substract(tcutactive_false5a6, 4.4)
tcutactive_false1a47 = cut_end_substract(tcutactive_false1a47, 3)
tcutactive_false2a47 = cut_end_substract(tcutactive_false2a47, 3)
tcutactive_false3a47 = cut_end_substract(tcutactive_false3a47, 3)
tcutactive_false4a47 = cut_end_substract(tcutactive_false4a47, 3)
tcutactive_false5a47 = cut_end_substract(tcutactive_false5a47, 3)
tcutactive_false1a49 = cut_end_substract(tcutactive_false1a49, 3)
tcutactive_false2a49 = cut_end_substract(tcutactive_false2a49, 3)
tcutactive_false3a49 = cut_end_substract(tcutactive_false3a49, 3)
tcutactive_false4a49 = cut_end_substract(tcutactive_false4a49, 3)
tcutactive_false5a49 = cut_end_substract(tcutactive_false5a49, 3)




# seperate data again with new endpoint
active_cut_data1a6_new = sep_cuts(cutactive_true1a6, cutactive_false1a6, k1a6_id, 13, 0, 4)
active_cut_data2a6_new = sep_cuts(cutactive_true2a6, cutactive_false2a6, k2a6_id, 13, 0, 4)
active_cut_data3a6_new = sep_cuts(cutactive_true3a6, cutactive_false3a6, k3a6_id, 13, 0, 4)
active_cut_data4a6_new = sep_cuts(cutactive_true4a6, cutactive_false4a6, k4a6_id, 13, 0, 4)
active_cut_data5a6_new = sep_cuts(cutactive_true5a6, cutactive_false5a6, k5a6_id, 13, 0, 4)
active_cut_data1a47_new = sep_cuts(cutactive_true1a47, cutactive_false1a47, k1a47_id, 13, 0, 4)
active_cut_data2a47_new = sep_cuts(cutactive_true2a47, cutactive_false2a47, k2a47_id, 13, 0, 4)
active_cut_data3a47_new = sep_cuts(cutactive_true3a47, cutactive_false3a47, k3a47_id, 13, 0, 4)
active_cut_data4a47_new = sep_cuts(cutactive_true4a47, cutactive_false4a47, k4a47_id, 13, 0, 4)
active_cut_data5a47_new = sep_cuts(cutactive_true5a47, cutactive_false5a47, k5a47_id, 13, 0, 4)
active_cut_data1a49_new = sep_cuts(cutactive_true1a49, cutactive_false1a49, k1a49_id, 13, 0, 4)
active_cut_data2a49_new = sep_cuts(cutactive_true2a49, cutactive_false2a49, k2a49_id, 13, 0, 4)
active_cut_data3a49_new = sep_cuts(cutactive_true3a49, cutactive_false3a49, k3a49_id, 13, 0, 4)
active_cut_data4a49_new = sep_cuts(cutactive_true4a49, cutactive_false4a49, k4a49_id, 13, 0, 4)
active_cut_data5a49_new = sep_cuts(cutactive_true5a49, cutactive_false5a49, k5a49_id, 13, 0, 4)


tactive_cut_data1a6_new = sep_cuts(tcutactive_true1a6, tcutactive_false1a6, tk1a6_id, 13, 0, 4)
tactive_cut_data2a6_new = sep_cuts(tcutactive_true2a6, tcutactive_false2a6, tk2a6_id, 13, 0, 4)
tactive_cut_data3a6_new = sep_cuts(tcutactive_true3a6, tcutactive_false3a6, tk3a6_id, 13, 0, 4)
tactive_cut_data4a6_new = sep_cuts(tcutactive_true4a6, tcutactive_false4a6, tk4a6_id, 13, 0, 4)
tactive_cut_data5a6_new = sep_cuts(tcutactive_true5a6, tcutactive_false5a6, tk5a6_id, 13, 0, 4)
tactive_cut_data1a47_new = sep_cuts(tcutactive_true1a47, tcutactive_false1a47, tk1a47_id, 13, 0, 4)
tactive_cut_data2a47_new = sep_cuts(tcutactive_true2a47, tcutactive_false2a47, tk2a47_id, 13, 0, 4)
tactive_cut_data3a47_new = sep_cuts(tcutactive_true3a47, tcutactive_false3a47, tk3a47_id, 13, 0, 4)
tactive_cut_data4a47_new = sep_cuts(tcutactive_true4a47, tcutactive_false4a47, tk4a47_id, 13, 0, 4)
tactive_cut_data5a47_new = sep_cuts(tcutactive_true5a47, tcutactive_false5a47, tk5a47_id, 13, 0, 4)
tactive_cut_data1a49_new = sep_cuts(tcutactive_true1a49, tcutactive_false1a49, tk1a49_id, 13, 0, 4)
tactive_cut_data2a49_new = sep_cuts(tcutactive_true2a49, tcutactive_false2a49, tk2a49_id, 13, 0, 4)
tactive_cut_data3a49_new = sep_cuts(tcutactive_true3a49, tcutactive_false3a49, tk3a49_id, 13, 0, 4)
tactive_cut_data4a49_new = sep_cuts(tcutactive_true4a49, tcutactive_false4a49, tk4a49_id, 13, 0, 4)
tactive_cut_data5a49_new = sep_cuts(tcutactive_true5a49, tcutactive_false5a49, tk5a49_id, 13, 0, 4)



#start_times_1a4 = calc_start_time_per_max_timedelta(active_cut_data1a4)
#start_times_1a6 = calc_start_time_per_max_timedelta(active_cut_data1a6)

## DONE wtf
#a = pd.DataFrame((cutactive_true1a4['source'].values - cutactive_false1a4['shifted'].values)/ np.timedelta64(1, 's'))
##unii, coui = np.unique(a, return_counts=True)

# cals starttime by counting space between nulldurchgänge of slope of rolling mean of pvorschub
start_times_1a6_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true1a6, cutactive_false1a6, k1a6_id, 13, 0, 4))
start_times_2a6_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true2a6, cutactive_false2a6, k2a6_id, 13, 0, 4))
start_times_3a6_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true3a6, cutactive_false3a6, k3a6_id, 13, 0, 4))
start_times_4a6_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true4a6, cutactive_false4a6, k4a6_id, 13, 0, 4))
start_times_5a6_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true5a6, cutactive_false5a6, k5a6_id, 13, 0, 4))
start_times_1a47_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true1a47, cutactive_false1a47, k1a47_id, 13, 0, 4))
start_times_2a47_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true2a47, cutactive_false2a47, k2a47_id, 13, 0, 4))
start_times_3a47_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true3a47, cutactive_false3a47, k3a47_id, 13, 0, 4))
start_times_4a47_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true4a47, cutactive_false4a47, k4a47_id, 13, 0, 4))
start_times_5a47_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true5a47, cutactive_false5a47, k5a47_id, 13, 0, 4))
start_times_1a49_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true1a49, cutactive_false1a49, k1a49_id, 13, 0, 4))
start_times_2a49_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true2a49, cutactive_false2a49, k2a49_id, 13, 0, 4))
start_times_3a49_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true3a49, cutactive_false3a49, k3a49_id, 13, 0, 4))
start_times_4a49_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true4a49, cutactive_false4a49, k4a49_id, 13, 0, 4))
start_times_5a49_timedelta = calc_start_time_per_max_timedelta(sep_cuts(cutactive_true5a49, cutactive_false5a49, k5a49_id, 13, 0, 4))

# update start
cutactive_true1a6 = update_cut_begin_time(cutactive_true1a6, start_times_1a6_timedelta, 'shifted')
cutactive_true2a6 = update_cut_begin_time(cutactive_true2a6, start_times_2a6_timedelta, 'shifted')
cutactive_true3a6 = update_cut_begin_time(cutactive_true3a6, start_times_3a6_timedelta, 'shifted')
cutactive_true4a6 = update_cut_begin_time(cutactive_true4a6, start_times_4a6_timedelta, 'shifted')
cutactive_true5a6 = update_cut_begin_time(cutactive_true5a6, start_times_5a6_timedelta, 'shifted')
cutactive_true1a47 = update_cut_begin_time(cutactive_true1a47, start_times_1a47_timedelta, 'shifted')
cutactive_true2a47 = update_cut_begin_time(cutactive_true2a47, start_times_2a47_timedelta, 'shifted')
cutactive_true3a47 = update_cut_begin_time(cutactive_true3a47, start_times_3a47_timedelta, 'shifted')
cutactive_true4a47 = update_cut_begin_time(cutactive_true4a47, start_times_4a47_timedelta, 'shifted')
cutactive_true5a47 = update_cut_begin_time(cutactive_true5a47, start_times_5a47_timedelta, 'shifted')
cutactive_true1a49 = update_cut_begin_time(cutactive_true1a49, start_times_1a49_timedelta, 'shifted')
cutactive_true2a49 = update_cut_begin_time(cutactive_true2a49, start_times_2a49_timedelta, 'shifted')
cutactive_true3a49 = update_cut_begin_time(cutactive_true3a49, start_times_3a49_timedelta, 'shifted')
cutactive_true4a49 = update_cut_begin_time(cutactive_true4a49, start_times_4a49_timedelta, 'shifted')
cutactive_true5a49 = update_cut_begin_time(cutactive_true5a49, start_times_5a49_timedelta, 'shifted')


# TOdo DONE wenn du start und stop vertauschst, warum sind dann daten drin? Check ob am ende alles leer ist, sollte nicht gehen
#sep_cuts(cutactive_false1a6, cutactive_true1a6, k1a6_id, 13, 3,4)
#sep_cuts(cutactive_false2a6, cutactive_true2a6, k2a6_id, 13, 3,4)
#sep_cuts(cutactive_false3a6, cutactive_true3a6, k3a6_id, 13, 3,4)
#sep_cuts(cutactive_false4a6, cutactive_true4a6, k4a6_id, 13, 3,4)
#sep_cuts(cutactive_false5a6, cutactive_true5a6, k5a6_id, 13, 3,4)
#sep_cuts(cutactive_false1a47, cutactive_true1a47, k1a47_id, 13, 3,4)
#sep_cuts(cutactive_false2a47, cutactive_true2a47, k2a47_id, 13, 3,4)
#sep_cuts(cutactive_false3a47, cutactive_true3a47, k3a47_id, 13, 3,4)
#sep_cuts(cutactive_false4a47, cutactive_true4a47, k4a47_id, 13, 3,4)
#sep_cuts(cutactive_false5a47, cutactive_true5a47, k5a47_id, 13, 3,4)
#sep_cuts(cutactive_false1a49, cutactive_true1a49, k1a49_id, 13, 3,4)
#sep_cuts(cutactive_false2a49, cutactive_true2a49, k2a49_id, 13, 3,4)
#sep_cuts(cutactive_false3a49, cutactive_true3a49, k3a49_id, 13, 3,4)
#sep_cuts(cutactive_false4a49, cutactive_true4a49, k4a49_id, 13, 3,4)
#sep_cuts(cutactive_false5a49, cutactive_true5a49, k5a49_id, 13, 3,4)


#aaa = np.array([len(active_cut_data1a4_new[0][x]) for x in range(len(active_cut_data1a4_new[0]))])
#unique, counts = np.unique(aaa, return_counts=True)
#plot_all_cuts_overlapping(active_cut_data1a4_new_falschrum, 0, '1a4 new cut boundaries')
#plot_all_cuts_overlapping(active_cut_data1a6_new_falschrum, 0, '1a6 new cut boundaries')
#print('indeces where it could happen: ')
#print(np.where(aaa != aaa.min()))

# calc new cuta start with slopes
peak_number = 2
start_times_1a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true1a6, cutactive_false1a6, k1a6_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_2a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true2a6, cutactive_false2a6, k2a6_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_3a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true3a6, cutactive_false3a6, k3a6_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_4a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true4a6, cutactive_false4a6, k4a6_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_5a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true5a6, cutactive_false5a6, k5a6_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_1a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true1a47, cutactive_false1a47, k1a47_id, 13, 0, 4), 35, peak_number=peak_number) # 40?
start_times_2a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true2a47, cutactive_false2a47, k2a47_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_3a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true3a47, cutactive_false3a47, k3a47_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_4a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true4a47, cutactive_false4a47, k4a47_id, 13, 0, 4),   30, peak_number=peak_number)
start_times_5a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true5a47, cutactive_false5a47, k5a47_id, 13, 0, 4), 40, peak_number=peak_number) #50
start_times_1a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true1a49, cutactive_false1a49, k1a49_id, 13, 0, 4), 35, peak_number=peak_number) # 40?
start_times_2a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true2a49, cutactive_false2a49, k2a49_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_3a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true3a49, cutactive_false3a49, k3a49_id, 13, 0, 4), 50, peak_number=peak_number)
start_times_4a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true4a49, cutactive_false4a49, k4a49_id, 13, 0, 4),   30, peak_number=peak_number)
start_times_5a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(cutactive_true5a49, cutactive_false5a49, k5a49_id, 13, 0, 4), 40, peak_number=peak_number) #50
tpeak_number = 2
tstart_times_1a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true1a6, tcutactive_false1a6, tk1a6_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_2a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true2a6, tcutactive_false2a6, tk2a6_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_3a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true3a6, tcutactive_false3a6, tk3a6_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_4a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true4a6, tcutactive_false4a6, tk4a6_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_5a6_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true5a6, tcutactive_false5a6, tk5a6_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_1a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true1a47, tcutactive_false1a47, tk1a47_id, 13, 0, 4), 40, peak_number=tpeak_number)
tstart_times_2a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true2a47, tcutactive_false2a47, tk2a47_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_3a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true3a47, tcutactive_false3a47, tk3a47_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_4a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true4a47, tcutactive_false4a47, tk4a47_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_5a47_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true5a47, tcutactive_false5a47, tk5a47_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_1a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true1a49, tcutactive_false1a49, tk1a49_id, 13, 0, 4), 40, peak_number=tpeak_number)
tstart_times_2a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true2a49, tcutactive_false2a49, tk2a49_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_3a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true3a49, tcutactive_false3a49, tk3a49_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_4a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true4a49, tcutactive_false4a49, tk4a49_id, 13, 0, 4), 50, peak_number=tpeak_number)
tstart_times_5a49_slopecount = calc_start_time_per_third_after_max_slope(sep_cuts(tcutactive_true5a49, tcutactive_false5a49, tk5a49_id, 13, 0, 4), 50, peak_number=tpeak_number)

#plot_all_cuts_overlapping(active_cut_data1a4_new, 0, '1a4 new cut boundaries')
#plot_all_cuts_overlapping(active_cut_data1a6_new, 0, '1a6 new cut boundaries')

cutactive_true1a6 = update_cut_begin_time(cutactive_true1a6, start_times_1a6_slopecount, 'shifted')
cutactive_true2a6 = update_cut_begin_time(cutactive_true2a6, start_times_2a6_slopecount, 'shifted')
cutactive_true3a6 = update_cut_begin_time(cutactive_true3a6, start_times_3a6_slopecount, 'shifted')
cutactive_true4a6 = update_cut_begin_time(cutactive_true4a6, start_times_4a6_slopecount, 'shifted')
cutactive_true5a6 = update_cut_begin_time(cutactive_true5a6, start_times_5a6_slopecount, 'shifted')
cutactive_true1a47 = update_cut_begin_time(cutactive_true1a47, start_times_1a47_slopecount, 'shifted')
cutactive_true2a47 = update_cut_begin_time(cutactive_true2a47, start_times_2a47_slopecount, 'shifted')
cutactive_true3a47 = update_cut_begin_time(cutactive_true3a47, start_times_3a47_slopecount, 'shifted')
cutactive_true4a47 = update_cut_begin_time(cutactive_true4a47, start_times_4a47_slopecount, 'shifted')
cutactive_true5a47 = update_cut_begin_time(cutactive_true5a47, start_times_5a47_slopecount, 'shifted')
cutactive_true1a49 = update_cut_begin_time(cutactive_true1a49, start_times_1a49_slopecount, 'shifted')
cutactive_true2a49 = update_cut_begin_time(cutactive_true2a49, start_times_2a49_slopecount, 'shifted')
cutactive_true3a49 = update_cut_begin_time(cutactive_true3a49, start_times_3a49_slopecount, 'shifted')
cutactive_true4a49 = update_cut_begin_time(cutactive_true4a49, start_times_4a49_slopecount, 'shifted')
cutactive_true5a49 = update_cut_begin_time(cutactive_true5a49, start_times_5a49_slopecount, 'shifted')


tcutactive_true1a6 = update_cut_begin_time(tcutactive_true1a6, tstart_times_1a6_slopecount, 'shifted')
tcutactive_true2a6 = update_cut_begin_time(tcutactive_true2a6, tstart_times_2a6_slopecount, 'shifted')
tcutactive_true3a6 = update_cut_begin_time(tcutactive_true3a6, tstart_times_3a6_slopecount, 'shifted')
tcutactive_true4a6 = update_cut_begin_time(tcutactive_true4a6, tstart_times_4a6_slopecount, 'shifted')
tcutactive_true5a6 = update_cut_begin_time(tcutactive_true5a6, tstart_times_5a6_slopecount, 'shifted')
tcutactive_true1a47 = update_cut_begin_time(tcutactive_true1a47, tstart_times_1a47_slopecount, 'shifted')
tcutactive_true2a47 = update_cut_begin_time(tcutactive_true2a47, tstart_times_2a47_slopecount, 'shifted')
tcutactive_true3a47 = update_cut_begin_time(tcutactive_true3a47, tstart_times_3a47_slopecount, 'shifted')
tcutactive_true4a47 = update_cut_begin_time(tcutactive_true4a47, tstart_times_4a47_slopecount, 'shifted')
tcutactive_true5a47 = update_cut_begin_time(tcutactive_true5a47, tstart_times_5a47_slopecount, 'shifted')
tcutactive_true1a49 = update_cut_begin_time(tcutactive_true1a49, tstart_times_1a49_slopecount, 'shifted')
tcutactive_true2a49 = update_cut_begin_time(tcutactive_true2a49, tstart_times_2a49_slopecount, 'shifted')
tcutactive_true3a49 = update_cut_begin_time(tcutactive_true3a49, tstart_times_3a49_slopecount, 'shifted')
tcutactive_true4a49 = update_cut_begin_time(tcutactive_true4a49, tstart_times_4a49_slopecount, 'shifted')
tcutactive_true5a49 = update_cut_begin_time(tcutactive_true5a49, tstart_times_5a49_slopecount, 'shifted')



active_cut_data1a6_newer = sep_cuts(cutactive_true1a6, cutactive_false1a6, k1a6_id, 13, 3, 4)
active_cut_data2a6_newer = sep_cuts(cutactive_true2a6, cutactive_false2a6, k2a6_id, 13, 3, 4)
active_cut_data3a6_newer = sep_cuts(cutactive_true3a6, cutactive_false3a6, k3a6_id, 13, 3, 4)
active_cut_data4a6_newer = sep_cuts(cutactive_true4a6, cutactive_false4a6, k4a6_id, 13, 3, 4)
active_cut_data5a6_newer = sep_cuts(cutactive_true5a6, cutactive_false5a6, k5a6_id, 13, 3, 4)
active_cut_data1a47_newer = sep_cuts(cutactive_true1a47, cutactive_false1a47, k1a47_id, 13, 3, 4)
active_cut_data2a47_newer = sep_cuts(cutactive_true2a47, cutactive_false2a47, k2a47_id, 13, 3, 4)
active_cut_data3a47_newer = sep_cuts(cutactive_true3a47, cutactive_false3a47, k3a47_id, 13, 3, 4)
active_cut_data4a47_newer = sep_cuts(cutactive_true4a47, cutactive_false4a47, k4a47_id, 13, 3, 4)
active_cut_data5a47_newer = sep_cuts(cutactive_true5a47, cutactive_false5a47, k5a47_id, 13, 3, 4)
active_cut_data1a49_newer = sep_cuts(cutactive_true1a49, cutactive_false1a49, k1a49_id, 13, 3, 4)
active_cut_data2a49_newer = sep_cuts(cutactive_true2a49, cutactive_false2a49, k2a49_id, 13, 3, 4)
active_cut_data3a49_newer = sep_cuts(cutactive_true3a49, cutactive_false3a49, k3a49_id, 13, 3, 4)
active_cut_data4a49_newer = sep_cuts(cutactive_true4a49, cutactive_false4a49, k4a49_id, 13, 3, 4)
active_cut_data5a49_newer = sep_cuts(cutactive_true5a49, cutactive_false5a49, k5a49_id, 13, 3, 4)


tactive_cut_data1a6_newer = sep_cuts(tcutactive_true1a6, tcutactive_false1a6, tk1a6_id, 13, 3, 4)
tactive_cut_data2a6_newer = sep_cuts(tcutactive_true2a6, tcutactive_false2a6, tk2a6_id, 13, 3, 4)
tactive_cut_data3a6_newer = sep_cuts(tcutactive_true3a6, tcutactive_false3a6, tk3a6_id, 13, 3, 4)
tactive_cut_data4a6_newer = sep_cuts(tcutactive_true4a6, tcutactive_false4a6, tk4a6_id, 13, 3, 4)
tactive_cut_data5a6_newer = sep_cuts(tcutactive_true5a6, tcutactive_false5a6, tk5a6_id, 13, 3, 4)
tactive_cut_data1a47_newer = sep_cuts(tcutactive_true1a47, tcutactive_false1a47, tk1a47_id, 13, 3, 4)
tactive_cut_data2a47_newer = sep_cuts(tcutactive_true2a47, tcutactive_false2a47, tk2a47_id, 13, 3, 4)
tactive_cut_data3a47_newer = sep_cuts(tcutactive_true3a47, tcutactive_false3a47, tk3a47_id, 13, 3, 4)
tactive_cut_data4a47_newer = sep_cuts(tcutactive_true4a47, tcutactive_false4a47, tk4a47_id, 13, 3, 4)
tactive_cut_data5a47_newer = sep_cuts(tcutactive_true5a47, tcutactive_false5a47, tk5a47_id, 13, 3, 4)
tactive_cut_data1a49_newer = sep_cuts(tcutactive_true1a49, tcutactive_false1a49, tk1a49_id, 13, 3, 4)
tactive_cut_data2a49_newer = sep_cuts(tcutactive_true2a49, tcutactive_false2a49, tk2a49_id, 13, 3, 4)
tactive_cut_data3a49_newer = sep_cuts(tcutactive_true3a49, tcutactive_false3a49, tk3a49_id, 13, 3, 4)
tactive_cut_data4a49_newer = sep_cuts(tcutactive_true4a49, tcutactive_false4a49, tk4a49_id, 13, 3, 4)
tactive_cut_data5a49_newer = sep_cuts(tcutactive_true5a49, tcutactive_false5a49, tk5a49_id, 13, 3, 4)


plot_all_cuts_overlapping(active_cut_data1a6_newer, 0, '1a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data2a6_newer, 0, '2a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data3a6_newer, 0, '3a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data4a6_newer, 0, '4a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data5a6_newer, 0, '5a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data1a47_newer, 0, '1a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data2a47_newer, 0, '2a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data3a47_newer, 0, '3a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data4a47_newer, 0, '4a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data5a47_newer, 0, '5a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data1a49_newer, 0, '1a49 newer slopecount')
plot_all_cuts_overlapping(active_cut_data2a49_newer, 0, '2a49 newer slopecount')
plot_all_cuts_overlapping(active_cut_data3a49_newer, 0, '3a49 newer slopecount')
plot_all_cuts_overlapping(active_cut_data4a49_newer, 0, '4a49 newer slopecount')
plot_all_cuts_overlapping(active_cut_data5a49_newer, 0, '5a49 newer slopecount')
#"""
bereinigung_grenzen_low_high_grob = """
# lösche alle mit zu hohen oder zu niedrigen werten je nach klasse - nochmal von hand für die übriggebliebenen
list_1a6_bandpass = qnd_bandpass_per_class(active_cut_data1a6_newer, 16.67, 15.7)
list_2a6_bandpass = qnd_bandpass_per_class(active_cut_data2a6_newer, 17, 15.9156)
list_3a6_bandpass = qnd_bandpass_per_class(active_cut_data3a6_newer, 18.5, 16)
list_4a6_bandpass = qnd_bandpass_per_class(active_cut_data4a6_newer, 19.44, 17.44)
list_5a6_bandpass = qnd_bandpass_per_class(active_cut_data5a6_newer, 19, 16)
list_1a47_bandpass = qnd_bandpass_per_class(active_cut_data1a47_newer, 16.67, 15.7)
list_2a47_bandpass = qnd_bandpass_per_class(active_cut_data2a47_newer, 19, 15.9156)
list_3a47_bandpass = qnd_bandpass_per_class(active_cut_data3a47_newer, 18.5, 16)
list_4a47_bandpass = qnd_bandpass_per_class(active_cut_data4a47_newer, 18.5, 16.2)             # TODO sind die grenzen richtig?  a47 a49
list_5a47_bandpass = qnd_bandpass_per_class(active_cut_data5a47_newer, 19, 16.5)
list_1a49_bandpass = qnd_bandpass_per_class(active_cut_data1a49_newer, 16.67, 15.7)            # TODO sind die grenzen richtig?  a47 a49
list_2a49_bandpass = qnd_bandpass_per_class(active_cut_data2a49_newer, 17, 15.9156)            # TODO sind die grenzen richtig?  a47 a49
list_3a49_bandpass = qnd_bandpass_per_class(active_cut_data3a49_newer, 18.5, 16)                # TODO sind die grenzen richtig?  a47 a49
list_4a49_bandpass = qnd_bandpass_per_class(active_cut_data4a49_newer, 19.5, 16.2)              # TODO sind die grenzen richtig?  a47 a49
list_5a49_bandpass = qnd_bandpass_per_class(active_cut_data5a49_newer, 20, 18)
list_1a6_bandpass.sort(reverse=True)
list_2a6_bandpass.sort(reverse=True)
list_3a6_bandpass.sort(reverse=True)
list_4a6_bandpass.sort(reverse=True)
list_5a6_bandpass.sort(reverse=True)
list_1a47_bandpass.sort(reverse=True)
list_2a47_bandpass.sort(reverse=True)
list_3a47_bandpass.sort(reverse=True)
list_4a47_bandpass.sort(reverse=True)
list_5a47_bandpass.sort(reverse=True)
list_1a49_bandpass.sort(reverse=True)
list_2a49_bandpass.sort(reverse=True)
list_3a49_bandpass.sort(reverse=True)
list_4a49_bandpass.sort(reverse=True)
list_5a49_bandpass.sort(reverse=True)
for i in list_1a6_bandpass:
    active_cut_data1a6_newer[0].pop(i)
for i in list_2a6_bandpass:
    active_cut_data2a6_newer[0].pop(i)
for i in list_3a6_bandpass:
    active_cut_data3a6_newer[0].pop(i)
for i in list_4a6_bandpass:
    active_cut_data4a6_newer[0].pop(i)
for i in list_5a6_bandpass:
    active_cut_data5a6_newer[0].pop(i)
for i in list_1a47_bandpass:
    active_cut_data1a47_newer[0].pop(i)
for i in list_2a47_bandpass:
    active_cut_data2a47_newer[0].pop(i)
for i in list_3a47_bandpass:
    active_cut_data3a47_newer[0].pop(i)
for i in list_4a47_bandpass:
    active_cut_data4a47_newer[0].pop(i)
for i in list_5a47_bandpass:
    active_cut_data5a47_newer[0].pop(i)
for i in list_1a49_bandpass:
    active_cut_data1a49_newer[0].pop(i)
for i in list_2a49_bandpass:
    active_cut_data2a49_newer[0].pop(i)
for i in list_3a49_bandpass:
    active_cut_data3a49_newer[0].pop(i)
for i in list_4a49_bandpass:
    active_cut_data4a49_newer[0].pop(i)
for i in list_5a49_bandpass:
    active_cut_data5a49_newer[0].pop(i)



#tlist_1a6_bandpass = qnd_bandpass_per_class(tactive_cut_data1a6_newer, 16.67, 15.7)
#tlist_2a6_bandpass = qnd_bandpass_per_class(tactive_cut_data2a6_newer, 17, 15.9156)
#tlist_3a6_bandpass = qnd_bandpass_per_class(tactive_cut_data3a6_newer, 18.5, 16)
#tlist_4a6_bandpass = qnd_bandpass_per_class(tactive_cut_data4a6_newer, 19.5, 16.2)
#tlist_5a6_bandpass = qnd_bandpass_per_class(tactive_cut_data5a6_newer, 19, 16)
#tlist_1a47_bandpass = qnd_bandpass_per_class(tactive_cut_data1a47_newer, 16.67, 15.7)
#tlist_2a47_bandpass = qnd_bandpass_per_class(tactive_cut_data2a47_newer, 17, 15.9156)                 # TODO sind die grenzen richtig?  a47 a49 # TODO sind die grenzen richtig?  a47 a49 # TODO sind die grenzen richtig?  a47 a49
#tlist_3a47_bandpass = qnd_bandpass_per_class(tactive_cut_data3a47_newer, 18.5, 16)
#tlist_4a47_bandpass = qnd_bandpass_per_class(tactive_cut_data4a47_newer, 19.5, 16)
#tlist_5a47_bandpass = qnd_bandpass_per_class(tactive_cut_data5a47_newer, 18.7, 16)              # TODO sind die grenzen richtig?  a47 a49
#tlist_1a49_bandpass = qnd_bandpass_per_class(tactive_cut_data1a49_newer, 16.67, 15.7)
#tlist_2a49_bandpass = qnd_bandpass_per_class(tactive_cut_data2a49_newer, 17, 15.9156)
#tlist_3a49_bandpass = qnd_bandpass_per_class(tactive_cut_data3a49_newer, 18.5, 16)                             # TODO sind die grenzen richtig?  a47 a49
#tlist_4a49_bandpass = qnd_bandpass_per_class(tactive_cut_data4a49_newer, 19.5, 16)
#tlist_5a49_bandpass = qnd_bandpass_per_class(tactive_cut_data5a49_newer, 18.7, 16)
#tlist_1a6_bandpass.sort(reverse=True)
#tlist_2a6_bandpass.sort(reverse=True)
#tlist_3a6_bandpass.sort(reverse=True)
#tlist_4a6_bandpass.sort(reverse=True)
#tlist_5a6_bandpass.sort(reverse=True)
#tlist_1a47_bandpass.sort(reverse=True)
#tlist_2a47_bandpass.sort(reverse=True)
#tlist_3a47_bandpass.sort(reverse=True)
#tlist_4a47_bandpass.sort(reverse=True)
#tlist_5a47_bandpass.sort(reverse=True)
#tlist_1a49_bandpass.sort(reverse=True)
#tlist_2a49_bandpass.sort(reverse=True)
#tlist_3a49_bandpass.sort(reverse=True)
#tlist_4a49_bandpass.sort(reverse=True)
#tlist_5a49_bandpass.sort(reverse=True)
#for i in tlist_1a6_bandpass:
#    tactive_cut_data1a6_newer[0].pop(i)
#for i in tlist_2a6_bandpass:
#    tactive_cut_data2a6_newer[0].pop(i)
#for i in tlist_3a6_bandpass:
#    tactive_cut_data3a6_newer[0].pop(i)
#for i in tlist_4a6_bandpass:
#    tactive_cut_data4a6_newer[0].pop(i)
#for i in tlist_5a6_bandpass:
#    tactive_cut_data5a6_newer[0].pop(i)
#for i in tlist_1a47_bandpass:
#    tactive_cut_data1a47_newer[0].pop(i)
#for i in tlist_2a47_bandpass:
#    tactive_cut_data2a47_newer[0].pop(i)
#for i in tlist_3a47_bandpass:
#    tactive_cut_data3a47_newer[0].pop(i)
#for i in tlist_4a47_bandpass:
#    tactive_cut_data4a47_newer[0].pop(i)
#for i in tlist_5a47_bandpass:
#    tactive_cut_data5a47_newer[0].pop(i)
#for i in tlist_1a49_bandpass:
#    tactive_cut_data1a49_newer[0].pop(i)
#for i in tlist_2a49_bandpass:
#    tactive_cut_data2a49_newer[0].pop(i)
#for i in tlist_3a49_bandpass:
#    tactive_cut_data3a49_newer[0].pop(i)
#for i in tlist_4a49_bandpass:
#    tactive_cut_data4a49_newer[0].pop(i)
#for i in tlist_5a49_bandpass:
#    tactive_cut_data5a49_newer[0].pop(i)
#"""


calc_bereinigung_per_abweichung_len = """
# TODO genauere berechnung oben anstellen
active_cut_data1a6_newer_lens = np.array([len(active_cut_data1a6_newer[0][x]) for x in range(len(active_cut_data1a6_newer[0]))]).reshape(len(active_cut_data1a6_newer[0]), 1)
active_cut_data2a6_newer_lens = np.array([len(active_cut_data2a6_newer[0][x]) for x in range(len(active_cut_data2a6_newer[0]))]).reshape(len(active_cut_data2a6_newer[0]), 1)
active_cut_data3a6_newer_lens = np.array([len(active_cut_data3a6_newer[0][x]) for x in range(len(active_cut_data3a6_newer[0]))]).reshape(len(active_cut_data3a6_newer[0]), 1)
active_cut_data4a6_newer_lens = np.array([len(active_cut_data4a6_newer[0][x]) for x in range(len(active_cut_data4a6_newer[0]))]).reshape(len(active_cut_data4a6_newer[0]), 1)
active_cut_data5a6_newer_lens = np.array([len(active_cut_data5a6_newer[0][x]) for x in range(len(active_cut_data5a6_newer[0]))]).reshape(len(active_cut_data5a6_newer[0]), 1)
active_cut_data1a47_newer_lens = np.array([len(active_cut_data1a47_newer[0][x]) for x in range(len(active_cut_data1a47_newer[0]))]).reshape(len(active_cut_data1a47_newer[0]), 1)
active_cut_data2a47_newer_lens = np.array([len(active_cut_data2a47_newer[0][x]) for x in range(len(active_cut_data2a47_newer[0]))]).reshape(len(active_cut_data2a47_newer[0]), 1)
active_cut_data3a47_newer_lens = np.array([len(active_cut_data3a47_newer[0][x]) for x in range(len(active_cut_data3a47_newer[0]))]).reshape(len(active_cut_data3a47_newer[0]), 1)
active_cut_data4a47_newer_lens = np.array([len(active_cut_data4a47_newer[0][x]) for x in range(len(active_cut_data4a47_newer[0]))]).reshape(len(active_cut_data4a47_newer[0]), 1)
active_cut_data5a47_newer_lens = np.array([len(active_cut_data5a47_newer[0][x]) for x in range(len(active_cut_data5a47_newer[0]))]).reshape(len(active_cut_data5a47_newer[0]), 1)
active_cut_data1a49_newer_lens = np.array([len(active_cut_data1a49_newer[0][x]) for x in range(len(active_cut_data1a49_newer[0]))]).reshape(len(active_cut_data1a49_newer[0]), 1)
active_cut_data2a49_newer_lens = np.array([len(active_cut_data2a49_newer[0][x]) for x in range(len(active_cut_data2a49_newer[0]))]).reshape(len(active_cut_data2a49_newer[0]), 1)
active_cut_data3a49_newer_lens = np.array([len(active_cut_data3a49_newer[0][x]) for x in range(len(active_cut_data3a49_newer[0]))]).reshape(len(active_cut_data3a49_newer[0]), 1)
active_cut_data4a49_newer_lens = np.array([len(active_cut_data4a49_newer[0][x]) for x in range(len(active_cut_data4a49_newer[0]))]).reshape(len(active_cut_data4a49_newer[0]), 1)
active_cut_data5a49_newer_lens = np.array([len(active_cut_data5a49_newer[0][x]) for x in range(len(active_cut_data5a49_newer[0]))]).reshape(len(active_cut_data5a49_newer[0]), 1)


tactive_cut_data1a6_newer_lens = np.array([len(tactive_cut_data1a6_newer[0][x]) for x in range(len(tactive_cut_data1a6_newer[0]))]).reshape(len(tactive_cut_data1a6_newer[0]), 1)
tactive_cut_data2a6_newer_lens = np.array([len(tactive_cut_data2a6_newer[0][x]) for x in range(len(tactive_cut_data2a6_newer[0]))]).reshape(len(tactive_cut_data2a6_newer[0]), 1)
tactive_cut_data3a6_newer_lens = np.array([len(tactive_cut_data3a6_newer[0][x]) for x in range(len(tactive_cut_data3a6_newer[0]))]).reshape(len(tactive_cut_data3a6_newer[0]), 1)
tactive_cut_data4a6_newer_lens = np.array([len(tactive_cut_data4a6_newer[0][x]) for x in range(len(tactive_cut_data4a6_newer[0]))]).reshape(len(tactive_cut_data4a6_newer[0]), 1)
tactive_cut_data5a6_newer_lens = np.array([len(tactive_cut_data5a6_newer[0][x]) for x in range(len(tactive_cut_data5a6_newer[0]))]).reshape(len(tactive_cut_data5a6_newer[0]), 1)
tactive_cut_data1a47_newer_lens = np.array([len(tactive_cut_data1a47_newer[0][x]) for x in range(len(tactive_cut_data1a47_newer[0]))]).reshape(len(tactive_cut_data1a47_newer[0]), 1)
tactive_cut_data2a47_newer_lens = np.array([len(tactive_cut_data2a47_newer[0][x]) for x in range(len(tactive_cut_data2a47_newer[0]))]).reshape(len(tactive_cut_data2a47_newer[0]), 1)
tactive_cut_data3a47_newer_lens = np.array([len(tactive_cut_data3a47_newer[0][x]) for x in range(len(tactive_cut_data3a47_newer[0]))]).reshape(len(tactive_cut_data3a47_newer[0]), 1)
tactive_cut_data4a47_newer_lens = np.array([len(tactive_cut_data4a47_newer[0][x]) for x in range(len(tactive_cut_data4a47_newer[0]))]).reshape(len(tactive_cut_data4a47_newer[0]), 1)
tactive_cut_data5a47_newer_lens = np.array([len(tactive_cut_data5a47_newer[0][x]) for x in range(len(tactive_cut_data5a47_newer[0]))]).reshape(len(tactive_cut_data5a47_newer[0]), 1)
tactive_cut_data1a49_newer_lens = np.array([len(tactive_cut_data1a49_newer[0][x]) for x in range(len(tactive_cut_data1a49_newer[0]))]).reshape(len(tactive_cut_data1a49_newer[0]), 1)
tactive_cut_data2a49_newer_lens = np.array([len(tactive_cut_data2a49_newer[0][x]) for x in range(len(tactive_cut_data2a49_newer[0]))]).reshape(len(tactive_cut_data2a49_newer[0]), 1)
tactive_cut_data3a49_newer_lens = np.array([len(tactive_cut_data3a49_newer[0][x]) for x in range(len(tactive_cut_data3a49_newer[0]))]).reshape(len(tactive_cut_data3a49_newer[0]), 1)
tactive_cut_data4a49_newer_lens = np.array([len(tactive_cut_data4a49_newer[0][x]) for x in range(len(tactive_cut_data4a49_newer[0]))]).reshape(len(tactive_cut_data4a49_newer[0]), 1)
tactive_cut_data5a49_newer_lens = np.array([len(tactive_cut_data5a49_newer[0][x]) for x in range(len(tactive_cut_data5a49_newer[0]))]).reshape(len(tactive_cut_data5a49_newer[0]), 1)




#  TODO sind überhaupt ausreisser vorhanden?




offset_percent = 0.5;print('a6')
wrong_len_list_1a6 = qnd_outlier_indices(active_cut_data1a6_newer_lens, offset_percent  , '1a6 ')
wrong_len_list_2a6 = qnd_outlier_indices(active_cut_data2a6_newer_lens, offset_percent  , '2a6 ')
wrong_len_list_3a6 = qnd_outlier_indices(active_cut_data3a6_newer_lens, offset_percent  , '3a6 ')
wrong_len_list_4a6 = qnd_outlier_indices(active_cut_data4a6_newer_lens, offset_percent  , '4a6 ')
wrong_len_list_5a6 = qnd_outlier_indices(active_cut_data5a6_newer_lens, offset_percent  , '5a6 ');print('a4')
wrong_len_list_1a47 = qnd_outlier_indices(active_cut_data1a47_newer_lens, offset_percent, '1a47')
wrong_len_list_2a47 = qnd_outlier_indices(active_cut_data2a47_newer_lens, offset_percent, '2a47')
wrong_len_list_3a47 = qnd_outlier_indices(active_cut_data3a47_newer_lens, offset_percent, '3a47')
wrong_len_list_4a47 = qnd_outlier_indices(active_cut_data4a47_newer_lens, offset_percent, '4a47')
wrong_len_list_5a47 = qnd_outlier_indices(active_cut_data5a47_newer_lens, offset_percent, '5a47')
wrong_len_list_1a49 = qnd_outlier_indices(active_cut_data1a49_newer_lens, offset_percent, '1a49')
wrong_len_list_2a49 = qnd_outlier_indices(active_cut_data2a49_newer_lens, offset_percent, '2a49')
wrong_len_list_3a49 = qnd_outlier_indices(active_cut_data3a49_newer_lens, offset_percent, '3a49')
wrong_len_list_4a49 = qnd_outlier_indices(active_cut_data4a49_newer_lens, offset_percent, '4a49')
wrong_len_list_5a49 = qnd_outlier_indices(active_cut_data5a49_newer_lens, offset_percent, '5a49')

toffset_percent =  0.5
twrong_len_list_1a6 = qnd_outlier_indices(tactive_cut_data1a6_newer_lens, toffset_percent, 't1a6 ')
twrong_len_list_2a6 = qnd_outlier_indices(tactive_cut_data2a6_newer_lens, toffset_percent, 't2a6 ')
twrong_len_list_3a6 = qnd_outlier_indices(tactive_cut_data3a6_newer_lens, toffset_percent, 't3a6 ')
twrong_len_list_4a6 = qnd_outlier_indices(tactive_cut_data4a6_newer_lens, toffset_percent, 't4a6 ')
twrong_len_list_5a6 = qnd_outlier_indices(tactive_cut_data5a6_newer_lens, toffset_percent, 't5a6 ')
twrong_len_list_1a47 = qnd_outlier_indices(tactive_cut_data1a47_newer_lens, toffset_percent, 't1a47')
twrong_len_list_2a47 = qnd_outlier_indices(tactive_cut_data2a47_newer_lens, toffset_percent, 't2a47')
twrong_len_list_3a47 = qnd_outlier_indices(tactive_cut_data3a47_newer_lens, toffset_percent, 't3a47')
twrong_len_list_4a47 = qnd_outlier_indices(tactive_cut_data4a47_newer_lens, toffset_percent, 't4a47')
twrong_len_list_5a47 = qnd_outlier_indices(tactive_cut_data5a47_newer_lens, toffset_percent, 't5a47')
twrong_len_list_1a49 = qnd_outlier_indices(tactive_cut_data1a49_newer_lens, toffset_percent, 't1a49')
twrong_len_list_2a49 = qnd_outlier_indices(tactive_cut_data2a49_newer_lens, toffset_percent, 't2a49')
twrong_len_list_3a49 = qnd_outlier_indices(tactive_cut_data3a49_newer_lens, toffset_percent, 't3a49')
twrong_len_list_4a49 = qnd_outlier_indices(tactive_cut_data4a49_newer_lens, toffset_percent, 't4a49')
twrong_len_list_5a49 = qnd_outlier_indices(tactive_cut_data5a49_newer_lens, toffset_percent, 't5a49')

# damit pop den korrekten index löschen kann, muss von hinten nach vorne gepoppt werden, sonst passen die kleineren indices nicht mehr
wrong_len_list_1a6.sort(reverse=True)
wrong_len_list_2a6.sort(reverse=True)
wrong_len_list_3a6.sort(reverse=True)
wrong_len_list_4a6.sort(reverse=True)
wrong_len_list_5a6.sort(reverse=True)
wrong_len_list_1a47.sort(reverse=True)
wrong_len_list_2a47.sort(reverse=True)
wrong_len_list_3a47.sort(reverse=True)
wrong_len_list_4a47.sort(reverse=True)
wrong_len_list_5a47.sort(reverse=True)
wrong_len_list_1a49.sort(reverse=True)
wrong_len_list_2a49.sort(reverse=True)
wrong_len_list_3a49.sort(reverse=True)
wrong_len_list_4a49.sort(reverse=True)
wrong_len_list_5a49.sort(reverse=True)

o1a6_active_cut_data1a6_newer_lens  = list(active_cut_data1a6_newer_lens.reshape(-1))
o2a6_active_cut_data2a6_newer_lens  = list(active_cut_data2a6_newer_lens.reshape(-1))
o3a6_active_cut_data3a6_newer_lens  = list(active_cut_data3a6_newer_lens.reshape(-1))
o4a6_active_cut_data4a6_newer_lens  = list(active_cut_data4a6_newer_lens.reshape(-1))
o5a6_active_cut_data5a6_newer_lens  = list(active_cut_data5a6_newer_lens.reshape(-1))
o1a47active_cut_data1a47_newer_lens = list(active_cut_data1a47_newer_lens.reshape(-1))
o2a47active_cut_data2a47_newer_lens = list(active_cut_data2a47_newer_lens.reshape(-1))
o3a47active_cut_data3a47_newer_lens = list(active_cut_data3a47_newer_lens.reshape(-1))
o4a47active_cut_data4a47_newer_lens = list(active_cut_data4a47_newer_lens.reshape(-1))
o5a47active_cut_data5a47_newer_lens = list(active_cut_data5a47_newer_lens.reshape(-1))
o1a49active_cut_data1a49_newer_lens = list(active_cut_data1a49_newer_lens.reshape(-1))
o2a49active_cut_data2a49_newer_lens = list(active_cut_data2a49_newer_lens.reshape(-1))
o3a49active_cut_data3a49_newer_lens = list(active_cut_data3a49_newer_lens.reshape(-1))
o4a49active_cut_data4a49_newer_lens = list(active_cut_data4a49_newer_lens.reshape(-1))
o5a49active_cut_data5a49_newer_lens = list(active_cut_data5a49_newer_lens.reshape(-1))

o1a6_active_cut_data1a6_newer_lens.sort()
o2a6_active_cut_data2a6_newer_lens.sort()
o3a6_active_cut_data3a6_newer_lens.sort()
o4a6_active_cut_data4a6_newer_lens.sort()
o5a6_active_cut_data5a6_newer_lens.sort()
o1a47active_cut_data1a47_newer_lens.sort()
o2a47active_cut_data2a47_newer_lens.sort()
o3a47active_cut_data3a47_newer_lens.sort()
o4a47active_cut_data4a47_newer_lens.sort()
o5a47active_cut_data5a47_newer_lens.sort()
o1a49active_cut_data1a49_newer_lens.sort()
o2a49active_cut_data2a49_newer_lens.sort()
o3a49active_cut_data3a49_newer_lens.sort()
o4a49active_cut_data4a49_newer_lens.sort()
o5a49active_cut_data5a49_newer_lens.sort()

plt.figure()
plt.scatter(range(len(o1a6_active_cut_data1a6_newer_lens)), o1a6_active_cut_data1a6_newer_lens, label='1a6')
plt.scatter(range(len(o2a6_active_cut_data2a6_newer_lens)), o2a6_active_cut_data2a6_newer_lens, label='2a6')
plt.scatter(range(len(o3a6_active_cut_data3a6_newer_lens)), o3a6_active_cut_data3a6_newer_lens, label='3a6')
plt.scatter(range(len(o4a6_active_cut_data4a6_newer_lens)), o4a6_active_cut_data4a6_newer_lens, label='4a6')
plt.scatter(range(len(o5a6_active_cut_data5a6_newer_lens)), o5a6_active_cut_data5a6_newer_lens, label='5a6')
plt.legend()
plt.figure()
plt.scatter(range(len(o1a47active_cut_data1a47_newer_lens)), o1a47active_cut_data1a47_newer_lens, label='1a47')
plt.scatter(range(len(o2a47active_cut_data2a47_newer_lens)), o2a47active_cut_data2a47_newer_lens, label='2a47')
plt.scatter(range(len(o3a47active_cut_data3a47_newer_lens)), o3a47active_cut_data3a47_newer_lens, label='3a47')
plt.scatter(range(len(o4a47active_cut_data4a47_newer_lens)), o4a47active_cut_data4a47_newer_lens, label='4a47')
plt.scatter(range(len(o5a47active_cut_data5a47_newer_lens)), o5a47active_cut_data5a47_newer_lens, label='5a47')
plt.scatter(range(len(o1a49active_cut_data1a49_newer_lens)), o1a49active_cut_data1a49_newer_lens, label='1a49')
plt.scatter(range(len(o2a49active_cut_data2a49_newer_lens)), o2a49active_cut_data2a49_newer_lens, label='2a49')
plt.scatter(range(len(o3a49active_cut_data3a49_newer_lens)), o3a49active_cut_data3a49_newer_lens, label='3a49')
plt.scatter(range(len(o4a49active_cut_data4a49_newer_lens)), o4a49active_cut_data4a49_newer_lens, label='4a49')
plt.scatter(range(len(o5a49active_cut_data5a49_newer_lens)), o5a49active_cut_data5a49_newer_lens, label='5a49')
plt.legend()

twrong_len_list_1a6.sort(reverse=True)
twrong_len_list_2a6.sort(reverse=True)
twrong_len_list_3a6.sort(reverse=True)
twrong_len_list_4a6.sort(reverse=True)
twrong_len_list_5a6.sort(reverse=True)
twrong_len_list_1a47.sort(reverse=True)
twrong_len_list_2a47.sort(reverse=True)
twrong_len_list_3a47.sort(reverse=True)
twrong_len_list_4a47.sort(reverse=True)
twrong_len_list_5a47.sort(reverse=True)
twrong_len_list_1a49.sort(reverse=True)
twrong_len_list_2a49.sort(reverse=True)
twrong_len_list_3a49.sort(reverse=True)
twrong_len_list_4a49.sort(reverse=True)
twrong_len_list_5a49.sort(reverse=True)
#"""

do_bereinigung_per_abweichung_len = """

for i in wrong_len_list_1a6:
    active_cut_data1a6_newer[0].pop(i)
for i in wrong_len_list_2a6:
    active_cut_data2a6_newer[0].pop(i)
for i in wrong_len_list_3a6:
    active_cut_data3a6_newer[0].pop(i)
for i in wrong_len_list_4a6:
    active_cut_data4a6_newer[0].pop(i)
for i in wrong_len_list_5a6:
    active_cut_data5a6_newer[0].pop(i)
for i in wrong_len_list_1a47:
    active_cut_data1a47_newer[0].pop(i)
for i in wrong_len_list_2a47:
    active_cut_data2a47_newer[0].pop(i)
for i in wrong_len_list_3a47:
    active_cut_data3a47_newer[0].pop(i)
for i in wrong_len_list_4a47:
    active_cut_data4a47_newer[0].pop(i)
for i in wrong_len_list_5a47:
    active_cut_data5a47_newer[0].pop(i)
for i in wrong_len_list_1a49:
    active_cut_data1a49_newer[0].pop(i)
for i in wrong_len_list_2a49:
    active_cut_data2a49_newer[0].pop(i)
for i in wrong_len_list_3a49:
    active_cut_data3a49_newer[0].pop(i)
for i in wrong_len_list_4a49:
    active_cut_data4a49_newer[0].pop(i)
for i in wrong_len_list_5a49:
    active_cut_data5a49_newer[0].pop(i)


for i in twrong_len_list_1a6:
    tactive_cut_data1a6_newer[0].pop(i)
for i in twrong_len_list_2a6:
    active_cut_data2a6_newer[0].pop(i)
for ti in twrong_len_list_3a6:
    tactive_cut_data3a6_newer[0].pop(i)
for i in twrong_len_list_4a6:
    tactive_cut_data4a6_newer[0].pop(i)
for i in twrong_len_list_5a6:
    tactive_cut_data5a6_newer[0].pop(i)
for i in twrong_len_list_1a47:
    tactive_cut_data1a47_newer[0].pop(i)
for i in twrong_len_list_2a47:
    tactive_cut_data2a47_newer[0].pop(i)
for i in twrong_len_list_3a47:
    tactive_cut_data3a47_newer[0].pop(i)
for i in twrong_len_list_4a47:
    tactive_cut_data4a47_newer[0].pop(i)
for i in twrong_len_list_5a47:
    tactive_cut_data5a47_newer[0].pop(i)
for i in twrong_len_list_1a49:
    tactive_cut_data1a49_newer[0].pop(i)
for i in twrong_len_list_2a49:
    tactive_cut_data2a49_newer[0].pop(i)
for i in twrong_len_list_3a49:
    tactive_cut_data3a49_newer[0].pop(i)
for i in twrong_len_list_4a49:
    tactive_cut_data4a49_newer[0].pop(i)
for i in twrong_len_list_5a49:
    tactive_cut_data5a49_newer[0].pop(i)
    
    
#"""


save_new_cutactives = """
cutactive_true1a6.to_csv(os.path.join(path_final_data, 'cutactive_true1a6.csv'), index_label='idx')
cutactive_true2a6.to_csv(os.path.join(path_final_data, 'cutactive_true2a6.csv'), index_label='idx')
cutactive_true3a6.to_csv(os.path.join(path_final_data, 'cutactive_true3a6.csv'), index_label='idx')
cutactive_true4a6.to_csv(os.path.join(path_final_data, 'cutactive_true4a6.csv'), index_label='idx')
cutactive_true5a6.to_csv(os.path.join(path_final_data, 'cutactive_true5a6.csv'), index_label='idx')
cutactive_true1a47.to_csv(os.path.join(path_final_data, 'cutactive_true1a47.csv'), index_label='idx')
cutactive_true2a47.to_csv(os.path.join(path_final_data, 'cutactive_true2a47.csv'), index_label='idx')
cutactive_true3a47.to_csv(os.path.join(path_final_data, 'cutactive_true3a47.csv'), index_label='idx')
cutactive_true4a47.to_csv(os.path.join(path_final_data, 'cutactive_true4a47.csv'), index_label='idx')
cutactive_true5a47.to_csv(os.path.join(path_final_data, 'cutactive_true5a47.csv'), index_label='idx')
cutactive_true1a49.to_csv(os.path.join(path_final_data, 'cutactive_true1a49.csv'), index_label='idx')
cutactive_true2a49.to_csv(os.path.join(path_final_data, 'cutactive_true2a49.csv'), index_label='idx')
cutactive_true3a49.to_csv(os.path.join(path_final_data, 'cutactive_true3a49.csv'), index_label='idx')
cutactive_true4a49.to_csv(os.path.join(path_final_data, 'cutactive_true4a49.csv'), index_label='idx')
cutactive_true5a49.to_csv(os.path.join(path_final_data, 'cutactive_true5a49.csv'), index_label='idx')


tcutactive_true1a6.to_csv(os.path.join(path_final_data, 'tcutactive_true1a6.csv'), index_label='idx')
tcutactive_true2a6.to_csv(os.path.join(path_final_data, 'tcutactive_true2a6.csv'), index_label='idx')
tcutactive_true3a6.to_csv(os.path.join(path_final_data, 'tcutactive_true3a6.csv'), index_label='idx')
tcutactive_true4a6.to_csv(os.path.join(path_final_data, 'tcutactive_true4a6.csv'), index_label='idx')
tcutactive_true5a6.to_csv(os.path.join(path_final_data, 'tcutactive_true5a6.csv'), index_label='idx')
tcutactive_true1a47.to_csv(os.path.join(path_final_data, 'tcutactive_true1a47.csv'), index_label='idx')
tcutactive_true2a47.to_csv(os.path.join(path_final_data, 'tcutactive_true2a47.csv'), index_label='idx')
tcutactive_true3a47.to_csv(os.path.join(path_final_data, 'tcutactive_true3a47.csv'), index_label='idx')
tcutactive_true4a47.to_csv(os.path.join(path_final_data, 'tcutactive_true4a47.csv'), index_label='idx')
tcutactive_true5a47.to_csv(os.path.join(path_final_data, 'tcutactive_true5a47.csv'), index_label='idx')
tcutactive_true1a49.to_csv(os.path.join(path_final_data, 'tcutactive_true1a49.csv'), index_label='idx')
tcutactive_true2a49.to_csv(os.path.join(path_final_data, 'tcutactive_true2a49.csv'), index_label='idx')
tcutactive_true3a49.to_csv(os.path.join(path_final_data, 'tcutactive_true3a49.csv'), index_label='idx')
tcutactive_true4a49.to_csv(os.path.join(path_final_data, 'tcutactive_true4a49.csv'), index_label='idx')
tcutactive_true5a49.to_csv(os.path.join(path_final_data, 'tcutactive_true5a49.csv'), index_label='idx')

# train false
cutactive_false1a6.to_csv(os.path.join(path_final_data, 'cutactive_false1a6.csv'), index_label='idx')
cutactive_false2a6.to_csv(os.path.join(path_final_data, 'cutactive_false2a6.csv'), index_label='idx')
cutactive_false3a6.to_csv(os.path.join(path_final_data, 'cutactive_false3a6.csv'), index_label='idx')
cutactive_false4a6.to_csv(os.path.join(path_final_data, 'cutactive_false4a6.csv'), index_label='idx')
cutactive_false5a6.to_csv(os.path.join(path_final_data, 'cutactive_false5a6.csv'), index_label='idx')
cutactive_false1a47.to_csv(os.path.join(path_final_data, 'cutactive_false1a47.csv'), index_label='idx')
cutactive_false2a47.to_csv(os.path.join(path_final_data, 'cutactive_false2a47.csv'), index_label='idx')
cutactive_false3a47.to_csv(os.path.join(path_final_data, 'cutactive_false3a47.csv'), index_label='idx')
cutactive_false4a47.to_csv(os.path.join(path_final_data, 'cutactive_false4a47.csv'), index_label='idx')
cutactive_false5a47.to_csv(os.path.join(path_final_data, 'cutactive_false5a47.csv'), index_label='idx')
cutactive_false1a49.to_csv(os.path.join(path_final_data, 'cutactive_false1a49.csv'), index_label='idx')
cutactive_false2a49.to_csv(os.path.join(path_final_data, 'cutactive_false2a49.csv'), index_label='idx')
cutactive_false3a49.to_csv(os.path.join(path_final_data, 'cutactive_false3a49.csv'), index_label='idx')
cutactive_false4a49.to_csv(os.path.join(path_final_data, 'cutactive_false4a49.csv'), index_label='idx')
cutactive_false5a49.to_csv(os.path.join(path_final_data, 'cutactive_false5a49.csv'), index_label='idx')


# test false
tcutactive_false1a6.to_csv(os.path.join(path_final_data, 'tcutactive_false1a6.csv'), index_label='idx')
tcutactive_false2a6.to_csv(os.path.join(path_final_data, 'tcutactive_false2a6.csv'), index_label='idx')
tcutactive_false3a6.to_csv(os.path.join(path_final_data, 'tcutactive_false3a6.csv'), index_label='idx')
tcutactive_false4a6.to_csv(os.path.join(path_final_data, 'tcutactive_false4a6.csv'), index_label='idx')
tcutactive_false5a6.to_csv(os.path.join(path_final_data, 'tcutactive_false5a6.csv'), index_label='idx')
tcutactive_false1a47.to_csv(os.path.join(path_final_data, 'tcutactive_false1a47.csv'), index_label='idx')
tcutactive_false2a47.to_csv(os.path.join(path_final_data, 'tcutactive_false2a47.csv'), index_label='idx')
tcutactive_false3a47.to_csv(os.path.join(path_final_data, 'tcutactive_false3a47.csv'), index_label='idx')
tcutactive_false4a47.to_csv(os.path.join(path_final_data, 'tcutactive_false4a47.csv'), index_label='idx')
tcutactive_false5a47.to_csv(os.path.join(path_final_data, 'tcutactive_false5a47.csv'), index_label='idx')
tcutactive_false1a49.to_csv(os.path.join(path_final_data, 'tcutactive_false1a49.csv'), index_label='idx')
tcutactive_false2a49.to_csv(os.path.join(path_final_data, 'tcutactive_false2a49.csv'), index_label='idx')
tcutactive_false3a49.to_csv(os.path.join(path_final_data, 'tcutactive_false3a49.csv'), index_label='idx')
tcutactive_false4a49.to_csv(os.path.join(path_final_data, 'tcutactive_false4a49.csv'), index_label='idx')
tcutactive_false5a49.to_csv(os.path.join(path_final_data, 'tcutactive_false5a49.csv'), index_label='idx')

#"""



path_final_data = 'E:\\ausgelagert thesis daten\\final_data\\cut_start_stop_times'

#load_new_cutas = """
# train true
cutactive_true1a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true1a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true2a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true2a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true3a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true3a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true4a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true4a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true5a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true5a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true1a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true1a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true2a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true2a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true3a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true3a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true4a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true4a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true5a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true5a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true1a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true1a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true2a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true2a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true3a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true3a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true4a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true4a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_true5a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true5a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])

#test true
tcutactive_true1a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true1a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true2a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true2a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true3a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true3a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true4a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true4a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true5a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true5a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true1a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true1a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true2a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true2a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true3a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true3a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true4a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true4a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true5a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true5a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true1a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true1a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true2a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true2a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true3a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true3a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true4a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true4a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_true5a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true5a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
# train true
cutactive_false1a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false1a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false2a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false2a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false3a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false3a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false4a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false4a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false5a6 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false5a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false1a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false1a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false2a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false2a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false3a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false3a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false4a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false4a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false5a47 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false5a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false1a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false1a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false2a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false2a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false3a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false3a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false4a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false4a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
cutactive_false5a49 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false5a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
#test true
tcutactive_false1a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false1a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false2a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false2a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false3a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false3a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false4a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false4a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false5a6 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false5a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false1a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false1a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false2a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false2a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false3a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false3a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false4a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false4a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false5a47 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false5a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false1a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false1a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false2a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false2a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false3a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false3a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false4a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false4a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
tcutactive_false5a49 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false5a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
#"""


final_cut_relevant_data = """
active_cut_data1a6_newer =  sep_cuts_all(cutactive_true1a6, cutactive_false1a6, k1a6_id, rel_, 0, 0)
active_cut_data2a6_newer =  sep_cuts_all(cutactive_true2a6, cutactive_false2a6, k2a6_id, rel_, 0, 0)
active_cut_data3a6_newer =  sep_cuts_all(cutactive_true3a6, cutactive_false3a6, k3a6_id, rel_, 0, 0)
active_cut_data4a6_newer =  sep_cuts_all(cutactive_true4a6, cutactive_false4a6, k4a6_id, rel_, 0, 0)
active_cut_data5a6_newer =  sep_cuts_all(cutactive_true5a6, cutactive_false5a6, k5a6_id, rel_, 0, 0)
active_cut_data1a47_newer =  sep_cuts_all(cutactive_true1a47, cutactive_false1a47, k1a47_id, _ids, 0, 0)
active_cut_data2a47_newer =  sep_cuts_all(cutactive_true2a47, cutactive_false2a47, k2a47_id, _ids, 0, 0)
active_cut_data3a47_newer =  sep_cuts_all(cutactive_true3a47, cutactive_false3a47, k3a47_id, _ids, 0, 0)
active_cut_data4a47_newer =  sep_cuts_all(cutactive_true4a47, cutactive_false4a47, k4a47_id, _ids, 0, 0)
active_cut_data5a47_newer =  sep_cuts_all(cutactive_true5a47, cutactive_false5a47, k5a47_id, _ids, 0, 0)
active_cut_data1a49_newer =  sep_cuts_all(cutactive_true1a49, cutactive_false1a49, k1a49_id, _ids, 0, 0)
active_cut_data2a49_newer =  sep_cuts_all(cutactive_true2a49, cutactive_false2a49, k2a49_id, _ids, 0, 0)
active_cut_data3a49_newer =  sep_cuts_all(cutactive_true3a49, cutactive_false3a49, k3a49_id, _ids, 0, 0)
active_cut_data4a49_newer =  sep_cuts_all(cutactive_true4a49, cutactive_false4a49, k4a49_id, _ids, 0, 0)
active_cut_data5a49_newer =  sep_cuts_all(cutactive_true5a49, cutactive_false5a49, k5a49_id, _ids, 0, 0)

tactive_cut_data1a6_newer = sep_cuts_all(tcutactive_true1a6, tcutactive_false1a6, tk1a6_id, rids, 0, 0)
tactive_cut_data2a6_newer = sep_cuts_all(tcutactive_true2a6, tcutactive_false2a6, tk2a6_id, rids, 0, 0)
tactive_cut_data3a6_newer = sep_cuts_all(tcutactive_true3a6, tcutactive_false3a6, tk3a6_id, rids, 0, 0)
tactive_cut_data4a6_newer = sep_cuts_all(tcutactive_true4a6, tcutactive_false4a6, tk4a6_id, rids, 0, 0)
tactive_cut_data5a6_newer = sep_cuts_all(tcutactive_true5a6, tcutactive_false5a6, tk5a6_id, rids, 0, 0)
tactive_cut_data1a47_newer = sep_cuts_all(tcutactive_true1a47, tcutactive_false1a47, tk1a47_id, rids, 0, 0)
tactive_cut_data2a47_newer = sep_cuts_all(tcutactive_true2a47, tcutactive_false2a47, tk2a47_id, rids, 0, 0)
tactive_cut_data3a47_newer = sep_cuts_all(tcutactive_true3a47, tcutactive_false3a47, tk3a47_id, rids, 0, 0)
tactive_cut_data4a47_newer = sep_cuts_all(tcutactive_true4a47, tcutactive_false4a47, tk4a47_id, rids, 0, 0)
tactive_cut_data5a47_newer = sep_cuts_all(tcutactive_true5a47, tcutactive_false5a47, tk5a47_id, rids, 0, 0)
tactive_cut_data1a49_newer = sep_cuts_all(tcutactive_true1a49, tcutactive_false1a49, tk1a49_id, rids, 0, 0)
tactive_cut_data2a49_newer = sep_cuts_all(tcutactive_true2a49, tcutactive_false2a49, tk2a49_id, rids, 0, 0)
tactive_cut_data3a49_newer = sep_cuts_all(tcutactive_true3a49, tcutactive_false3a49, tk3a49_id, rids, 0, 0)
tactive_cut_data4a49_newer = sep_cuts_all(tcutactive_true4a49, tcutactive_false4a49, tk4a49_id, rids, 0, 0)
tactive_cut_data5a49_newer = sep_cuts_all(tcutactive_true5a49, tcutactive_false5a49, tk5a49_id, rids, 0, 0)
#"""

#load_precut_class_sigraw_TRAIN = """
print('0')
#sig1a6_id = concat_dfs_sep_ids(sig1a6, sig=True)
#cut_concat_save_sig('1a6', cutactive_true1a6, cutactive_false1a6, sig1a6_id)
print('0')
#sig2a6_id = concat_dfs_sep_ids(sig2a6, sig=True)
#cut_concat_save_sig('2a6', cutactive_true2a6, cutactive_false2a6, sig2a6_id)
print('0')
#sig3a6_id = concat_dfs_sep_ids(sig3a6, sig=True)
#cut_concat_save_sig('3a6', cutactive_true3a6, cutactive_false3a6, sig3a6_id)
print('0')
#sig4a6_id = concat_dfs_sep_ids(sig4a6, sig=True)
#cut_concat_save_sig('4a6', cutactive_true4a6, cutactive_false4a6, sig4a6_id)
print('0')
sig5a6_id = concat_dfs_sep_ids(sig5a6, sig=True)
cut_concat_save_sig('5a6', cutactive_true5a6, cutactive_false5a6, sig5a6_id)
print('1')
sig1a47_id = concat_dfs_sep_ids(sig1a47, sig=True)
cut_concat_save_sig('1a47', cutactive_true1a47, cutactive_false1a47, sig1a47_id)
print('1')
sig2a47_id = concat_dfs_sep_ids(sig2a47, sig=True)
cut_concat_save_sig('2a47', cutactive_true2a47, cutactive_false2a47, sig2a47_id)
print('1')
sig3a47_id = concat_dfs_sep_ids(sig3a47, sig=True)
cut_concat_save_sig('3a47', cutactive_true3a47, cutactive_false3a47, sig3a47_id)
print('1')
sig4a47_id = concat_dfs_sep_ids(sig4a47, sig=True)
cut_concat_save_sig('4a47', cutactive_true4a47, cutactive_false4a47, sig4a47_id)
print('1')
sig5a47_id = concat_dfs_sep_ids(sig5a47, sig=True)
cut_concat_save_sig('5a47', cutactive_true5a47, cutactive_false5a47, sig5a47_id)
print('2')
sig1a49_id = concat_dfs_sep_ids(sig1a49, sig=True)
cut_concat_save_sig('1a49', cutactive_true1a49, cutactive_false1a49, sig1a49_id)
print('2')
sig2a49_id = concat_dfs_sep_ids(sig2a49, sig=True)
cut_concat_save_sig('2a49', cutactive_true2a49, cutactive_false2a49, sig2a49_id)
print('2')
sig3a49_id = concat_dfs_sep_ids(sig3a49, sig=True)
cut_concat_save_sig('3a49', cutactive_true3a49, cutactive_false3a49, sig3a49_id)
print('2')
sig4a49_id = concat_dfs_sep_ids(sig4a49, sig=True)
cut_concat_save_sig('4a49', cutactive_true4a49, cutactive_false4a49, sig4a49_id)
print('2')
sig5a49_id = concat_dfs_sep_ids(sig5a49, sig=True)
cut_concat_save_sig('5a49', cutactive_true5a49, cutactive_false5a49, sig5a49_id)


#"""

load_precut_class_sigraw_TEST = """


tsig1a6_id = concat_dfs_sep_ids(tsig1a6, sig=True)
cut_concat_save_sig('t1a6', tcutactive_true1a6, tcutactive_false1a6, tsig1a6_id)
print('3')
tsig2a6_id = concat_dfs_sep_ids(tsig2a6, sig=True)
cut_concat_save_sig('t2a6', tcutactive_true2a6, tcutactive_false2a6, tsig2a6_id)
print('3')
tsig3a6_id = concat_dfs_sep_ids(tsig3a6, sig=True)
print('3')
cut_concat_save_sig('t3a6', tcutactive_true3a6, tcutactive_false3a6, tsig3a6_id)
tsig4a6_id = concat_dfs_sep_ids(tsig4a6, sig=True)
cut_concat_save_sig('t4a6', tcutactive_true4a6, tcutactive_false4a6, tsig4a6_id)
tsig5a6_id = concat_dfs_sep_ids(tsig5a6, sig=True)
cut_concat_save_sig('t5a6', tcutactive_true5a6, tcutactive_false5a6, tsig5a6_id)
print('4')
tsig1a47_id = concat_dfs_sep_ids(tsig1a47, sig=True)
cut_concat_save_sig('t1a47', tcutactive_true1a47, tcutactive_false1a47, tsig1a47_id)
tsig2a47_id = concat_dfs_sep_ids(tsig2a47, sig=True)
cut_concat_save_sig('t2a47', tcutactive_true2a47, tcutactive_false2a47, tsig2a47_id)
tsig3a47_id = concat_dfs_sep_ids(tsig3a47, sig=True)
cut_concat_save_sig('t3a47', tcutactive_true3a47, tcutactive_false3a47, tsig3a47_id)
print('4')
tsig4a47_id = concat_dfs_sep_ids(tsig4a47, sig=True)
cut_concat_save_sig('t4a47', tcutactive_true4a47, tcutactive_false4a47, tsig4a47_id)
tsig5a47_id = concat_dfs_sep_ids(tsig5a47, sig=True)
cut_concat_save_sig('t5a47', tcutactive_true5a47, tcutactive_false5a47, tsig5a47_id)
tsig1a49_id = concat_dfs_sep_ids(tsig1a49, sig=True)                               
cut_concat_save_sig('t1a49', tcutactive_true1a49, tcutactive_false1a49, tsig1a49_id) 
tsig2a49_id = concat_dfs_sep_ids(tsig2a49, sig=True)                               
cut_concat_save_sig('t2a49', tcutactive_true2a49, tcutactive_false2a49, tsig2a49_id) 
print('4')
tsig3a49_id = concat_dfs_sep_ids(tsig3a49, sig=True)                               
cut_concat_save_sig('t3a49', tcutactive_true3a49, tcutactive_false3a49, tsig3a49_id) 
tsig4a49_id = concat_dfs_sep_ids(tsig4a49, sig=True)                               
cut_concat_save_sig('t4a49', tcutactive_true4a49, tcutactive_false4a49, tsig4a49_id) 
tsig5a49_id = concat_dfs_sep_ids(tsig5a49, sig=True)                               
cut_concat_save_sig('t5a49', tcutactive_true5a49, tcutactive_false5a49, tsig5a49_id) 


#"""

seperiere_sig_daten = """


tsig1a6_id_cuta = sep_cuts(tcutactive_true1a6, tcutactive_false1a6, tsig1a6_id, 0, 0, 0, sig=True)
tsig2a6_id_cuta = sep_cuts(tcutactive_true2a6, tcutactive_false2a6, tsig2a6_id, 0, 0, 0, sig=True)
tsig3a6_id_cuta = sep_cuts(tcutactive_true3a6, tcutactive_false3a6, tsig3a6_id, 0, 0, 0, sig=True)
tsig4a6_id_cuta = sep_cuts(tcutactive_true4a6, tcutactive_false4a6, tsig4a6_id, 0, 0, 0, sig=True)
tsig5a6_id_cuta = sep_cuts(tcutactive_true5a6, tcutactive_false5a6, tsig5a6_id, 0, 0, 0, sig=True)
tsig1a47_id_cuta = sep_cuts(tcutactive_true1a47, tcutactive_false1a47, tsig1a47_id, 0, 0, 0, sig=True)
tsig2a47_id_cuta = sep_cuts(tcutactive_true2a47, tcutactive_false2a47, tsig2a47_id, 0, 0, 0, sig=True)
tsig3a47_id_cuta = sep_cuts(tcutactive_true3a47, tcutactive_false3a47, tsig3a47_id, 0, 0, 0, sig=True)
tsig4a47_id_cuta = sep_cuts(tcutactive_true4a47, tcutactive_false4a47, tsig4a47_id, 0, 0, 0, sig=True)
tsig5a47_id_cuta = sep_cuts(tcutactive_true5a47, tcutactive_false5a47, tsig5a47_id, 0, 0, 0, sig=True)
tsig1a49_id_cuta = sep_cuts(tcutactive_true1a49, tcutactive_false1a49, tsig1a49_id, 0, 0, 0, sig=True)
tsig2a49_id_cuta = sep_cuts(tcutactive_true2a49, tcutactive_false2a49, tsig2a49_id, 0, 0, 0, sig=True)
tsig3a49_id_cuta = sep_cuts(tcutactive_true3a49, tcutactive_false3a49, tsig3a49_id, 0, 0, 0, sig=True)
tsig4a49_id_cuta = sep_cuts(tcutactive_true4a49, tcutactive_false4a49, tsig4a49_id, 0, 0, 0, sig=True)
tsig5a49_id_cuta = sep_cuts(tcutactive_true5a49, tcutactive_false5a49, tsig5a49_id, 0, 0, 0, sig=True)
#"""

plot = """
# vergleiche mit den alten - nur raw bCutactive True/False
plot_all_cuts_overlapping(active_cut_data1a6, 0, '1a6 old')
plot_all_cuts_overlapping(active_cut_data2a6, 0, '2a6 old')
plot_all_cuts_overlapping(active_cut_data3a6, 0, '3a6 old')
plot_all_cuts_overlapping(active_cut_data4a6, 0, '4a6 old')
plot_all_cuts_overlapping(active_cut_data5a6, 0, '5a6 old')
plot_all_cuts_overlapping(active_cut_data1a47, 0, '1a47 old')
plot_all_cuts_overlapping(active_cut_data2a47, 0, '2a47 old')
plot_all_cuts_overlapping(active_cut_data3a47, 0, '3a47 old')
plot_all_cuts_overlapping(active_cut_data4a47, 0, '4a47 old')
plot_all_cuts_overlapping(active_cut_data5a47, 0, '5a47 old')
plot_all_cuts_overlapping(active_cut_data1a49, 0, '1a49 old')
plot_all_cuts_overlapping(active_cut_data2a49, 0, '2a49 old')
plot_all_cuts_overlapping(active_cut_data3a49, 0, '3a49 old')
plot_all_cuts_overlapping(active_cut_data4a49, 0, '4a49 old')
plot_all_cuts_overlapping(active_cut_data5a49, 0, '5a49 old')


plot_all_cuts_overlapping(active_cut_data1a6_new, 0, '1a6 new sort maxima')
plot_all_cuts_overlapping(active_cut_data2a6_new, 0, '2a6 new sort maxima')
plot_all_cuts_overlapping(active_cut_data3a6_new, 0, '3a6 new sort maxima')
plot_all_cuts_overlapping(active_cut_data4a6_new, 0, '4a6 new sort maxima')
plot_all_cuts_overlapping(active_cut_data5a6_new, 0, '5a6 new sort maxima')
plot_all_cuts_overlapping(active_cut_data1a47_new, 0, '1a47 new sort maxima')
plot_all_cuts_overlapping(active_cut_data2a47_new, 0, '2a47 new sort maxima')
plot_all_cuts_overlapping(active_cut_data3a47_new, 0, '3a47 new sort maxima')
plot_all_cuts_overlapping(active_cut_data4a47_new, 0, '4a47 new sort maxima')
plot_all_cuts_overlapping(active_cut_data5a47_new, 0, '5a47 new sort maxima')
plot_all_cuts_overlapping(active_cut_data1a49_new, 0, '1a49 new sort maxima')
plot_all_cuts_overlapping(active_cut_data2a49_new, 0, '2a49 new sort maxima')
plot_all_cuts_overlapping(active_cut_data3a49_new, 0, '3a49 new sort maxima')
plot_all_cuts_overlapping(active_cut_data4a49_new, 0, '4a49 new sort maxima')
plot_all_cuts_overlapping(active_cut_data5a49_new, 0, '5a49 new sort maxima')

plot_all_cuts_overlapping(active_cut_data1a6_newer, 0, '1a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data2a6_newer, 0, '2a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data3a6_newer, 0, '3a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data4a6_newer, 0, '4a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data5a6_newer, 0, '5a6 newer slopecount')
plot_all_cuts_overlapping(active_cut_data1a47_newer, 0, '1a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data2a47_newer, 0, '2a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data3a47_newer, 0, '3a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data4a47_newer, 0, '4a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data5a47_newer, 0, '5a47 newer slopecount')
plot_all_cuts_overlapping(active_cut_data1a49_newer, 0, '1a49 newer slopecount') 
plot_all_cuts_overlapping(active_cut_data2a49_newer, 0, '2a49 newer slopecount') 
plot_all_cuts_overlapping(active_cut_data3a49_newer, 0, '3a49 newer slopecount') 
plot_all_cuts_overlapping(active_cut_data4a49_newer, 0, '4a49 newer slopecount') 
plot_all_cuts_overlapping(active_cut_data5a49_newer, 0, '5a49 newer slopecount') 

plot_all_cuts_overlapping(tactive_cut_data1a6_newer, 0, 't1a6 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data2a6_newer, 0, 't2a6 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data3a6_newer, 0, 't3a6 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data4a6_newer, 0, 't4a6 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data5a6_newer, 0, 't5a6 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data1a47_newer, 0, 't1a47 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data2a47_newer, 0, 't2a47 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data3a47_newer, 0, 't3a47 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data4a47_newer, 0, 't4a47 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data5a47_newer, 0, 't5a47 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data1a49_newer, 0, 't1a49 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data2a49_newer, 0, 't2a49 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data3a49_newer, 0, 't3a49 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data4a49_newer, 0, 't4a49 newer slopecount')
plot_all_cuts_overlapping(tactive_cut_data5a49_newer, 0, 't5a49 newer slopecount')
#"""

"""
k1 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__13-58-30_28-02-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__16-21-47_28-02-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__11-10-27_01-03-2022_data.csv']
k2 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-01-59_01-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__16-49-50_01-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__12-57-39_01-03-2022_data.csv']
k3 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__15-30-29_19-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__17-35-40_19-03-2022_data.csv',
]
k4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-10-19_21-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__14-45-28_21-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-58-22_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__16-48-04_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-24-51_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-36-01_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__09-13-12_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__12-18-38_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-21-33_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__15-12-05_01-04-2022_data.csv',
]
k5 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__10-57-16_02-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__14-30-07_02-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-09-48_05-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-13-10_05-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__11-41-57_07-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__14-24-55_07-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-28-33_08-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__08-43-54_08-04-2022_data     Lücke in sig.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__12-34-31_08-04-2022_data.csv',
]

k1_id = concat_dfs_sep_ids(k1)
k2_id = concat_dfs_sep_ids(k2)
k3_id = concat_dfs_sep_ids(k3)
k4_id = concat_dfs_sep_ids(k4)
k5_id = concat_dfs_sep_ids(k5)

k1_id[13] = add_feature_seeds(k1_id[13])
k2_id[13] = add_feature_seeds(k2_id[13])
k3_id[13] = add_feature_seeds(k3_id[13])
k4_id[13] = add_feature_seeds(k4_id[13])
k5_id[13] = add_feature_seeds(k5_id[13])

# TODO alles in eine? ne, dann weis ich nicht was was anfängt/aufhört
cutactive_true1, cutactive_false1 = vis.get_bCutActives(k1_id)
cutactive_true2, cutactive_false2 = vis.get_bCutActives(k2_id)
cutactive_true3, cutactive_false3 = vis.get_bCutActives(k3_id)
cutactive_true4, cutactive_false4 = vis.get_bCutActives(k4_id)
cutactive_true5, cutactive_false5 = vis.get_bCutActives(k5_id)

cuta_test_list = [
cutactive_true1, cutactive_true2, cutactive_true3, cutactive_true4, cutactive_true5,
cutactive_false1, cutactive_false2, cutactive_false3, cutactive_false4, cutactive_false5]

def check(cuta_test_list):
    def check_cuta_true_false_is_pos(df):
        return (np.array(vis.faster_timedetla_datachange(df)) < 0).any()

    please_be_false = [check_cuta_true_false_is_pos(x) for x in cuta_test_list]
    print('if zero, order of cuta true false is correct: ', sum(please_be_false))
check(cuta_test_list)

def check_true_false_alternating(arg_list):
    trues = []
    falses = []
    for i in arg_list:
        current = False
        truefalselist = i[0]['val'].values
        for j in range(i[0].shape[0]):

            if j % 2 == 0:
                trues.append(truefalselist[j])
            elif j % 2 == 1:
                falses.append(truefalselist[j])
            else:
                print('oopsy false')
        print('wrong trues: ' + str(sum(trues) - len(trues)))
        print('wrong falses: ' + str(sum(falses)))
all_class_list = [k1_id, k2_id, k3_id, k4_id, k5_id]
check_true_false_alternating(all_class_list)
"""

#plt.figure()
#plt.plot(k1a6_id[13]['val'])
#plt.title(title)
#plt.xlabel('Messungen')
#plt.ylabel('P_Vorschub')


#with open('k1_id.pkl', 'wb') as outp:
#    pickle.dump(k1_id, outp, pickle.HIGHEST_PROTOCOL)
#with open('k2_id.pkl', 'wb') as outp:
#    pickle.dump(k2_id, outp, pickle.HIGHEST_PROTOCOL)
#with open('k3_id.pkl', 'wb') as outp:
#    pickle.dump(k3_id, outp, pickle.HIGHEST_PROTOCOL)
#with open('k4_id.pkl', 'wb') as outp:
#    pickle.dump(k4_id, outp, pickle.HIGHEST_PROTOCOL)
#with open('k5_id.pkl', 'wb') as outp:
#    pickle.dump(k5_id, outp, pickle.HIGHEST_PROTOCOL)

#





