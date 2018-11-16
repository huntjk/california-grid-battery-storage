import config as cfg
import csv
<<<<<<< HEAD
import operator
import math
from geopy.distance import geodesic

#NOTES: needs to be made faster when finding closest zipcodes
# - should interate through zipcodes that are numerically close first i.e 94305 --> 94306 next
# - maybe just write this all to a csv instead of storing it as a dict? 
# Need to do the demand zip code dictionary as well
def get_suppliers(): 
    suppliers = {}
    #5 MW * 1000 * 5 hr * 30 days 
    battery_monthly =  750000
    for zipcode in cfg.data.keys():
        if math.isnan(cfg.data[zipcode][cfg.LATITUDE]) or math.isnan(cfg.data[zipcode][cfg.LONGITUDE]):
            continue
        neighbor_dists = {}
        for neighbor in cfg.data.keys():
            if cfg.data[neighbor][cfg.SUPPLY_KW] == 0: continue
            if math.isnan(cfg.data[neighbor][cfg.LATITUDE]) or math.isnan(cfg.data[neighbor][cfg.LONGITUDE]):
                continue
            coords_zip = (cfg.data[zipcode][cfg.LATITUDE], cfg.data[zipcode][cfg.LONGITUDE])
            coords_neighbor = (cfg.data[neighbor][cfg.LATITUDE], cfg.data[neighbor][cfg.LONGITUDE])
            distance = geodesic(coords_zip, coords_neighbor).miles
            neighbor_dists[neighbor] = distance
        kw_sum = cfg.data[zipcode][cfg.SUPPLY_KW] * 5 * 30
        suppliers[zipcode] = []
        for n in sorted(neighbor_dists.items()):  
            kw_sum += neighbor_dists[n[0]]
            if kw_sum <= battery_monthly:
                suppliers[zipcode].append(n[0])
            else:
                break
    print suppliers
    return suppliers

if __name__ == "__main__":
    get_suppliers()
=======
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

>>>>>>> 2c36cf702e5d6692bccae5215a58330b3eedec52
