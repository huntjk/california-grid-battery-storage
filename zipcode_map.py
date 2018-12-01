import csv
import operator
import math
from geopy.distance import geodesic

LATITUDE = 0
LONGITUDE = 1
SUPPLY_KW = 2
#NOTES: needs to be made faster when finding closest zipcodes
# - should interate through zipcodes that are numerically close first i.e 94305 --> 94306 next
# - maybe just write this all to a csv instead of storing it as a dict?
# Need to do the demand zip code dictionary as well

# This function currently uses a test data set of zipcodes, and produces a dictionary that maps zipcode to
# any neighboring zipcodes that can be supplied with electricity if a battery was to be placed in the
# key zipcode location.
def getReachableNeighbors(data, battery_month_KWH, demand_percentage, month_index):
    neighbors = {}
    for zipcode in data.keys():
        if math.isnan(data[zipcode][LATITUDE]) or math.isnan(data[zipcode][LONGITUDE]):
            continue
        neighbor_dists = {}
        for neighbor in data.keys():
            if data[neighbor][SUPPLY_KW] == 0: continue
            if zipcode == neighbor: continue
            if math.isnan(data[neighbor][LATITUDE]) or math.isnan(data[neighbor][LONGITUDE]):
                continue
            distance = geodesic((data[zipcode][LATITUDE], data[zipcode][LONGITUDE]), (data[neighbor][LATITUDE], data[neighbor][LONGITUDE])).miles
            #distance = util.getDistance((data[zipcode][LATITUDE], data[zipcode][LONGITUDE]), (data[neighbor][LATITUDE], data[neighbor][LONGITUDE]))
            neighbor_dists[neighbor] = distance
        kw_sum = data[zipcode][month_index] * demand_percentage # Assume meet 20% of demand per zipcode
        neighbors[zipcode] = [zipcode]
        for n in sorted(neighbor_dists.items()):
            kw_sum += neighbor_dists[n[0]]
            if kw_sum <= battery_month_KWH:
                neighbors[zipcode].append(n[0])
            else:
                break
    return neighbors

if __name__ == "__main__":
    getReachableNeighbors()
