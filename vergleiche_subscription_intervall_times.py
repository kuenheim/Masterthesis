"""
Hier werden verschiedene update intervalls für die OPCUA subscription getestet und verglichen, um die optimale zu finden
"""

import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from helpers.lists import ids, names

nonstationary_names = ['ns=6;s=::AsGlobalPV:CPU_Kuehler_Temp',
                       'ns=6;s=::AsGlobalPV:CPU_Temp',
                       'ns=6;s=::AsGlobalPV:P_Vorschub',
                       'ns=6;s=::AsGlobalPV:Position',
                       'ns=6;s=::AsGlobalPV:vVorschub',
                       'ns=6;s=::AsGlobalPV:TData.T1',
                       'ns=6;s=::AsGlobalPV:TData.T2',
                       'ns=6;s=::AsGlobalPV:TData.T3',
                       'ns=6;s=::AsGlobalPV:TData.T4',
                       'ns=6;s=::AsGlobalPV:Vib01.Peak',
                       'ns=6;s=::AsGlobalPV:Vib01.CREST',
                       'ns=6;s=::AsGlobalPV:Vib01.Skewness',
                       'ns=6;s=::AsGlobalPV:Vib01.Kurtosis',
                       'ns=6;s=::AsGlobalPV:Vib02.Peak',
                       'ns=6;s=::AsGlobalPV:Vib02.CREST',
                       'ns=6;s=::AsGlobalPV:Vib02.Skewness',
                       'ns=6;s=::AsGlobalPV:Vib02.Kurtosis',
                       'ns=6;s=::AsGlobalPV:Vib03.Peak',
                       'ns=6;s=::AsGlobalPV:Vib03.CREST',
                       'ns=6;s=::AsGlobalPV:Vib03.Skewness',
                       'ns=6;s=::AsGlobalPV:Vib03.Kurtosis']


def dfs_for_timetest(path):
    return pd.read_csv(path,
                       skiprows=65,
                       names=header,
                       delimiter=' ',
                       usecols=[0, 1, 2, 3, 5],
                       parse_dates={'source': ['source_date', 'source_time'], 'server': ['server_date', 'server_time']})


header = ['source_date', 'source_time', 'server_date', 'server_time', 'ID']
paths = ['file10_10min.csv', 'file100_10min.csv', 'file30_10min.csv', 'file50_10min.csv', 'file500_10min.csv']


df_10 = dfs_for_timetest(paths[0])
df_100 = dfs_for_timetest(paths[1])
df_30 = dfs_for_timetest(paths[2])
df_50 = dfs_for_timetest(paths[3])
df_500 = dfs_for_timetest(paths[4])

count_10 = df_10['ID'].value_counts()
count_30 = df_30['ID'].value_counts()
count_100 = df_100['ID'].value_counts()
count_50 = df_50['ID'].value_counts()
count_500 = df_500['ID'].value_counts()

#sensors = [x[20:] for x in nonstationary_names]


sensors = []
for sensor in sensors:
    print(sensor)

    v1K_10 = df_10.loc[df_10['ID'] == sensor]
    v1K_30 = df_30.loc[df_30['ID'] == sensor]
    v1K_100 = df_100.loc[df_100['ID'] == sensor]
    v1K_50 = df_50.loc[df_50['ID'] == sensor]
    v1K_500 = df_500.loc[df_500['ID'] == sensor]

    deltas_10 = []
    deltas_30 = []
    deltas_100 = []
    deltas_50 = []
    deltas_500 = []

    for i in range(v1K_10.shape[0] - 1):
        delta = v1K_10.iloc[i+1, 0] - v1K_10.iloc[i, 0]
        deltas_10.append(delta.total_seconds())

    for i in range(v1K_30.shape[0] - 1):
        delta = v1K_30.iloc[i+1, 0] - v1K_30.iloc[i, 0]
        deltas_30.append(delta.total_seconds())

    for j in range(v1K_100.shape[0] - 1):
        delta = v1K_100.iloc[j+1, 0] - v1K_100.iloc[j, 0]
        deltas_100.append(delta.total_seconds())

    for k in range(v1K_50.shape[0] - 1):
        delta = v1K_50.iloc[k+1, 0] - v1K_50.iloc[k, 0]
        deltas_50.append(delta.total_seconds())

    for l in range(v1K_500.shape[0] - 1):
        delta = v1K_500.iloc[l + 1, 0] - v1K_500.iloc[l, 0]
        deltas_500.append(delta.total_seconds())

    unique_10, counts_10 = np.unique(deltas_10, return_counts=True)
    unique_30, counts_30 = np.unique(deltas_30, return_counts=True)
    unique_100, counts_100 = np.unique(deltas_100, return_counts=True)
    unique_50, counts_50 = np.unique(deltas_50, return_counts=True)
    unique_500, counts_500 = np.unique(deltas_500, return_counts=True)

    plt.plot(unique_10, counts_10, label='10')
    plt.plot(unique_30, counts_30, label='30')
    plt.plot(unique_100, counts_100, label='100')
    plt.plot(unique_50, counts_50, label='50')
    #plt.plot(unique_500, counts_500, label='500')
    plt.title(sensor)
    plt.xlabel('publishing intervall in seconds')
    plt.ylabel('count')
    plt.legend()
    #plt.savefig('images\\publishing period ohne 500\\overlay\\times_' + str(sensor) + '.jpg')
    #plt.close()

    uc_10 = np.vstack((counts_10, unique_10)).T
    uc_30 = np.vstack((counts_30, unique_30)).T
    uc_100 = np.vstack((counts_100, unique_100)).T
    uc_50 = np.vstack((counts_50, unique_50)).T
    uc_500 = np.vstack((counts_500, unique_500)).T

    peaks_10, properties_10 = find_peaks(counts_10, prominence=20, height=5, wlen=5)
    peaks_30, properties_30 = find_peaks(counts_30, prominence=20, height=5, wlen=5)
    peaks_100, properties_100 = find_peaks(counts_100, prominence=20, height=5, wlen=5)
    peaks_50, properties_50 = find_peaks(counts_50, prominence=20, height=5, wlen=5)
    peaks_500, properties_500 = find_peaks(counts_500, prominence=20, height=5, wlen=5)

    x_10 = unique_10[peaks_10]
    x_30 = unique_30[peaks_30]
    x_100 = unique_100[peaks_100]
    x_50 = unique_50[peaks_50]
    x_500 = unique_500[peaks_500]

    y_10 = [counts_10[x] for x in peaks_10]
    y_30 = [counts_30[x] for x in peaks_30]
    y_100 = [counts_100[x] for x in peaks_100]
    y_50 = [counts_50[x] for x in peaks_50]
    y_500 = [counts_500[x] for x in peaks_500]

    time_10 = np.round(np.sum(x_10*y_10/np.sum(y_10)), 4)
    time_30 = np.round(np.sum(x_30*y_30/np.sum(y_30)), 4)
    time_100 = np.round(np.sum(x_100*y_100/np.sum(y_100)), 4)
    time_50 = np.round(np.sum(x_50*y_50/np.sum(y_50)), 4)
    time_500 = np.round(np.sum(x_500*y_500/np.sum(y_500)), 4)

    f, axs = plt.subplots(4, 1, figsize=(12, 12), sharey=True, sharex=True)
    plt.title(sensor)
    plt.xlabel('publishing intervall in seconds')
    plt.ylabel('count')

    axs[0].plot(unique_10, counts_10, label='10')
    axs[0].plot(x_10, y_10, "x")
    axs[0].legend()
    axs[0].set_title('weighted mean = ' + str(time_10))

    axs[1].plot(unique_30, counts_30, label='30')
    axs[1].plot(x_30, y_30, "x")
    axs[1].legend()
    axs[1].set_title('weighted mean = ' + str(time_30))

    axs[2].plot(unique_100, counts_100, label='100')
    axs[2].plot(x_100, y_100, "x")
    axs[2].legend()
    axs[2].set_title('weighted mean = ' + str(time_100))

    axs[3].plot(unique_50, counts_50, label='50')
    axs[3].plot(x_50, y_50, "x")
    axs[3].legend()
    axs[3].set_title('weighted mean = ' + str(time_50))

    #axs[4].plot(unique_500, counts_500, label='500')
    #axs[4].plot(x_500, y_500, "x")
    #axs[4].legend()
    #axs[4].set_title('weighted mean = ' + str(time_500))

    #f.savefig('images\\publishing period ohne 500\\subplots\\times_' + str(sensor) + '.jpg')
    #plt.close(f)
