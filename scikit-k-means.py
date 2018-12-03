import config as cfg
import util
import numpy as np
import pandas as pd
import collections as col
import graphPlot as gp
import copy
from sklearn.cluster import KMeans

data = cfg.data_set

def main():
    zip_coords = []
    zip_weights = []
    zip_map = []
    for zipcode, val in data.items():
        zip_coords.append([val[0], val[1]])
        zip_weights.append(val[cfg.month_index])
        zip_map.append(zipcode)
    kmeans = KMeans(n_clusters = cfg.n_batteries, init = 'k-means++', n_init = cfg.n_k_iters)
    kmeans.fit(np.array(zip_coords), sample_weight = np.array(zip_weights))
    distribution = label_distribution(kmeans.labels_)
    sort_distribution(distribution, zip_coords, kmeans.cluster_centers_)

    battery_supplied_zipcodes = [col.defaultdict(float) for i in range(cfg.n_batteries)]
    energy_supplied_zipcodes = np.zeros(len(data.values()))
    battery_energies = [cfg.battery_month_KWH for i in range(cfg.n_batteries)]
    for index, zip_indexes in distribution.items():
        battery_assignments(index, zip_indexes, battery_energies, battery_supplied_zipcodes, zip_weights, energy_supplied_zipcodes, tuple(kmeans.cluster_centers_[index]), zip_coords)

    printInfo((scoreFunction(energy_supplied_zipcodes, zip_weights), battery_supplied_zipcodes, energy_supplied_zipcodes), zip_weights, zip_map)

    # print kmeans.inertia_
    # print_distribution_info(distribution, zip_weights)
    # detect_stacked(kmeans.cluster_centers_)
    gp.graph_scikit(kmeans.cluster_centers_, zip_coords, battery_supplied_zipcodes, energy_supplied_zipcodes)

def battery_assignments(index, zip_indexes, battery_energies, battery_supplied_zipcodes, zip_demands, energy_supplied_zipcodes, battery_coord, zip_coords):
    for zip_index in zip_indexes:
        if battery_energies[index] <= 0: break
        zip_energy_demand = zip_demands[zip_index] * cfg.percentage_fulfill
        current_zip_supply = energy_supplied_zipcodes[zip_index]
        distance = util.getDistance(battery_coord, tuple(zip_coords[zip_index]))
        if battery_energies[index] + current_zip_supply <= zip_energy_demand:
            energy_supplied_zipcodes[zip_index] += util.energyLoss(distance, battery_energies[index])
            battery_supplied_zipcodes[index][zip_index] += battery_energies[index]
            break
        else:
            required_energy_to_max = zip_energy_demand - current_zip_supply
            if required_energy_to_max <= 0: continue
            energy_supplied_zipcodes[zip_index] = zip_energy_demand
            battery_energy_supply = util.inverseEnergyLoss(distance, required_energy_to_max)
            battery_supplied_zipcodes[index][zip_index] = battery_energy_supply
            battery_energies[index] -= battery_energy_supply

def scoreFunction(energy_supplied_zipcodes, zip_demands):
    score = 0
    total = 0
    for index, val in enumerate(energy_supplied_zipcodes):
        score += val
        total += zip_demands[index]
    return score / total

def sort_distribution(distribution, coords, centers):
    for index, arr in distribution.items():
        distances = [(i, util.getDistance(coords[i], centers[index])) for i in arr]
        sorted_distances = sorted(distances, key = lambda tup: tup[1])
        distribution[index] = [x for x, y in sorted_distances]
    return distribution

def print_distribution_info(distribution, weights):
    result = []
    for index, arr in distribution.items():
        demands = [weights[i] for i in arr]
        result.append(sum(demands))
        # print 'Cluster Mean {}: {}'.format(index, mean)
    print 'Min: {}, Max: {}, STD: {}, Average: {}'.format(np.min(result), np.max(result), np.std(result), np.mean(result))

def label_distribution(labels):
    result = col.defaultdict(list)
    for index, val in enumerate(labels):
        result[val].append(index)
    # print_distribution_counts(result)
    return result

def print_distribution_counts(distribution):
    result = col.defaultdict(int)
    total = 0
    for index, arr in distribution.items():
        result[index] = len(arr)
        total += len(arr)
    print result, total

def detect_stacked(centers):
    result = col.defaultdict(list)
    for index, val in enumerate(centers):
        result[tuple(val)].append(index)
    print len(result)

def printInfo(val, zip_demands, zip_map):
    print 'Score: {} (given {} batteries of size {} MW)\n'.format(val[0], cfg.n_batteries, cfg.battery_size_MW)
    print 'Battery Zipcode Supply Distributions (KWh):'
    util.printListDict(val[1], zip_map)
    print 'Zipcode Energy Supplied (KWh):'
    util.printListDictAppend(val[2], zip_demands, zip_map)

if __name__ == '__main__':
	main()
