import csv
import pandas as pd

df = pd.read_csv('output.csv')
zipcode_location_df = pd.read_csv('US Zip Codes from 2013 Government Data')
df.columns = ['Zipcode', 'Supply_KW', 'Demand_Month_1_KWh', 'Demand_Month_2_KWh', 'Demand_Month_3_KWh', 'Demand_Month_4_KWh', 'Demand_Month_5_KWh', 'Demand_Month_6_KWh', 'Demand_Month_7_KWh', 'Demand_Month_8_KWh', 'Demand_Month_9_KWh', 'Demand_Month_10_KWh', 'Demand_Month_11_KWh', 'Demand_Month_12_KWh']
#df = df.append(df.agg(['sum', 'mean']))
print zipcode_location_df
print df
