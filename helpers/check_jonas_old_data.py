import pandas as pd
import os

path = 'D:\\Uni\\Masterthesis doc\\Jonas\\Thesis-20220110T110127Z-001\\Thesis\\Datensaetze zu csv'

band1_all = pd.read_csv(os.path.join(path, 'Band1_All.csv'), delimiter=',')
band1_mean = pd.read_csv(os.path.join(path, 'Band1_Mean.csv'), delimiter=',')
band2_mean = pd.read_csv(os.path.join(path, 'Band2_Mean.csv'), delimiter=',')

