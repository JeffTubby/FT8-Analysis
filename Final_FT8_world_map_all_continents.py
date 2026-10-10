# This script generates a world map highlighting QSO counts for each continent.
# Author: Jeff Tubbenhauer VK5IU
# Date: 10/09/2026
# Version: 2.0
# Description: Generates a world map highlighting QSO counts for each continent
#using Geopandas and Matplotlib. 
# The world map is generated using Geopandas and Matplotlib.

import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns
import matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime, argparse
import geopandas as gpd
import geodatasets
import matplotlib.patheffects as path_effects

from datetime import datetime
from collections import Counter

# Import the custom drop down box function for selecting band and year.
# This function will be used to create a drop down box for selecting the band and year.
from my_dropdown_box_func import my_drop_down_box as ddb

def get_all_data():
    """Fetches and processes data for the specified band and year."""
        
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
    #df["CONT"] = df["CONT"].replace("AN", "NA")


    # Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time
    data = pd.DataFrame(df.copy())
    return data


def main():
    # Fetch all QSO data from the Excel datasheet.
    # Initialize a dictionary to store QSO counts for each continent.
    df = get_all_data()
    qso_cont = {}

    # Count the number of QSOs for each continent.
    if df is not None:
        qso_cont = (
            df["CONT"].fillna("").astype(str).str.strip()
            .loc[lambda s: s != ""]
            .value_counts()
            .to_dict()
        )

    # Load the world map shapefile for plotting.
    # Read the world map shapefile from the provided URL.   
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

    # Create the plot for the world map with QSO counts for each continent.
    # Set up the figure and axis for the plot.
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

    plt.title("World Map with Continents QSO Total Count", fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()