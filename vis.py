"""
verschiedene visualisierungen
"""
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from helpers.lists import ids, val_id_type_dict, paths, sig_time
from helpers.functions import dfs_for_timetest_csv, sort_per_id, sort_per_id_vib

from datetime import datetime
import os
from ast import literal_eval
from scipy.stats import kurtosis, skew


#  das lassen wir feature engeneering letztendlich entscheiden, hier abschätzung


important_sensors = [4, 8, 13, 14, 16, 30, 31, 32,     33,34,35,36,37,38,       39,40,42,64,        43,44,45,46,47,48,   50,51,52,53,54,55,   57,58,59,60,61,62]
maybe_important = [3, 15, 17, 41]

int_sensor_values = [1, 2, 3, 6, 8, 9, 15, 17]
float_sensor_values = [4, 12, 13, 14, 16, 30, 31, 32, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56,
                       58, 59, 60, 61, 62, 63, 64]
bool_sensor_values = [0, 5, 7, 10, 11]
list_sensor_values = [33, 34, 35, 36, 37, 38, 43, 50, 57]
temp_sensor_values = [39, 40, 41, 42, 64]
#P_sensor_values =
relevant_sensors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 30, 31, 32, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 64]


def calc_timedelta_server_source(data):
    """
    :returns list of timedeltas of each row between the first and second col
    """
    # only if server and source time columns are there
    horizontal_timedeltas = []
    for i in range(data.shape[0]):
        timedelta = data.iloc[i, 0] - data.iloc[i, 1]
        horizontal_timedeltas.append(timedelta.total_seconds())
    return horizontal_timedeltas

def faster_timedetla_datachange(data, col = 0):
    timedeltas_between_rows = []
    timelist = data['source'].values
    for i in range(data.shape[0] - 1):
        #timedelta = data.iloc[i + 1, col] - data.iloc[i, col]
        #timedeltas_between_rows.append(timedelta.total_seconds())
        timedelta = (timelist[i+1] - timelist[i]) / np.timedelta64(1, 's')
        timedeltas_between_rows.append(timedelta)
    return timedeltas_between_rows

def calc_timedelta_datachange(data, col=0):
    """
    :param data: dataset that has a row with times/dates
    :param col: for which row?
    :return:  list, its one shorter than the original
    """
    timedeltas_between_rows = []
    for i in range(data.shape[0]-1):
        timedelta = data.iloc[i+1, col] - data.iloc[i, col]
        timedeltas_between_rows.append(timedelta.total_seconds())
    return timedeltas_between_rows

def plot_or_scatter_single_sensor(data, idx, scatter=True, scatter_size=2):
    if scatter:
        data[idx].plot.scatter(x='source', y='val', title=ids[idx], figsize=(20, 11), s=scatter_size)
    else:
        data[idx].plot(x='source', y='val', title=ids[idx], figsize=(20, 11))

def plot_timedelta_server_source_count(data, path, save=False):
    """
    saves or shows timedelta count between the times
    """

    unique, counts = np.unique(data, return_counts=True)

    # plt.figure() prevents drawing in an open figure
    plt.figure(figsize=(19, 10))

    plt.scatter(unique, counts, s=4)
    #plt.plot(unique, counts)
    plt.title('timedelta source pc: ' + os.path.basename(path))
    plt.xlabel('Timedelta in seconds')
    plt.ylabel('Count')
    if save:
        plt.savefig('images\\first tests\\timedeltas_server-source_count' + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + '.jpg')
        plt.close()
    else:
        plt.show()

def plot_timedelta_source_and_real_over_time(print_too=False, save=False):
    """
    Timedifference noticed.
    Server time to real time is off by about 2h, this checks whether it is constant or stationary
    :return:
    """

    # use all data till now
    data_path = 'C:\\Users\\Kuni\\PycharmProjects\\Übung\\Masterthesis\\data\\first tests'
    """
    # übung 1
    list_dir = os.listdir(data_path)
    abs_path_list = [os.path.join(data_path, x) for x in list_dir]
    abs_path_list_savetimes = [os.path.getmtime(x) for x in abs_path_list]
    str_paths_sorted = [x for (x, y) in sorted(zip(abs_path_list, abs_path_list_savetimes), key=lambda pair: pair[1])]
    """

    # way 2
    from pathlib import Path
    # sort paths by date of data saving on pc  # paths sorted nach änderungsdatum
    paths = sorted(Path(data_path).iterdir(), key=os.path.getmtime)
    str_paths_sorted = [str(x) for x in paths]

    # extract time
    date_str = [x[-23:-4] for x in str_paths_sorted]

    # since in the loaded data pd datetime is used, we use it here too, to be able to substract them
    target_timestamps = [pd.to_datetime(x, format='%d-%m-%Y_%H-%M-%S') for x in date_str]


    datasets = [dfs_for_timetest_csv(path, with_second_time=False, skip_initial_lines=False) for path in paths]

    empty_counter = 0
    str_counter = 0
    other_count = 0
    timedelta_list = []
    dates = []
    for i, j in enumerate(datasets):
        if j.shape[0] == 0:
            empty_counter += 1
            #timedelta_list.append('len=0')
        else:
            try:
                timedelta_list.append(target_timestamps[i] - j.iloc[0, 0])
                dates.append(target_timestamps[i])
            except:
                if type(j.iloc[0, 0]) == str:
                    str_counter += 1
                else:
                    other_count += 1
                #timedelta_list.append('str')
    print('empty datasets: ', empty_counter)
    print('str at 0,0: ', str_counter)
    print('useful datasets: ', len(datasets) - empty_counter - str_counter)
    print('other than time or str in data: ', other_count)

    if print_too:
        for i, j in enumerate(timedelta_list):
            print(i, j)

    seconds = [x.total_seconds() for x in timedelta_list]
    min_td = min(seconds)
    min_td_hours = int(min_td // 3600)
    min_td_minutes = int(min_td % 3600 // 60)
    min_td_seconds = round(min_td % 3600 % 60, 1)

    seconds_to_substract = min_td_hours * 3600 + min_td_minutes * 60 + min_td_seconds
    seconds = [x - seconds_to_substract for x in seconds]

    plt.figure()
    plt.scatter(dates, seconds, s=5)

    plt.title('timedelta between csv_created and first source time')

    plt.ylabel('seconds - (' + str(min_td_hours) + 'h + ' + str(min_td_minutes) + 'm + ' + str(min_td_seconds) + 's)')
    plt.xlabel('dates')
    plt.xticks(rotation=25)
    plt.tight_layout()

    if save:
        plt.savefig('images\\first tests\\timedelta_source_and_real_over_time' + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + '.jpg')
        plt.close()
    else:
        plt.show()

def plot_timedeltas_datachange(data, col, title, path='_none', save=False):
    delta_list = faster_timedetla_datachange(data, col)
    plt.figure(figsize=(19, 10))
    #print(delta_list[-5:])
    #print(delta_list[:5])
    #plt.scatter(data['source'][:-1], delta_list, s=5)

    plt.scatter(range(len(delta_list)), delta_list, s=5)
    #plt.title('row timedeltas of col: ' + col + '  ' + os.path.basename(path))
    plt.title(title)
    plt.xlabel('index')
    plt.ylabel('seconds')
    plt.ylim(0,120)
    if save:
        plt.savefig('images\\first tests\\timedeltas-rows of col-' + col + ' ' + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + '.jpg')
        plt.close()
    else:
        plt.show()
    #return delta_list

vvorschub = """
plt.figure(figsize= (19, 12))
plt.scatter(id_data[16]['source'], id_data[16]['val'])
plt.title(ids[16])
plt.xticks(rotation=25)
#"""

def get_update_intervalls(id_data):

    # TODO daten standardisieren
    simple_feature_columns = ['Max', 'Min', 'Peak-to-peak', 'Mean', 'Standard Dev.', 'RMS', 'Kurtosis', 'Skewness',
                              'Crest', 'Form factor', 'Variation Coefficient']
    features = np.zeros((len(ids), len(simple_feature_columns)))
    a60_data_path = paths[16]

    #a60_k1_b1 = dfs_for_timetest_csv(a60_data_path, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
    #id_data = sort_per_id(a60_k1_b1)
    for j, i in enumerate(id_data):
        i = np.array(calc_timedelta_datachange(i, 0))

        if j in relevant_sensors:
            print(j)
            features[j, 0] = np.max(i)
            features[j, 1] = np.min(i)
            features[j, 3] = np.mean(i)
            features[j, 4] = np.std(i, ddof=1)
            features[j, 5] = np.sqrt(np.mean(i ** 2))
            features[j, 6] = kurtosis(i)
            features[j, 7] = skew(i)
            features[j, 2] = features[j, 0] - features[j, 1]
            features[j, 8] = features[j, 0] / features[j, 5]
            features[j, 9] = features[j, 5] / features[j, 3]
            features[j, 10] = features[j, 4] / features[j, 3]

    aa = pd.DataFrame(features, columns=simple_feature_columns, index=ids)
    # drop all rows with 0
    aaa = aa.drop(aa[aa['Mean'] == 0].index)
    aaa = aaa.sort_values(by=['Mean'], ascending=False)
    #UI_a40_k1_b3.to_csv('Update_Intervall_a40_k1_b3.csv')
    return aaa

def get_bCutActives(data):
    cutactive_data = data[0]
    cutactive_true = cutactive_data.loc[cutactive_data['val'] == True]
    cutactive_false = cutactive_data.loc[cutactive_data['val'] == False]
    print('cutactives done')
    return cutactive_true, cutactive_false

#pd.read_csv('Update intervalls raw data\\Update_Intervall_a60_k1_b1.csv', index_col=0)
#pd.read_csv('Update intervalls raw data\\Update_Intervall_a60_k1_b2.csv', index_col=0)
#pd.read_csv('Update intervalls raw data\\Update_Intervall_a40_k1_b1.csv', index_col=0)
#pd.read_csv('Update intervalls raw data\\Update_Intervall_a40_k1_b2.csv', index_col=0)
#pd.read_csv('Update intervalls raw data\\Update_Intervall_a40_k1_b3.csv', index_col=0)


# skeleton
""" skeleton

def (delta_list, dataset_name, save=False):
    plt.figure()
    plt.()
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks(rotation=25)
    if save:
        plt.savefig('images\\first tests\\' + str(dataset_name) + '_' + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + '.jpg')
        plt.close()
    else:
        plt.show()


"""

def find_neighbours(value, df, colname):
    exactmatch = df[df[colname] == value]
    if not exactmatch.empty:
        return exactmatch.index
    else:
        lowerneighbour_ind = df[df[colname] < value][colname].idxmax()
        upperneighbour_ind = df[df[colname] > value][colname].idxmin()
        return [lowerneighbour_ind, upperneighbour_ind]


get_idx_list = """
numeric_sensors_without_vibs = []
indices = []
for i, j in enumerate(val_id_type_dict.keys()):
    if val_id_type_dict[j] == float:
        indices.append(i)
indices
#"""

"""
def plot_numeric_sensors(data, data2=None, subplots=False, save=False):
    for i, j in enumerate(data):
        try:
            if j.shape[0] != 0: # no errors for empty data
                if subplots:
                    fig, axs = plt.subplots(rows, 1, figsize=(19, 10), sharex=True, sharey=True)
                else:
                    id = ids[i]
                    plotty = j.plot(x='source', y='val', title=id, figsize=(20,11))
                if save:
                    plotty.figure.savefig('images\\' + id + '_' + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + '.jpg')
                    plt.close()
                print('plotted:', ids[i])
            else:
                print('len=0 at: ', ids[i])
        except:
            print('plot_all_sensors except empty ones at index: ', ids[i])
"""

def plot_signal_raw(id_data, seperate_file_for_sigraw=True, save=False):
    # Todo how many - cut off vorne und hinten - un terschied zuschen seperate file und gesamtfile

    if seperate_file_for_sigraw:
        print('then waht') # todo

    else:
        for i in range(33, 39, 2):# data and time are in two rows seperated
            rows = id_data[i].shape[0]
            fig, axs = plt.subplots(rows, 1, figsize=(19, 10), sharex=True, sharey=True)
            fig.suptitle(ids[i])
            for j in range(rows):
                if rows == 1:
                    # extrawurst falls nur eine Zeile vorhanden
                    axs.plot(id_data[i + 1]['val'].values[0], id_data[i]['val'].iloc[j][:])
                    timestamp = id_data[i].iloc[j][0]
                    timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')
                    axs.set_ylabel(timestamp_str[5:-3])
                else:
                    axs[j].plot(id_data[i + 1]['val'].values[0], id_data[i]['val'].iloc[j][:])
                    timestamp = id_data[i].iloc[j][0]
                    timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')
                    axs[j].set_ylabel(timestamp_str[5:-3])
            if save:
                fig.savefig('first tests\\' + ids[i] + '.jpg')
                plt.close(fig)
            else:
                plt.show()


"""
def plot_bool_sensors():
for i in [val_id_type_dict[x] for x in ids
fft_anf = id_data[5]
fft_anf_true = fft_anf.loc[fft_anf['val'] == True]
fft_anf_false = fft_anf.loc[fft_anf['val'] == False]

plt.scatter(fft_anf_true['source'], np.zeros(len(fft_anf_true['source'])), c='g', s=5)
plt.scatter(fft_anf_false['source'], np.zeros(len(fft_anf_true['source'])), c='r', s=5)

plt.vlines(fft_anf_true['source'], ymin=-1, ymax=+1, colors ='g', )
plt.vlines(fft_anf_false['source'], ymin=-1, ymax=+1, colors ='r',)
plt.xticks(rotation=25)

"""
def vibs123(data, bands=True, rest=False, save=False):
    cutactive_data = data[0]
    cutactive_true = cutactive_data.loc[cutactive_data['val'] == True]
    cutactive_false = cutactive_data.loc[cutactive_data['val'] == False]

    for g in range(43, 64):
        """
        if bands:
            # frequency bands
            if g in [43, 50, 57]:
                fig, axs = plt.subplots(8, 3, figsize=(20, 11), sharex=True, sharey='row')
              
                fig.suptitle(ids[g] + ' CutActive True/False g/r')
                titles = ['Zahn f', 'Zahn f 3ZpZ', 'Zahn f 4ZpZ', 'Hyd 23.33Hz', 'Säge 67hz', 'Säge 91Hz', 'Rolle',
                          'Säge 13.22Hz']
                for h in range(8):
                    #
                    frequ_band_per_idx1 = []
                    for i in range(data1[g].shape[0]):
                        frequ_band_per_idx1.append(data1[g]['val'].iloc[i][h])
                    freq_band_per_idx2 = []
                    for i in range(data2[g].shape[0]):
                        freq_band_per_idx2.append(data2[g]['val'].iloc[i][h])

                    axs[h, 1].plot(data2[g]['source'], freq_band_per_idx2)
                    # axs[h,1].set_ylabel(str(h + 1))
                    axs[h, 1].set_ylabel(titles[h])

                    axs[h, 1].scatter(cutactive_true2['source'], np.zeros(len(cutactive_true2['source'])), c='g',
                                      s=5)
                    axs[h, 1].scatter(cutactive_false2['source'], np.zeros(len(cutactive_false2['source'])), c='r',
                                      s=5)

                    axs[h, 0].plot(data1[g]['source'], frequ_band_per_idx1)
                    # axs[h,0].set_ylabel(str(h + 1))
                    axs[h, 0].set_ylabel(titles[h])

                    axs[h, 0].scatter(cutactive_true1['source'], np.zeros(len(cutactive_true1['source'])), c='g',
                                      s=5)
                    axs[h, 0].scatter(cutactive_false1['source'], np.zeros(len(cutactive_false1['source'])), c='r',
                                      s=5)
                if save:
                    fig.savefig(path + ids[g] + '.jpg')
                    plt.close(fig)
                """
    if rest:
        for i in range(5):
            try:
                fig, axs = plt.subplots(3, 1, figsize=(20, 11), sharex=True, sharey='row')
                #for j in [44, 51, 58]:
                #    plotty = data[j+i].plot(x='source', y='val', title=ids[j+i], figsize=(20, 11), ax=axs[0])
                #    plotty = data[j+i].plot(x='source', y='val', title=ids[j+i], figsize=(20, 11), ax=axs[1])
                #    plotty = data[j+i].plot(x='source', y='val', title=ids[j+i], figsize=(20, 11), ax=axs[2])
                plotty = data[44+i].plot(x='source', y='val', title=ids[44+i], figsize=(20, 11), ax=axs[0])
                plotty = data[51+i].plot(x='source', y='val', title=ids[51+i], figsize=(20, 11), ax=axs[1])
                plotty = data[58+i].plot(x='source', y='val', title=ids[58+i], figsize=(20, 11), ax=axs[2])
            except:
                print(ids[i+44] + ' has no data')


            #plotty.scatter(cutactive_true['source'], np.zeros(len(cutactive_true['source'])), c='g', s=5)
            #plotty.scatter(cutactive_false['source'], np.zeros(len(cutactive_false['source'])), c='r', s=5)
            #if save:
            #    plotty.figure.savefig(path + ids[g] + '.jpg')
            #    plt.close()

def plot_vibs(data1, path='images', data2=None, vdi=False, bands=True, rest=False, save=False, vgl_two=False):
    cutactive_data1 = data1[0]
    cutactive_true1 = cutactive_data1.loc[cutactive_data1['val'] == True]
    cutactive_false1 = cutactive_data1.loc[cutactive_data1['val'] == False]


    # all vibs in this range
    for g in range(43, 64):
        if vdi:
            if g in [49, 56, 63]:
                try:
                    # VDI dings fast immer
                    plotty = data1[g].plot(x='source', y='val', title=ids[g], figsize=(20, 11))
                    if save:
                        plotty.figure.savefig(path + ids[g] + '.jpg')
                        plt.close()
                except:
                    print('index:', g, 'might be empty.  [49, 56, 63] are VDI, may be empty')
        if bands:
            # frequency bands
            if g in [43, 50, 57]:

                if vgl_two:

                    cutactive_data2 = data2[0]
                    cutactive_true2 = cutactive_data2.loc[cutactive_data2['val'] == True]
                    cutactive_false2 = cutactive_data2.loc[cutactive_data2['val'] == False]


                    fig, axs = plt.subplots(8, 2, figsize=(20,11), sharex='col', sharey='row')
                    fig.suptitle(ids[g] + ' CutActive True/False g/r')
                    titles = ['Zahn f', 'Zahn f 3ZpZ', 'Zahn f 4ZpZ', 'Hyd 23.33Hz', 'Säge 67hz', 'Säge 91Hz', 'Rolle', 'Säge 13.22Hz']
                    for h in range(8):
                        #
                        frequ_band_per_idx1 = []
                        for i in range(data1[g].shape[0]):
                            frequ_band_per_idx1.append(data1[g]['val'].iloc[i][h])
                        freq_band_per_idx2 = []
                        for i in range(data2[g].shape[0]):
                            freq_band_per_idx2.append(data2[g]['val'].iloc[i][h])

                        axs[h,1].plot(data2[g]['source'], freq_band_per_idx2)
                        #axs[h,1].set_ylabel(str(h + 1))
                        axs[h,1].set_ylabel(titles[h])


                        axs[h,1].scatter(cutactive_true2['source'], np.zeros(len(cutactive_true2['source'])), c='g', s=5)
                        axs[h,1].scatter(cutactive_false2['source'], np.zeros(len(cutactive_false2['source'])), c='r', s=5)

                        axs[h,0].plot(data1[g]['source'], frequ_band_per_idx1)
                        #axs[h,0].set_ylabel(str(h + 1))
                        axs[h,0].set_ylabel(titles[h])


                        axs[h,0].scatter(cutactive_true1['source'], np.zeros(len(cutactive_true1['source'])), c='g', s=5)
                        axs[h,0].scatter(cutactive_false1['source'], np.zeros(len(cutactive_false1['source'])), c='r', s=5)
                    if save:
                        fig.savefig(path + ids[g] + '.jpg')
                        plt.close(fig)
                else:
                    fig, axs = plt.subplots(8, 1, figsize=(20,11), sharex='col', sharey='row')
                    fig.suptitle(ids[g] + ' CutActive True/False g/r')
                    titles = ['Zahn f', 'Zahn f 3ZpZ', 'Zahn f 4ZpZ', 'Hyd 23.33Hz', 'Säge 67hz', 'Säge 91Hz', 'Rolle', 'Säge 13.22Hz']
                    for h in range(8):
                        frequ_band_per_idx1 = []
                        for i in range(data1[g].shape[0]):
                            frequ_band_per_idx1.append(data1[g]['val'].iloc[i][h])

                        axs[h].plot(data1[g]['source'], frequ_band_per_idx1)
                        #axs[h].set_ylabel(str(h + 1))
                        axs[h].set_ylabel(titles[h])

                        axs[h].scatter(cutactive_true1['source'], np.zeros(len(cutactive_true1['source'])), c='g', s=5)
                        axs[h].scatter(cutactive_false1['source'], np.zeros(len(cutactive_false1['source'])), c='r', s=5)
                    if save:
                        fig.savefig(path + ids[g] + '.jpg')
                        plt.close(fig)

        if rest:
            try:
                plotty = data1[g].plot(x='source', y='val', title=ids[g], figsize=(20, 11))
                plotty.scatter(cutactive_true1['source'], np.zeros(len(cutactive_true1['source'])), c='g', s=5)
                plotty.scatter(cutactive_false1['source'], np.zeros(len(cutactive_false1['source'])), c='r', s=5)
                if save:
                    plotty.figure.savefig(path + ids[g] + '.jpg')
                    plt.close()
            except:
                print('no data')

def calculate_time_per_cut(id_data):
    # check when P_Vorschub suddenly drops, only look at low values so jumps at indices can be taken as start signal
    values_cut_time_calc = id_data[13].loc[id_data[13]['val'] <= 8]
    #Edelstahl 60
    print(values_cut_time_calc.loc[20637, 'source'] - values_cut_time_calc.loc[10293, 'source'])
    print(values_cut_time_calc.loc[31140, 'source'] - values_cut_time_calc.loc[20637, 'source'])
    #Alu 60
    print(values_cut_time_calc.loc[7026, 'source'] - values_cut_time_calc.loc[3309, 'source'])
    print(values_cut_time_calc.loc[10791, 'source'] - values_cut_time_calc.loc[7026, 'source'])
    #Alu 30
    print(values_cut_time_calc.loc[5369, 'source'] - values_cut_time_calc.loc[2383, 'source'])
    print(values_cut_time_calc.loc[8205, 'source'] - values_cut_time_calc.loc[5369, 'source'])
#calculate_time_per_cut()


def uniques_in_frequency_bands(data):
    listi = []
    for i in range(data.shape[0]):
        listi.append(data['val'].iloc[i])
    return [item for sublist in listi for item in sublist]

def print_unique_values_of_frequency_bands(with_second_time):
    paths = [path1, path2, path4, path5]

    for path in paths:
        df = dfs_for_timetest_csv(path, with_second_time)

        id_data = sort_per_id(df)
        listi = uniques_in_frequency_bands(id_data[57])
        print(np.unique(listi))


#data_path = paths[16]
#raw_path = paths
# skip 65 all, skip 47 no flatstream
#df_data = dfs_for_timetest_csv(data_path, with_second_time=True, skip_initial_lines=False, optional_skip_row=46)
#df_raw = dfs_for_timetest_csv(raw_path, with_second_time=True, skip_initial_lines=True, optional_skip_row=6)
#id_data = sort_per_id(df_data)
"""
a60_data_path = paths[16]
a60_sig_path = paths[17]
a40_data_path = paths[18]
a40_sig_path = paths[19]
s_data_path = paths[20]
# band 1
a60_k1_b1 = dfs_for_timetest_csv(a60_data_path, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)

a40_k1_b1 = dfs_for_timetest_csv(a40_data_path, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#s_k1_b1 = dfs_for_timetest_csv(s_data_path, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
# band 2
a60_k1_b2 = dfs_for_timetest_csv(paths[22], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
a40_k1_b2 = dfs_for_timetest_csv(paths[23], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
# band 3
a60_k1_b3 = dfs_for_timetest_csv(paths[24], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
a40_k1_b3 = dfs_for_timetest_csv(paths[25], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
# = dfs_for_timetest_csv(paths[27], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
# einlauf
einlauf1 = dfs_for_timetest_csv(paths[28], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
einlauf2 = dfs_for_timetest_csv(paths[29], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)

temptest = dfs_for_timetest_csv(paths[23], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)


#a60_k1_b1 = a60_k1_b1.sort_values(by=['source'])
#a40_k1_b1 = a40_k1_b1.sort_values(by=['source'])
#s_k1_b1 = s_k1_b1.sort_values(by=['source'])
id_a60_k1_b1 = sort_per_id(a60_k1_b1)
id_a40_k1_b1 = sort_per_id(a40_k1_b1)
#id_s_k1_b1 = sort_per_id(s_k1_b1)

id_a40_k1_b2 = sort_per_id(a40_k1_b2)
id_a60_k1_b2 = sort_per_id(a60_k1_b2)

id_a60_k1_b3 = sort_per_id(a60_k1_b3)
id_a40_k1_b3 = sort_per_id(a40_k1_b3)
#id_s_k1_b3 = sort_per_id(s_k1_b3)


id_einlauf1 = sort_per_id(einlauf1)
id_einlauf2 = sort_per_id(einlauf2)

id_temptest = sort_per_id(temptest)

#a60_sig = dfs_for_timetest_csv(a60_sig_path, with_second_time=True, skip_initial_lines=False, optional_skip_row=46)
#a60_sig.loc[:, 'val'] = a60_sig['val'].map(literal_eval)

#a40_k1_b1_sig = dfs_for_timetest_csv(a40_sig_path, with_second_time=True, skip_initial_lines=False, optional_skip_row=5)
#a40_sig.loc[:, 'val'] = a40_sig['val'].map(literal_eval)
anlauf = dfs_for_timetest_csv(paths[58], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
id_anlauf = sort_per_id(anlauf)
id_data = id_anlauf
"""
def insight_cutactive(id_data, title='placeholder', save=False):

    data = id_data[13]
    data1 = id_data[16]

    # signal vVorschub
    cutting_off = data1.loc[data1['val'] <= 0]
    cutting_on = data1.loc[data1['val'] > 0]
    np.sign(data1['val']).diff().ne(0)

    # take only the indices where the signs change
    abc = data.loc[(np.sign(data['val']).diff().ne(0))]
    abc0 = abc[abc['val'] == 0]
    abcneg = abc[abc['val'] < 0]
    abcpos = abc[abc['val'] > 0]

    cutactive_data = id_data[0]
    cutactive_true = cutactive_data.loc[cutactive_data['val'] == True]
    cutactive_false = cutactive_data.loc[cutactive_data['val'] == False]

    heben_data = id_data[10]
    heben_true = heben_data.loc[heben_data['val'] == True]
    heben_false = heben_data.loc[heben_data['val'] == False]

    fig, axs = plt.subplots(10, 1, figsize=(22, 16), sharex=True)

    fig.suptitle(title)
    axs[0].scatter(data['source'], data['val'], s=15, color='grey')
    axs[0].plot(data['source'], data['val'], label='P_Vorschub')

    axs[0].scatter(abcneg['source'], np.ones(abcneg['val'].shape[0]), s=15, color='red')
    axs[0].scatter(abc0['source'], np.ones(abc0['val'].shape[0]), s=15, color='blue')
    axs[0].scatter(abcpos['source'], np.ones(abcpos['val'].shape[0]), s=15, color='green')

    axs[0].scatter(cutactive_true['source'], np.full(len(cutactive_true['source']), 15), c='g', s=25)
    axs[0].scatter(cutactive_false['source'], np.full(len(cutactive_false['source']), 15), c='r', s=25)
    axs[0].plot(data['source'], np.full(len(data['source']), 15), label='cutactive')

    axs[0].scatter(heben_true['source'], np.full(len(heben_true['source']), 14), c='g', s=25)
    axs[0].scatter(heben_false['source'], np.full(len(heben_false['source']), 14), c='r', s=25)
    axs[0].plot(data['source'], np.full(len(data['source']), 14), label='Heben aktiv')

    axs[0].legend()
    # axs[0].set_ylim([5,20])

    # axs[0].set_title(ids[13])

    axs[1].scatter(data1['source'], data1['val'], s=15, color='grey')
    axs[1].plot(data1['source'], data1['val'], label='vVorschub')
    axs[1].scatter(abcneg['source'], np.ones(abcneg['val'].shape[0]), s=15, color='red')
    axs[1].scatter(abc0['source'], np.ones(abc0['val'].shape[0]), s=20, color='black')
    axs[1].scatter(abcpos['source'], np.ones(abcpos['val'].shape[0]), s=15, color='green')

    axs[1].plot(data1['source'], np.zeros(data1['source'].shape[0]), label='cutactive')
    axs[1].scatter(cutactive_true['source'], np.zeros(len(cutactive_true['source'])), c='g', s=20)
    axs[1].scatter(cutactive_false['source'], np.zeros(len(cutactive_false['source'])), c='r', s=20)

    axs[1].plot(data1['source'], np.full(len(data1['source']), -1), label='Heben aktiv')
    axs[1].scatter(heben_true['source'], np.full(len(heben_true['source']), -1), c='g', s=20)
    axs[1].scatter(heben_false['source'], np.full(len(heben_false['source']), -1), c='r', s=20)
    axs[1].legend()
    # axs[1].set_ylim([-15, 15])
    # axs[2].plot(id_data[14]['source'], id_data[14]['val'], label='Position')
    # axs[2].legend()

    # axs[1].set_title(ids[16])
    # """
    axs[2].plot(id_data[45]['source'], id_data[45]['val'], label=ids[45])
    axs[2].legend()
    # axs[2].set_ylim([500, 1800])

    axs[3].plot(id_data[52]['source'], id_data[52]['val'], label=ids[52])
    axs[3].legend()
    # axs[3].set_ylim([500, 1800])

    axs[4].plot(id_data[59]['source'], id_data[59]['val'], label=ids[59])
    axs[4].legend()
    # axs[4].set_ylim([0, 500])

    axs[5].plot(id_data[39]['source'], id_data[39]['val'], label='T1')
    axs[5].legend()
    # axs[5].set_ylim([20, 50])

    axs[6].plot(id_data[40]['source'], id_data[40]['val'], label='T2')
    axs[6].legend()
    # axs[6].set_ylim([20, 50])

    axs[7].plot(id_data[41]['source'], id_data[41]['val'], label='T3')
    axs[7].legend()
    # axs[7].set_ylim([20, 50])

    axs[8].plot(id_data[8]['source'], id_data[8]['val'], label='Hz')
    axs[8].legend()
    # axs[8].set_ylim([20, 50])

    axs[9].plot(id_data[64]['source'], id_data[64]['val'], label='T_IR')
    axs[9].legend()
    # axs[9].set_ylim([20, 50])
    # """
    if save:
        fig.savefig('images\\cutactiveerssatz_' + title + '.jpg')
        plt.close(fig)

sigraw_and_p_vorschub ="""

path40 = 'E:\\ausgelagert thesis daten\\Testband\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__13-46-22_26-02-2022_data.csv'
a40_k2_t = dfs_for_timetest_csv(path40, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
id_a40_k2_t = sort_per_id(a40_k2_t)

path40sig = 'E:\\ausgelagert thesis daten\\Testband\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__13-46-22_26-02-2022_SigRaw.csv'
a40_k2_t_sig = dfs_for_timetest_csv(path40sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
id_a40_k2_t_sig = sort_per_id_vib(a40_k2_t_sig)

data1 = id_a40_k2_t[13]
data2 = id_a40_k2_t[14]
data3 = id_a40_k2_t_sig[0]
data4 = id_a40_k2_t_sig[1]
data5 = id_a40_k2_t_sig[2]

from datetime import timedelta
def make_sigraw_timestamps(start_timestamp):
    timestamps = []
    for i in sig_time:
        timestamps.append(start_timestamp + timedelta(seconds=i))
    return timestamps

fig, axs = plt.subplots(5, 1, figsize=(22, 16), sharex=True)

axs[0].scatter(data1['source'], data1['val'], s=15, color='grey')
axs[0].plot(data1['source'], data1['val'], label='P_Vorschub')
axs[0].legend()

axs[1].plot(data2['source'], data2['val'], label='Position')
axs[1].legend()
for i in range(6//3):
    axs[2].plot(make_sigraw_timestamps(data3.iloc[i, 0]), data3.iloc[i, 4], label='Raw 1', color='b')
    axs[2].legend()

    axs[3].plot(make_sigraw_timestamps(data4.iloc[i, 0]), data4.iloc[i, 4], label='Raw 2', color='b')
    axs[3].legend()

    axs[4].plot(make_sigraw_timestamps(data5.iloc[i, 0]), data5.iloc[i, 4], label='Raw 3', color='b')
    axs[4].legend()
#"""

hammertest = """
pathhammer = 'data\\LeertestkeinMaterial_Vors-0_Bandv-0_5-ms__07-41-56_11-03-2022_data.csv'
hammer = dfs_for_timetest_csv(pathhammer, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
id_hammer = sort_per_id(hammer)
vibs123(id_hammer, rest=True)



hammer = dfs_for_timetest_csv(paths[51], with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
id_hammer = sort_per_id(hammer)
insight_cutactive(id_hammer, title='Klasse 1')

hammer = dfs_for_timetest_csv(paths[54], with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
id_hammer = sort_per_id(hammer)
insight_cutactive(id_hammer, title='Klasse 2')
#"""


vierter_Bruch = """
pathwtf = 'data\\Trainingsband\\4\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_data.csv'
wtf = dfs_for_timetest_csv(pathwtf, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
id_wtf = sort_per_id(wtf)
insight_cutactive(id_wtf, title='wtf')
#"""



testband_load_data = """
data36 = dfs_for_timetest_csv(paths[36], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data37 = dfs_for_timetest_csv(paths[37], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data38 = dfs_for_timetest_csv(paths[38], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data39 = dfs_for_timetest_csv(paths[39], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data40 = dfs_for_timetest_csv(paths[40], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data41 = dfs_for_timetest_csv(paths[41], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data42 = dfs_for_timetest_csv(paths[42], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data43 = dfs_for_timetest_csv(paths[43], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data44 = dfs_for_timetest_csv(paths[44], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data45 = dfs_for_timetest_csv(paths[45], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data46 = dfs_for_timetest_csv(paths[46], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data47 = dfs_for_timetest_csv(paths[47], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data48 = dfs_for_timetest_csv(paths[48], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data49 = dfs_for_timetest_csv(paths[49], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data50 = dfs_for_timetest_csv(paths[50], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data36 = sort_per_id(data36)
data37 = sort_per_id(data37)
data38 = sort_per_id(data38)
data39 = sort_per_id(data39)
data40 = sort_per_id(data40)
data41 = sort_per_id(data41)
data42 = sort_per_id(data42)
data43 = sort_per_id(data43)
data44 = sort_per_id(data44)
data45 = sort_per_id(data45)
data46 = sort_per_id(data46)
data47 = sort_per_id(data47)
data48 = sort_per_id(data48)
data49 = sort_per_id(data49)
data50 = sort_per_id(data50)
#"""
testband_subplots_P_V_vorschub_sig = """
insight_cutactive(data36, 'Klasse_1_Alu-60-90')
insight_cutactive(data37, 'Klasse_1_Alu-40-90')
insight_cutactive(data38, 'Klasse_1_Alu-40-75')
insight_cutactive(data39, 'Klasse_2_Alu-60-90')
insight_cutactive(data40, 'Klasse_2_Alu-40-90')
insight_cutactive(data41, 'Klasse_2_Alu-40-75')
insight_cutactive(data42, 'Klasse_3_Alu-60-90')
insight_cutactive(data43, 'Klasse_3_Alu-40-90')
insight_cutactive(data44, 'Klasse_3_Alu-40-75')
insight_cutactive(data45, 'Klasse_4_Alu-60-90')
insight_cutactive(data46, 'Klasse_4_Alu-40-90')
insight_cutactive(data47, 'Klasse_4_Alu-40-75')
insight_cutactive(data48, 'Klasse_5_Alu-60-90')
insight_cutactive(data49, 'Klasse_5_Alu-40-90')
insight_cutactive(data50, 'Klasse_5_Alu-40-75')
#"""
Trainband_load_data = """
# Trainingsband
data51 = dfs_for_timetest_csv(paths[51], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data52 = dfs_for_timetest_csv(paths[52], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data53 = dfs_for_timetest_csv(paths[53], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data54 = dfs_for_timetest_csv(paths[54], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data55 = dfs_for_timetest_csv(paths[55], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data56 = dfs_for_timetest_csv(paths[56], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data57 = dfs_for_timetest_csv(paths[57], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data51 = sort_per_id(data51)
data52 = sort_per_id(data52)
data53 = sort_per_id(data53)
data54 = sort_per_id(data54)
data55 = sort_per_id(data55)
data56 = sort_per_id(data56)
data57 = sort_per_id(data57)
data58 = dfs_for_timetest_csv(paths[34], with_second_time=True, skip_initial_lines=True, optional_skip_row=46) # Teil von data56
#"""


def get_cuts(data, idx, cuts_manual):
    cutactive_data = data[0]
    cutactive_true = cutactive_data.loc[cutactive_data['val'] == True]
    cutactive_false = cutactive_data.loc[cutactive_data['val'] == False]


    vVorschub_data = data[16]['val'].values
    start_list = []
    stop_list = []
    #for i in range(vVorschub_data.shape[0]):

    cutting_off = data[16].loc[data[16]['val'] <= 0]
    cutting_on = data[16].loc[data[16]['val'] > 0]

    trues = len(cutactive_true)
    falses = len(cutactive_false)
    cuts = min(trues, falses)
    #print(cuts)

    if cutactive_data.iloc[0,4] == False:
        # if cutactive False is the first value, we skip it by adding one to the index below
        helper = 1
    else:
        helper = 0

    cut_list = []
    for i in range(cuts):

        # select values between cutactive true and false
        one_cut = data[idx][data[idx]['source'].between(cutactive_true.iloc[0+i, 0], cutactive_false.iloc[0+i+helper, 0])]
        cut_list.append(one_cut['val'].values)

    return cut_list


"""
cuts_a60_k1_b1 = 151
cuts_a40_k1_b1 = 149
cuts_a60_k1_b2 = 157
cuts_a40_k1_b2 = 150 - 1
cuts_a60_k1_b3 = 149
cuts_a40_k1_b3 = 149-1
cuts_a40_e1 = 56
cuts_a40_e2 = 41

cuts_s = 9
idx = [8, 14, 30, 31, 13, 16, 44, 51, 58, 64]
means_60_k1_b1 = np.zeros((cuts_a60_k1_b1, len(idx)))
means_40_k1_b1 = np.zeros((cuts_a40_k1_b1, len(idx)))
means_60_k1_b2 = np.zeros((cuts_a60_k1_b2, len(idx)))
means_40_k1_b2 = np.zeros((cuts_a40_k1_b2, len(idx)))
means_60_k1_b3 = np.zeros((cuts_a60_k1_b3, len(idx)))
means_40_k1_b3 = np.zeros((cuts_a40_k1_b3, len(idx)))
means_40_e1 = np.zeros((cuts_a40_e1, len(idx)))
means_40_e2 = np.zeros((cuts_a40_e2, len(idx)))

#means_s = np.zeros((cuts_s, len(idx)))


for i, j in enumerate(idx):
    cut_vals60_k1_b1 = get_cuts(id_a60_k1_b1, j, cuts_a60_k1_b1)
    cut_vals40_k1_b1 = get_cuts(id_a40_k1_b1, j, cuts_a40_k1_b1)
    cut_vals60_k1_b2 = get_cuts(id_a60_k1_b2, j, cuts_a60_k1_b2)
    cut_vals40_k1_b2 = get_cuts(id_a40_k1_b2, j, cuts_a40_k1_b2)
    cut_vals60_k1_b3 = get_cuts(id_a60_k1_b3, j, cuts_a60_k1_b3)
    cut_vals40_k1_b3 = get_cuts(id_a40_k1_b3, j, cuts_a40_k1_b3)
    cut_vals40_e1 = get_cuts(id_einlauf1, j, cuts_a40_e1)
    cut_vals40_e2 = get_cuts(id_einlauf2, j, cuts_a40_e2)
    #cut_valss = get_cuts(id_s_k1_b1, j, cuts_s)


    mean_row60_k1_b1 = [np.mean(x) for x in cut_vals60_k1_b1]
    mean_row40_k1_b1 = [np.mean(x) for x in cut_vals40_k1_b1]
    mean_row60_k1_b2 = [np.mean(x) for x in cut_vals60_k1_b2]
    mean_row40_k1_b2 = [np.mean(x) for x in cut_vals40_k1_b2]
    mean_row60_k1_b3 = [np.mean(x) for x in cut_vals60_k1_b3]
    mean_row40_k1_b3 = [np.mean(x) for x in cut_vals40_k1_b3]
    mean_row40_e1 = [np.mean(x) for x in cut_vals40_e1]
    mean_row40_e2 = [np.mean(x) for x in cut_vals40_e2]
    #mean_row_s = [np.mean(x) for x in cut_valss]


    means_60_k1_b1[:, i] = mean_row60_k1_b1
    means_40_k1_b1[:, i] = mean_row40_k1_b1
    means_60_k1_b2[:, i] = mean_row60_k1_b2
    means_40_k1_b2[:, i] = mean_row40_k1_b2
    means_60_k1_b3[:, i] = mean_row60_k1_b3
    means_40_k1_b3[:, i] = mean_row40_k1_b3
    means_40_e1[:, i] = mean_row40_e1
    means_40_e2[:, i] = mean_row40_e2
    #means_s[:, i] = mean_row_s


mmeans_60_k1_b1_mean = np.mean(means_60_k1_b1, axis=0)
mmeans_40_k1_b1_mean = np.mean(means_40_k1_b1, axis=0)
mmeans_60_k1_b2_mean = np.mean(means_60_k1_b2, axis=0)
mmeans_40_k1_b2_mean = np.mean(means_40_k1_b2, axis=0)
mmeans_60_k1_b3_mean = np.mean(means_60_k1_b3, axis=0)
mmeans_40_k1_b3_mean = np.mean(means_40_k1_b3, axis=0)
mmeans_40_e1_mean = np.mean(means_40_e1, axis=0)
mmeans_40_e2_mean = np.mean(means_40_e2, axis=0)


idx = [8, 14, 30, 31, 13, 16, 44, 51, 58, 64]
idx_names = [ids[x] for x in idx]
plt.figure(figsize=(19, 10))
#plt.scatter(idx_names, mmeans_60_k1_b1_mean, s=4, color='blue')
#plt.scatter(idx_names, mmeans_40_k1_b1_mean, s=4, color='red')
plt.scatter(idx_names, mmeans_60_k1_b2_mean, s=4, color='blue')
plt.scatter(idx_names, mmeans_40_k1_b2_mean, s=4, color='red')
plt.scatter(idx_names, mmeans_60_k1_b3_mean, s=4, color='blue')
plt.scatter(idx_names, mmeans_40_k1_b3_mean, s=4, color='red')
#plt.xticks(rotation=25, labels=idx_names)


#idx = [14, 30, 13, 16, 44, 51, 58]

fig, axs = plt.subplots(len(idx), 2, figsize=(20, 11), sharex=True, sharey='row')
fig.suptitle('same color for same sawblade')
for f, g in enumerate(idx):
    axs[f, 1].scatter(range(len(means_60_k1_b1[:, f])), means_60_k1_b1[:, f], s=3, color='blue')
    axs[f, 0].scatter(range(len(means_40_k1_b1[:, f])), means_40_k1_b1[:, f], s=3, color='blue')
    axs[f, 1].scatter(range(len(means_60_k1_b2[:, f])), means_60_k1_b2[:, f], s=3, color='green')
    axs[f, 0].scatter(range(len(means_40_k1_b2[:, f])), means_40_k1_b2[:, f], s=3, color='green')
    axs[f, 1].scatter(range(len(means_60_k1_b3[:, f])), means_60_k1_b3[:, f], s=3, color='red')
    axs[f, 0].scatter(range(len(means_40_k1_b3[:, f])), means_40_k1_b3[:, f], s=3, color='red')
    axs[f, 0].set_title(ids[g] + 'Alu 40')
    axs[f, 1].set_title(ids[g] + 'Alu 60')

fig, axs = plt.subplots(len(idx), 1, figsize=(20, 11), sharex=True, sharey='row')
fig.suptitle(' Band 2+3 red = Alu40, blue = Alu60')
for f, g in enumerate(idx):
    #axs[f].scatter(range(len(means_60_k1_b1[:, f])), means_60_k1_b1[:, f], s=6, color='blue')
    #axs[f].scatter(range(len(means_40_k1_b1[:, f])), means_40_k1_b1[:, f], s=6, color='red')
    axs[f].scatter(range(len(means_60_k1_b2[:, f])), means_60_k1_b2[:, f], s=6, color='blue')
    axs[f].scatter(range(len(means_40_k1_b2[:, f])), means_40_k1_b2[:, f], s=6, color='red')
    axs[f].scatter(range(len(means_60_k1_b3[:, f])), means_60_k1_b3[:, f], s=6, color='blue')
    axs[f].scatter(range(len(means_40_k1_b3[:, f])), means_40_k1_b3[:, f], s=6, color='red')
    axs[f].set_title(ids[g])

# einlaufbänder
fig, axs = plt.subplots(len(idx), 1, figsize=(20, 11), sharex=True, sharey='row')
fig.suptitle('')
for f, g in enumerate(idx):
    axs[f].plot(range(len(means_40_e1[:, f])), means_40_e1[:, f], color='blue')
    axs[f].plot(range(len(means_40_e2[:, f])), means_40_e2[:, f], color='red')
    axs[f].set_title(ids[g])


plt.figure(figsize=(19, 10))
cut_vals60_k1_b1 = get_cuts(id_a60_k1_b1, 14, cuts_a60_k1_b1)
cut_vals60_k1_b2 = get_cuts(id_a60_k1_b2, 14, cuts_a60_k1_b2)
cut_vals60_k1_b3 = get_cuts(id_a60_k1_b3, 14, cuts_a60_k1_b3)

plt.figure(figsize=(19, 10))
for i in range(5):
    plt.plot(cut_vals60_k1_b1[i], color='red', label='band 1')
    plt.plot(cut_vals60_k1_b2[i], color='green', label='band 2')
    plt.plot(cut_vals60_k1_b3[i], color='blue', label='band 3')
plt.legend()


plot_vibs(id_a60_k1_b2, id_a40_k1_b2,'path', vdi=False, bands=True, rest=False, save=False)
"""

"""
# plot a few useful next to each other
data = id_a40_k1_b1
data1 = id_einlauf2

#id_a60_k1_b21

cutactive_data = data[0]
cutactive_true = cutactive_data.loc[cutactive_data['val'] == True]
cutactive_false = cutactive_data.loc[cutactive_data['val'] == False]
idx = [8, 14, 30, 31,13, 16,44,51, 58,39,40,64]
#idx = [14, 30, 13, 16,44, 45, 46, 47, 48]
#idx = [14, 30, 13, 16,44,51, 58]
fig, axs = plt.subplots(len(idx), 1, figsize=(20,11), sharey='row', sharex=True)
for f, g in enumerate(idx):
    plotty = data[g].plot.scatter(x='source', y='val', title=ids[g], figsize=(20, 11), ax=axs[f], s=2, color='blue')
    #plotty = data1[g].plot.scatter(x='source', y='val', title=ids[g], figsize=(20, 11), ax=axs[f], s=2, color='green')

plotty.scatter(cutactive_true['source'], np.zeros(len(cutactive_true['source'])), c='g', s=5)
plotty.scatter(cutactive_false['source'], np.zeros(len(cutactive_false['source'])), c='r', s=5)


data2 = id_a60_k1_b1

# plot all vibs 3x7
vib1 = [44, 45, 46, 47, 48]
vib2 = [51, 52, 53, 54, 55]
vib3 = [58, 59, 60, 61, 62]

vibs = [vib1, vib2, vib3]

fig, axs = plt.subplots(len(vib1), 3, figsize=(20,11), sharex=True)
for i, j in enumerate(vibs):
    for f, g in enumerate(j):
        plotty = data2[g].plot(x='source', y='val', title=ids[g], figsize=(20, 11), ax=axs[f, i])

"""

"""
timedelta_per_datachange_sensors_source = calc_timedelta_datachange(df_data, 0)
timedelta_per_datachange_sensors_pc = calc_timedelta_datachange(df_data, 1)
#timedelta_per_datachange_raw_source = calc_timedelta_datachange(df_raw, 0)
#timedelta_per_datachange_raw_pc = calc_timedelta_datachange(df_raw, 1)
plot_timedeltas_datachange(timedelta_per_datachange_sensors_source, data_path, 'source', save=True)
plot_timedeltas_datachange(timedelta_per_datachange_sensors_pc, data_path, 'pc', save=True)
#plot_timedeltas_datachange(timedelta_per_datachange_raw_source, raw_path, 'source', save=True)
#plot_timedeltas_datachange(timedelta_per_datachange_raw_pc, raw_path, 'pc', save=True)

timedelta_server_source_data = calc_timedelta_server_source(df_data)
#timedelta_server_source_raw = calc_timedelta_server_source(df_raw)
plot_timedelta_server_source_count(timedelta_server_source_data, data_path, save=True)
#plot_timedelta_server_source_count(timedelta_server_source_raw, raw_path)
"""

#plot_timedelta_source_and_real_over_time(save=True)

#plot_numeric_sensors(id_a60, save=True)
#plot_signal_raw()
#plot_vibs(id_a60, 'images\\failed trainingbaender\\')

#plot_timedelta_source_and_real_over_time()
# print_unique_values_of_frequency_bands(with_second_time=True)



# How many time points are needed i,e., Sampling Frequency



#dft_magnitudes = np.abs(np.fft.rfft(np.vstack([id_data[34]['val'].iloc[0], id_data[33]['val'].iloc[0]]), axis=1))

"""
from numpy import array, sign, zeros
from scipy.interpolate import interp1d
from matplotlib.pyplot import plot,show,grid

signal_raw_time = np.array(id_data[34]['val'].iloc[0])
signal_raw_value = np.array(id_data[33]['val'].iloc[0])
signal_raw_time = pd.DataFrame(data={'value': signal_raw_value}, index=signal_raw_time)


from scipy.signal import hilbert
duration = 1.5885576009750366
fs = 5157
samples = int(fs*duration)
t = np.arange(samples) / fs


analytic_signal = hilbert(signal_raw_value)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = np.diff(instantaneous_phase) / (2.0*np.pi) * fs

fig, ax = plt.subplots(nrows=2, sharex=True)
ax[0].plot(signal_raw_time, signal_raw_value, c="b")
ax[0].plot(signal_raw_time, amplitude_envelope)
ax[1].plot(signal_raw_time.values[1:], instantaneous_frequency)
ax[1].set_xlabel("time in seconds")




x = np.arange(0, 20.1, 0.1)
y = abs(np.sin(x)) * np.sin(x*20)

x = signal_raw_time[:100]
y = signal_raw_value[:100]



analytic_signal = hilbert(y)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = np.diff(instantaneous_phase) / (2.0*np.pi) * fs



fig, ax = plt.subplots(nrows=2, sharex=True)
ax[0].plot(x, y, label="original")
ax[0].plot(x, amplitude_envelope, label='r')
ax[0].legend()
ax[1].plot(x[1:], instantaneous_frequency)
ax[1].set_xlabel("time in seconds")

"""




#----------------------------------
# only if both times are read/saved
# delete servertime
# df = df.drop(['server'], axis=1)

#df = df.drop(['server'], axis=1)



def plot_fraktale_sampling_intervall_signal_raw():
    # check sampling interval of signal raw time, should be
    sampling_intervall_signal_raw = []
    for i in range(len(id_data[34]['val'].iloc[0]) - 1):
        sampling_intervall_signal_raw.append(id_data[34]['val'].iloc[0][i + 1] - id_data[34]['val'].iloc[0][i])

    timedeltas_sampling_intervall_signal_raw = []
    for i, j in enumerate(sampling_intervall_signal_raw):
        if i == 0:
            continue
        i -= 1
        timedeltas_sampling_intervall_signal_raw.append(j - sampling_intervall_signal_raw[i])

    again_timedeltas_sampling_intervall_signal_raw = []
    for i, j in enumerate(timedeltas_sampling_intervall_signal_raw):
        if i == 0:
            continue
        i -= 1

        again_timedeltas_sampling_intervall_signal_raw.append(j - timedeltas_sampling_intervall_signal_raw[i])

    again_timedeltas_sampling_intervall_signal_raw_2 = []
    for i, j in enumerate(again_timedeltas_sampling_intervall_signal_raw):
        if i == 0:
            continue
        i -= 1
        again_timedeltas_sampling_intervall_signal_raw_2.append(j - again_timedeltas_sampling_intervall_signal_raw[i])

    lengths = [4000, 400, 200, 40]

    fig, axs = plt.subplots(4,5, figsize=(12, 8))
    axs[0, 0].scatter(list(range(len(sampling_intervall_signal_raw))), sampling_intervall_signal_raw, s=1)
    for i, j in enumerate(lengths):
        axs[0, i+1].scatter(list(range(len(sampling_intervall_signal_raw[:j]))), sampling_intervall_signal_raw[:j], s=1)

    #axs[0,0].set_title('"checking 1/f", Timedeltas of signal_raw')

    axs[1,0].scatter(list(range(len(timedeltas_sampling_intervall_signal_raw))), timedeltas_sampling_intervall_signal_raw, s=1)
    for i, j in enumerate(lengths):
        axs[1, i+1].scatter(list(range(len(timedeltas_sampling_intervall_signal_raw[:j]))), timedeltas_sampling_intervall_signal_raw[:j], s=1)
    #axs[1, 0].set_title('"checking 1/f consitency", Timedeltas of Timedeltas of signal_raw')

    axs[2,0].scatter(list(range(len(again_timedeltas_sampling_intervall_signal_raw))), again_timedeltas_sampling_intervall_signal_raw, s=1)
    for i, j in enumerate(lengths):
        axs[2, i+1].scatter(list(range(len(again_timedeltas_sampling_intervall_signal_raw[:j]))), again_timedeltas_sampling_intervall_signal_raw[:j], s=1)
    axs[3,0].scatter(list(range(len(again_timedeltas_sampling_intervall_signal_raw_2))), again_timedeltas_sampling_intervall_signal_raw_2, s=1)
    for i, j in enumerate(lengths):
        axs[3, i+1].scatter(list(range(len(again_timedeltas_sampling_intervall_signal_raw_2[:j]))), again_timedeltas_sampling_intervall_signal_raw_2[:j], s=1)
    plt.tight_layout()


    list(range(70, 92, 2))

def plot_fft_hk_raw():
    """
    run this with the initial lines, to get the signal times
    :return:
    """
    # At what intervals time points are sampled
    sampling_frequency = 5157
    sampling_interval = 1 / sampling_frequency


    # Create subplot
    figure, axis = plt.subplots(6, 1)
    plt.subplots_adjust(hspace=0.5)

    # Time domain representation for sine wave 1
    axis[0].set_title('Raw Signal Sent From SPS')
    axis[0].plot(id_data[34]['val'].iloc[0], id_data[33]['val'].iloc[0])
    axis[0].set_xlabel('Time')
    axis[0].set_ylabel('Amplitude')

    # Time domain representation for sine wave 2
    axis[1].set_title('FFT_Raw Sent From SPS')
    axis[1].plot(id_data[25]['val'].iloc[0], id_data[24]['val'].iloc[0])
    axis[1].set_xlabel('Time')
    axis[1].set_ylabel('Amplitude')

    # Frequency domain representation
    fourierTransform = np.abs(np.fft.rfft(id_data[33]['val'].iloc[0]) / len(id_data[33]['val'].iloc[0]))  # Normalize amplitude)
    fourierTransform = fourierTransform[range(int(len(id_data[33]['val'].iloc[0]) / 2))]  # Exclude sampling frequency
    tpCount = len(id_data[33]['val'].iloc[0])
    values = np.arange(int(tpCount / 2))
    timePeriod = tpCount / sampling_frequency
    frequencies = values / timePeriod

    fourierTransform[0] = 0

    axis[2].set_title('Computed FFT Of Raw Signal')
    axis[2].plot(frequencies, fourierTransform)
    axis[2].set_xlabel('Frequency')
    axis[2].set_ylabel('Amplitude')

    axis[3].set_title('FFT Of Envelope From SPS')
    axis[3].plot(id_data[19]['val'].iloc[0], id_data[18]['val'].iloc[0])
    axis[3].set_xlabel('Frequency')
    axis[3].set_ylabel('Amplitude')

    signal_raw_time = np.array(id_data[34]['val'].iloc[0])
    signal_raw_value = np.array(id_data[33]['val'].iloc[0])
    signal_raw_time = pd.DataFrame(data={'value': signal_raw_value}, index=signal_raw_time)
    windowsize = 10
    HK_upper_raw_signal = signal_raw_time['value'].rolling(window=windowsize).max().shift(int(-windowsize / 2))
    HK_lower_raw_signal = signal_raw_time['value'].rolling(window=windowsize).min().shift(int(-windowsize / 2))

    fourierTransform_h = np.abs(np.fft.rfft(HK_upper_raw_signal / len(HK_upper_raw_signal)))  # Normalize amplitude)
    fourierTransform_h = fourierTransform_h[range(int(len(HK_upper_raw_signal) / 2))]  # Exclude sampling frequency
    tpCount = len(HK_upper_raw_signal)
    values = np.arange(int(tpCount / 2))
    timePeriod = tpCount / sampling_frequency
    frequencies_h = values / timePeriod

    fourierTransform_h[0] = 0

    axis[4].set_title('Computed Evelope From Raw Signal')
    axis[4].plot(HK_upper_raw_signal, label='upper')
    axis[4].plot(HK_lower_raw_signal, label='lower')
    axis[4].set_xlabel('Frequency')
    axis[4].set_ylabel('Amplitude')
    axis[5].legend()

    axis[5].set_title('HK from raw')
    axis[5].plot()
    axis[5].set_xlabel('Frequency')
    axis[5].set_ylabel('Amplitude')
    plt.legend()
    plt.show()

#if __name__ == "__main__":
#    print('where do i read this? comes from vis')
