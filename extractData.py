import csv
import collections
import numpy as np
import pandas as pd

data_dict = {}
with open('NEM.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if len(row) < 15: continue
        if row[3] == 'PGE' and (row[14] == 'Industrial' or row[14] == 'Commercial'):
            if row[5] not in d1.keys():
                data_dict[row[5]] = np.zeros(13)
            data_dict[row[5]][0] += float(row[9])

with open('PGE_2017_Q1.csv', 'r') as csv1_file:
    reader1 = csv.reader(csv1_file, delimiter=',')
    reader1.next()
    for row in reader1:
        if row[0] not in d1.keys():
            data_dict[row[0]] = np.zeros(13)
        else:
            data_dict[row[0]][int(row[1])] += float(row[6].replace(',', ''))

with open('PGE_2017_Q2.csv', 'r') as csv2_file:
    reader2 = csv.reader(csv2_file, delimiter=',')
    reader2.next()
    for row in reader2:
        if row[0] not in d1.keys():
            data_dict[row[0]] = np.zeros(13)
        else:
            data_dict[row[0]][int(row[1])] += float(row[6].replace(',', ''))

with open('PGE_2017_Q3.csv', 'r') as csv3_file:
    reader3 = csv.reader(csv3_file, delimiter=',')
    reader3.next()
    for row in reader3:
        if row[0] not in d1.keys():
            data_dict[row[0]] = np.zeros(13)
        else:
            data_dict[row[0]][int(row[1])] += float(row[6].replace(',', ''))

with open('PGE_2017_Q4.csv', 'r') as csv4_file:
    reader4 = csv.reader(csv4_file, delimiter=',')
    reader4.next()
    for row in reader4:
        if int(row[1]) == 9: continue
        if row[0] not in d1.keys():
            data_dict[row[0]] = np.zeros(13)
        else:
            data_dict[row[0]][int(row[1])] += float(row[6].replace(',', ''))

df = pd.DataFrame.from_dict(data_dict)
dfT = df.transpose()
dfT.columns = ['Supply', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dfT.to_csv('output.csv')
