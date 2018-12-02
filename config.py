import parseCSVToDataFrame
import zipcode_map

# Modify any global variables here:
battery_size_MW = 20 # MW size per battery
battery_month_KWH = battery_size_MW * 1000 * 5 * 30 # size * 1000 * 5 hours * 30 days = 750,000 (size = 5 MW)
neighbors_percentage_fulfill = 0.2 # percentage of zipcode demand fulfilled for neighbors set precomputation
percentage_fulfill = 1 # general percentage aim for model
n_batteries = 40
n_iters = 1
n_k_iters = 10
k_efficiency_loss = 0.0001 # assumption % per mile (true amount is probably even smaller)

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

month_index = MONTH_1_KWH

# IMPORTANT: Do not modify lines below in this section, further global variables are listed below this part!
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
data_df = parseCSVToDataFrame.df
test_data_df = data_df.iloc[300:320]
data = data_df.T.to_dict(orient = 'list')
test_data = test_data_df.T.to_dict(orient = 'list')
test_supply_neighbors = zipcode_map.getReachableNeighbors(test_data, battery_month_KWH, neighbors_percentage_fulfill, month_index)

# Modify as needed below:
data_set = data # represents current data set model uses
neighbors_set = test_supply_neighbors # represents current neighbors set of data model uses
