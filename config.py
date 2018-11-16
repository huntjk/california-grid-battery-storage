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
data = parseCSVToDataFrame.df
