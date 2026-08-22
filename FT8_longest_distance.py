# This script calculates the FT8 A index based on the provided data.
import sys, pandas as pd, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates
from wsgiref import headers
import numpy as np, mplcursors, pathlib 
import FT8_plots_v1
import FT8_data_functions
from my_dropdown_box_func import my_drop_down_box as ddb

from datetime import datetime

from FT8_data_functions import get_data_for_year as gdfy

def load_year_data(year_type: str) -> pd.DataFrame:
    """loads the data"""
    data = gdfy(year_type).copy()
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.set_index('DATE').sort_index().reset_index()
    data['YEAR'] = data['DATE'].dt.year.astype(str)
    data['TIME_ADL'] = pd.to_datetime(data['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time
    data['DISTANCE'] = pd.to_numeric(data['DISTANCE'], errors='coerce')
    data['SFI'] = pd.to_numeric(data['SFI'], errors='coerce')
    data['BAND'] = data['BAND'].astype(str).str.strip()
    data['YEAR'] = data['YEAR'].astype(str).str.strip()
    data['A_INDEX'] = data['A_INDEX'].astype(float)
    data['K_INDEX'] = data['K_INDEX'].astype(float)
    data['SFI'] = data['SFI'].astype(float)
    data['MONTH'] = data['MONTH'].astype(str).str.strip()
    data['TIME_ADL'] = data['TIME_ADL'].astype(str).str.strip()
    data['DISTANCE'] = data['DISTANCE'].astype(float)
    # Format DATE as day-month-year string in the requested display format.
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce').dt.strftime('%d-%m-%Y')
    
    return data

def main():

    cols = ["DATE", "CALL", "BAND", "YEAR", "RST_RCVD", "RST_SENT",
        "DISTANCE", "TIME_ADL"]
    headers = ["DATE", "CALL", "BAND", "YEAR", "RST_RCVD", "RST_SENT",
        "DISTANCE", "TIME_ADL"]
    
    master_list = [headers]

    for year in ["2024", "2025", "2026"]:
        data = load_year_data(year)
        max_distance = data["DISTANCE"].max()
        rows = data[data["DISTANCE"] == max_distance][cols]
        master_list.extend(rows.to_numpy().tolist())

    longest_distance = [
        [str(value) for value in row]
        for row in master_list
    ]

    widths = [
        max(len(row[i]) for row in longest_distance)
        for i in range(len(headers))
    ]

    for row in longest_distance:
        #print(" | ".join(f"{value:<{widths[i]}}" for i, value in enumerate(row)))
        ld = " | " .join(f"{value:<{widths[i]}}" for i, value in enumerate(row))
        

        #plotting the longest distance data
    df_longest_distance = pd.DataFrame(master_list[1:], columns=master_list[0])
    df_longest_distance['DATE'] = pd.to_datetime(df_longest_distance['DATE'], format='%d-%m-%Y', errors='coerce')
    df_longest_distance['DISTANCE'] = pd.to_numeric(df_longest_distance['DISTANCE'], errors='coerce')
    df_longest_distance = df_longest_distance.sort_values(by='DATE')    
    sns.set(style="whitegrid")
    plt.figure(figsize=(6, 4)) 
    ax = sns.barplot(data=df_longest_distance, x='DATE', y='DISTANCE', palette='viridis')
    # annotate each bar with its band and callsign
    for bar, (_, row) in zip(ax.patches, df_longest_distance.iterrows()):
        label = f"{row['BAND']}\n{row['CALL']}\n{row['DISTANCE']:.0f} km"
        ax.annotate(
            label,
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    #plt.title('Longest Distance Over Time')
    plt.xlabel('Longest Distance by Date')
    plt.ylabel('Distance')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  


if __name__ == "__main__":
    main()
