import config as cfg
import csv
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
