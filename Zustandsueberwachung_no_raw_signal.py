from helpers.functions import dfs_for_timetest_csv, sort_per_id, sort_per_id_vib
from helpers.lists import ids, val_id_type_dict, paths, short_labels, rel_ids, rel_ids_no_list, pahts_sigs
from helpers.lists import tpahts_sigs, pahts_data, tpahts_data, rel_ids_no_list_no_vibs, rel_ids_vib_only_no_list
from seperate_cuts import sep_cuts_all_sensors, concat_dfs_sep_ids, qnd_outlier_indices, qnd_bandpass_per_class, plot_all_cuts_overlapping, plot_sensors_and_cutactive
from helpers.functions import cuta_TRAINBAND_true, cuta_TESTBAND_true, cuta_TRAINBAND_false, cuta_TESTBAND_false

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import pickle
import vis
from scipy.signal import find_peaks
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

def classifiers(X__train, y__train, X__test, y__test):
    classification_reports = []
    predictions = []
    models = []
    target_names = ['class 1', 'class 2', 'class 3', 'class 4', 'class 5']
    classifier_list = [DecisionTreeClassifier(random_state=42),
                       LogisticRegression(random_state=42, solver='liblinear'),
                       BaggingClassifier(random_state=42),
                       RandomForestClassifier(random_state=42),
                       LinearDiscriminantAnalysis(),
                       QuadraticDiscriminantAnalysis(),
                       SVC(random_state=42),
                       KNeighborsClassifier(),
                       GaussianNB()]

    for clf in classifier_list:
        single_instance = clf
        single_instance.fit(X__train, y__train)
        models.append(single_instance)
        y_pred = single_instance.predict(X__test)
        predictions.append(y_pred)
        classification_reports.append(classification_report(y__test, y_pred, target_names=target_names))

    return predictions, classification_reports

class Classifiers:
    def __init__(self, domain):
        self.classification_reports = []
        self.domain = domain
        self.predictions = []
        self.models = []
        self.target_names = ['class 1', 'class 2', 'class 3', 'class 4', 'class 5']
        self.classifier_list = [DecisionTreeClassifier(random_state=42),
                                LogisticRegression(random_state=42, solver='liblinear'),
                                BaggingClassifier(random_state=42),
                                RandomForestClassifier(random_state=42),
                                LinearDiscriminantAnalysis(),
                                QuadraticDiscriminantAnalysis(),
                                SVC(random_state=42),
                                KNeighborsClassifier(),
                                GaussianNB()]

    def fitting(self, X__train, y__train):
        for clf in self.classifier_list:
            single_instance = clf
            single_instance.fit(X__train, y__train)
            self.models.append(single_instance)
        return self.models

    def predicting(self, X__test):
        # clear prediction, to not combine predictions unwanted
        self.predictions = []
        for model in self.models:
            y_pred = model.predict(X__test)
            self.predictions.append(y_pred)
        return self

    def class_report(self, y__test):
        self.classification_reports = []
        for y_pred in self.predictions:
            self.classification_reports.append(classification_report(y__test, y_pred, target_names=self.target_names))
        return self.classification_reports

    def score_table(self, y_test_TRAINBAND):
        # def metric_tables(y_test_TRAINBAND, res1, res2, res3, res4):

        metrics_count = 5
        scores_vanilla = np.zeros((len(self.predictions), metrics_count))
        # scores_adv_fe = np.zeros((len(res2), metrics_count))
        # scores_simple_fe = np.zeros((len(res3), metrics_count))
        # scores_ts_fe = np.zeros((len(res4), metrics_count))

        for i, j in enumerate(self.predictions):
            scores_vanilla[i, :] = self.scores(y_test_TRAINBAND, j)
        # for i, j in enumerate(res3):
        #    scores_simple_fe[i, :] = scores(y_test_TRAINBAND, j)
        #
        #    for i, j in enumerate(res2,):
        #        scores_adv_fe[i, :] = scores(y_test_TRAINBAND, j)
        #
        #    for i, j in enumerate(res4):
        #        scores_ts_fe[i, :] = scores(y_test_TRAINBAND, j)
        #
        return self.results_dataframe(scores_vanilla)  #\
            # , results_dataframe(scores_simple_fe), \
        #   results_dataframe(scores_adv_fe), results_dataframe(scores_ts_fe)

    #@staticmethod
    def scores(self, y_test_TRAINBAND, pred):
        #  ROCAUC needs one-hot encoding
        enc = OneHotEncoder(handle_unknown='ignore').fit(y_test_TRAINBAND.reshape(-1, 1))
        pred_one_hot = enc.transform(pred.reshape(-1, 1)).toarray()

        # Macro because each class has the same number of examples
        scores_list = [accuracy_score(y_test_TRAINBAND, pred),
                       precision_score(y_test_TRAINBAND, pred, average='macro'),
                       recall_score(y_test_TRAINBAND, pred, average='macro'),
                       f1_score(y_test_TRAINBAND, pred, average='macro'),
                       roc_auc_score(y_test_TRAINBAND, pred_one_hot, multi_class='ovr')]

        return [np.round(x, 3) for x in scores_list]

    #@staticmethod
    def results_dataframe(self, data):
        return pd.DataFrame(data, columns=['Accuracy', 'Precision macro', 'Recall macro', 'F1 macro', 'ROCAUC'],
                            index=['DecisionTreeClassifier', 'LogisticRegression', 'BaggingClassifier',
                                   'RandomForestClassifier', 'LinearDiscriminantAnalysis',
                                   'QuadraticDiscriminantAnalysis', 'SVC', 'KNeighborsClassifier',
                                   'GaussianNB']).sort_values('F1 macro', ascending=False)


def standardize_data(X__train, X__test):
    scaler = StandardScaler()
    #  Fit with training data, only transform the test data
    return scaler.fit_transform(X__train), scaler.transform(X__test)


def scores(y_test_TRAINBAND, pred):
    #  ROCAUC needs one-hot encoding
    from sklearn.preprocessing import OneHotEncoder
    enc = OneHotEncoder(handle_unknown='ignore').fit(y_test_TRAINBAND.reshape(-1, 1))
    pred_one_hot = enc.transform(pred.reshape(-1, 1)).toarray()

    # Macro because each class has the same number of examples
    scores_list = [accuracy_score(y_test_TRAINBAND, pred),
                   precision_score(y_test_TRAINBAND, pred, average='macro'),
                   recall_score(y_test_TRAINBAND, pred, average='macro'),
                   f1_score(y_test_TRAINBAND, pred, average='macro'),
                   roc_auc_score(y_test_TRAINBAND, pred_one_hot, multi_class='ovr')]

    return [np.round(x, 3) for x in scores_list]


def results_dataframe(data):
    return pd.DataFrame(data, columns=['Accuracy', 'Precision macro', 'Recall macro', 'F1 macro', 'ROCAUC'],
                        index=['DecisionTreeClassifier', 'LogisticRegression', 'BaggingClassifier',
                               'RandomForestClassifier',  'LinearDiscriminantAnalysis',
                               'QuadraticDiscriminantAnalysis',  'SVC', 'KNeighborsClassifier',
                               'GaussianNB']).sort_values('F1 macro', ascending=False)


def metric_tables(y_test_TRAINBAND, res1):
#def metric_tables(y_test_TRAINBAND, res1, res2, res3, res4):

    metrics_count = 5
    scores_vanilla = np.zeros((len(res1), metrics_count))
    #scores_adv_fe = np.zeros((len(res2), metrics_count))
    #scores_simple_fe = np.zeros((len(res3), metrics_count))
    #scores_ts_fe = np.zeros((len(res4), metrics_count))

    for i, j in enumerate(res1):
        scores_vanilla[i, :] = scores(y_test_TRAINBAND, j)

    #for i, j in enumerate(res3):
    #    scores_simple_fe[i, :] = scores(y_test_TRAINBAND, j)
#
#    for i, j in enumerate(res2,):
#        scores_adv_fe[i, :] = scores(y_test_TRAINBAND, j)
#
#    for i, j in enumerate(res4):
#        scores_ts_fe[i, :] = scores(y_test_TRAINBAND, j)
#
    return results_dataframe(scores_vanilla)\
        #, results_dataframe(scores_simple_fe), \
        #   results_dataframe(scores_adv_fe), results_dataframe(scores_ts_fe)


def list_col_to_arr(data, idx, cols):
    df = data[idx]['val'].values
    rows = len(df)
    arr = np.zeros((rows, cols))
    for i in range(rows):
        arr[i, :] = df[i]
    return arr


def seperate_fbands(df):
    if len(df[0]) <= 66:
        for i in range(5):
            data = df[i]
            indices = [43, 50, 57]
            bands = [list_col_to_arr(data, indices[0], 8), list_col_to_arr(data, indices[1], 8),
                     list_col_to_arr(data, indices[2], 8)]

            for g, h in zip(indices, bands):
                for j in range(8):
                    data.append(pd.DataFrame({'source': data[g]['source'].values, 'val': h[:, j]}))
    else:
        print('List already seperated')
    return df


def clean_train_quick_and_dirty(data, offset_percent, class_=None):
    print('start clean clean_train_quick_and_dirty')
    len_data = len(data[0])
    if class_ == 'a6':
        active_cut_data1a6_newer, active_cut_data2a6_newer, active_cut_data3a6_newer, active_cut_data4a6_newer, \
        active_cut_data5a6_newer = data[0], data[1], data[2], data[3], data[4]

        # kick indices ouf of p_vorschub out of these bounds
        list_1a6_bandpass = qnd_bandpass_per_class(active_cut_data1a6_newer, 1, 16.67, 15.7)
        list_2a6_bandpass = qnd_bandpass_per_class(active_cut_data2a6_newer, 1, 17, 15.9156)
        list_3a6_bandpass = qnd_bandpass_per_class(active_cut_data3a6_newer, 1, 18.5, 16)
        list_4a6_bandpass = qnd_bandpass_per_class(active_cut_data4a6_newer, 1, 19.44, 17.44)
        list_5a6_bandpass = qnd_bandpass_per_class(active_cut_data5a6_newer, 1, 19, 16)
        list_1a6_bandpass.sort(reverse=True)
        list_2a6_bandpass.sort(reverse=True)
        list_3a6_bandpass.sort(reverse=True)
        list_4a6_bandpass.sort(reverse=True)
        list_5a6_bandpass.sort(reverse=True)

        for i in list_1a6_bandpass:
            for j in range(len_data):
                active_cut_data1a6_newer[j].pop(i)
        for i in list_2a6_bandpass:
            for j in range(len_data):
                active_cut_data2a6_newer[j].pop(i)
        for i in list_3a6_bandpass:
            for j in range(len_data):
                active_cut_data3a6_newer[j].pop(i)
        for i in list_4a6_bandpass:
            for j in range(len_data):
                active_cut_data4a6_newer[j].pop(i)
        for i in list_5a6_bandpass:
            for j in range(len_data):
                active_cut_data5a6_newer[j].pop(i)

        active_cut_data1a6_newer_lens = np.array(
            [len(active_cut_data1a6_newer[2][x]) for x in range(len(active_cut_data1a6_newer[2]))]).reshape(
            len(active_cut_data1a6_newer[2]), 1)
        active_cut_data2a6_newer_lens = np.array(
            [len(active_cut_data2a6_newer[2][x]) for x in range(len(active_cut_data2a6_newer[2]))]).reshape(
            len(active_cut_data2a6_newer[2]), 1)
        active_cut_data3a6_newer_lens = np.array(
            [len(active_cut_data3a6_newer[2][x]) for x in range(len(active_cut_data3a6_newer[2]))]).reshape(
            len(active_cut_data3a6_newer[2]), 1)
        active_cut_data4a6_newer_lens = np.array(
            [len(active_cut_data4a6_newer[2][x]) for x in range(len(active_cut_data4a6_newer[2]))]).reshape(
            len(active_cut_data4a6_newer[2]), 1)
        active_cut_data5a6_newer_lens = np.array(
            [len(active_cut_data5a6_newer[2][x]) for x in range(len(active_cut_data5a6_newer[2]))]).reshape(
            len(active_cut_data5a6_newer[2]), 1)
        wrong_len_list_1a6 = qnd_outlier_indices(active_cut_data1a6_newer_lens, offset_percent, '1a6 ')
        wrong_len_list_2a6 = qnd_outlier_indices(active_cut_data2a6_newer_lens, offset_percent, '2a6 ')
        wrong_len_list_3a6 = qnd_outlier_indices(active_cut_data3a6_newer_lens, offset_percent, '3a6 ')
        wrong_len_list_4a6 = qnd_outlier_indices(active_cut_data4a6_newer_lens, offset_percent, '4a6 ')
        wrong_len_list_5a6 = qnd_outlier_indices(active_cut_data5a6_newer_lens, offset_percent, '5a6 ')
        wrong_len_list_1a6.sort(reverse=True)
        wrong_len_list_2a6.sort(reverse=True)
        wrong_len_list_3a6.sort(reverse=True)
        wrong_len_list_4a6.sort(reverse=True)
        wrong_len_list_5a6.sort(reverse=True)
        o1a6_active_cut_data1a6_newer_lens = list(active_cut_data1a6_newer_lens.reshape(-1))
        o2a6_active_cut_data2a6_newer_lens = list(active_cut_data2a6_newer_lens.reshape(-1))
        o3a6_active_cut_data3a6_newer_lens = list(active_cut_data3a6_newer_lens.reshape(-1))
        o4a6_active_cut_data4a6_newer_lens = list(active_cut_data4a6_newer_lens.reshape(-1))
        o5a6_active_cut_data5a6_newer_lens = list(active_cut_data5a6_newer_lens.reshape(-1))
        o1a6_active_cut_data1a6_newer_lens.sort()
        o2a6_active_cut_data2a6_newer_lens.sort()
        o3a6_active_cut_data3a6_newer_lens.sort()
        o4a6_active_cut_data4a6_newer_lens.sort()
        o5a6_active_cut_data5a6_newer_lens.sort()
        plt.figure()
        plt.scatter(range(len(o1a6_active_cut_data1a6_newer_lens)), o1a6_active_cut_data1a6_newer_lens, label='1a6')
        plt.scatter(range(len(o2a6_active_cut_data2a6_newer_lens)), o2a6_active_cut_data2a6_newer_lens, label='2a6')
        plt.scatter(range(len(o3a6_active_cut_data3a6_newer_lens)), o3a6_active_cut_data3a6_newer_lens, label='3a6')
        plt.scatter(range(len(o4a6_active_cut_data4a6_newer_lens)), o4a6_active_cut_data4a6_newer_lens, label='4a6')
        plt.scatter(range(len(o5a6_active_cut_data5a6_newer_lens)), o5a6_active_cut_data5a6_newer_lens, label='5a6')
        plt.legend()
        plt.title('sorted lenghts of cuts')
        for i in wrong_len_list_1a6:
            for j in range(len_data):
                active_cut_data1a6_newer[j].pop(i)
        for i in wrong_len_list_2a6:
            for j in range(len_data):
                active_cut_data2a6_newer[j].pop(i)
        for i in wrong_len_list_3a6:
            for j in range(len_data):
                active_cut_data3a6_newer[j].pop(i)
        for i in wrong_len_list_4a6:
            for j in range(len_data):
                active_cut_data4a6_newer[j].pop(i)
        for i in wrong_len_list_5a6:
            for j in range(len_data):
                active_cut_data5a6_newer[j].pop(i)

        data[0], data[1], data[2], data[3], data[4] = active_cut_data1a6_newer, active_cut_data2a6_newer, \
                                                      active_cut_data3a6_newer, active_cut_data4a6_newer, \
        active_cut_data5a6_newer

    elif class_ == 'a47':
        active_cut_data1a47_newer, active_cut_data2a47_newer, active_cut_data3a47_newer, active_cut_data4a47_newer, \
        active_cut_data5a47_newer = data[0], data[1], data[2], data[3], data[4]

        list_1a47_bandpass = qnd_bandpass_per_class(active_cut_data1a47_newer, 16.67, 15.7)
        list_2a47_bandpass = qnd_bandpass_per_class(active_cut_data2a47_newer, 19, 15.9156)
        list_3a47_bandpass = qnd_bandpass_per_class(active_cut_data3a47_newer, 18.5, 16)
        list_4a47_bandpass = qnd_bandpass_per_class(active_cut_data4a47_newer, 18.5, 16.2)
        list_5a47_bandpass = qnd_bandpass_per_class(active_cut_data5a47_newer, 19, 16.5)
        list_1a47_bandpass.sort(reverse=True)
        list_2a47_bandpass.sort(reverse=True)
        list_3a47_bandpass.sort(reverse=True)
        list_4a47_bandpass.sort(reverse=True)
        list_5a47_bandpass.sort(reverse=True)
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
        active_cut_data1a47_newer_lens = np.array(
            [len(active_cut_data1a47_newer[0][x]) for x in range(len(active_cut_data1a47_newer[0]))]).reshape(
            len(active_cut_data1a47_newer[0]), 1)
        active_cut_data2a47_newer_lens = np.array(
            [len(active_cut_data2a47_newer[0][x]) for x in range(len(active_cut_data2a47_newer[0]))]).reshape(
            len(active_cut_data2a47_newer[0]), 1)
        active_cut_data3a47_newer_lens = np.array(
            [len(active_cut_data3a47_newer[0][x]) for x in range(len(active_cut_data3a47_newer[0]))]).reshape(
            len(active_cut_data3a47_newer[0]), 1)
        active_cut_data4a47_newer_lens = np.array(
            [len(active_cut_data4a47_newer[0][x]) for x in range(len(active_cut_data4a47_newer[0]))]).reshape(
            len(active_cut_data4a47_newer[0]), 1)
        active_cut_data5a47_newer_lens = np.array(
            [len(active_cut_data5a47_newer[0][x]) for x in range(len(active_cut_data5a47_newer[0]))]).reshape(
            len(active_cut_data5a47_newer[0]), 1)
        wrong_len_list_1a47 = qnd_outlier_indices(active_cut_data1a47_newer_lens, offset_percent, '1a47')
        wrong_len_list_2a47 = qnd_outlier_indices(active_cut_data2a47_newer_lens, offset_percent, '2a47')
        wrong_len_list_3a47 = qnd_outlier_indices(active_cut_data3a47_newer_lens, offset_percent, '3a47')
        wrong_len_list_4a47 = qnd_outlier_indices(active_cut_data4a47_newer_lens, offset_percent, '4a47')
        wrong_len_list_5a47 = qnd_outlier_indices(active_cut_data5a47_newer_lens, offset_percent, '5a47')
        wrong_len_list_1a47.sort(reverse=True)
        wrong_len_list_2a47.sort(reverse=True)
        wrong_len_list_3a47.sort(reverse=True)
        wrong_len_list_4a47.sort(reverse=True)
        wrong_len_list_5a47.sort(reverse=True)
        o1a47active_cut_data1a47_newer_lens = list(active_cut_data1a47_newer_lens.reshape(-1))
        o2a47active_cut_data2a47_newer_lens = list(active_cut_data2a47_newer_lens.reshape(-1))
        o3a47active_cut_data3a47_newer_lens = list(active_cut_data3a47_newer_lens.reshape(-1))
        o4a47active_cut_data4a47_newer_lens = list(active_cut_data4a47_newer_lens.reshape(-1))
        o5a47active_cut_data5a47_newer_lens = list(active_cut_data5a47_newer_lens.reshape(-1))
        o1a47active_cut_data1a47_newer_lens.sort()
        o2a47active_cut_data2a47_newer_lens.sort()
        o3a47active_cut_data3a47_newer_lens.sort()
        o4a47active_cut_data4a47_newer_lens.sort()
        o5a47active_cut_data5a47_newer_lens.sort()
        plt.figure()
        plt.scatter(range(len(o1a47active_cut_data1a47_newer_lens)), o1a47active_cut_data1a47_newer_lens, label='1a47')
        plt.scatter(range(len(o2a47active_cut_data2a47_newer_lens)), o2a47active_cut_data2a47_newer_lens, label='2a47')
        plt.scatter(range(len(o3a47active_cut_data3a47_newer_lens)), o3a47active_cut_data3a47_newer_lens, label='3a47')
        plt.scatter(range(len(o4a47active_cut_data4a47_newer_lens)), o4a47active_cut_data4a47_newer_lens, label='4a47')
        plt.scatter(range(len(o5a47active_cut_data5a47_newer_lens)), o5a47active_cut_data5a47_newer_lens, label='5a47')
        plt.legend()

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

        data[0], data[1], data[2], data[3], data[4] = active_cut_data1a47_newer, active_cut_data2a47_newer, \
                                                      active_cut_data3a47_newer, active_cut_data4a47_newer, \
        active_cut_data5a47_newer

    elif class_ == 'a49':
        active_cut_data1a49_newer, active_cut_data2a49_newer, active_cut_data3a49_newer, active_cut_data4a49_newer,\
        active_cut_data5a49_newer  = data[0], data[1], data[2], data[3], data[4]
        list_1a49_bandpass = qnd_bandpass_per_class(active_cut_data1a49_newer, 16.67, 15.7)
        list_2a49_bandpass = qnd_bandpass_per_class(active_cut_data2a49_newer, 17, 15.9156)
        list_3a49_bandpass = qnd_bandpass_per_class(active_cut_data3a49_newer, 18.5, 16)
        list_4a49_bandpass = qnd_bandpass_per_class(active_cut_data4a49_newer, 19.5, 16.2)
        list_5a49_bandpass = qnd_bandpass_per_class(active_cut_data5a49_newer, 20, 18)
        list_1a49_bandpass.sort(reverse=True)
        list_2a49_bandpass.sort(reverse=True)
        list_3a49_bandpass.sort(reverse=True)
        list_4a49_bandpass.sort(reverse=True)
        list_5a49_bandpass.sort(reverse=True)
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
        active_cut_data1a49_newer_lens = np.array(
            [len(active_cut_data1a49_newer[0][x]) for x in range(len(active_cut_data1a49_newer[0]))]).reshape(
            len(active_cut_data1a49_newer[0]), 1)
        active_cut_data2a49_newer_lens = np.array(
            [len(active_cut_data2a49_newer[0][x]) for x in range(len(active_cut_data2a49_newer[0]))]).reshape(
            len(active_cut_data2a49_newer[0]), 1)
        active_cut_data3a49_newer_lens = np.array(
            [len(active_cut_data3a49_newer[0][x]) for x in range(len(active_cut_data3a49_newer[0]))]).reshape(
            len(active_cut_data3a49_newer[0]), 1)
        active_cut_data4a49_newer_lens = np.array(
            [len(active_cut_data4a49_newer[0][x]) for x in range(len(active_cut_data4a49_newer[0]))]).reshape(
            len(active_cut_data4a49_newer[0]), 1)
        active_cut_data5a49_newer_lens = np.array(
            [len(active_cut_data5a49_newer[0][x]) for x in range(len(active_cut_data5a49_newer[0]))]).reshape(
            len(active_cut_data5a49_newer[0]), 1)
        wrong_len_list_1a49 = qnd_outlier_indices(active_cut_data1a49_newer_lens, offset_percent, '1a49')
        wrong_len_list_2a49 = qnd_outlier_indices(active_cut_data2a49_newer_lens, offset_percent, '2a49')
        wrong_len_list_3a49 = qnd_outlier_indices(active_cut_data3a49_newer_lens, offset_percent, '3a49')
        wrong_len_list_4a49 = qnd_outlier_indices(active_cut_data4a49_newer_lens, offset_percent, '4a49')
        wrong_len_list_5a49 = qnd_outlier_indices(active_cut_data5a49_newer_lens, offset_percent, '5a49')
        wrong_len_list_1a49.sort(reverse=True)
        wrong_len_list_2a49.sort(reverse=True)
        wrong_len_list_3a49.sort(reverse=True)
        wrong_len_list_4a49.sort(reverse=True)
        wrong_len_list_5a49.sort(reverse=True)
        o1a49active_cut_data1a49_newer_lens = list(active_cut_data1a49_newer_lens.reshape(-1))
        o2a49active_cut_data2a49_newer_lens = list(active_cut_data2a49_newer_lens.reshape(-1))
        o3a49active_cut_data3a49_newer_lens = list(active_cut_data3a49_newer_lens.reshape(-1))
        o4a49active_cut_data4a49_newer_lens = list(active_cut_data4a49_newer_lens.reshape(-1))
        o5a49active_cut_data5a49_newer_lens = list(active_cut_data5a49_newer_lens.reshape(-1))
        o1a49active_cut_data1a49_newer_lens.sort()
        o2a49active_cut_data2a49_newer_lens.sort()
        o3a49active_cut_data3a49_newer_lens.sort()
        o4a49active_cut_data4a49_newer_lens.sort()
        o5a49active_cut_data5a49_newer_lens.sort()
        plt.figure()
        plt.scatter(range(len(o1a49active_cut_data1a49_newer_lens)), o1a49active_cut_data1a49_newer_lens, label='1a49')
        plt.scatter(range(len(o2a49active_cut_data2a49_newer_lens)), o2a49active_cut_data2a49_newer_lens, label='2a49')
        plt.scatter(range(len(o3a49active_cut_data3a49_newer_lens)), o3a49active_cut_data3a49_newer_lens, label='3a49')
        plt.scatter(range(len(o4a49active_cut_data4a49_newer_lens)), o4a49active_cut_data4a49_newer_lens, label='4a49')
        plt.scatter(range(len(o5a49active_cut_data5a49_newer_lens)), o5a49active_cut_data5a49_newer_lens, label='5a49')
        plt.legend()
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

        data[0], data[1], data[2], data[3], data[4] = active_cut_data1a49_newer, active_cut_data2a49_newer, \
                                                      active_cut_data3a49_newer, active_cut_data4a49_newer, \
        active_cut_data5a49_newer

    else:
        data = None
        print('wrong class namestring in clean_quick_and_dirty TRAINBAND')
    return data


def clean_test_quick_and_dirty(data, toffset_percent, class_=None):
    print('start clean clean_test_quick_and_dirty')

    if class_ == 'a6':
        tactive_cut_data1a6_newer, tactive_cut_data2a6_newer, tactive_cut_data3a6_newer, tactive_cut_data4a6_newer, \
        tactive_cut_data5a6_newer = data[0], data[1], data[2], data[3], data[4]

        # tlist_1a6_bandpass = qnd_bandpass_per_class(tactive_cut_data1a6_newer, 16.67, 15.7)
        # tlist_2a6_bandpass = qnd_bandpass_per_class(tactive_cut_data2a6_newer, 17, 15.9156)
        # tlist_3a6_bandpass = qnd_bandpass_per_class(tactive_cut_data3a6_newer, 18.5, 16)
        # tlist_4a6_bandpass = qnd_bandpass_per_class(tactive_cut_data4a6_newer, 19.5, 16.2)
        # tlist_5a6_bandpass = qnd_bandpass_per_class(tactive_cut_data5a6_newer, 19, 16)
        # tlist_1a6_bandpass.sort(reverse=True)
        # tlist_2a6_bandpass.sort(reverse=True)
        # tlist_3a6_bandpass.sort(reverse=True)
        # tlist_4a6_bandpass.sort(reverse=True)
        # tlist_5a6_bandpass.sort(reverse=True)
        # for i in tlist_1a6_bandpass:
        #    tactive_cut_data1a6_newer[0].pop(i)
        # for i in tlist_2a6_bandpass:
        #    tactive_cut_data2a6_newer[0].pop(i)
        # for i in tlist_3a6_bandpass:
        #    tactive_cut_data3a6_newer[0].pop(i)
        # for i in tlist_4a6_bandpass:
        #    tactive_cut_data4a6_newer[0].pop(i)
        # for i in tlist_5a6_bandpass:
        #    tactive_cut_data5a6_newer[0].pop(i)
        tactive_cut_data1a6_newer_lens = np.array(
            [len(tactive_cut_data1a6_newer[0][x]) for x in range(len(tactive_cut_data1a6_newer[0]))]).reshape(
            len(tactive_cut_data1a6_newer[0]), 1)
        tactive_cut_data2a6_newer_lens = np.array(
            [len(tactive_cut_data2a6_newer[0][x]) for x in range(len(tactive_cut_data2a6_newer[0]))]).reshape(
            len(tactive_cut_data2a6_newer[0]), 1)
        tactive_cut_data3a6_newer_lens = np.array(
            [len(tactive_cut_data3a6_newer[0][x]) for x in range(len(tactive_cut_data3a6_newer[0]))]).reshape(
            len(tactive_cut_data3a6_newer[0]), 1)
        tactive_cut_data4a6_newer_lens = np.array(
            [len(tactive_cut_data4a6_newer[0][x]) for x in range(len(tactive_cut_data4a6_newer[0]))]).reshape(
            len(tactive_cut_data4a6_newer[0]), 1)
        tactive_cut_data5a6_newer_lens = np.array(
            [len(tactive_cut_data5a6_newer[0][x]) for x in range(len(tactive_cut_data5a6_newer[0]))]).reshape(
            len(tactive_cut_data5a6_newer[0]), 1)
        twrong_len_list_1a6 = qnd_outlier_indices(tactive_cut_data1a6_newer_lens, toffset_percent, 't1a6 ')
        twrong_len_list_2a6 = qnd_outlier_indices(tactive_cut_data2a6_newer_lens, toffset_percent, 't2a6 ')
        twrong_len_list_3a6 = qnd_outlier_indices(tactive_cut_data3a6_newer_lens, toffset_percent, 't3a6 ')
        twrong_len_list_4a6 = qnd_outlier_indices(tactive_cut_data4a6_newer_lens, toffset_percent, 't4a6 ')
        twrong_len_list_5a6 = qnd_outlier_indices(tactive_cut_data5a6_newer_lens, toffset_percent, 't5a6 ')
        twrong_len_list_1a6.sort(reverse=True)
        twrong_len_list_2a6.sort(reverse=True)
        twrong_len_list_3a6.sort(reverse=True)
        twrong_len_list_4a6.sort(reverse=True)
        twrong_len_list_5a6.sort(reverse=True)
        for i in twrong_len_list_1a6:
            tactive_cut_data1a6_newer[0].pop(i)
        for i in twrong_len_list_2a6:
            tactive_cut_data2a6_newer[0].pop(i)
        for ti in twrong_len_list_3a6:
            tactive_cut_data3a6_newer[0].pop(i)
        for i in twrong_len_list_4a6:
            tactive_cut_data4a6_newer[0].pop(i)
        for i in twrong_len_list_5a6:
            tactive_cut_data5a6_newer[0].pop(i)

        data[0], data[1], data[2], data[3], data[4] = tactive_cut_data1a6_newer, tactive_cut_data2a6_newer, \
                                                      tactive_cut_data3a6_newer, tactive_cut_data4a6_newer, \
                                                      tactive_cut_data5a6_newer

    elif class_ == 'a47':
        tactive_cut_data1a47_newer, tactive_cut_data2a47_newer, tactive_cut_data3a47_newer, tactive_cut_data4a47_newer, \
        tactive_cut_data5a47_newer = data[0], data[1], data[2], data[3], data[4]

        # tlist_1a47_bandpass = qnd_bandpass_per_class(tactive_cut_data1a47_newer, 16.67, 15.7)
        # tlist_2a47_bandpass = qnd_bandpass_per_class(tactive_cut_data2a47_newer, 17, 15.9156)
        # tlist_3a47_bandpass = qnd_bandpass_per_class(tactive_cut_data3a47_newer, 18.5, 16)
        # tlist_4a47_bandpass = qnd_bandpass_per_class(tactive_cut_data4a47_newer, 19.5, 16)
        # tlist_5a47_bandpass = qnd_bandpass_per_class(tactive_cut_data5a47_newer, 18.7, 16)
        # tlist_1a47_bandpass.sort(reverse=True)
        # tlist_2a47_bandpass.sort(reverse=True)
        # tlist_3a47_bandpass.sort(reverse=True)
        # tlist_4a47_bandpass.sort(reverse=True)
        # tlist_5a47_bandpass.sort(reverse=True)
        # for i in tlist_1a47_bandpass:
        #    tactive_cut_data1a47_newer[0].pop(i)
        # for i in tlist_2a47_bandpass:
        #    tactive_cut_data2a47_newer[0].pop(i)
        # for i in tlist_3a47_bandpass:
        #    tactive_cut_data3a47_newer[0].pop(i)
        # for i in tlist_4a47_bandpass:
        #    tactive_cut_data4a47_newer[0].pop(i)
        # for i in tlist_5a47_bandpass:
        #    tactive_cut_data5a47_newer[0].pop(i)
        tactive_cut_data1a47_newer_lens = np.array(
            [len(tactive_cut_data1a47_newer[0][x]) for x in range(len(tactive_cut_data1a47_newer[0]))]).reshape(
            len(tactive_cut_data1a47_newer[0]), 1)
        tactive_cut_data2a47_newer_lens = np.array(
            [len(tactive_cut_data2a47_newer[0][x]) for x in range(len(tactive_cut_data2a47_newer[0]))]).reshape(
            len(tactive_cut_data2a47_newer[0]), 1)
        tactive_cut_data3a47_newer_lens = np.array(
            [len(tactive_cut_data3a47_newer[0][x]) for x in range(len(tactive_cut_data3a47_newer[0]))]).reshape(
            len(tactive_cut_data3a47_newer[0]), 1)
        tactive_cut_data4a47_newer_lens = np.array(
            [len(tactive_cut_data4a47_newer[0][x]) for x in range(len(tactive_cut_data4a47_newer[0]))]).reshape(
            len(tactive_cut_data4a47_newer[0]), 1)
        tactive_cut_data5a47_newer_lens = np.array(
            [len(tactive_cut_data5a47_newer[0][x]) for x in range(len(tactive_cut_data5a47_newer[0]))]).reshape(
            len(tactive_cut_data5a47_newer[0]), 1)
        twrong_len_list_1a47 = qnd_outlier_indices(tactive_cut_data1a47_newer_lens, toffset_percent, 't1a47')
        twrong_len_list_2a47 = qnd_outlier_indices(tactive_cut_data2a47_newer_lens, toffset_percent, 't2a47')
        twrong_len_list_3a47 = qnd_outlier_indices(tactive_cut_data3a47_newer_lens, toffset_percent, 't3a47')
        twrong_len_list_4a47 = qnd_outlier_indices(tactive_cut_data4a47_newer_lens, toffset_percent, 't4a47')
        twrong_len_list_5a47 = qnd_outlier_indices(tactive_cut_data5a47_newer_lens, toffset_percent, 't5a47')
        twrong_len_list_1a47.sort(reverse=True)
        twrong_len_list_2a47.sort(reverse=True)
        twrong_len_list_3a47.sort(reverse=True)
        twrong_len_list_4a47.sort(reverse=True)
        twrong_len_list_5a47.sort(reverse=True)
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

        data[0], data[1], data[2], data[3], data[4] = tactive_cut_data1a47_newer, tactive_cut_data2a47_newer, \
                                                      tactive_cut_data3a47_newer, tactive_cut_data4a47_newer, \
                                                      tactive_cut_data5a47_newer

    elif class_ == 'a49':
        tactive_cut_data1a49_newer, tactive_cut_data2a49_newer, tactive_cut_data3a49_newer, tactive_cut_data4a49_newer, \
        tactive_cut_data5a49_newer = data[0], data[1], data[2], data[3], data[4]

        # tlist_1a49_bandpass = qnd_bandpass_per_class(tactive_cut_data1a49_newer, 16.67, 15.7)
        # tlist_2a49_bandpass = qnd_bandpass_per_class(tactive_cut_data2a49_newer, 17, 15.9156)
        # tlist_3a49_bandpass = qnd_bandpass_per_class(tactive_cut_data3a49_newer, 18.5, 16)
        # tlist_4a49_bandpass = qnd_bandpass_per_class(tactive_cut_data4a49_newer, 19.5, 16)
        # tlist_5a49_bandpass = qnd_bandpass_per_class(tactive_cut_data5a49_newer, 18.7, 16)
        # tlist_1a49_bandpass.sort(reverse=True)
        # tlist_2a49_bandpass.sort(reverse=True)
        # tlist_3a49_bandpass.sort(reverse=True)
        # tlist_4a49_bandpass.sort(reverse=True)
        # tlist_5a49_bandpass.sort(reverse=True)
        # for i in tlist_1a49_bandpass:
        #    tactive_cut_data1a49_newer[0].pop(i)
        # for i in tlist_2a49_bandpass:
        #    tactive_cut_data2a49_newer[0].pop(i)
        # for i in tlist_3a49_bandpass:
        #    tactive_cut_data3a49_newer[0].pop(i)
        # for i in tlist_4a49_bandpass:
        #    tactive_cut_data4a49_newer[0].pop(i)
        # for i in tlist_5a49_bandpass:
        #    tactive_cut_data5a49_newer[0].pop(i)
        tactive_cut_data1a49_newer_lens = np.array(
            [len(tactive_cut_data1a49_newer[0][x]) for x in range(len(tactive_cut_data1a49_newer[0]))]).reshape(
            len(tactive_cut_data1a49_newer[0]), 1)
        tactive_cut_data2a49_newer_lens = np.array(
            [len(tactive_cut_data2a49_newer[0][x]) for x in range(len(tactive_cut_data2a49_newer[0]))]).reshape(
            len(tactive_cut_data2a49_newer[0]), 1)
        tactive_cut_data3a49_newer_lens = np.array(
            [len(tactive_cut_data3a49_newer[0][x]) for x in range(len(tactive_cut_data3a49_newer[0]))]).reshape(
            len(tactive_cut_data3a49_newer[0]), 1)
        tactive_cut_data4a49_newer_lens = np.array(
            [len(tactive_cut_data4a49_newer[0][x]) for x in range(len(tactive_cut_data4a49_newer[0]))]).reshape(
            len(tactive_cut_data4a49_newer[0]), 1)
        tactive_cut_data5a49_newer_lens = np.array(
            [len(tactive_cut_data5a49_newer[0][x]) for x in range(len(tactive_cut_data5a49_newer[0]))]).reshape(
            len(tactive_cut_data5a49_newer[0]), 1)
        twrong_len_list_1a49 = qnd_outlier_indices(tactive_cut_data1a49_newer_lens, toffset_percent, 't1a49')
        twrong_len_list_2a49 = qnd_outlier_indices(tactive_cut_data2a49_newer_lens, toffset_percent, 't2a49')
        twrong_len_list_3a49 = qnd_outlier_indices(tactive_cut_data3a49_newer_lens, toffset_percent, 't3a49')
        twrong_len_list_4a49 = qnd_outlier_indices(tactive_cut_data4a49_newer_lens, toffset_percent, 't4a49')
        twrong_len_list_5a49 = qnd_outlier_indices(tactive_cut_data5a49_newer_lens, toffset_percent, 't5a49')
        twrong_len_list_1a49.sort(reverse=True)
        twrong_len_list_2a49.sort(reverse=True)
        twrong_len_list_3a49.sort(reverse=True)
        twrong_len_list_4a49.sort(reverse=True)
        twrong_len_list_5a49.sort(reverse=True)
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

        data[0], data[1], data[2], data[3], data[4] = tactive_cut_data1a49_newer, tactive_cut_data2a49_newer, \
                                                      tactive_cut_data3a49_newer, tactive_cut_data4a49_newer, \
                                                      tactive_cut_data5a49_newer

    else:
        data = None
        print('wrong class namestring in clean_quick_and_dirty TESTBAND')
    return data
def calc_cut_durations(ctru, cfa):
    begin_a6 = [x['shifted'].values for x in ctru]
    end_a6 = [x['shifted'].values for x in cfa]

    durations = []
    assert len(begin_a6) == len(end_a6)
    for i in range(len(begin_a6)):
        cut_time = (end_a6[i] - begin_a6[i]) / np.timedelta64(1, 'ns')
        durations.append(cut_time)
    durations = np.concatenate(durations)
    return durations

def make_array(all_active_cut, cuta_true, cuta_false, col_size):

    durations = calc_cut_durations(cuta_true, cuta_false)

    col_size = col_size
    row_size = len(durations)
    first_bigger_array = np.zeros((row_size, col_size))

    first_bigger_array[:, 1] = durations
    end1 = len(cuta_true[0])
    end2 = end1 + len(cuta_true[1])
    end3 = end2 + len(cuta_true[2])
    end4 = end3 + len(cuta_true[3])
    end5 = end4 + len(cuta_true[4])
    #end1 = len(all_active_cut[0][0])
    #end2 = end1 + len(all_active_cut[0][1])
    #end3 = end2 + len(all_active_cut[0][2])
    #end4 = end3 + len(all_active_cut[0][3])
    #end5 = end4 + len(all_active_cut[0][4])
    ends = [end1, end2, end3, end4, end5]

    #first_bigger_array[0:end1, -1] = 1
    #first_bigger_array[end1:end2, -1] = 2
    #first_bigger_array[end2:end3, -1] = 3
    #first_bigger_array[end3:end4, -1] = 4
    #first_bigger_array[end4:end5, -1] = 5
    ##  Done same as above in  loop below
    # first col gets the class
    for i, j in enumerate(ends):
        # first one should be zero, rest um eins verschoben wie oben
        if i == 0:
            row = 0
        else:
            row = ends[i-1]
        first_bigger_array[row:j, 0] = i + 1


    #all_active_cut = [active_cut_data1a6_newer, active_cut_data2a6_newer, active_cut_data3a6_newer, active_cut_data4a6_newer, active_cut_data5a6_newer]
    for g, h in enumerate(rel_ids_no_list):
        for i, j in enumerate(ends):
            if i == 0:
                row = 0
            else:
                row = ends[i - 1]

            first_bigger_array[row:j, g + 1] = [all_active_cut[i][g][x]['val'].mean() for x in range(len(all_active_cut[i][g]))]



    # TODO understand the fillna
    mask = np.isnan(first_bigger_array)
    idx = np.where(~mask, np.arange(mask.shape[1]),0)
    np.maximum.accumulate(idx, axis=1, out=idx)
    first_bigger_array[mask] = first_bigger_array[np.nonzero(mask)[0], idx[mask]]

    return first_bigger_array, ends

path_final_data = 'E:\\ausgelagert thesis daten\\final_data\\cut_start_stop_times'
print('here')
cutas_TRAINBAND_true_a6 = cuta_TRAINBAND_true(path_final_data, 'a6')
cutas_TRAINBAND_false_a6 = cuta_TRAINBAND_false(path_final_data, 'a6')
cutas_TRAINBAND_true_a47 = cuta_TRAINBAND_true(path_final_data, 'a47')
cutas_TRAINBAND_false_a47 = cuta_TRAINBAND_false(path_final_data, 'a47')
cutas_TRAINBAND_true_a49 = cuta_TRAINBAND_true(path_final_data, 'a49')
cutas_TRAINBAND_false_a49 = cuta_TRAINBAND_false(path_final_data, 'a49')

cutas_TESTBAND_true_a6 = cuta_TRAINBAND_true(path_final_data, 'a6')
cutas_TESTBAND_false_a6 = cuta_TRAINBAND_false(path_final_data, 'a6')
cutas_TESTBAND_true_a47 = cuta_TRAINBAND_true(path_final_data, 'a47')
cutas_TESTBAND_false_a47 = cuta_TRAINBAND_false(path_final_data, 'a47')
cutas_TESTBAND_true_a49 = cuta_TRAINBAND_true(path_final_data, 'a49')
cutas_TESTBAND_false_a49 = cuta_TRAINBAND_false(path_final_data, 'a49')

print('load data')
ka6_id_ = [concat_dfs_sep_ids(x) for x in pahts_data[0:5]]
ka47_id_ = [concat_dfs_sep_ids(x) for x in pahts_data[5:10]]
ka49_id_ = [concat_dfs_sep_ids(x) for x in pahts_data[10:]]
print('load data')
tka6_id_ = [concat_dfs_sep_ids(x) for x in tpahts_data[0:5]]
tka47_id_ = [concat_dfs_sep_ids(x) for x in tpahts_data[5:10]]
tka49_id_ = [concat_dfs_sep_ids(x) for x in tpahts_data[10:]]

# TODO Hier daten zwischenspeichern?


print('sep')
TRAINBAND_ka6_id =  seperate_fbands(ka6_id_)
TRAINBAND_ka47_id = seperate_fbands(ka47_id_)
TRAINBAND_ka49_id = seperate_fbands(ka49_id_)
print('sep')

TESTBAND_ka6_id =  seperate_fbands(tka6_id_)
TESTBAND_ka47_id = seperate_fbands(tka47_id_)
TESTBAND_ka49_id = seperate_fbands(tka49_id_)


idx_range_with_seperate_fbands = list(range(65, 89))

ids_data_only = rel_ids_no_list_no_vibs
ids_vibs_only = rel_ids_vib_only_no_list + idx_range_with_seperate_fbands
ids_vibs_data_no_sig = rel_ids_no_list + idx_range_with_seperate_fbands
ids_all_with_sig = 'yet to come'
print('a')
""""""
def pipeline(new_ids, col_size):
    active_cut_data_a6_pre = [sep_cuts_all_sensors(cutas_TRAINBAND_true_a6[i], cutas_TRAINBAND_false_a6[i], j, new_ids, 0, 0) for i, j in enumerate(TRAINBAND_ka6_id)]
    print('ta')
    active_cut_data_a47_pre = [sep_cuts_all_sensors(cutas_TRAINBAND_true_a47[i], cutas_TRAINBAND_false_a47[i], j, new_ids, 0, 0) for i, j in enumerate(TRAINBAND_ka47_id)]
    print('ta')
    active_cut_data_a49_pre = [sep_cuts_all_sensors(cutas_TRAINBAND_true_a49[i], cutas_TRAINBAND_false_a49[i], j, new_ids, 0, 0) for i, j in enumerate(TRAINBAND_ka49_id)]
    print('ta')

    tactive_cut_data_a6_pre = [sep_cuts_all_sensors(cutas_TESTBAND_true_a6[i], cutas_TESTBAND_false_a6[i], j, new_ids, 0, 0) for i, j in enumerate(TESTBAND_ka6_id)]
    tactive_cut_data_a47_pre = [sep_cuts_all_sensors(cutas_TESTBAND_true_a47[i], cutas_TESTBAND_false_a47[i], j, new_ids, 0, 0) for i, j in enumerate(TESTBAND_ka47_id)]
    tactive_cut_data_a49_pre = [sep_cuts_all_sensors(cutas_TESTBAND_true_a49[i], cutas_TESTBAND_false_a49[i], j, new_ids, 0, 0) for i, j in enumerate(TESTBAND_ka49_id)]
    #active_cut_data1a6_newer =  sep_cuts_all_sensors(cutactive_true1a6, cutactive_false1a6, k1a6_id, rel_ids_no_list, 0, 0)
    #active_cut_data2a6_newer =  sep_cuts_all_sensors(cutactive_true2a6, cutactive_false2a6, k2a6_id, rel_ids_no_list, 0, 0)
    #active_cut_data3a6_newer =  sep_cuts_all_sensors(cutactive_true3a6, cutactive_false3a6, k3a6_id, rel_ids_no_list, 0, 0)
    #active_cut_data4a6_newer =  sep_cuts_all_sensors(cutactive_true4a6, cutactive_false4a6, k4a6_id, rel_ids_no_list, 0, 0)
    #active_cut_data5a6_newer =  sep_cuts_all_sensors(cutactive_true5a6, cutactive_false5a6, k5a6_id, rel_ids_no_list, 0, 0)

    #plot_all_cuts_overlapping(active_cut_data_a6_pre[0], 1, '1a6 newer slopecount')
    #plot_all_cuts_overlapping(active_cut_data_a6_pre[1], 1, '2a6 newer slopecount')
    #plot_all_cuts_overlapping(active_cut_data_a6_pre[2], 1, '3a6 newer slopecount')
    #plot_all_cuts_overlapping(active_cut_data_a6_pre[3], 1, '4a6 newer slopecount')
    #plot_all_cuts_overlapping(active_cut_data_a6_pre[4], 1, '5a6 newer slopecount')

    # TODO Hier daten zwischenspeichern?


    # TODO cutas mit löschen sonst stimmen hinterher die dimensionen nicht merh
    # active_cut_data_a6 = clean_train_quick_and_dirty(active_cut_data_a6_pre, 0.5, 'a6')
    # active_cut_data_a47 = clean_train_quick_and_dirty(active_cut_data_a47_pre, 0.5, 'a47')
    # active_cut_data_a49 = clean_train_quick_and_dirty(active_cut_data_a49_pre, 0.5, 'a49')
    #  TODO dureations berechne ich erst nachdem ich bereinigt habe - ich brauche die bereinidungsindizes, dennn aud den cutas bereinige ich nicht!





    all_3_domains = [active_cut_data_a6_pre, active_cut_data_a47_pre, active_cut_data_a49_pre]
    print('ma')

    arr_TRAINBAND_49, ends_TRAINBAND_49 = make_array(active_cut_data_a49_pre, cutas_TRAINBAND_true_a49, cutas_TRAINBAND_false_a49, col_size)
    arr_TRAINBAND_47, ends_TRAINBAND_47 = make_array(active_cut_data_a47_pre, cutas_TRAINBAND_true_a47, cutas_TRAINBAND_false_a47, col_size)
    arr_TRAINBAND__6, ends_TRAINBAND__6 = make_array(active_cut_data_a6_pre, cutas_TRAINBAND_true_a6, cutas_TRAINBAND_false_a6, col_size)
    print('ma')

    arr_TESTBAND_49, ends_TESTBAND_49 = make_array(active_cut_data_a49_pre, cutas_TESTBAND_true_a49, cutas_TESTBAND_false_a49, col_size)
    arr_TESTBAND_47, ends_TESTBAND_47 = make_array(active_cut_data_a47_pre, cutas_TESTBAND_true_a47, cutas_TESTBAND_false_a47, col_size)
    arr_TESTBAND__6, ends_TESTBAND__6 = make_array(active_cut_data_a6_pre, cutas_TRAINBAND_true_a6, cutas_TRAINBAND_false_a6, col_size)

    # TODO Hier daten zwischenspeichern?


    # -------|
    # SPLIT--|
    # -------|
    test_split_size = 0.33
    X_train_TRAINBAND_49, X_test_TRAINBAND_49, y_train_TRAINBAND_49, y_test_TRAINBAND_49 = train_test_split(arr_TRAINBAND_49[:, 1:], arr_TRAINBAND_49[:, 0], test_size=test_split_size)
    X_train_TRAINBAND_47, X_test_TRAINBAND_47, y_train_TRAINBAND_47, y_test_TRAINBAND_47 = train_test_split(arr_TRAINBAND_47[:, 1:], arr_TRAINBAND_47[:, 0], test_size=test_split_size)
    X_train_TRAINBAND__6,  X_test_TRAINBAND__6,  y_train_TRAINBAND__6, y_test_TRAINBAND__6 = train_test_split(arr_TRAINBAND__6[:, 1:], arr_TRAINBAND__6[:, 0], test_size=test_split_size)

    #X_train_TRAINBAND_scaled_49, X_test_TRAINBAND_scaled_49 = standardize_data(X_train_TRAINBAND_49, X_test_TRAINBAND_49)
    #X_train_TRAINBAND_scaled_47, X_test_TRAINBAND_scaled_47 = standardize_data(X_train_TRAINBAND_47, X_test_TRAINBAND_47)
    #X_train_TRAINBAND_scaled__6, X_test_TRAINBAND_scaled__6 = standardize_data(X_train_TRAINBAND__6, X_test_TRAINBAND__6)
    X_test_TESTBAND__6 = arr_TESTBAND__6[:, 1:]
    X_test_TESTBAND_47 = arr_TESTBAND_47[:, 1:]
    X_test_TESTBAND_49 = arr_TESTBAND_49[:, 1:]
    y_test_TESTBAND__6 = arr_TESTBAND__6[:, 0]
    y_test_TESTBAND_47 = arr_TESTBAND_47[:, 0]
    y_test_TESTBAND_49 = arr_TESTBAND_49[:, 0]

    # brauche ich nicht, da ich nicht dauarf trainiere
    #test_split_size = 0.33
    #X_train_TESTBAND_49, X_test_TESTBAND_49, y_train_TESTBAND_49, y_test_TESTBAND_49 = train_test_split(arr_TESTBAND_49[:, 1:], arr_TESTBAND_49[:, 0], test_size=test_split_size)
    #X_train_TESTBAND_47, X_test_TESTBAND_47, y_train_TESTBAND_47, y_test_TESTBAND_47 = train_test_split(arr_TESTBAND_47[:, 1:], arr_TESTBAND_47[:, 0], test_size=test_split_size)
    #X_train_TESTBAND__6,  X_test_TESTBAND__6,  y_train_TESTBAND__6, y_test_TESTBAND__6 = train_test_split(arr_TESTBAND__6[:, 1:], arr_TESTBAND__6[:, 0], test_size=test_split_size)

    #standardizing = """
    # train scaler on TRAININGBAND and transform TESTBAND
    _, X_test_TESTBAND_49 = standardize_data(X_train_TRAINBAND_49, X_test_TESTBAND_49)
    _, X_test_TESTBAND_47 = standardize_data(X_train_TRAINBAND_47, X_test_TESTBAND_47)
    _, X_test_TESTBAND__6 = standardize_data(X_train_TRAINBAND__6, X_test_TESTBAND__6)

    X_train_TRAINBAND_49, X_test_TRAINBAND_49 = standardize_data(X_train_TRAINBAND_49, X_test_TRAINBAND_49)
    X_train_TRAINBAND_47, X_test_TRAINBAND_47 = standardize_data(X_train_TRAINBAND_47, X_test_TRAINBAND_47)
    X_train_TRAINBAND__6, X_test_TRAINBAND__6 = standardize_data(X_train_TRAINBAND__6, X_test_TRAINBAND__6)
    #"""
    print('ca')

    # ------------------------
    # ------PERFORMANCE-------
    # ------------------------
    # ---
    # a49
    # ---

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
    TESTBANDreport__6    = clf__6.predicting(X_test_TESTBAND__6).class_report(y_test_TESTBAND__6)
    TESTBANDscores__6    = clf__6.score_table(y_test_TESTBAND__6)
    TESTBANDreport_47    = clf_47.predicting(X_test_TESTBAND_47).class_report(y_test_TESTBAND_47)
    TESTBANDscores_47    = clf_47.score_table(y_test_TESTBAND_47)
    TESTBANDreport_49    = clf_49.predicting(X_test_TESTBAND_49).class_report(y_test_TESTBAND_49)
    TESTBANDscores_49    = clf_49.score_table(y_test_TESTBAND_49)
    TESTBANDreport__6_47 = clf__6.predicting(X_test_TESTBAND_47).class_report(y_test_TESTBAND_47)
    TESTBANDscores__6_47 = clf__6.score_table(y_test_TESTBAND_47)
    TESTBANDreport_47__6 = clf_47.predicting(X_test_TESTBAND__6).class_report(y_test_TESTBAND__6)
    TESTBANDscores_47__6 = clf_47.score_table(y_test_TESTBAND__6)
    TESTBANDreport_49__6 = clf_49.predicting(X_test_TESTBAND__6).class_report(y_test_TESTBAND__6)
    TESTBANDscores_49__6 = clf_49.score_table(y_test_TESTBAND__6)
    TESTBANDreport__6_49 = clf__6.predicting(X_test_TESTBAND_49).class_report(y_test_TESTBAND_49)
    TESTBANDscores__6_49 = clf__6.score_table(y_test_TESTBAND_49)
    TESTBANDreport_47_49 = clf_47.predicting(X_test_TESTBAND_49).class_report(y_test_TESTBAND_49)
    TESTBANDscores_47_49 = clf_47.score_table(y_test_TESTBAND_49)
    TESTBANDreport_49_47 = clf_49.predicting(X_test_TESTBAND_47).class_report(y_test_TESTBAND_47)
    TESTBANDscores_49_47 = clf_49.score_table(y_test_TESTBAND_47)

    return {'report__6': report__6, 'scores__6': scores__6,'report_47': report_47,'scores_47': scores_47,
            'report_49': report_49,'scores_49': scores_49,'report__6_47': report__6_47,'scores__6_47': scores__6_47,
            'report_47__6': report_47__6,'scores_47__6': scores_47__6,'report_49__6': report_49__6,
            'scores_49__6': scores_49__6,'report__6_49': report__6_49,'scores__6_49': scores__6_49,
            'report_47_49': report_47_49,'scores_47_49': scores_47_49,'report_49_47': report_49_47,
            'scores_49_47': scores_49_47,'TESTBANDreport__6': TESTBANDreport__6,'TESTBANDscores__6': TESTBANDscores__6,
            'TESTBANDreport_47': TESTBANDreport_47,'TESTBANDscores_47': TESTBANDscores_47,
            'TESTBANDreport_49': TESTBANDreport_49,'TESTBANDscores_49': TESTBANDscores_49,
            'TESTBANDreport__6_47': TESTBANDreport__6_47,'TESTBANDscores__6_47': TESTBANDscores__6_47,
            'TESTBANDreport_47__6': TESTBANDreport_47__6,'TESTBANDscores_47__6': TESTBANDscores_47__6,
            'TESTBANDreport_49__6': TESTBANDreport_49__6,'TESTBANDscores_49__6': TESTBANDscores_49__6,
            'TESTBANDreport__6_49': TESTBANDreport__6_49,'TESTBANDscores__6_49': TESTBANDscores__6_49,
            'TESTBANDreport_47_49': TESTBANDreport_47_49,'TESTBANDscores_47_49': TESTBANDscores_47_49,
            'TESTBANDreport_49_47': TESTBANDreport_49_47,'TESTBANDscores_49_47': TESTBANDscores_49_47}

if __name__ == "__main__":
    col_size = len(['duration'] + ids_data_only + ['class']) #+24 #7 für die restlichen einträge in fbands

    dict_ids_data_only = pipeline(ids_data_only, col_size)



"""
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate

cl = [DecisionTreeClassifier(random_state=42),
                        LogisticRegression(random_state=42, solver='liblinear'),
                        BaggingClassifier(random_state=42),
                        RandomForestClassifier(random_state=42),
                        LinearDiscriminantAnalysis(),
                        QuadraticDiscriminantAnalysis(),
                        SVC(random_state=42),
                        KNeighborsClassifier(),
                        GaussianNB()]
sc =['accuracy', 'precision_macro', 'f1_macro', 'recall_macro']
cv = KFold(n_splits=5, random_state=1, shuffle=True)
res = []
for c in cl:
    res.append(cross_validate(c, X_train_TRAINBAND__6, y_train_TRAINBAND__6, scoring=sc, cv=cv, n_jobs=-1, return_estimator=True))
"""

scoring="f1"


# macro treats classes equally

"""
results_vanilla_49, reports_vanilla_49 = classifiers(X_train_TRAINBAND_49, y_train_TRAINBAND_49, X_test_TRAINBAND_49, y_test_TRAINBAND_49)
scores_vanilla_49 = metric_tables(y_test_TRAINBAND_49, results_vanilla_49)
results_vanilla_scaled_49, reports_vanilla_scaled_49 = classifiers(X_train_TRAINBAND_scaled_49, y_train_TRAINBAND_49, X_test_TRAINBAND_scaled_49, y_test_TRAINBAND_49)
scores_vanilla_scaled_49 = metric_tables(y_test_TRAINBAND_49, results_vanilla_scaled_49)

# ----
# a47
# ----
results_vanilla_47, reports_vanilla_47 = classifiers(X_train_TRAINBAND_47, y_train_TRAINBAND_47, X_test_TRAINBAND_47, y_test_TRAINBAND_47)
scores_vanilla_47 = metric_tables(y_test_TRAINBAND_47, results_vanilla_47)
results_vanilla_scaled_47, reports_vanilla_scaled_47 = classifiers(X_train_TRAINBAND_scaled_47, y_train_TRAINBAND_47, X_test_TRAINBAND_scaled_47, y_test_TRAINBAND_47)
scores_vanilla_scaled_47 = metric_tables(y_test_TRAINBAND_47, results_vanilla_scaled_47)

# ----
#  a6
# ----
results_vanilla__6, reports_vanilla__6 = classifiers(X_train_TRAINBAND__6, y_train_TRAINBAND__6, X_test_TRAINBAND__6, y_test_TRAINBAND__6)
scores_vanilla__6 = metric_tables(y_test_TRAINBAND__6, results_vanilla__6)
results_vanilla_scaled__6, reports_vanilla_scaled__6 = classifiers(X_train_TRAINBAND_scaled__6, y_train_TRAINBAND__6, X_test_TRAINBAND_scaled__6, y_test_TRAINBAND__6)
scores_vanilla_scaled__6 = metric_tables(y_test_TRAINBAND__6, results_vanilla_scaled__6)

# ------------------------------
#      CROSS PERFORMANCE - same Sägeband
# ------------------------------

# ----------
# a49 -> a47
# ----------
results_vanilla_49_47, reports_vanilla_49_47 = classifiers(X_train_TRAINBAND_49, y_train_TRAINBAND_49, X_test_TRAINBAND_47, y_test_TRAINBAND_47)
scores_vanilla_49_47 = metric_tables(y_test_TRAINBAND_47, results_vanilla_49_47)
results_vanilla_scaled_49_47, reports_vanilla_scaled_49_47 = classifiers(X_train_TRAINBAND_scaled_49, y_train_TRAINBAND_49, X_test_TRAINBAND_scaled_47, y_test_TRAINBAND_47)
scores_vanilla_scaled_49_47 = metric_tables(y_test_TRAINBAND_47, results_vanilla_scaled_49_47)


# ----------
# a47 -> a49
# ----------
results_vanilla_47_49, reports_vanilla_47_49 = classifiers(X_train_TRAINBAND_47, y_train_TRAINBAND_47, X_test_TRAINBAND_49, y_test_TRAINBAND_49)
scores_vanilla_47_49 = metric_tables(y_test_TRAINBAND_49, results_vanilla_47_49)
results_vanilla_scaled_47_49, reports_vanilla_scaled_47_49 = classifiers(X_train_TRAINBAND_scaled_47, y_train_TRAINBAND_47, X_test_TRAINBAND_scaled_49, y_test_TRAINBAND_49)
scores_vanilla_scaled_47_49 = metric_tables(y_test_TRAINBAND_49, results_vanilla_scaled_47_49)


# ----------
# a49 -> a6
# ----------
results_vanilla_49__6, reports_vanilla_49__6 = classifiers(X_train_TRAINBAND_49, y_train_TRAINBAND_49, X_test_TRAINBAND__6, y_test_TRAINBAND__6)
scores_vanilla_49__6 = metric_tables(y_test_TRAINBAND__6, results_vanilla_49__6)
results_vanilla_scaled_49__6, reports_vanilla_scaled_49__6 = classifiers(X_train_TRAINBAND_scaled_49, y_train_TRAINBAND_49, X_test_TRAINBAND_scaled__6, y_test_TRAINBAND__6)
scores_vanilla_scaled_49__6 = metric_tables(y_test_TRAINBAND__6, results_vanilla_scaled_49__6)


# ----------
# a47 -> a6
# ----------
results_vanilla_47__6, reports_vanilla_47__6 = classifiers(X_train_TRAINBAND_47, y_train_TRAINBAND_47, X_test_TRAINBAND__6, y_test_TRAINBAND__6)
scores_vanilla_47__6 = metric_tables(y_test_TRAINBAND__6, results_vanilla_47__6)
results_vanilla_scaled_47__6, reports_vanilla_scaled_47__6 = classifiers(X_train_TRAINBAND_scaled_47, y_train_TRAINBAND_47, X_test_TRAINBAND_scaled__6, y_test_TRAINBAND__6)
scores_vanilla_scaled_47__6 = metric_tables(y_test_TRAINBAND__6, results_vanilla_scaled_47__6)



# ----------
# a6 -> a47
# ----------
results_vanilla__6_47, reports_vanilla__6_47 = classifiers(X_train_TRAINBAND__6, y_train_TRAINBAND__6, X_test_TRAINBAND_47, y_test_TRAINBAND_47)
scores_vanilla__6_47 = metric_tables(y_test_TRAINBAND_47, results_vanilla__6_47)
results_vanilla_scaled__6_47, reports_vanilla_scaled__6_47 = classifiers(X_train_TRAINBAND_scaled__6, y_train_TRAINBAND__6, X_test_TRAINBAND_scaled_47, y_test_TRAINBAND_47)
scores_vanilla_scaled__6_47 = metric_tables(y_test_TRAINBAND_47, results_vanilla_scaled__6_47)


# ----------
# a6 -> a49
# ----------
results_vanilla__6_49, reports_vanilla__6_49 = classifiers(X_train_TRAINBAND__6, y_train_TRAINBAND__6, X_test_TRAINBAND_49, y_test_TRAINBAND_49)
scores_vanilla__6_49 = metric_tables(y_test_TRAINBAND_49, results_vanilla__6_49)
results_vanilla_scaled__6_49, reports_vanilla_scaled__6_49 = classifiers(X_train_TRAINBAND_scaled__6, y_train_TRAINBAND__6, X_test_TRAINBAND_scaled_49, y_test_TRAINBAND_49)
scores_vanilla_scaled__6_49 = metric_tables(y_test_TRAINBAND_49, results_vanilla_scaled__6_49)
"""

# ------------------------------
#      CROSS PERFORMANCE - DIFFERENT Sägeband
# ------------------------------
#for i in rel_ids_no_list:
#    print(i, ids[i])




# scaled 49 ist schlechter als ohne scaling - aber nur svc

# TODO cross -check that X and y have same number of rows


# TODO plot max min für jede auswertung mit so balken
# TODO warum metrics gewählt? mini macro erklären



#ends = [ends_TRAINBAND__6, ends_TRAINBAND_47, ends_TRAINBAND_49]
#colors = ['r', 'g', 'b', 'y', 'k']
#col = 1
#fig, axs = plt.subplots(3,1, figsize=(19,10), sharey=True)
#plt.suptitle('cut duration')
#for i, j in enumerate(ends):
#    if i == 0:
#        row = 0
#    else:
#        row = ends[i-1]
#    axs[0].scatter(range(row + ends[i]), arr_TRAINBAND__6[row:j, col], label='a6', color=colors[i])
#    axs[0].legend()
#    axs[1].scatter(range(row + ends[i]), arr_TRAINBAND_47[row:j, col], label='a47', color=colors[i])
##    axs[1].legend()
 #   axs[2].scatter(range(row + ends[i]), arr_TRAINBAND_49[row:j, col], label='a49', color=colors[i])
 #   axs[2].legend()
##
#
#
#for i, j in enumerate(ends):
#    # first one should be zero, rest um eins verschoben wie oben
#    if i == 0:
#        row = 0
#    else:
#        row = ends[i-1]
#    first_bigger_array[row:j, 0] = i + 1



"""

clf_index = ['DecisionTreeClassifier', 'BaggingClassifier', 'RandomForestClassifier',
             'GaussianNB', 'LogisticRegression', 'LinearDiscriminantAnalysis',
             'QuadraticDiscriminantAnalysis', 'SVC', 'KNeighborsClassifier']
all_scores = [scores__6, scores_47, scores_49, scores__6_47, scores_47__6, scores_49__6, scores__6_49, scores_47_49, scores_49_47, TESTBANDscores__6, TESTBANDscores_47, TESTBANDscores_49, TESTBANDscores__6_47, TESTBANDscores_47__6, TESTBANDscores_49__6, TESTBANDscores__6_49, TESTBANDscores_47_49, TESTBANDscores_49_47]
colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'gray', 'mediumpurple', 'orange']
colors_clfs = dict(zip(clf_index, colours))
labels = ['scores__6', 'scores_47', 'scores_49', 'scores__6_47', 'scores_47__6', 'scores_49__6', 'scores__6_49', 'scores_47_49', 'scores_49_47', 'TESTBANDscores__6', 'TESTBANDscores_47', 'TESTBANDscores_49', 'TESTBANDscores__6_47', 'TESTBANDscores_47__6', 'TESTBANDscores_49__6', 'TESTBANDscores__6_49', 'TESTBANDscores_47_49', 'TESTBANDscores_49_47']

ticks = list(range(len(labels)))
sc_col = 'F1 macro'
table_rows = list(range(18))
plt.figure()
for i, j in enumerate(all_scores):
    plt.plot([j.loc[:, sc_col].min(), j.loc[:, sc_col].max()], [i, i], linewidth=10, label=labels[i], color='brown')
plt.yticks(ticks, labels)
plt.xlim((0,1.05))
plt.title('Range of F1 Scores across 9 Classifiers')
plt.tight_layout()

plt.figure()
classifier_list = list(all_scores[0].index)
for i, j in enumerate(all_scores):
    for k, l in enumerate(classifier_list):
        plt.scatter([j.loc[l, sc_col]], [i], c=colors_clfs[l], marker='s', s=150)
        #if i == len(all_scores):
        #    plt.scatter([j.iloc[k, sc_col]], [i], c=colours[k], label=l)
        #plt.legend()
plt.yticks(ticks, labels)
plt.title('F1 Scores For Each Classifier')

plt.xlim((0,1.05))
plt.tight_layout()

class_names = ['class 1', 'class 2', 'class 3', 'class 4', 'class 5']
X_test, =
y_test =
classifier =
titles_options = [
    ("Confusion matrix, without normalization", None),
    ("Normalized confusion matrix", "true"),
]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        clf__6.models[6],
        X_test,
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()





# Todo lowest f1 for each classifier
# todo hyperparameteroptimization for each
# todo more features
# todo less features

   # durations
dur_list_false = [cutas_TRAINBAND_false_a49 + cutas_TRAINBAND_false_a6 + cutas_TRAINBAND_false_a47]
dur_list_true = [cutas_TRAINBAND_true_a49 + cutas_TRAINBAND_true_a6 + cutas_TRAINBAND_true_a47 ]
dur_list_false = dur_list_false[0]
dur_list_true = dur_list_true[0]
dur_list_false = pd.concat(dur_list_false)
dur_list_true = pd.concat(dur_list_true)
dur_list_false = dur_list_false.sort_values(by=['shifted'])
dur_list_true = dur_list_true.sort_values(by=['shifted'])

begin_a6 = dur_list_true.values
end_a6 = dur_list_false.values

duration = []
assert len(begin_a6) == len(end_a6)
for i in range(len(begin_a6)):
    cut_time = (end_a6[i] - begin_a6[i]) / np.timedelta64(1, 's')
    duration.append(cut_time)
duration = np.concatenate(duration)
plt.figure()
plt.plot(dur_list_true['shifted'], duration)
duration = np.array(duration)
duratio = duration[np.argwhere(duration < 245)]
plt.plot(duratio)


#plot_sensors_and_cutactive(ka6_id_[2][13], cutas_TRAINBAND_true_a6[2], cutas_TRAINBAND_false_a6[2], 'shifted')


plt.figure()
numbr = 1
plt.plot(ka49_id_[numbr][13]['source'], ka49_id_[numbr][13]['val'])
column = 'shifted'
plt.scatter(cutas_TRAINBAND_true_a49[numbr][column], np.full(len(cutas_TRAINBAND_true_a49[numbr][column]), 16), c='g', s=25)
plt.scatter(cutas_TRAINBAND_false_a49[numbr][column], np.full(len(cutas_TRAINBAND_false_a49[numbr][column]), 16), c='r', s=25)



# TODO cuta true 49 class 4 kannst du direkt übernehmen




means_avg_clfs = []
avg_f1_clfs = []
for i in clf_index:
    means_of_one_clf = []
    f1_of_one_clf = []
    print('start\n')
    for j in all_scores:
        means_of_one_clf.append(j.loc[i].mean())
        f1_of_one_clf.append(j.loc[i, 'F1 macro'])
        print(j.loc[i, 'F1 macro'])
    means_avg_clfs.append(sum(means_of_one_clf) / len(all_scores))
    avg_f1_clfs.append(sum(f1_of_one_clf) / len(all_scores))




df_means_avg_clfs = pd.DataFrame(list(zip(means_avg_clfs, avg_f1_clfs)), index=clf_index, columns=['mean over all scores', 'mean F1 macro over all domains'])
df_means_avg_clfs = df_means_avg_clfs.sort_values(by='mean F1 macro over all domains', ascending=False)

plt.figure()
df_means_avg_clfs.loc[:, 'mean F1 macro over all domains'].plot( kind='bar', rot=35, color=[colors_clfs[x] for x in df_means_avg_clfs.index ], ylim=[0, 1], title='mean F1 macro over all domains')
plt.tight_layout()

normal_idx = [0,1,2, 10, 11, 12]
cross_idx = [3,4,5,6,7,8,9,13,14,15,16,17]
all_idx = list(range(len(all_scores)))
def df_mean_scores(normal_idx):
    normal_scores = [all_scores[x] for x in normal_idx]
    means_normal_clfs = []
    avg_f1_normal_clfs = []
    for i in clf_index:
        means_of_one_clf = []
        f1_of_one_clf = []
        print('start\n')
        for j in normal_scores:
            means_of_one_clf.append(j.loc[i].mean())
            f1_of_one_clf.append(j.loc[i, 'F1 macro'])
            print(j.loc[i, 'F1 macro'])
        means_normal_clfs.append(sum(means_of_one_clf) / len(normal_scores))
        avg_f1_normal_clfs.append(sum(f1_of_one_clf) / len(normal_scores))
    return means_normal_clfs, avg_f1_normal_clfs
means_normal_clfs, avg_f1_normal_clfs = df_mean_scores(normal_idx)
means_cross_clfs, avg_f1_cross_clfs = df_mean_scores(cross_idx)
means_all_clfs, avg_f1_all_clfs = df_mean_scores(all_idx)

df_means_normal_clfs = pd.DataFrame(list(zip(means_normal_clfs, avg_f1_normal_clfs)), index=clf_index, columns=['mean over all scores', 'mean F1 macro over all domains'])
df_means_normal_clfs = df_means_normal_clfs.sort_values(by='mean F1 macro over all domains', ascending=False)
df_means_cross_clfs = pd.DataFrame(list(zip(means_cross_clfs, avg_f1_cross_clfs)), index=clf_index, columns=['mean over all scores', 'mean F1 macro over all domains'])
df_means_cross_clfs = df_means_cross_clfs.sort_values(by='mean F1 macro over all domains', ascending=False)
df_means_all_clfs = pd.DataFrame(list(zip(means_all_clfs, avg_f1_all_clfs)), index=clf_index, columns=['mean over all scores', 'mean F1 macro over all domains'])
df_means_all_clfs = df_means_all_clfs.sort_values(by='mean F1 macro over all domains', ascending=False)


plt.figure()
df_means_normal_clfs.loc[:, 'mean F1 macro over all domains'].plot( kind='bar', rot=35, color=[colors_clfs[x] for x in df_means_avg_clfs.index ], ylim=[0, 1], title='mean F1 macro cross domains')
plt.tight_layout()


fig, axs = plt.subplots(3, 1, sharey=True, sharex=True)
df_means_normal_clfs.loc[:, 'mean F1 macro over all domains'].plot(ax=axs[0], kind='bar', rot=35,
                                                         color=[colors_clfs[x] for x in df_means_normal_clfs.index],
                                                         ylim=[0, 1], title='mean F1 same dim domains', grid=True)
df_means_cross_clfs.loc[:, 'mean F1 macro over all domains'].plot(ax=axs[1], kind='bar', rot=35,
                                                         color=[colors_clfs[x] for x in df_means_cross_clfs.index],
                                                         ylim=[0, 1], title='mean F1 cross dim domains', grid=True)
df_means_all_clfs.loc[:, 'mean F1 macro over all domains'].plot(ax=axs[2], kind='bar', rot=35,
                                                           color=[colors_clfs[x] for x in df_means_all_clfs.index],
                                                           ylim=[0, 1], title='mean F1 all domains', grid=True)
plt.tight_layout()
"""


