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
    for val in data.values():
        zip_coords.append([val[0], val[1]])
        zip_weights.append(val[cfg.month_index])
    kmeans = KMeans(n_clusters = cfg.n_batteries, init = 'k-means++', n_init = 50)
    kmeans.fit(np.array(zip_coords), sample_weight = np.array(zip_weights))
    distribution = label_distribution(kmeans.labels_)
    # print kmeans.inertia_
    # print_distribution_info(distribution, zip_weights)
    # detect_stacked(kmeans.cluster_centers_)
    gp.graph_scikit(kmeans.cluster_centers_, zip_coords, distribution)

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

if __name__ == '__main__':
	main()
