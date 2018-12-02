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
    kmeans = KMeans(n_clusters = cfg.n_batteries, init = 'k-means++')
    kmeans.fit(np.array(zip_coords), sample_weight = np.array(zip_weights))
    distribution = label_distribution(kmeans.labels_)
    print_distribution(distribution)
    gp.graph_scikit(kmeans.cluster_centers_, zip_coords, distribution)
    # print kmeans.cluster_centers_
    # print kmeans.labels_
    # print kmeans.inertia_
    # print kmeans.n_iter_

def label_distribution(labels):
    result = col.defaultdict(list)
    for index, val in enumerate(labels):
        result[val].append(index)
    return result

def print_distribution(distribution):
    for index, arr in distribution.items():
        print '{}: {}'.format(index, len(arr))

if __name__ == '__main__':
	main()
