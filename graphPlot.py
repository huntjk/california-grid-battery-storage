import config
import numpy as np
import folium
from folium import plugins
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

def main():
    folium_map = folium.Map([37.7783, -119.4179], zoom_start = 7)

    print config.test_data_df

    for index, row in config.test_data_df.iterrows():
        if np.isnan(row['Latitude']) or np.isnan(row['Longitude']): continue

        popup_text = """Zipcode: {}<br>
                        2017 Supply (KW): {}<br>
                        2017 Demand (KWh): {}"""
        popup_text = popup_text.format(str(index), row['Supply_KW'], 1)

        folium.CircleMarker([row['Latitude'], row['Longitude']], radius = 0.001 * row['Supply_KW'], popup = popup_text).add_to(folium_map)
    folium_map.save("/Users/jkhunt/github/batteries-california/test_map.html")

if __name__ == '__main__':
	main()
