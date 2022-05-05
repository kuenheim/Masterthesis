from helpers.functions import cuta_TRAINBAND_true, cuta_TESTBAND_true, cuta_TRAINBAND_false, cuta_TESTBAND_false
from seperate_cuts import sep_cuts_all_sensors, concat_dfs_sep_ids, qnd_outlier_indices, qnd_bandpass_per_class, plot_all_cuts_overlapping, plot_sensors_and_cutactive
from helpers.lists import ids, val_id_type_dict, paths, short_labels, rel_ids, rel_ids_no_list, pahts_sigs , tpahts_sigs, pahts_data , tpahts_data
import pandas as pd
import os

path_final_data = 'E:\\ausgelagert thesis daten\\final_data\\sigraw\\old'


sig1a6 = pd.read_csv(os.path.join(path_final_data,  'sig1a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig2a6 = pd.read_csv(os.path.join(path_final_data,  'sig2a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig3a6 = pd.read_csv(os.path.join(path_final_data,  'sig3a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig4a6 = pd.read_csv(os.path.join(path_final_data,  'sig4a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig5a6 = pd.read_csv(os.path.join(path_final_data,  'sig5a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig1a47 = pd.read_csv(os.path.join(path_final_data, 'sig1a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig2a47 = pd.read_csv(os.path.join(path_final_data, 'sig2a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig3a47 = pd.read_csv(os.path.join(path_final_data, 'sig3a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig4a47 = pd.read_csv(os.path.join(path_final_data, 'sig4a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig5a47 = pd.read_csv(os.path.join(path_final_data, 'sig5a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig1a49 = pd.read_csv(os.path.join(path_final_data, 'sig1a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig2a49 = pd.read_csv(os.path.join(path_final_data, 'sig2a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig3a49 = pd.read_csv(os.path.join(path_final_data, 'sig3a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig4a49 = pd.read_csv(os.path.join(path_final_data, 'sig4a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
sig5a49 = pd.read_csv(os.path.join(path_final_data, 'sig5a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig1a6 = pd.read_csv(os.path.join(path_final_data, 'tsig1a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig2a6 = pd.read_csv(os.path.join(path_final_data, 'tsig2a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig3a6 = pd.read_csv(os.path.join(path_final_data, 'tsig3a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig4a6 = pd.read_csv(os.path.join(path_final_data, 'tsig4a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig5a6 = pd.read_csv(os.path.join(path_final_data, 'tsig5a6.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig1a47 = pd.read_csv(os.path.join(path_final_data, 'tsig1a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig2a47 = pd.read_csv(os.path.join(path_final_data, 'tsig2a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig3a47 = pd.read_csv(os.path.join(path_final_data, 'tsig3a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig4a47 = pd.read_csv(os.path.join(path_final_data, 'tsig4a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig5a47 = pd.read_csv(os.path.join(path_final_data, 'tsig5a47.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig1a49 = pd.read_csv(os.path.join(path_final_data, 'tsig1a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig2a49 = pd.read_csv(os.path.join(path_final_data, 'tsig2a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig3a49 = pd.read_csv(os.path.join(path_final_data, 'tsig3a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig4a49 = pd.read_csv(os.path.join(path_final_data, 'tsig4a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])
tsig5a49 = pd.read_csv(os.path.join(path_final_data, 'tsig5a49.csv'), index_col='idx', usecols=['idx', 'ID', 'source'], parse_dates=['source'])


