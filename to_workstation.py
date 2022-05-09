import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tsfresh.utilities.dataframe_functions import impute
from tsfresh import extract_relevant_features, extract_features

def label_encoding_int_tsfresh(sample_count, class_count):
    """
    Turns the label string into integer values for each class

    :param sample_count: int
    :param class_count: int
    :return: ndarray
    """

    #  For as many samples in a class, there must be the same label
    labels_int = []
    for i in range(class_count):
        labels_int.append(np.full(shape=sample_count, fill_value=i))
    return np.array(labels_int).ravel()


def time_column(data):
    """
    creates time column values for ts_fresh

    :param data:
    :return: 1D ndarray
    """
    ids = []
    shape = data.shape
    for i in range(shape[0]):
        ids.append(np.arange(shape[1]))
    return np.array(ids).ravel()


def get_ts_ready_dataframes(X_train, X_test):
    col_id_train = time_column(X_train)
    col_id_test = time_column(X_test)

    col_time_test = label_encoding_int_tsfresh(X_test.shape[1], X_test.shape[0])
    col_time_train = label_encoding_int_tsfresh(X_train.shape[1], X_train.shape[0])

    X_train_ts = np.hstack((col_id_train.reshape(len(col_id_train), 1), col_time_train.reshape(len(col_time_train), 1)))
    X_test_ts = np.hstack((col_id_test.reshape(len(col_id_test), 1), col_time_test.reshape(len(col_time_test), 1)))

    X_train_ts = np.hstack((X_train_ts, X_train.ravel().reshape(len(X_train_ts), 1)))
    X_test_ts = np.hstack((X_test_ts, X_test.ravel().reshape(len(X_test_ts), 1)))

    return pd.DataFrame(X_train_ts, columns=['time', 'id', 'data']), pd.DataFrame(X_test_ts, columns=['time', 'id',
                                                                                                      'data'])

sig_array_TRAINBAND_a6 = np.load('data\\arrays\\sig_array_TRAINBAND_a6.npy')
sig_array_TRAINBAND_a47 = np.load('data\\arrays\\sig_array_TRAINBAND_a47.npy')
sig_array_TRAINBAND_a49 = np.load('data\\arrays\\sig_array_TRAINBAND_a49.npy')
sig_array_TESTB_a6 = np.load('data\\arrays\\sig_array_TESTB_a6.npy')
sig_array_TESTB_a47 = np.load('data\\arrays\\sig_array_TESTB_a47.npy')
sig_array_TESTB_a49 = np.load('data\\arrays\\sig_array_TESTB_a49.npy')
labels_TRAINBAND_a6  = np.load('data\\arrays\\labels_TRAINBAND_a6.npy')
labels_TRAINBAND_a47 = np.load('data\\arrays\\labels_TRAINBAND_a47.npy')
labels_TRAINBAND_a49 = np.load('data\\arrays\\labels_TRAINBAND_a49.npy')
labels_TESTB_a6   = np.load('data\\arrays\\labels_TESTB_a6.npy')
labels_TESTB_a47  = np.load('data\\arrays\\labels_TESTB_a47.npy')
labels_TESTB_a49  = np.load('data\\arrays\\labels_TESTB_a49.npy')





#  Compute ts_fresh train features and select at the same time
ts_train_TRAINBAND__6 = extract_relevant_features(X_train_TRAINBAND__6_ts_ready, y_train_TRAINBAND__6_ts_ready['label'], column_id='id', column_sort='time')
ts_train_TRAINBAND__6.to_csv('data\\features\\ts_train_TRAINBAND__6.csv')


#  Compute all ts_fresh test features - the relevant features are collected later according to the train features
ts_test_TRAINBAND__6_all = extract_features(X_test_TESTB__6, column_id='id', column_sort='time', impute_function=impute)
ts_test_TRAINBAND__6_all.to_csv('data\\features\\ts_test_TRAINBAND__6_all.csv')
#ts_test_TRAINBAND__6_all = pd.read_csv('data\\features\\1750_DE_features_test_all.csv', index_col=0)
print('d2')
#  Use the same features for testing that were selected for training
ts_test_TRAINBAND__6 = ts_test_TRAINBAND__6_all[ts_train_TRAINBAND__6.columns]

#  Fill the NaN values with a interpolation of the surrounding values in the column
ts_test_TRAINBAND__6 = ts_test_TRAINBAND__6.interpolate(axis=0)

# does it make sense to search tsfresh for all 15 domains?
# or better 3 times on the 5 domains

# todo 47 gibts schon, umbenennen
ts_train_TRAINBAND_47 = extract_relevant_features(X_train_TRAINBAND_47_ts_ready, y_train_TRAINBAND_47_ts_ready['label'], column_id='id', column_sort='time')
ts_train_TRAINBAND_47.to_csv('data\\features\\ts_train_TRAINBAND_47.csv')
#ts_train_TRAINBAND_47 = pd.read_csv('data\\features\\ts_train_TRAINBAND_47.csv', index_col=0)

ts_test_TRAINBAND_47_all = extract_features(X_test_TRAINBAND_47, column_id='id', column_sort='time', impute_function=impute)
ts_test_TRAINBAND_47_all.to_csv('data\\features\\ts_test_TRAINBAND_47_all.csv')
#ts_test_TRAINBAND_47_all = pd.read_csv('data\\features\\ts_test_TRAINBAND_47_all.csv', index_col=0)


ts_train_TRAINBAND_49 = extract_relevant_features(X_train_TRAINBAND_49_ts_ready, y_train_TRAINBAND_49_ts_ready['label'], column_id='id', column_sort='time')
ts_train_TRAINBAND_49.to_csv('data\\features\\ts_train_TRAINBAND_49.csv')
#ts_train_TRAINBAND_49 = pd.read_csv('data\\features\\ts_train_TRAINBAND_49.csv', index_col=0)






#data_for_tsfresh = """
test_split_size = 0.2
X_train_TRAINBAND__6, X_test_TRAINBAND__6, y_train_TRAINBAND__6, y_test_TRAINBAND__6 = train_test_split(sig_array_TRAINBAND_a6, labels_TRAINBAND_a6, test_size=test_split_size)
X_train_TRAINBAND_47, X_test_TRAINBAND_47, y_train_TRAINBAND_47, y_test_TRAINBAND_47 = train_test_split(sig_array_TRAINBAND_a47, labels_TRAINBAND_a47, test_size=test_split_size)
X_train_TRAINBAND_49, X_test_TRAINBAND_49, y_train_TRAINBAND_49, y_test_TRAINBAND_49 = train_test_split(sig_array_TRAINBAND_a49, labels_TRAINBAND_a49, test_size=test_split_size)
X_test_TESTB__6, y_test_TESTB__6 =   sig_array_TESTB_a6 , labels_TESTB_a6
X_test_TESTB_47, y_test_TESTB_47 = sig_array_TESTB_a47, labels_TESTB_a47
X_test_TESTB_49, y_test_TESTB_49 = sig_array_TESTB_a49, labels_TESTB_a49


X_train_TRAINBAND__6_ts_ready, X_test_TRAINBAND__6_ts_ready = get_ts_ready_dataframes(X_train_TRAINBAND__6, X_test_TRAINBAND__6)
X_train_TRAINBAND_47_ts_ready, X_test_TRAINBAND_47_ts_ready = get_ts_ready_dataframes(X_train_TRAINBAND_47, X_test_TRAINBAND_47)
X_train_TRAINBAND_49_ts_ready, X_test_TRAINBAND_49_ts_ready = get_ts_ready_dataframes(X_train_TRAINBAND_49, X_test_TRAINBAND_49)
X_test_TESTB__6_ts_ready, _ = get_ts_ready_dataframes(X_test_TESTB__6, X_test_TESTB__6)
X_test_TESTB_47_ts_ready, _ = get_ts_ready_dataframes(X_test_TESTB_47, X_test_TESTB_47)
X_test_TESTB_49_ts_ready, _ = get_ts_ready_dataframes(X_test_TESTB_49, X_test_TESTB_49)


# TODO scale und fit transform
y_train_TRAINBAND__6_ts_ready = pd.DataFrame(y_train_TRAINBAND__6, columns=['label'])
y_test_TRAINBAND__6_ts_ready = pd.DataFrame(y_test_TRAINBAND__6, columns=['label'])
y_train_TRAINBAND_47_ts_ready = pd.DataFrame(y_train_TRAINBAND_47, columns=['label'])
y_test_TRAINBAND_47_ts_ready = pd.DataFrame(y_test_TRAINBAND_47, columns=['label'])
y_train_TRAINBAND_49_ts_ready = pd.DataFrame(y_train_TRAINBAND_49, columns=['label'])
y_test_TRAINBAND_49_ts_ready = pd.DataFrame(y_test_TRAINBAND_49, columns=['label'])