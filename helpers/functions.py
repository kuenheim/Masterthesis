import time
from datetime import datetime
import csv
import os
import time
from numpy import genfromtxt
from opcua import Client
from Masterthesis.helpers.lists import ids, val_id_type_dict
import pandas as pd
from ast import literal_eval



def cuta_TRAINBAND_true(path_final_data, class_=None):
    print('load cuta_TRAINBAND_true')
    if class_ == 'a6':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true1a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true2a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true3a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true4a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true5a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    elif class_ == 'a47':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true1a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true2a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true3a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true4a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true5a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    elif class_ == 'a49':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true1a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true2a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true3a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true4a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'cutactive_true5a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    else:
        cutactive_true1 = None
        cutactive_true2 = None
        cutactive_true3 = None
        cutactive_true4 = None
        cutactive_true5 = None
        print('wrong class namestring in cuta_TRAINBAND_true')
    return [cutactive_true1, cutactive_true2, cutactive_true3, cutactive_true4, cutactive_true5]


def cuta_TESTBAND_true(path_final_data, class_=None):
    print('load cuta_TESTBAND_true')

    if class_ == 'a6':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true1a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true2a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true3a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true4a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true5a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    elif class_ == 'a47':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true1a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true2a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true3a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true4a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true5a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    elif class_ == 'a49':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true1a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true2a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true3a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true4a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_true5a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    else:
        cutactive_true1 = None
        cutactive_true2 = None
        cutactive_true3 = None
        cutactive_true4 = None
        cutactive_true5 = None
        print('wrong class namestring in cuta_TESTBAND_true')
    return [cutactive_true1, cutactive_true2, cutactive_true3, cutactive_true4, cutactive_true5]


def cuta_TRAINBAND_false(path_final_data, class_=None):
    print('load cuta_TRAINBAND_false')
    if class_ == 'a6':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false1a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false2a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false3a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false4a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false5a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    elif class_ == 'a47':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false1a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false2a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false3a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false4a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false5a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    elif class_ == 'a49':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false1a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false2a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false3a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false4a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'cutactive_false5a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    else:
        cutactive_true1 = None
        cutactive_true2 = None
        cutactive_true3 = None
        cutactive_true4 = None
        cutactive_true5 = None
        print('wrong class namestring in cuta_TRAINBAND_false')
    return [cutactive_true1, cutactive_true2, cutactive_true3, cutactive_true4, cutactive_true5]


def cuta_TESTBAND_false(path_final_data, class_=None):
    print('load cuta_TESTBAND_false')

    if class_ == 'a6':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false1a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false2a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false3a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false4a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false5a6.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    elif class_ == 'a47':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false1a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false2a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false3a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false4a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false5a47.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    elif class_ == 'a49':
        cutactive_true1 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false1a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true2 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false2a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true3 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false3a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true4 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false4a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
        cutactive_true5 = pd.read_csv(os.path.join(path_final_data, 'tcutactive_false5a49.csv'), index_col='idx', usecols=['idx', 'shifted'], parse_dates=['shifted'])
    else:
        cutactive_true1 = None
        cutactive_true2 = None
        cutactive_true3 = None
        cutactive_true4 = None
        cutactive_true5 = None
        print('wrong class namestring in cuta_TESTBAND_false')
    return [cutactive_true1, cutactive_true2, cutactive_true3, cutactive_true4, cutactive_true5]


def create_header(header):
    header = [x[20:] for x in header]
    logger = Logger()
    logger.create_csv('header_', header, with_header=True)


def dfs_for_timetest_terminal_output(path):
    """
    for the files that seperated with ' ', that created a need for 2 extra cols because the time was seperated in
    time and date

    """
    header = ['source_time', 'server_time', 'Status', 'ID', 'val']
    return pd.read_csv(path,
                       names=header,
                       skiprows=64,
                       delimiter=' ',
                       usecols=[0, 1, 2, 3, 4, 5, 6],
                       parse_dates={'source': ['source_date', 'source_time'], 'server': ['server_date', 'server_time']})


def dfs_for_timetest_csv(path, optional_skip_row = 0, with_second_time=False, skip_initial_lines=True):
    """
    :param path:
    :param optional_skip_row: if, then that many lines are skipped an the beginning
    :param with_second_time: then we read more cols than if only one time col is there
    :param skip_initial_lines: yes or no?
    :return: dataframe
    """

    # some visualizations need the values in the first lines, some dont
    if skip_initial_lines:
        skipper = optional_skip_row
    else:
        skipper = 0

    if with_second_time:
        # header for the parser to know what to parse and for indexing later
        header = ['source_time', 'pc_time', 'Status', 'ID', 'val']

        dataframe = pd.read_csv(path,
                       names=header,
                       skiprows=skipper,
                       delimiter=',',
                       usecols=[0, 1, 2, 3, 4],
                       parse_dates={'source': ['source_time'], 'receiver': ['pc_time']}, low_memory=False)

    else:
        header = ['source_time', 'ID', 'val']

        dataframe = pd.read_csv(path,
                         names=header,
                         skiprows=skipper,
                         delimiter=',',
                         usecols=[0, 3, 4],
                         parse_dates={'source': ['source_time']}, low_memory=False)
    return dataframe.sort_values(by=['source'])

#def load_new_sig(path):
#    header = ['idx', 'ID', 'val']
#
#        dataframe = pd.read_csv(path,
#                         names=header,
##                         skiprows=skipper,
 #                        delimiter=',',
 #                        usecols=[0, 3, 4],
 #                        parse_dates={'source': ['source_time']}, low_memory=False)
 #   return dataframe.sort_values(by=['source'])#

def sort_per_id(data):
    """
    Takes recorded data and sorts it into list of seperate DataFrames for each ID

    :return: list of DataFrames
    """
    id_data = []
    for i, j in enumerate(ids):
        #aaa[i].append(df.loc[df['ID']==j])
        temp = data.loc[data['ID'] == j]
        # avoid error for the "list" entries

        if val_id_type_dict[j] == bool:
            # convert val columns from string to their type
            #temp = temp.astype({'val': val_id_type_dict[j]})
            #temp = temp.convert_dtypes({'val': val_id_type_dict[j]})
            temp.loc[:, 'val'] = temp['val'].map(literal_eval)
        else:
            # convert strings to arrays
            temp.loc[:, 'val'] = temp['val'].map(literal_eval)
        id_data.append(temp[['source', 'ID', 'val']])
    return id_data


def sort_per_id_vib(data):
    """
    Takes recorded data and sorts it into list of seperate DataFrames for each ID

    :return: list of DataFrames
    """
    id_data = []
    for i, j in enumerate(['Signal_Raw1.value', 'Signal_Raw2.value', 'Signal_Raw3.value']):
        #aaa[i].append(df.loc[df['ID']==j])
        temp = data.loc[data['ID'] == j]
        # avoid error for the "list" entries


        # convert strings to arrays
        temp.loc[:, 'val'] = temp['val'].map(literal_eval)


        id_data.append(temp[['source', 'ID', 'val']])
    return id_data



def sort_per_axis(raw_data):
    """
    Signal_Raw comes from 3 sensors for 2 axis, this puts each axis together
    :param raw_data:
    :return:
    """

class OPCConnection():
    def __init__(self, url="opc.tcp://192.168.125.52:4840"):
        self.url = url
        self.client = None

    def connect_client(self):
        self.client = Client(self.url)
        try:
            self.client.connect()
            print('server connected')
        except:
            print('no server connection established')
        return self.client

    def disconnect(self):
        self.client.disconnect()
        print('server disconnected')


class Logger():
    def __init__(self):
        self.write_path = None

    def create_csv(self, filenamestart, filenameend, csv_path, header_path='data\\header_20-01-2022_14-07-50.csv', with_header=False):
        """
        ‘r’	    Read        (default)	Open a file for read only
        ‘w’	    Write	    Open a file for write only (overwrite)
        ‘a’	    Append	    Open a file for write only (append)
        ‘r+’    Read+Write	open a file for both reading and writing
        ‘x’	    Create	    Create a new file
        """

        header = genfromtxt(header_path, delimiter=",", dtype='str')

        date_time = datetime.now().strftime("%H-%M-%S_%d-%m-%Y")
        self.write_path = os.path.join(csv_path, filenamestart + date_time + filenameend + '.csv')

        #  TODO, check wheter faster encoding necessary, eg ascii possible
        connection = open(self.write_path, 'a', newline='', encoding='utf-8')
        csv_writer = csv.writer(connection)
        if with_header:
            csv_writer.writerow(header)
        connection.close()
        print('csv created ' + filenameend)
        return self.write_path

    def write_line(self, line):
        with open(self.write_path, 'a', newline='\n', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(line)


class IdCollector():
    def __init__(self):
        self.global_PV_children = None
        self.node_indices_one_level = []
        self.node_indices_two_levels = []
        self.list_of_id_lists = []
        self.test1 = []
        self.test2 = []

    def get_process_variables_nico(self, client):
        objects = client.get_objects_node()
        children_of_node = objects.get_children()
        PLC = children_of_node[2]
        self.global_PV_children = PLC.get_children()
        return self.global_PV_children

    def get_Global_PV_nodes(self, client):
        objects = client.get_objects_node()
        children_of_node = objects.get_children()
        PLC = children_of_node[4]
        Modules = PLC.get_children()[0]
        default = Modules.get_children()[0]
        Global_PV = default.get_children()[0]
        self.global_PV_children = Global_PV.get_children()
        return self.global_PV_children

    def get_indices_one_level(self):
        for i, j in enumerate(self.global_PV_children):
            first = j.get_children()
            if not first:
                print(i, ' this index is the test node')
            else:
                second = j.get_children()[0].get_children()
                if not second:
                    print(i, second)
                    self.node_indices_one_level.append(i)
                else:
                    third = j.get_children()[0].get_children()[0].get_children()
                    if not third:
                        print(i, third, 'multi')
                        self.node_indices_two_levels.append(i)
        return self.node_indices_two_levels, self.node_indices_one_level






    def get_one_level_nodes(self):
        stringNodeId = []
        for i in self.node_indices_one_level:
            try:
                #stringNodeId.append('ns=6;s=' + self.global_PV_children[i].nodeid.Identifier)
                stringNodeId.append('ns=5;s=' + self.global_PV_children[i].nodeid.Identifier)
            except:
                print(str(i) + ' nodeid problem')

        self.list_of_id_lists.append(stringNodeId)

    def get_FFT_HK_nodes(self):
        stringNodeId = []
        for i in [6, 7, 8]:
            for j in range(len(self.global_PV_children[i].get_children())):
                stringNodeId.append('ns=6;s=' + self.global_PV_children[i].get_children()[j].nodeid.Identifier)
        self.list_of_id_lists.append(stringNodeId)

    def get_FFT_Raw_nodes(self):
        stringNodeId = []
        for i in [9, 10, 11]:
            for j in range(len(self.global_PV_children[i].get_children())):
                stringNodeId.append('ns=6;s=' + self.global_PV_children[i].get_children()[j].nodeid.Identifier)
        self.list_of_id_lists.append(stringNodeId)

    def get_PData_nodes(self):
        stringNodeId = []
        for j in range(len(self.global_PV_children[20].get_children())):
            stringNodeId.append('ns=6;s=' + self.global_PV_children[20].get_children()[j].nodeid.Identifier)
        self.list_of_id_lists.append(stringNodeId)

    def get_Signal_Raw_nodes(self):
        stringNodeId = []
        for i in [23, 24, 25]:
            for j in range(len(self.global_PV_children[i].get_children())):
                stringNodeId.append('ns=6;s=' + self.global_PV_children[i].get_children()[j].nodeid.Identifier)
        self.list_of_id_lists.append(stringNodeId)

    def get_TData_nodes(self):
        stringNodeId = []
        for j in range(len(self.global_PV_children[26].get_children())):
            stringNodeId.append('ns=6;s=' + self.global_PV_children[26].get_children()[j].nodeid.Identifier)
        self.list_of_id_lists.append(stringNodeId)

    def get_Vib_nodes(self):
        stringNodeId = []
        for i in [28, 29, 30]:
            for j in range(len(self.global_PV_children[i].get_children())):
                stringNodeId.append('ns=6;s=' + self.global_PV_children[i].get_children()[j].nodeid.Identifier)
        self.list_of_id_lists.append(stringNodeId)

    def flatten_list(self):
        self.get_indices_one_level()

        self.get_one_level_nodes()
        self.get_FFT_HK_nodes()
        self.get_FFT_Raw_nodes()
        self.get_Signal_Raw_nodes()
        self.get_TData_nodes()
        self.get_Vib_nodes()
        self.get_PData_nodes()
        return [item for sublist in self.list_of_id_lists for item in sublist]


