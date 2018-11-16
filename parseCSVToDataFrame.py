import csv
import pandas as pd

df_columns = ['Zipcode', 'Supply_KW', 'Demand_Month_1_KWh', 'Demand_Month_2_KWh', 'Demand_Month_3_KWh', 'Demand_Month_4_KWh', 'Demand_Month_5_KWh', 'Demand_Month_6_KWh', 'Demand_Month_7_KWh', 'Demand_Month_8_KWh', 'Demand_Month_9_KWh', 'Demand_Month_10_KWh', 'Demand_Month_11_KWh', 'Demand_Month_12_KWh']

# Read in 2017 supply demand data csv and output dataframe including zipcode location data.
# Uses format 'Zipcode', 'Latitude', 'Longitude', 'Supply (KW)', 'Demand per month (KWh)'
df = pd.read_csv('/Users/jkhunt/github/batteries-california/output_without_locations_2017.csv')
zipcode_df = pd.read_csv('/Users/jkhunt/github/batteries-california/US_Zipcodes.csv', skiprows = range(1, 30022))
df.columns = df_columns

zipcode_list = []
for index, row in df.iterrows():
    zip_df = zipcode_df.loc[zipcode_df['ZIP'] == row[0]][['LAT', 'LNG']].values.flatten()
    zipcode_list.append(zip_df)

lat_long_df = pd.DataFrame(zipcode_list, columns = ['Latitude', 'Longitude'])
df = df.join(lat_long_df)
df = df[[df_columns[0]] + ['Latitude', 'Longitude'] + df_columns[1:]]
df = df[df['Demand_Month_1_KWh'] != 0]
df = df.set_index('Zipcode')
# print df
# print df.columns.tolist()
# df.to_csv('/Users/jkhunt/github/batteries-california/output_with_locations_2017.csv', index = False)
