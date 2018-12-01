import config as cfg
import numpy as np
import folium
from folium import plugins
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

<<<<<<< HEAD
data = cfg.data_set
# folium_map = folium.Map([37.7783, -119.4179], zoom_start = 7)
folium_map = folium.Map([37.804, -122.2711], zoom_start = 12)
=======
def main():
    folium_map = folium.Map([37.7783, -119.4179], zoom_start = 7)

    for index, row in cfg.test_data_df.iterrows():
        if np.isnan(row['Latitude']) or np.isnan(row['Longitude']): continue
>>>>>>> 6703202d1a5efd12ff6b4fcaeea3a792072888ac

def graph(battery_locations, energy_mapping):
    nf = getNormalizeFactor(cfg.month_index) # maximize size of possible ring radius
    for zipcode, values in data.items():
        if np.isnan(values[cfg.LATITUDE]) or np.isnan(values[cfg.LONGITUDE]): continue
        popup_text = """Zipcode: {}<br>
                        2017 Supply (KW): {}<br>
                        2017 Demand (KWh): {}"""
<<<<<<< HEAD
        popup_text = popup_text.format(str(zipcode), values[cfg.SUPPLY_KW], values[cfg.month_index])
        folium.CircleMarker([values[cfg.LATITUDE], values[cfg.LONGITUDE]], radius = 100 * (values[cfg.month_index] / nf), popup = popup_text).add_to(folium_map)

    for location in battery_locations.keys():
        folium.Marker([location[0], location[1]]).add_to(folium_map)

    for location, energy in energy_mapping.items():
        if energy == 0: continue
        folium.CircleMarker([location[0], location[1]], radius = 100 * (energy / nf), color = 'crimson').add_to(folium_map)

=======
        popup_text = popup_text.format(str(index), row['Supply_KW'], sum(cfg.test_data[index][cfg.MONTH_1_KWH:]))

        folium.CircleMarker([row['Latitude'], row['Longitude']], radius = 0.01 * row['Supply_KW'], popup = popup_text).add_to(folium_map)
>>>>>>> 6703202d1a5efd12ff6b4fcaeea3a792072888ac
    folium_map.save("/Users/jkhunt/github/batteries-california/test_map.html")

def getNormalizeFactor(index):
    return max([x[index] for x in cfg.data_set.values()])

if __name__ == '__main__':
	graph()
