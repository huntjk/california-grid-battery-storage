import config as cfg
import util
import numpy as np
import pandas as pd
import collections as col
import graphPlot as gp

data = cfg.data_set
neighbors = cfg.neighbors_set

def main():
    scores = []
    for i in range(cfg.n_iters):
        energy_supplied_zipcodes = col.defaultdict(float)
        batteries = randomInitialize()
        for battery_zip, index in batteries.keys():
            remaining_energy = cfg.battery_month_KWH
            for supply_zip in neighbors[battery_zip]:
                if remaining_energy <= 0: break
                zip_energy_demand = data[supply_zip][cfg.month_index] * cfg.percentage_fulfill # percentage of zipcode demand to be fulfilled
                current_zip_supply = energy_supplied_zipcodes[supply_zip]
                distance = util.getDistance(util.getCoords(battery_zip), util.getCoords(supply_zip))

                if remaining_energy + current_zip_supply <= zip_energy_demand: # If battery max less than zipcode demand
                    energy_supplied_zipcodes[supply_zip] += util.energyLoss(distance, remaining_energy)
                    batteries[(battery_zip, index)][supply_zip] += remaining_energy
                    break
                else:
                    required_energy_to_max = zip_energy_demand - current_zip_supply
                    if required_energy_to_max <= 0: continue
                    energy_supplied_zipcodes[supply_zip] = zip_energy_demand
                    battery_energy_supply = util.inverseEnergyLoss(distance, required_energy_to_max)
                    batteries[(battery_zip, index)][supply_zip] = battery_energy_supply
                    remaining_energy -= battery_energy_supply

        scores.append((scoreFunction(energy_supplied_zipcodes), batteries, energy_supplied_zipcodes))
    max_loc = getMax(scores) # max_loc is tuple (score, batteries zipcode energy mapping, supplied energy per zipcode)
    printInfo(max_loc)
    gp.graph(util.getLatLongTuple(max_loc[1]), util.getLatLong(max_loc[2]))

def randomInitialize():
    batteries = {}
    for i in range(cfg.n_batteries):
        random_zip = np.random.choice(data.keys(), replace = False)
        batteries[(random_zip, i)] = col.defaultdict(float)
    return batteries

def scoreFunction(energy_supplied_zipcodes):
    score = 0
    total = 0
    for zipcode, val in data.items():
        score += energy_supplied_zipcodes[zipcode]
        total += val[cfg.month_index]
    return score / total

def getMax(scores):
    max_loc = (0, [])
    for x in scores:
        if x[0] > max_loc[0]:
            max_loc = x
    return max_loc

def printInfo(tuple):
    print 'Score: {} (given {} batteries of size {} MW)\n'.format(tuple[0], cfg.n_batteries, cfg.battery_size_MW)
    print 'Battery Zipcode Supply Distributions (KWh):'
    util.printDict(tuple[1])
    print 'Zipcode Energy Supplied (KWh):'
    util.printDictAppend(tuple[2])

if __name__ == '__main__':
	main()
