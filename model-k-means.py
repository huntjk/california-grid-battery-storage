import config as cfg
import util
import numpy as np
import pandas as pd
import collections as col
import graphPlot as gp
import copy

data = cfg.data_set

def main():
    for i in range(cfg.n_iters):
        battery_locations, battery_info = randomInitialize()
        # energy_supplied_zipcodes = col.defaultdict(float)
        iterations = 0
        old_battery_locations = col.defaultdict()
        start_battery_locations = copy.deepcopy(battery_locations)
        while not shouldStop(old_battery_locations, battery_locations, iterations):
            old_battery_locations = battery_locations
            labels = getLabels(battery_locations)
            getNewBatteries(labels, battery_locations)
        print start_battery_locations
        print battery_locations
        gp.graph_comparison(start_battery_locations, battery_locations)

def getLabels(battery_locations):
    labels = col.defaultdict(list)
    for zipcode, index in data.items():
        min = [float("inf"), float("inf")]
        zip_coords = util.getCoords(zipcode)
        for index, val in battery_locations.items():
            distance = util.getDistance(zip_coords, val[0])
            if distance < min[0]:
                min[0] = distance
                min[1] = index
        labels[min[1]].append((zipcode, zip_coords))
    return labels

def getNewBatteries(labels, battery_locations):
    for index, arr in labels.items():
        new_lat = float(np.mean(np.array([val[1][0] for val in arr])))
        new_long = float(np.mean(np.array([val[1][1] for val in arr])))
        battery_locations[index][0] = (new_lat, new_long)

def shouldStop(oldBatteries, batteries, iterations):
    if iterations > cfg.n_k_iters: return True
    return oldBatteries == batteries

def randomInitialize():
    battery_locations = col.defaultdict()
    battery_info = col.defaultdict()
    battery_zips = np.random.choice(data.keys(), size = cfg.n_batteries)
    battery_zip_counts = col.defaultdict(int)
    for zipcode in battery_zips:
        battery_zip_counts[zipcode] += 1
    for index, val in enumerate(battery_zip_counts.items()):
        lat_long = util.getCoords(val[0])
        battery_locations[index] = [lat_long, val[1] * cfg.battery_size_MW]
        battery_info[index] = col.defaultdict(float)
    return battery_locations, battery_info

def scoreFunction(energy_supplied_zipcodes):
    score = 0
    total = 0
    for zipcode, val in data.items():
        score += energy_supplied_zipcodes[zipcode]
        total += val[cfg.month_index]
    return score / total

if __name__ == '__main__':
	main()
