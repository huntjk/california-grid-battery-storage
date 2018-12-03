import folium
import json
import pandas as pd
import csv
import config as cfg


def graph_clusters(battery_locations, battery_supplied_zipcodes, original_zip_coords): 
    #create map
    m = folium.Map(location=[37, -120], tiles='Mapbox Bright', zoom_start=6)
    ca_zips = 'ca_zips.json' 
    add_json(m, ca_zips)

    loc_to_zipname_dict = {}
    get_zip_names(loc_to_zipname_dict)

    # make data frame with columns "zip_name" and "cluster_num"
    df = pd.DataFrame(columns=['zip_name', 'cluster_num'])
    for i in range(len(battery_supplied_zipcodes)):
        for zipcode_i in battery_supplied_zipcodes[i].keys():
            coords = original_zip_coords[zipcode_i]
            coords = (round(coords[0], 6), round(coords[1], 6))
            zip_name = loc_to_zipname_dict[tuple(coords)]
            df.loc[df.shape[0]] = [zip_name, i]

    # make choropleth layer to color the clusters on the map
    m.choropleth(
        geo_data=ca_zips,
        fill_opacity=.7,
        line_opacity=.2, 
        data=df,
        key_on='feature.properties.zcta',
        columns=['zip_name', 'cluster_num'],
        fill_color='RdYlGn',
        legend_name='Cluster Number',
        highlight=True
    )
    
    add_battery_locs(m, battery_locations)
    folium.LayerControl().add_to(m)
    m.save('map_clusters_' + str(cfg.n_batteries) + '_' + str(cfg.percentage_fulfill) +'.html')


def graph_supplied_energy(battery_locations, energy_supplied_zipcodes, original_zip_demand, original_zip_coords):
   #create map
    m = folium.Map(location=[37, -120], tiles='Mapbox Bright', zoom_start=6)
    ca_zips = 'ca_zips.json' 
    add_json(m, ca_zips)

    loc_to_zipname_dict = {}
    get_zip_names(loc_to_zipname_dict)

    # make data frame with columns "zip_name" and "energy_supplied"
    df = pd.DataFrame(columns=['zip_name', 'energy_supplied'])
    for i in range(len(energy_supplied_zipcodes)):
        coords = original_zip_coords[i]
        coords = (round(coords[0], 6), round(coords[1], 6))
        zip_name = loc_to_zipname_dict[tuple(coords)]
        total = original_zip_demand[i]
        supplied = energy_supplied_zipcodes[i]
        df.loc[df.shape[0]] = [zip_name, round(float(supplied/total), 2)]
    
    # make choropleth layer to color the clusters on the map
    m.choropleth(
        geo_data=ca_zips,
        fill_opacity=.7,
        line_opacity=.2, 
        data=df,
        key_on='feature.properties.zcta',
        columns=['zip_name', 'energy_supplied'],
        fill_color='RdYlGn',
        legend_name='Percentage of Demand Being Supplied',
        highlight=True
    )

    add_battery_locs(m, battery_locations)
    folium.LayerControl().add_to(m)
    m.save('map_supply_' + str(cfg.n_batteries) + '_' + str(cfg.percentage_fulfill) + '.html')
    
def add_json(m, ca_zips):
    m.add_child(folium.LatLngPopup())
    #add zip code JSON

    folium.GeoJson(
        ca_zips,
        name='geojson'
    ).add_to(m)  

def get_zip_names(loc_to_zipname_dict):
    # make dictionary from lat,longs to zips
    with open('data/US_Zipcodes.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader.next() # skip over header
        for row in reader: 
            loc = (float(row[1]), float(row[2]))
            loc_to_zipname_dict[loc] = str(row[0])

def add_battery_locs(m, battery_locations):
    # add batteries to the map as circles
    for batt in battery_locations:
        folium.CircleMarker(
            location=[float(batt[0]), float(batt[1])],
            radius=5,
            color="black",
            fill=True,
        ).add_to(m) 