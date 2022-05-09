# workaraound for error with ts fresh, put everything in if name main
if __name__ == '__main__':
    import os
    from sklearn.model_selection import train_test_split
    from tsfresh.utilities.dataframe_functions import impute
    from tsfresh import extract_relevant_features, extract_features

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    #import matplotlib as mpl    # error when
    #mpl.use('Qt5Agg')
    from helpers.lists import classes
    from ast import literal_eval

    #print(os.getcwd())
    #import time
    #time.sleep(5)

    def add_class_col(data):
        # every domain gets a int for a class according to helpers.lists.classes
        for h, i in enumerate(data):

            # classes start with 1 but i starts with 0
            h += 1
            i['id'] = h


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


    def label_encoding_int(sample_counts):
        """
        Turns the label string into integer values for each class

        :param sample_count: list[int]
        :param class_count: int
        :return: ndarray
        """

        #  For as many samples in a class, there must be the same label
        labels_int = []
        for i in range(len(sample_counts)):
            labels_int.append(np.full(shape=sample_counts[i], fill_value=i+1))
        #return np.array(labels_int, dtype=object).ravel()
        return np.concatenate(labels_int, axis=0)


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


    load_cutactive_cut_sigraw = """
    path_final_data = 'E:\\ausgelagert thesis daten\\final_data\\sigraw'
    read_cols = ['idx', 'ID', 'source', 'val']
    sig1a6   = pd.read_csv(os.path.join(path_final_data,  'sig1a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig2a6   = pd.read_csv(os.path.join(path_final_data,  'sig2a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig3a6   = pd.read_csv(os.path.join(path_final_data,  'sig3a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig4a6   = pd.read_csv(os.path.join(path_final_data,  'sig4a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig5a6   = pd.read_csv(os.path.join(path_final_data,  'sig5a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig1a47  = pd.read_csv(os.path.join(path_final_data, 'sig1a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig2a47  = pd.read_csv(os.path.join(path_final_data, 'sig2a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig3a47  = pd.read_csv(os.path.join(path_final_data, 'sig3a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig4a47  = pd.read_csv(os.path.join(path_final_data, 'sig4a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig5a47  = pd.read_csv(os.path.join(path_final_data, 'sig5a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig1a49  = pd.read_csv(os.path.join(path_final_data, 'sig1a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig2a49  = pd.read_csv(os.path.join(path_final_data, 'sig2a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig3a49  = pd.read_csv(os.path.join(path_final_data, 'sig3a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig4a49  = pd.read_csv(os.path.join(path_final_data, 'sig4a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    sig5a49  = pd.read_csv(os.path.join(path_final_data, 'sig5a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig1a6  = pd.read_csv(os.path.join(path_final_data, 'sigt1a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig2a6  = pd.read_csv(os.path.join(path_final_data, 'sigt2a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig3a6  = pd.read_csv(os.path.join(path_final_data, 'sigt3a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig4a6  = pd.read_csv(os.path.join(path_final_data, 'sigt4a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig5a6  = pd.read_csv(os.path.join(path_final_data, 'sigt5a6.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig1a47 = pd.read_csv(os.path.join(path_final_data, 'sigt1a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig2a47 = pd.read_csv(os.path.join(path_final_data, 'sigt2a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig3a47 = pd.read_csv(os.path.join(path_final_data, 'sigt3a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig4a47 = pd.read_csv(os.path.join(path_final_data, 'sigt4a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig5a47 = pd.read_csv(os.path.join(path_final_data, 'sigt5a47.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig1a49 = pd.read_csv(os.path.join(path_final_data, 'sigt1a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig2a49 = pd.read_csv(os.path.join(path_final_data, 'sigt2a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig3a49 = pd.read_csv(os.path.join(path_final_data, 'sigt3a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig4a49 = pd.read_csv(os.path.join(path_final_data, 'sigt4a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    tsig5a49 = pd.read_csv(os.path.join(path_final_data, 'sigt5a49.csv'), index_col='idx', usecols=read_cols, parse_dates=['source'])
    print('loades sigraw')
    #"""





    # todo macht der unterschiedliche sample count probleme?

    calc_arr_and_label = """
    all_sig_data_list = [sig1a6  , sig2a6  , sig3a6  , sig4a6  , sig5a6  , sig1a47 , sig2a47 , sig3a47 , sig4a47 , sig5a47 , sig1a49 , sig2a49 , sig3a49 , sig4a49 , sig5a49 , tsig1a6 , tsig2a6 , tsig3a6 , tsig4a6 , tsig5a6 , tsig1a47, tsig2a47, tsig3a47, tsig4a47, tsig5a47, tsig1a49, tsig2a49, tsig3a49, tsig4a49, tsig5a49]
    
    sig_data_TRAINBAND_a6 = [sig1a6  , sig2a6  , sig3a6  , sig4a6  , sig5a6]
    sig_data_TRAINBAND_a47 = [sig1a47 , sig2a47 , sig3a47 , sig4a47 , sig5a47]
    sig_data_TRAINBAND_a49 = [sig1a49 , sig2a49 , sig3a49 , sig4a49 , sig5a49]
    sig_data_TESTB_a6 =  [tsig1a6  , tsig2a6  , tsig3a6  , tsig4a6  , tsig5a6]
    sig_data_TESTB_a47 = [tsig1a47 , tsig2a47 , tsig3a47 , tsig4a47 , tsig5a47]
    sig_data_TESTB_a49 = [tsig1a49 , tsig2a49 , tsig3a49 , tsig4a49 , tsig5a49]
    
    add_class_col(sig_data_TRAINBAND_a6)
    
    
    samples_per_domain_TRAINBAND_a6 = [len(x) for x in  sig_data_TRAINBAND_a6]
    samples_per_domain_TRAINBAND_a47 = [len(x) for x in sig_data_TRAINBAND_a47]
    samples_per_domain_TRAINBAND_a49 = [len(x) for x in sig_data_TRAINBAND_a49]
    samples_per_domain_TESTB_a6 = [len(x) for x in  sig_data_TESTB_a6]
    samples_per_domain_TESTB_a47 = [len(x) for x in sig_data_TESTB_a47]
    samples_per_domain_TESTB_a49 = [len(x) for x in sig_data_TESTB_a49]
    all_samples_per_domain = [len(x) for x in all_sig_data_list]
    
    sig_data_TRAINBAND_a6 = pd.concat(sig_data_TRAINBAND_a6)
    sig_data_TRAINBAND_a47 = pd.concat(sig_data_TRAINBAND_a47)
    sig_data_TRAINBAND_a49 = pd.concat(sig_data_TRAINBAND_a49)
    sig_data_TESTB_a6 = pd.concat(sig_data_TESTB_a6)
    sig_data_TESTB_a47 = pd.concat(sig_data_TESTB_a47)
    sig_data_TESTB_a49 = pd.concat(sig_data_TESTB_a49)
    
    #plt.figure()
    #plt.plot(all_samples_per_domain)
    #plt.xticks(list(range(len(all_samples_per_domain))), list(classes.values()) + ['t'+x for x in list(classes.values())])
    #plt.show()
    
    
    # get list from entry
    #tsig5a49.iloc[0:1]['val'].map(literal_eval).values[0]
    labels_TRAINBAND_a6 = label_encoding_int(samples_per_domain_TRAINBAND_a6)
    labels_TRAINBAND_a47 = label_encoding_int(samples_per_domain_TRAINBAND_a47)
    labels_TRAINBAND_a49 = label_encoding_int(samples_per_domain_TRAINBAND_a49)
    labels_TESTB_a6  = label_encoding_int(samples_per_domain_TESTB_a6)
    labels_TESTB_a47 = label_encoding_int(samples_per_domain_TESTB_a47)
    labels_TESTB_a49 = label_encoding_int(samples_per_domain_TESTB_a49)
    #"""

    save_labels = """
    np.save('data\\arrays\\labels_TRAINBAND_a6.npy', labels_TRAINBAND_a6 )
    np.save('data\\arrays\\labels_TRAINBAND_a47.npy', labels_TRAINBAND_a47)
    np.save('data\\arrays\\labels_TRAINBAND_a49.npy', labels_TRAINBAND_a49)
    np.save('data\\arrays\\labels_TESTB_a6.npy', labels_TESTB_a6  )
    np.save('data\\arrays\\labels_TESTB_a47.npy', labels_TESTB_a47 )
    np.save('data\\arrays\\labels_TESTB_a49.npy', labels_TESTB_a49 )
    #"""

    save_arrays = """
    sig_array_TRAINBAND_a6  = np.stack(sig_data_TRAINBAND_a6['val'].map(literal_eval).values, axis=0)
    np.save('data\\arrays\\sig_array_TRAINBAND_a6.npy', sig_array_TRAINBAND_a6 )
    print('1')
    sig_array_TRAINBAND_a47 = np.stack(sig_data_TRAINBAND_a47['val'].map(literal_eval).values, axis=0)
    np.save('data\\arrays\\sig_array_TRAINBAND_a47.npy', sig_array_TRAINBAND_a47)
    print('1')
    sig_array_TRAINBAND_a49 = np.stack(sig_data_TRAINBAND_a49['val'].map(literal_eval).values, axis=0)
    np.save('data\\arrays\\sig_array_TRAINBAND_a49.npy', sig_array_TRAINBAND_a49)
    print('1')
    sig_array_TESTB_a6   = np.stack(sig_data_TESTB_a6['val'].map(literal_eval).values, axis=0)
    np.save('data\\arrays\\sig_array_TESTB_a6.npy', sig_array_TESTB_a6  )
    print('1')
    sig_array_TESTB_a49 = np.stack(sig_data_TESTB_a49['val'].map(literal_eval).values, axis=0)
    np.save('data\\arrays\\sig_array_TESTB_a49.npy', sig_array_TESTB_a49)
    print('1')
    #sig_array_TESTB_a47  = np.stack(sig_data_TESTB_a47['val'].map(literal_eval).values, axis=0)
    #np.save('data\\arrays\\sig_array_TESTB_a47.npy', sig_array_TESTB_a47 )
    
    #"""


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
    #"""

    tsf = """
    # impute seems to be unexpected keyword     ts_fe_1750_train = extract_relevant_features(df_1750_train, y_1750_train['label'], column_id='id', column_sort='time', impute_function=impute)
    
    #  Compute ts_fresh train features and select at the same time
    ts_train_TRAINBAND__6 = extract_relevant_features(X_train_TRAINBAND__6_ts_ready, y_train_TRAINBAND__6_ts_ready['label'], column_id='id', column_sort='time')
    ts_train_TRAINBAND__6.to_csv('data\\features\\ts_train_TRAINBAND__6.csv')
    #ts_train_TRAINBAND__6 = pd.read_csv('data\\features\\ts_train_TRAINBAND__6.csv', index_col=0)
    
    
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
    
    
    #"""
    ts_test_TESTB_47_all = extract_features(X_test_TESTB_47_ts_ready, column_id='id', column_sort='time', impute_function=impute)
    ts_test_TESTB_47_all.to_csv('data\\features\\ts_test_TESTB_47_all.csv')
    #ts_test_TRAINBAND_49_all = pd.read_csv('data\\features\\ts_test_TESTB_49_all.csv', index_col=0)

    #ts_test_TESTB__6_all = extract_features(X_test_TESTB__6_ts_ready, column_id='id', column_sort='time', impute_function=impute)
    #ts_test_TESTB__6_all.to_csv('data\\features\\ts_test_TESTB__6_all.csv')

    #ts_test_TESTB_47_all = extract_features(X_test_TESTB_47_ts_ready, column_id='id', column_sort='time', impute_function=impute)
    #ts_test_TESTB_47_all.to_csv('data\\features\\ts_test_TESTB_47_all.csv')
    #ts_test_TRAINBAND_49_all = pd.read_csv('data\\features\\ts_test_TESTB_47_all.csv', index_col=0)

    #ts_train_TRAINBAND_47 = extract_relevant_features(X_train_TRAINBAND_47_ts_ready, y_train_TRAINBAND_47_ts_ready['label'], column_id='id', column_sort='time')
    #ts_train_TRAINBAND_47.to_csv('data\\features\\ts_train_TRAINBAND_47.csv')
    """
    
    ts_test_TRAINBAND_47 = ts_test_TRAINBAND_47_all[ts_train_TRAINBAND_47.columns]
    ts_test_TRAINBAND_47 = ts_test_TRAINBAND_47.interpolate(axis=0)
    ts_test_TRAINBAND_49 = ts_test_TRAINBAND_49_all[ts_train_TRAINBAND_49.columns]
    ts_test_TRAINBAND_49 = ts_test_TRAINBAND_49.interpolate(axis=0)
    
    
    from Zustandsueberwachung_no_raw_signal import Classifiers
    
    
    clf__6 = Classifiers('a6')
    models__6 = clf__6.fitting(X_train_TRAINBAND__6, y_train_TRAINBAND__6)
    clf_47 = Classifiers('a47')
    models_47 = clf_47.fitting(X_train_TRAINBAND_47, y_train_TRAINBAND_47)
    clf_49 = Classifiers('a49')
    models_49 = clf_49.fitting(X_train_TRAINBAND_49, y_train_TRAINBAND_49)
    
    report__6            = clf__6.predicting(X_test_TRAINBAND__6).class_report(y_test_TRAINBAND__6)
    scores__6            = clf__6.score_table(y_test_TRAINBAND__6)
    report_47            = clf_47.predicting(X_test_TRAINBAND_47).class_report(y_test_TRAINBAND_47)
    scores_47            = clf_47.score_table(y_test_TRAINBAND_47)
    report_49            = clf_49.predicting(X_test_TRAINBAND_49).class_report(y_test_TRAINBAND_49)
    scores_49            = clf_49.score_table(y_test_TRAINBAND_49)
    report__6_47         = clf__6.predicting(X_test_TRAINBAND_47).class_report(y_test_TRAINBAND_47)
    scores__6_47         = clf__6.score_table(y_test_TRAINBAND_47)
    report_47__6         = clf_47.predicting(X_test_TRAINBAND__6).class_report(y_test_TRAINBAND__6)
    scores_47__6         = clf_47.score_table(y_test_TRAINBAND__6)
    report_49__6         = clf_49.predicting(X_test_TRAINBAND__6).class_report(y_test_TRAINBAND__6)
    scores_49__6         = clf_49.score_table(y_test_TRAINBAND__6)
    report__6_49         = clf__6.predicting(X_test_TRAINBAND_49).class_report(y_test_TRAINBAND_49)
    scores__6_49         = clf__6.score_table(y_test_TRAINBAND_49)
    report_47_49         = clf_47.predicting(X_test_TRAINBAND_49).class_report(y_test_TRAINBAND_49)
    scores_47_49         = clf_47.score_table(y_test_TRAINBAND_49)
    report_49_47         = clf_49.predicting(X_test_TRAINBAND_47).class_report(y_test_TRAINBAND_47)
    scores_49_47         = clf_49.score_table(y_test_TRAINBAND_47)
    TESTBreport__6    = clf__6.predicting(X_test_TESTB__6).class_report(y_test_TESTB__6)
    TESTBscores__6    = clf__6.score_table(y_test_TESTB__6)
    TESTBreport_47    = clf_47.predicting(X_test_TESTB_47).class_report(y_test_TESTB_47)
    TESTBscores_47    = clf_47.score_table(y_test_TESTB_47)
    TESTBreport_49    = clf_49.predicting(X_test_TESTB_49).class_report(y_test_TESTB_49)
    TESTBscores_49    = clf_49.score_table(y_test_TESTB_49)
    TESTBreport__6_47 = clf__6.predicting(X_test_TESTB_47).class_report(y_test_TESTB_47)
    TESTBscores__6_47 = clf__6.score_table(y_test_TESTB_47)
    TESTBreport_47__6 = clf_47.predicting(X_test_TESTB__6).class_report(y_test_TESTB__6)
    TESTBscores_47__6 = clf_47.score_table(y_test_TESTB__6)
    TESTBreport_49__6 = clf_49.predicting(X_test_TESTB__6).class_report(y_test_TESTB__6)
    TESTBscores_49__6 = clf_49.score_table(y_test_TESTB__6)
    TESTBreport__6_49 = clf__6.predicting(X_test_TESTB_49).class_report(y_test_TESTB_49)
    TESTBscores__6_49 = clf__6.score_table(y_test_TESTB_49)
    TESTBreport_47_49 = clf_47.predicting(X_test_TESTB_49).class_report(y_test_TESTB_49)
    TESTBscores_47_49 = clf_47.score_table(y_test_TESTB_49)
    TESTBreport_49_47 = clf_49.predicting(X_test_TESTB_47).class_report(y_test_TESTB_47)
    TESTBscores_49_47 = clf_49.score_table(y_test_TESTB_47)
    
             
    
    
    """