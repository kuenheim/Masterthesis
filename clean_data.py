"""
visulalizations used to help clean the bCutActive True/False data errors and delete unnecessary data
"""

from helpers.functions import dfs_for_timetest_csv, sort_per_id
import matplotlib.pyplot as plt
import vis
import numpy as np
import helpers.lists as lists

#Testband

data = """
data36 = dfs_for_timetest_csv(lists.path36c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data37 = dfs_for_timetest_csv(lists.path37c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data38 = dfs_for_timetest_csv(lists.path38c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data39 = dfs_for_timetest_csv(lists.path39c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data40 = dfs_for_timetest_csv(lists.path40c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data41 = dfs_for_timetest_csv(lists.path41c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data42 = dfs_for_timetest_csv(lists.path42c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data43 = dfs_for_timetest_csv(lists.path43c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data44 = dfs_for_timetest_csv(lists.path44c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data45 = dfs_for_timetest_csv(lists.path45c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data46 = dfs_for_timetest_csv(lists.path46c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data47 = dfs_for_timetest_csv(lists.path47c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data48 = dfs_for_timetest_csv(lists.path48c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data49 = dfs_for_timetest_csv(lists.path49c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
data50 = dfs_for_timetest_csv(lists.path50c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
id_data36 = sort_per_id(data36)
id_data37 = sort_per_id(data37)
id_data38 = sort_per_id(data38)
id_data39 = sort_per_id(data39)
id_data40 = sort_per_id(data40)
id_data41 = sort_per_id(data41)
id_data42 = sort_per_id(data42)
id_data43 = sort_per_id(data43)
id_data44 = sort_per_id(data44)
id_data45 = sort_per_id(data45)
id_data46 = sort_per_id(data46)
id_data47 = sort_per_id(data47)
id_data48 = sort_per_id(data48)
id_data49 = sort_per_id(data49)
id_data50 = sort_per_id(data50)
#"""
sigraws = """
data36_sig = dfs_for_timetest_csv(lists.path36_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data37_sig = dfs_for_timetest_csv(lists.path37_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data38_sig = dfs_for_timetest_csv(lists.path38_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data39_sig = dfs_for_timetest_csv(lists.path39_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data40_sig = dfs_for_timetest_csv(lists.path40_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data41_sig = dfs_for_timetest_csv(lists.path41_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data42_sig = dfs_for_timetest_csv(lists.path42_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data43_sig = dfs_for_timetest_csv(lists.path43_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data44_sig = dfs_for_timetest_csv(lists.path44_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data45_sig = dfs_for_timetest_csv(lists.path45_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data46_sig = dfs_for_timetest_csv(lists.path46_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data47_sig = dfs_for_timetest_csv(lists.path47_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data48_sig = dfs_for_timetest_csv(lists.path48_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data49_sig = dfs_for_timetest_csv(lists.path49_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data50_sig = dfs_for_timetest_csv(lists.path50_sig, with_second_time=True, skip_initial_lines=True, optional_skip_row=5)
data36_sig = sort_per_id(data36_sig)                                                                               
data37_sig = sort_per_id(data37_sig)                                                                               
data38_sig = sort_per_id(data38_sig)                                                                               
data39_sig = sort_per_id(data39_sig)                                                                               
data40_sig = sort_per_id(data40_sig)                                                                               
data41_sig = sort_per_id(data41_sig)                                                                               
data42_sig = sort_per_id(data42_sig)                                                                               
data43_sig = sort_per_id(data43_sig)                                                                               
data44_sig = sort_per_id(data44_sig)                                                                               
data45_sig = sort_per_id(data45_sig)                                                                               
data46_sig = sort_per_id(data46_sig)                                                                               
data47_sig = sort_per_id(data47_sig)                                                                               
data48_sig = sort_per_id(data48_sig)                                                                               
data49_sig = sort_per_id(data49_sig)                                                                               
data50_sig = sort_per_id(data50_sig)                                                                               
#"""
#data37c = dfs_for_timetest_csv(lists.path37c, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#data37c = sort_per_id(data37c)
#data37 = dfs_for_timetest_csv(lists.path37, with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#data37 = sort_per_id(data37)

#dataerror = dfs_for_timetest_csv('E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__14-45-28_21-03-2022_data.csv', with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#datadataerror = sort_per_id(dataerror)
#dataerror1 = dfs_for_timetest_csv('E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__16-32-15_01-03-2022_data.csv', with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#datadataerror1 = sort_per_id(dataerror1)
#dataerror2 = dfs_for_timetest_csv('E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-01-59_01-03-2022_data.csv', with_second_time=True, skip_initial_lines=True, optional_skip_row=46)
#datadataerror2 = sort_per_id(dataerror2)

# pahts, data loading and sorting for band 4
paths_4 = [
 'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__11-10-27_01-03-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__16-21-47_28-02-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__13-58-30_28-02-2022_data.csv',
 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__15-03-30_28-02-2022_data.csv',

 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__08-25-51_02-03-2022_data.csv',
 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__08-53-28_02-03-2022_data.csv',
 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__10-38-50_02-03-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__16-49-50_01-03-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-01-59_01-03-2022_data.csv',
 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-18-37_01-03-2022_data.csv',
 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__16-32-15_01-03-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__12-57-39_01-03-2022_data.csv',

 'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_data.csv',
 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__11-42-05_08-03-2022_data.csv',
 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__12-16-59_02-03-2022_data.csv',
 #'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__13-02-29_02-03-2022_data.csv'
    ]

paths_5 = [
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__17-35-40_19-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__15-30-29_19-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__12-35-15_19-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__13-26-23_19-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__13-49-40_19-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__14-14-54_19-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__14-54-30_19-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-10-19_21-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__14-12-32_21-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__14-45-28_21-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_data.csv',
    'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-27-58_21-03-2022_data.csv']

def make_list_ids(pahts):
    data = [dfs_for_timetest_csv(x) for x in pahts]
    return [sort_per_id(x) for x in data]



rest = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-12-49_01-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-36-01_01-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__09-13-12_01-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__12-18-38_01-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-21-33_01-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-58-22_31-03-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__15-12-05_01-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__16-48-04_31-03-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-24-51_31-03-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-27-58_21-03-2022_data.csv'
]
klasse3 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__17-35-40_19-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__15-30-29_19-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_data.csv',
]
klasse_4_a699 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_data.csv',
    ]
"""
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-36-01_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__09-13-12_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__12-18-38_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-21-33_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-58-22_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__15-12-05_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__16-48-04_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-24-51_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-27-58_21-03-2022_data.csv',

]

 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-75_5-ms__10-57-16_02-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__11-41-57_07-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__14-30-07_02-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-09-48_05-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-40_Vors-90_Bandv-90_5-ms__16-13-10_05-04-2022_data.csv',
 'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_5_Alu-60_Vors-90_Bandv-90_5-ms__14-24-55_07-04-2022_data.csv']
"""


together3 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_data.csv']
class4 = ['E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_data.csv',]



k1 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-60_Vors-90_Bandv-90_5-ms__13-58-30_28-02-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-90_5-ms__16-21-47_28-02-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_1_Alu-40_Vors-90_Bandv-75_5-ms__11-10-27_01-03-2022_data.csv']
k2 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-60_Vors-90_Bandv-90_5-ms__12-57-39_01-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-90_5-ms__15-01-59_01-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_2_Alu-40_Vors-90_Bandv-75_5-ms__16-49-50_01-03-2022_data.csv']
k3 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\4\\cut\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__08-08-01_11-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-60_Vors-90_Bandv-90_5-ms__10-52-18_19-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-90_5-ms__15-30-29_19-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_3_Alu-40_Vors-90_Bandv-75_5-ms__17-35-40_19-03-2022_data.csv',
]
k4 = [
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-75_5-ms__11-10-19_21-03-2022_data.csv'
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Done\\Klasse_4_Alu-40_Vors-90_Bandv-90_5-ms__14-45-28_21-03-2022_data.csv'
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__14-58-22_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__16-48-04_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__17-24-51_31-03-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-12-49_01-04-2022_data.csv',
'E:\\ausgelagert thesis daten\\Trainingsband\\5\\cut\\Klasse_4_Alu-60_Vors-90_Bandv-90_5-ms__08-23-31_22-03-2022_data.csv',
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




#tog = make_list_ids(together3)
idk1 = make_list_ids(k1)
# hiermit anfang und ende weggeschnittten


paths = k1
id_data = idk1


half_cutactives = 0
for index in range(len(id_data)):
    input_data = id_data[index]
    #input_data = datadataerror
    cutactive_true, cutactive_false = vis.get_bCutActives(input_data)
    important_for_clean = [8, 13, 14, 39, 40, 64]
    extra = []

    fig, axs = plt.subplots(len(important_for_clean)-4, 1, figsize=(19, 16), sharex=True)
    #fig.suptitle(str(index) + ' ' + str(lists.paths[index]))
    #fig.suptitle('2')
    cuts = input_data[0].shape[0]/2
    half_cutactives += cuts
    fig.suptitle(paths[index][48:] + '      cuts: ' + str(cuts))

    for i,j in enumerate(important_for_clean):
        try:
            data = input_data[j]
            axs[i].scatter(data['source'], data['val'], s=15, color='grey')

            if j == 40:
                axs[3].plot(data['source'], data['val'], label=lists.short_labels[j])
                pass
            if j == 64:
                axs[3].plot(data['source'], data['val'], label=lists.short_labels[j])
                pass
            axs[i].plot(data['source'], data['val'], label=lists.short_labels[j])
            axs[i].legend()
            if j == 13 or j == 16:
                axs[i].scatter(cutactive_true['source'], np.full(len(cutactive_true['source']), 10), c='g', s=25)
                axs[i].scatter(cutactive_false['source'], np.full(len(cutactive_false['source']), 10), c='r', s=25)
        except:
            pass
print('possible cuts of all figs: ', half_cutactives)


#"""
"""
data_list = [data36,
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
id_data_list = [id_data36,
id_data37,
id_data38,
id_data39,
id_data40,
id_data41,
id_data42,
id_data43,
id_data44,
id_data45,
id_data46,
id_data47,
id_data48,
id_data49,
id_data50
]



data = data48


#np.mean(faster_timedetla_datachange(id_data36[13]))


# search for cutactive
mini = []
maxi = []
plot_index = 13
roll_window = 20
fig, axs = plt.subplots(len(id_data_list)//5, 1, figsize=(19, 16), sharex=True, sharey=True)
fig.suptitle(roll_window)
for i, j in enumerate(id_data_list):
    if i >= 3:
        break
    #rolling mean
#    j[plot_index]['roll'] = j[plot_index]['val'].rolling(roll_window).mean()

    #axs[i].scatter(data[plot_index]['source'], data[plot_index]['val'], s=15, color='grey')
    #axs[i].plot(data[plot_index]['source'], data[plot_index]['val'], label=lists.short_labels[j])


    #axs[i].scatter(range(roll_window-1, 6001), j[plot_index]['val'].values[roll_window-1:6001], s=15, color='grey')
    #axs[i].plot(range(0, 6001), j[plot_index]['val'].values[0:6001], label=lists.short_labels[plot_index])
    slope = pd.Series(np.gradient(j[plot_index]['roll'].values), j[plot_index]['roll'].index, name='slope')[0:600]

    axs[i].plot(j[plot_index]['roll'].values[0:6001-1-roll_window], label=lists.short_labels[plot_index])
    axs[i].plot(slope)

    #axs[i].legend()
    #if j == 13 or j == 16:
    #    axs[i].scatter(cutactive_true['source'], np.full(len(cutactive_true['source']), 10), c='g', s=25)
    #    axs[i].scatter(cutactive_false['source'], np.full(len(cutactive_false['source']), 10), c='r', s=25)
    #print(i, np.mean(faster_timedetla_datachange(j[plot_index])))
"""

