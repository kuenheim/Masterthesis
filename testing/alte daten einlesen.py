import pandas as pd
import matplotlib.pyplot as plt


Band1_Mean = pd.read_csv('D:\\Uni\\Masterthesis\\Jonas\\Thesis-20220110T110127Z-001\\Thesis\\Datensaetze zu csv\\Band1_Mean.csv', delimiter =',')
Band1_All = pd.read_csv('D:\\Uni\\Masterthesis\\Jonas\\Thesis-20220110T110127Z-001\\Thesis\\Datensaetze zu csv\\Band1_All.csv', delimiter =',')
Band2_Mean = pd.read_csv('D:\\Uni\\Masterthesis\\Jonas\\Thesis-20220110T110127Z-001\\Thesis\\Datensaetze zu csv\\Band2_Mean.csv', delimiter =',')
Band2_All = pd.read_csv('D:\\Uni\\Masterthesis\\Jonas\\Thesis-20220110T110127Z-001\\Thesis\\Datensaetze zu csv\\Band2_All.csv', delimiter =',',  low_memory=False)

plt.plot(Band2_Mean['SKV'])  # erst 150: 0.02, ab 150: 0.59