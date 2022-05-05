import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def timedelta_mean_min_per_id(data):

    fill_this = np.ones((len(data), 3))
    for i, j in enumerate(data):
        delta_list = np.array(calc_timedelta_datachange(j, 0))

        # only take the
        #if val_id_type_dict[ids[i]] == float or bool:
        try:
            fill_this[i, 0] = delta_list.mean()
            fill_this[i, 1] = delta_list.max()
            fill_this[i, 2] = delta_list.min()

            #print('mean:', delta_list.mean(), 'min:', delta_list.min(),   ids[i])
        #elif val_id_type_dict[ids[i]] == list:
        except:
            print('except',i)
            fill_this[i, 0] = 0
            fill_this[i, 1] = 0
            fill_this[i, 2] = 0
            #print('----:', len(delta_list), ids[i])
    #return pd.DataFrame(data=fill_this, columns=count_header)
    return fill_this

def create_table_timedeltas_vgl_datasets():

    paths = [path1, path2, path4, path5]
    subdataset_results = []
    for path in paths:
        df = dfs_for_timetest_csv(path, with_second_time=True)
        id_data_sub = sort_per_id(df)
        subdataset_results.append(timedelta_mean_min_per_id(id_data_sub))

    count_header = ['Edelstahl-mean', 'Alu60-mean', 'Alu30-30ms-mean', 'Alu30-2ms-mean',
                    'Edelstahl-max', 'Alu60-max', 'Alu30-30ms-max', 'Alu30-2ms-max',
                    'Edelstahl-min', 'Alu60-min', 'Alu30-30ms-min', 'Alu30-2ms-min']

    #nd_timedeltas = np.hstack(subdataset_results)
    nd_timedeltas = np.ones((64, 12))
    for i in range(4):
        for j in range(3):
            nd_timedeltas[:, i+4*j] = subdataset_results[i][:, j]
            print(i+4*j)
        print('\n')

    nd_timedeltas = np.round(nd_timedeltas, 2)
    df_timedeltas = pd.DataFrame(data=nd_timedeltas, columns=count_header, index=ids)
    #df_timedeltas.to_csv('timedeltas.csv')
    return  df_timedeltas
#aa = create_table_timedeltas_vgl_datasets()


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