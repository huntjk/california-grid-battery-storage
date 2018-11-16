import parseCSVToDataFrame

# Insert any global variables here:

# DataFrame containing all data so far.
# Uses format 'Zipcode', 'Latitude', 'Longitude', 'Supply (KW)', 'Demand per month (KWh)':
# To iterate through values:
#
# for index, row in config.data.iterrows():
#   zipcode = row['Zipcode']
#   latitude, longitude = row['Latitude'], row['Longitude']
#   supply_KW = row['Supply_KW']
#   demand_month_1_KWh, demand_month_2_KWh = row['Demand_Month_1_KWh'], row['Demand_Month_2_KWh']
#
# Can call up to 'Demand_Month_12_KWh'
#
# Indexes
LATITUDE = 0
LONGITUDE = 1
SUPPLY_KW = 2
MONTH_1_KWH = 3
MONTH_2_KWH = 4
MONTH_3_KWH = 5
MONTH_4_KWH = 6
MONTH_5_KWH = 7
MONTH_6_KWH = 8
MONTH_7_KWH = 9
MONTH_8_KWH = 10
MONTH_9_KWH = 11
MONTH_10_KWH = 12
MONTH_11_KWH = 13
MONTH_12_KWH = 14

data_df = parseCSVToDataFrame.df
test_data_df = parseCSVToDataFrame.df.iloc[300:320]
data = data_df.T.to_dict(orient = 'list')
test_data = test_data_df.T.to_dict(orient = 'list')
