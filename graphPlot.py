import config
import numpy as np
import folium
from folium import plugins
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

def main():
    folium_map = folium.Map([37.7783, -119.4179], zoom_start = 7)
    for index, row in config.data.iterrows():
        if np.isnan(row['Latitude']) or np.isnan(row['Longitude']): continue
        folium.CircleMarker([row['Latitude'], row['Longitude']], radius = 6, popup = str(int(row['Zipcode']))).add_to(folium_map)
    folium_map.save("/Users/jkhunt/github/batteries-california/test_map.html")

if __name__ == '__main__':
	main()
