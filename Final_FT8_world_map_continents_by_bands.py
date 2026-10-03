# Final_FT8_world_map_continents_by_bands.py
# Author: Jeff Tubbenhauer VK5IU
# Date: 05/06/2024
# This script generates a world map showing QSO counts for each continent, filtered by the selected band.

import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime, argparse
import geopandas as gpd
import geodatasets
import matplotlib.patheffects as path_effects
from datetime import datetime
# Import necessary libraries for data processing, plotting, and geospatial analysis.
# This includes libraries for handling Excel data, plotting maps, and managing date and time information.
# The script also includes functionality for selecting the desired band and year through a dropdown box.
from my_dropdown_box_func import my_drop_down_box as ddb

from collections import Counter

def get_my_data_by_band(band_type): #gmd
    """Fetches and processes data for the specified band and year."""
    #import pathlib
    #import pandas as pd
    #import sys
    
    Path = pathlib.Path('data/datasheet.xlsx')   
    df = pd.read_excel('data/datasheet.xlsx', keep_default_na=False)
    df['BAND'] = df['BAND'].astype(str).str.strip()
    df['YEAR'] = df['YEAR'].astype(str).str.strip()
    df['A_INDEX'] = df['A_INDEX'].astype(str).str.strip()
    df['K_INDEX'] = df['K_INDEX'].astype(str).str.strip()
    df['SFI'] = df['SFI'].astype(str).str.strip()
    df['MONTH'] = df['MONTH'].astype(str).str.strip()
    df['TIME_ADL'] = df['TIME_ADL'].astype(str).str.strip()
    df['DISTANCE'] = df['DISTANCE'].astype(str).str.strip() 
    df['DATE'] = df['DATE'].astype(str).str.strip()
    df['CALL'] = df['CALL'].astype(str).str.strip()
    df['DISTANCE'] = pd.to_numeric(df['DISTANCE'], errors='coerce')
    df['SFI'] = pd.to_numeric(df['SFI'], errors='coerce')
    df['A_INDEX'] = pd.to_numeric(df['A_INDEX'], errors='coerce')
    df['K_INDEX'] = pd.to_numeric(df['K_INDEX'], errors='coerce')
    df['CONT'] = df['CONT'].astype('string').str.strip()
    df['COUNTRY'] = df['COUNTRY'].astype(str).str.strip()
    

    # Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time

    # select the correct band and year
    mask = (df['BAND'] == band_type)
    df_filtered = df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                             'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE',
                             'CALL','DISTANCE', 'CONT', 'COUNTRY']]
    if df_filtered.empty:
        print('Your selection does not have band and/or year data!')
        
    my_data = df_filtered
    data = pd.DataFrame(my_data.copy())
    
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values(by='DATE')

    if data.empty:
        print('No data available for the selected band and year.')
        return None
    return data



def main():
    # get data from box input
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}")
    

    # Fetch and filter the data based on the selected band.
    # The get_my_data_by_band function retrieves the data filtered by the selected band.
    
    # If no data is returned, the script will handle it gracefully.
    
    if band_type is None:
        print("No band selected.")
        return  
    
    df = get_my_data_by_band(band_type)  # Example usage
    qso_cont = {}

    # Count QSOs per continent
    # Only proceed if the filtered DataFrame is not empty

    if df is not None:
        qso_cont = (
            df["CONT"].fillna("").astype(str).str.strip()
            .loc[lambda s: s != ""]
            .value_counts()
            .to_dict()
        )

    world = gpd.read_file(
        "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
    )

    cont_code_to_name = {
        "AF": "Africa",
        "AN": "Antarctica",
        "AS": "Asia",
        "EU": "Europe",
        "NA": "North America",
        "OC": "Oceania",
        "SA": "South America",
    }

    continent_counts = {
        cont_code_to_name[code]: count
        for code, count in qso_cont.items()
        if code in cont_code_to_name
    }

    label_positions = {
        "Africa": (20, 5),
        "Antarctica": (0, -75),
        "Asia": (90, 35),
        "Europe": (15, 52),
        "North America": (-100, 40),
        "Oceania": (145, -20),
        "South America": (-60, -15),
    }

    fig, ax = plt.subplots(figsize=(10, 6))
    world.plot(ax=ax, edgecolor="black", facecolor="#dddddd")

    if continent_counts:
        continent_df = world[world["CONTINENT"].isin(continent_counts)].copy()
        continent_df["QSO_COUNT"] = continent_df["CONTINENT"].map(continent_counts)
        continent_df.plot(
            ax=ax,
            column="QSO_COUNT",
            cmap="YlOrRd",
            edgecolor="black",
            legend=True,
            legend_kwds={"label": "QSO count", "shrink": 0.75},
        )

    for continent_name, count in continent_counts.items():
        longitude, latitude = label_positions[continent_name]
        txt = ax.text(
            longitude,
            latitude,
            str(count),
            ha="center",
            va="center",
            fontsize=15,
            color="yellow",
            fontweight="bold",
            bbox=dict(facecolor="black", edgecolor="none", alpha=0.7, boxstyle="round")            
        )
        txt.set_path_effects([
        path_effects.withSimplePatchShadow(offset=(2, -2), shadow_rgbFace='black')
        ])

    plt.title(f"World Map with Continents QSO Count for band {band_type}", fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()