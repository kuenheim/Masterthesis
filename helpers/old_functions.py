from helpers.lists import ids
import numpy as np


# first try, set big csv columns to a array with one row per unique source time
def col_to_array1():
    columns_list = ids
    columns_list.append('StatusCode')
    column_list_index = list(range(len(columns_list)))
    columns_dict = dict(zip(columns_list, column_list_index))
    unique_dates, date_counts = np.unique(df['source'].values, return_counts=True)

    counter = 0
    row_counter = 0
    dummy_array = np.zeros((len(unique_dates), len(columns_list)), dtype=object)
    dummy_array[:] = np.NaN
    #sum1 = np.isnan(dummy_array).sum()
    # i ist andzahl verschiedener Zeiten
    for i in range(len(unique_dates)):
        temp_time = df.iloc[row_counter, 0]
        for k in range(date_counts[i]):
            if df.iloc[row_counter, 0] == temp_time:
                single_id = df.iloc[row_counter, 2]
                column_number = columns_dict[single_id]
                dummy_array[i, column_number] = df.iloc[row_counter, 3]
            row_counter += 1
    return dummy_array
    #sum2 = np.isnan(dummy_array).sum()
    #summm = sum1 - sum2


def make_val_id_type_dict():
    types = [type(client.get_node(i).get_data_value().Value.Value) for i in names]
    ids = [x[20:] for x in names]
    return dict(zip(ids, types))
#val_id_type_dict = make_val_id_type_dict()


def log_lines_via_get_node(line_count, nodes_to_write):
    """
    takes about a second for all nodes

    :param line_count:
    :param nodes_to_write:
    :return:
    """
    logger = Logger()
    header_path = 'data\\header_20-01-2022_14-07-50.csv'
    header = genfromtxt(header_path, delimiter=",", dtype='str')

    logger.create_csv('data_', header)
    start1 = time.time()
    for i in range(line_count):
        # old :  logger.write_line(get_values(Global_PV_nodes))
        logger.write_line([x.get_value() for x in nodes_to_write])

    end1 = time.time()
    print('all: ', end1 - start1)

# aus main file
def visualize_raw_and_HK_data(start_indices, node_names):

    for name_idx in start_indices:

        fig, axs = plt.subplots(6, 1, figsize=(19, 10))
        for i, ax in enumerate(axs):
            aa = client.get_node(node_names[name_idx + i]).get_value()
            ax.plot(range(len(aa)), aa)
            ax.set_title(node_names[name_idx])
            plt.tight_layout()

class SubHandler_on_off(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        """
        called for every datachange notification from server
        """

        global Cut_Active
        Cut_Active = val

        #print('changed value of bCutactive: ', val, node)
        print(node, val)



    def event_notification(self, event):
        """
        called for every event notification from server
        """
        print('event_notification of bCutactive:', event, 'type: ', type(event))

    def status_change_notification(self, status):
        """
        called for every status change notification from server
        """
        print('status_change_notification of bCutactive:', status, 'type: ', type(status))


def print_values(node_in_list):
    print('Display Name:  ', node_in_list.get_browse_name().Name)
    # Node ID has redundant info, get [13:]
    id = node_in_list.nodeid.Identifier[13:]
    print('Identifier Name:  ', id)
    data_value = node_in_list.get_data_value()

    if data_value.StatusCode.is_good():
       print('status:   Good')
    else:
        print('WARNING Status not good')
    print('value: ', data_value.Value.Value)
    print('sourcetime: ', data_value.SourceTimestamp)
    print('Datatype:  ', data_value.Value.VariantType.name)
    print('ServerTimestamp', data_value.ServerTimestamp)
    print('\n')
    return id



def get_values(sensor_data_list):
    start = time.time()

    # counter for dict with names and indices

    values = []
    for i in sensor_data_list:
        next_children = i.get_children()
        # skip the empty test node by checking if the children list is empty
        if not next_children:
            continue
        next_next_children = next_children[0].get_children()

        # check if list one further down is empty, which means variables ar one level down
        if not next_next_children:
            node_id = i.nodeid.Identifier[13:]

            data_value = i.get_data_value()
            values.append(data_value.Value.Value)
            #if data_value.StatusCode.is_good():
            #    status_code = 'Good'
            #else:
            #    status_code = 'WARNING Status not good'
            source_timestamp = data_value.SourceTimestamp
            #print(source_timestamp)
            #print(data_value.SourceTimestamp)
            #datatype = data_value.Value.VariantType.name
            # TODO why servertimestamp empty...
        # if list one level down is not empty, then values are one more level down
        else:
            #
            for j in next_children:
                node_id = j.nodeid.Identifier[13:]
                data_value = j.get_data_value()
                values.append(data_value.Value.Value)

                #if data_value.StatusCode.is_good():
                #    status_code = 'Good'
                #else:
                #    status_code = 'WARNING Status not good'
                #source_timestamp = data_value.SourceTimestamp
                #print(source_timestamp)
                #datatype = data_value.Value.VariantType.name
                # TODO why servertimestamp empty...

                # TODO solve time delay between data requests
    end = time.time()
    print('get values: ', end - start)
    return values


def get_node_id_list(sensor_data_list):
    # counter for dict with names and indices
    counter = 0
    names_list = []

    for i in sensor_data_list:

        # skip the empty test node by checking if the children list is empty
        if not i.get_children():
            continue

        # check if list one further down is empty, which means variables ar one level down
        if not i.get_children()[0].get_children():
            id = print_values(i)
            names_list.append(id)
            counter += 1

        # if list one level down is not empty, then values are one more level down
        else:
            next_children = i.get_children()
            for j in next_children:
                id = print_values(j)
                names_list.append(id)
                counter += 1
    return names_list








print('why is this printed? should if __name__ == "__main__": prevent that?')



"""
# Statusvariablen
CutCounter = opcuanode(6, '::AsGlobalPV:CutCounter'),
FlatstreamCutCounter = opcuanode(6, '::AsGlobalPV:FlatstreamCutCounter'),
FlatstreamDone = opcuanode(6, '::AsGlobalPV:FlatstreamDone'),
FFT_Anforderung = opcuanode(6, '::AsGlobalPV:FFT_Anforderung'),

CutTime = opcuanode(6, '::AsGlobalPV:CutTime'),
HebenAktiv = opcuanode(6, '::AsGlobalPV:HebenAktiv'),
MotorAn = opcuanode(6, '::AsGlobalPV:MotorAn'),
Position = opcuanode(6, '::AsGlobalPV:Position'),
CutActive = opcuanode(6, '::AsGlobalPV:bCutActive'),
fLichtschranke = opcuanode(6, '::AsGlobalPV:fLichtschranke'),

# Vorschubdruck
P_Vorschub = opcuanode(6, '::AsGlobalPV:P_Vorschub'),

# Leistungsmessung
PData.CosPhi = opcuanode(6, '::AsGlobalPV:PData.CosPhi'),
PData.CutEnergy = opcuanode(6, '::AsGlobalPV:PData.CutEnergy'),
PData.PEff = opcuanode(6, '::AsGlobalPV:PData.PEff'),

# Temperatur
TData.T1 = opcuanode(6, '::AsGlobalPV:TData.T1'),
TData.T2 = opcuanode(6, '::AsGlobalPV:TData.T2'),
TData.T3 = opcuanode(6, '::AsGlobalPV:TData.T3'),
TData.T4 = opcuanode(6, '::AsGlobalPV:TData.T4'),
TData.T_IR = opcuanode(6, '::AsGlobalPV:TData.T_IR'),

# Vibrationsdaten
Vib01.Crest = opcuanode(6, '::AsGlobalPV:Vib01.CREST'),
Vib01.FrequencyBands = opcuanode(6, '::AsGlobalPV:Vib01.FrequencyBands'),
Vib01.Kurtosis = opcuanode(6, '::AsGlobalPV:Vib01.Kurtosis'),
Vib01.Peak = opcuanode(6, '::AsGlobalPV:Vib01.Peak'),
Vib01.RMS = opcuanode(6, '::AsGlobalPV:Vib01.RMS'),
Vib01.Skewness = opcuanode(6, '::AsGlobalPV:Vib01.Skewness'),
Vib01.VDI3832 = opcuanode(6, '::AsGlobalPV:Vib01.VDI3832'),

Vib02.Crest = opcuanode(6, '::AsGlobalPV:Vib02.CREST'),
Vib02.FrequencyBands = opcuanode(6, '::AsGlobalPV:Vib02.FrequencyBands'),
Vib02.Kurtosis = opcuanode(6, '::AsGlobalPV:Vib02.Kurtosis'),
Vib02.Peak = opcuanode(6, '::AsGlobalPV:Vib02.Peak'),
Vib02.RMS = opcuanode(6, '::AsGlobalPV:Vib02.RMS'),
Vib02.Skewness = opcuanode(6, '::AsGlobalPV:Vib02.Skewness'),
Vib02.VDI3832 = opcuanode(6, '::AsGlobalPV:Vib02.VDI3832'),

Vib03.Crest = opcuanode(6, '::AsGlobalPV:Vib03.CREST'),
Vib03.FrequencyBands = opcuanode(6, '::AsGlobalPV:Vib03.FrequencyBands'),
Vib03.Kurtosis = opcuanode(6, '::AsGlobalPV:Vib03.Kurtosis'),
Vib03.Peak = opcuanode(6, '::AsGlobalPV:Vib03.Peak'),
Vib03.RMS = opcuanode(6, '::AsGlobalPV:Vib03.RMS'),
Vib03.Skewness = opcuanode(6, '::AsGlobalPV:Vib03.Skewness'),
Vib03.VDI3832 = opcuanode(6, '::AsGlobalPV:Vib03.VDI3832'),

% Flatstream
Fs_Mode = opcuanode(6, '::AsGlobalPV:FsMode_1Raw_2FftRaw_3FttHK'),
FFT_Raw1.freq = opcuanode(6, '::AsGlobalPV:FFT_Raw1.freq'),
FFT_Raw1.value = opcuanode(6, '::AsGlobalPV:FFT_Raw1.value'),
FFT_Raw2.freq = opcuanode(6, '::AsGlobalPV:FFT_Raw2.freq'),
FFT_Raw2.value = opcuanode(6, '::AsGlobalPV:FFT_Raw2.value'),
FFT_Raw3.freq = opcuanode(6, '::AsGlobalPV:FFT_Raw3.freq'),
FFT_Raw3.value = opcuanode(6, '::AsGlobalPV:FFT_Raw3.value'),

FFT_HK1.freq = opcuanode(6, '::AsGlobalPV:FFT_HK1.freq'),
FFT_HK1.value = opcuanode(6, '::AsGlobalPV:FFT_HK1.value'),
FFT_HK2.freq = opcuanode(6, '::AsGlobalPV:FFT_HK2.freq'),
FFT_HK2.value = opcuanode(6, '::AsGlobalPV:FFT_HK2.value'),
FFT_HK3.freq = opcuanode(6, '::AsGlobalPV:FFT_HK3.freq'),
FFT_HK3.value = opcuanode(6, '::AsGlobalPV:FFT_HK3.value'),

Signal_Raw1.time = opcuanode(6, '::AsGlobalPV:Signal_Raw1.time'),
Signal_Raw1.value = opcuanode(6, '::AsGlobalPV:Signal_Raw1.value'),
Signal_Raw2.time = opcuanode(6, '::AsGlobalPV:Signal_Raw2.time'),
Signal_Raw2.value = opcuanode(6, '::AsGlobalPV:Signal_Raw2.value'),
Signal_Raw3.time = opcuanode(6, '::AsGlobalPV:Signal_Raw3.time'),
Signal_Raw3.value = opcuanode(6, '::AsGlobalPV:Signal_Raw3.value'),

statusList = [CutCounter,
CutActive,
FlatstreamDone,
FFT_Anforderung]

fastCycleList = [                 CutCounter,
CutTime,
HebenAktiv,
MotorAn,
Position,
CutActive,
fLichtschranke,
PData.CosPhi,
PData.CutEnergy,
PData.PEff,
TData.T1,
TData.T2,
TData.T3,
TData.T4,
TData.T_IR,
Vib01.Crest,
Vib01.FrequencyBands,
Vib01.Kurtosis,
Vib01.Peak,
Vib01.RMS,
Vib01.Skewness,
Vib01.VDI3832,
Vib02.Crest,
Vib02.FrequencyBands,
Vib02.Kurtosis,
Vib02.Peak,
Vib02.RMS,
Vib02.Skewness,
Vib02.VDI3832,
Vib03.Crest,
Vib03.FrequencyBands,
Vib03.Kurtosis,
Vib03.Peak,
Vib03.RMS,
Vib03.Skewness,
Vib03.VDI3832,
P_Vorschub
],

slowCycleList = [
    FlatstreamCutCounter,
Fs_Mode,
Signal_Raw1.time,
Signal_Raw1.value,
Signal_Raw2.time,
Signal_Raw2.value,
Signal_Raw3.time,
Signal_Raw3.value,
FFT_Raw1.freq,
FFT_Raw1.value,
FFT_Raw2.freq,
FFT_Raw2.value,
FFT_Raw3.freq,
FFT_Raw3.value,
FFT_HK1.freq,
FFT_HK1.value,
FFT_HK2.freq,
FFT_HK2.value,
FFT_HK3.freq,
FFT_HK3.value]

varList = {
    'CutCounter',
'FlatstreamCutCounter',
'FlatstreamDone',
'FFT_Anforderung',
'CutActive',
'CutTime',
'HebenAktiv',
'MotorAn',
'Position',
'CutActive',
'fLichtschranke',
'PData',
'TData',
'Vib01',
'Vib02',
'Vib03',
'Fs_Mode',
'FFT_Raw1',
'FFT_Raw2',
'FFT_Raw3',
'FFT_HK1',
'FFT_HK2',
'FFT_HK3',
'Signal_Raw1',
'Signal_Raw2',
'Signal_Raw3',
'P_Vorschub'}
"""