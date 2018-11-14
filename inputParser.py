import csv
import pandas as pd

df = pd.read_csv('output.csv')
#df = df.append(df.agg(['sum', 'mean']))
print df
