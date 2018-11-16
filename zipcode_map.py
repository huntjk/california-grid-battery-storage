import config as cfg
import csv
import collections 
import operator
from geopy.distance import geodesic

def find_suppliers(): 
    suppliers = collections.defaultdict()
    #5 MW * 1000 * 5 hr * 30 days 
    battery_monthly =  750000

 
    for zipcode in cfg.data.keys():
        distances = collections.defaultdict()
        for neighbor in cfg.data.keys():
            if neighbor != zipcode:
                #lat = data[0], long = data[1], supply in kW = data[2]
                zipcode = (cfg.data[zipcode][0], cfg.data[zipcode][1])
                neighbor = (cfg.data[neighbor][0], cfg.data[neighbor][1])
                distance = geodesic(zipcode, neighbor).miles
                distances[neighbor] = distance
        sum = (cfg.data[zipcode][2] * 5 * 30)
        suppliers[zipcode] = sum
        while(sum < battery_monthly):
            curr_max = max(distances.iteritems(), key=operator.itemgetter(1))[0]
            sum += (cfg.data[curr_max][2] * 5 * 30)
            suppliers[curr_max] = (cfg.data[curr_max][2] * 5 * 30)
            del distances[curr_max]

    return suppliers

def main():
    return find_suppliers()

