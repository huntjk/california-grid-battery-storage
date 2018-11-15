import csv
import pandas as pd
import numpy as np

df = pd.read_csv('output.csv')
zipcode_df = pd.read_csv('/Users/jkhunt/github/batteries-california/US_Zipcodes.csv', skiprows = range(1, 30022))
df.columns = ['Zipcode', 'Supply_KW', 'Demand_Month_1_KWh', 'Demand_Month_2_KWh', 'Demand_Month_3_KWh', 'Demand_Month_4_KWh', 'Demand_Month_5_KWh', 'Demand_Month_6_KWh', 'Demand_Month_7_KWh', 'Demand_Month_8_KWh', 'Demand_Month_9_KWh', 'Demand_Month_10_KWh', 'Demand_Month_11_KWh', 'Demand_Month_12_KWh']

zipcode_list = []
for index, row in df.iterrows():
    zip_df = zipcode_df.loc[zipcode_df['ZIP'] == row[0]][['LAT', 'LNG']].values.flatten()
    zipcode_list.append(zip_df)

lat_long_df = pd.DataFrame(zipcode_list, columns = ['Latitude', 'Longitude'])
df = df.join(lat_long_df)
df.to_csv('/Users/jkhunt/github/batteries-california/output_with_locations.csv', index = False)
