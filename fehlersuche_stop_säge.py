"""
am 02.03. trat eine plätzliche, starke Geschwindigkeitsabhanme auf, diese visualisierung half bei der Fehlersuche
"""

from helpers.functions import dfs_for_timetest_csv, sort_per_id
from helpers.lists import ids, val_id_type_dict, paths, short_labels
import matplotlib.pyplot as plt
import numpy as np
import vis

#band bleibt stehen
#data = dfs_for_timetest_csv(paths[31], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#data1 = dfs_for_timetest_csv(paths[32], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)

# band langsamer
#data = dfs_for_timetest_csv(paths[33], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#data1 = dfs_for_timetest_csv(paths[34], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#data2 = dfs_for_timetest_csv(paths[35], with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#data = sort_per_id(data) # a 40 2.3.
#data1 = sort_per_id(data1) # a40 1.3.
#data2 = sort_per_id(data2)  #a60 2.3.

#Testband
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

data_test = [
data36,
data37,
data38,
data39,
data40,
data41,
data42,
data43,
data44,
data45,
data46,
data47,
data48,
data49,
data50
]

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
#data58 = dfs_for_timetest_csv(paths[34], with_second_time=True, skip_initial_lines=True, optional_skip_row=46) # Teil von data56
#data58 = dfs_for_timetest_csv('data\\RiementestkeinMaterial_Vors-0_Bandv-0_5-ms__07-31-50_11-03-2022_data.csv', with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#data58 = sort_per_id(data58)
data_train = [
data51,
data52,
data53,
data54,
data55,
data56,
data57,
#data58
]




#id_a60_k1_b21

#cutactive_data = data[0]
#cutactive_true = cutactive_data.loc[cutactive_data['val'] == True]
#cutactive_false = cutactive_data.loc[cutactive_data['val'] == False]
idx = [8, 14, 30, 31,13, 16,44,51, 58,39,40,64]
#idx = [14, 30, 13, 16,44, 45, 46, 47, 48]
#idx = [14, 30, 13, 16,44,51, 58]


id = 8
fig, axs = plt.subplots(len(data_test), 2, figsize=(20,11), sharey=True, sharex=True)
fig.suptitle(ids[id])

#for f, g in enumerate(idx):
for f in range(0,15):
    #plotty = data[g].plot.scatter(x='source', y='val', title=ids[g], figsize=(20, 11), ax=axs[f], s=2, color='blue')
    #plotty = data1[g].plot.scatter(x='source', y='val', title=ids[g], figsize=(20, 11), ax=axs[f], s=2, color='green')

    axs[f, 0].plot(data_test[f][id]['val'])
    try:
        axs[f, 1].plot(data_train[f][id]['val'])
    except:
        pass
    #axs[f, 2].plot(data2[g]['val'])

#plt.figure(figsize=(19, 10))
#plt.plot(data_train[0][8]['val'])






"""
important_for_clean = [8, 13, 16, 14]



cutactive_true, cutactive_false = get_bCutActives(input_data)

fig, axs = plt.subplots(len(important_for_clean), 1, figsize=(20, 16), sharex=True)

for i,j in enumerate(important_for_clean):
    data = input_data[j]
    axs[i].scatter(data['source'], data['val'], s=15, color='grey')
    axs[i].plot(data['source'], data['val'], label=short_labels[j])
    axs[i].legend()
    if j == 13 or j == 16:
        axs[i].scatter(cutactive_true['source'], np.full(len(cutactive_true['source']), 10), c='g', s=25)
        axs[i].scatter(cutactive_false['source'], np.full(len(cutactive_false['source']), 10), c='r', s=25)

"""