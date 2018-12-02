import config as cfg
import numpy as np
import folium
from folium import plugins
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

data = cfg.data_set
# folium_map = folium.Map([37.7783, -119.4179], zoom_start = 7)
folium_map = folium.Map([37.805, -122.2711], zoom_start = 12)
colors = [
    'red',
    'blue',
    'gray',
    'darkred',
    'lightred',
    'orange',
    'beige',
    'green',
    'darkgreen',
    'lightgreen',
    'darkblue',
    'lightblue',
    'purple',
    'darkpurple',
    'pink',
    'cadetblue',
    'lightgray',
    'black'
]

def graph(battery_locations, energy_mapping):
    nf = getNormalizeFactor(cfg.month_index) # maximize size of possible ring radius
    for zipcode, values in data.items():
        if np.isnan(values[cfg.LATITUDE]) or np.isnan(values[cfg.LONGITUDE]): continue
        popup_text = """Zipcode: {}<br>
                        2017 Supply (KW): {}<br>
                        2017 Demand (KWh): {}"""
        popup_text = popup_text.format(str(zipcode), values[cfg.SUPPLY_KW], values[cfg.month_index])
        folium.CircleMarker([values[cfg.LATITUDE], values[cfg.LONGITUDE]], radius = 100 * (values[cfg.month_index] / nf), popup = popup_text).add_to(folium_map)

    for location in battery_locations.keys():
        folium.Marker([location[0], location[1]]).add_to(folium_map)

    for location, energy in energy_mapping.items():
        if energy == 0: continue
        folium.CircleMarker([location[0], location[1]], radius = 100 * (energy / nf), color = 'crimson').add_to(folium_map)

    folium_map.save("/Users/jkhunt/github/batteries-california/test_map.html")

def graph_scikit(battery_locations, zip_coords, distribution):
    nf = getNormalizeFactor(cfg.month_index) # maximize size of possible ring radius

    for i, location in enumerate(battery_locations):
        folium.Marker(location, icon = folium.Icon(color = colors[i % len(colors)])).add_to(folium_map)
        for val in distribution[i]:
            # if np.isnan(values[cfg.LATITUDE]) or np.isnan(values[cfg.LONGITUDE]): continue
            # popup_text = """Zipcode: {}<br>
            #                 2017 Supply (KW): {}<br>
            #                 2017 Demand (KWh): {}"""
            # popup_text = popup_text.format(str(zipcode), values[cfg.SUPPLY_KW], values[cfg.month_index])
            # folium.CircleMarker([values[cfg.LATITUDE], values[cfg.LONGITUDE]], radius = 100 * (values[cfg.month_index] / nf), popup = popup_text).add_to(folium_map)
            folium.CircleMarker(zip_coords[val], radius = 10, color = colors[i % len(colors)]).add_to(folium_map)

    folium_map.save("/Users/jkhunt/github/batteries-california/scikit_map.html")

def graph_comparison(battery_locations_start, battery_locations_end):
    nf = getNormalizeFactor(cfg.month_index) # maximize size of possible ring radius
    for zipcode, values in data.items():
        if np.isnan(values[cfg.LATITUDE]) or np.isnan(values[cfg.LONGITUDE]): continue
        popup_text = """Zipcode: {}<br>
                        2017 Supply (KW): {}<br>
                        2017 Demand (KWh): {}"""
        popup_text = popup_text.format(str(zipcode), values[cfg.SUPPLY_KW], values[cfg.month_index])
        folium.CircleMarker([values[cfg.LATITUDE], values[cfg.LONGITUDE]], radius = 100 * (values[cfg.month_index] / nf), popup = popup_text).add_to(folium_map)

    for location in battery_locations_start.values():
        folium.Marker([location[0][0], location[0][1]], icon = folium.Icon(color = 'blue')).add_to(folium_map)

    for location in battery_locations_end.values():
        folium.Marker([location[0][0], location[0][1]], icon = folium.Icon(color = 'red')).add_to(folium_map)

    folium_map.save("/Users/jkhunt/github/batteries-california/comparison_map.html")

def getNormalizeFactor(index):
    return max([x[index] for x in cfg.data_set.values()])

if __name__ == '__main__':
	graph()
