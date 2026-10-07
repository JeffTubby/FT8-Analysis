# This script generates scatter plots showing the Solar Flux Index (SFI) for each year.
# Author: Jeff Tubbenhauer VK5IU
# Date: 18/06/2024

import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime

from datetime import datetime

# Import the custom drop down box function for selecting band and year.
# This function will be used to create a drop down box for selecting the band and year.
from my_dropdown_box_func import my_drop_down_box as ddb

def get_data_for_year(year_type):
    """Retrieve and preprocess data for the specified year."""

    Path = pathlib.Path('data/datasheet.xlsx')
    df = pd.read_excel('data/datasheet.xlsx')
    df['BAND'] = df['BAND'].astype(str).str.strip()
    df['YEAR'] = df['YEAR'].astype(str).str.strip()
    df['A_INDEX'] = df['A_INDEX'].astype(float)
    df['K_INDEX'] = df['K_INDEX'].astype(float)
    df['SFI'] = df['SFI'].astype(float)
    df['MONTH'] = df['MONTH'].astype(str).str.strip()
    df['SFI'] = df['SFI'].astype(float)
    df['DISTANCE'] = df['DISTANCE'].astype(float)
    mask = (df['YEAR'] == year_type)
    df_filtered = df.loc[mask, ['DATE','RST_RCVD', 'RST_SENT', 'MONTH',
                                'CALL','BAND', 'YEAR','A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DISTANCE']]
    my_data = df_filtered   
    data =my_data.copy()

    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values('DATE')

    # format date to d%-m-%Y        
    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    data = data.sort_values('MONTH')
    #data=data.sort_values('SFI')
    return data

def main():
    
    # get data from box input
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}, Year selected: {year_type}")

    # Retrieve the data for the selected year.
    data = get_data_for_year(year_type)

    # Set the Seaborn style for the scatter plots.
    # Create the first scatter plot for SFI versus DISTANCE.
    
    sns.set_style("darkgrid")
    plt.figure(figsize=(6,4))   
    plot_data = data.dropna(subset=["DISTANCE", "SFI"]).reset_index(drop=True)
    ax = sns.scatterplot(x="DISTANCE", y="SFI", data=plot_data, label="SFI", color="green", s=25, edgecolor="black")
    plt.title(f"Plot 1C FT8 SFI Scatterplot for Year {year_type}", fontsize=10)
    plt.xlabel("DISTANCE", fontsize=10)
    plt.ylabel("SFI", fontsize=10)
    plt.xticks(rotation=30)
    plt.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)

    cursor = mplcursors.cursor(ax, hover=True)

    @cursor.connect("add")
    def show_date_and_sfi(selection):
        row = plot_data.iloc[selection.index]
        selection.annotation.set_text(
            f"DATE: {row['DATE']}\n"
            f"SFI: {row['SFI']:.1f}"
        )
    plt.show()
    
    sns.set_style("darkgrid")
    plt.figure(figsize=(6,4))   
    plot_data = data.dropna(subset=["DISTANCE", "A_INDEX"]).reset_index(drop=True)
    ax = sns.scatterplot(x="DISTANCE", y="A_INDEX", data=plot_data, label="A_INDEX", color="red", s=25, edgecolor="black")
    plt.title(f"PLOT 2A FT8 A_INDEX Scatterplot Analysis for Year {year_type}", fontsize=10)
    plt.xlabel("DISTANCE", fontsize=10)
    plt.ylabel("A_INDEX", fontsize=10)
    plt.xticks(rotation=30)
    plt.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)

    cursor = mplcursors.cursor(ax, hover=True)

    @cursor.connect("add")
    def show_date_and_a_index(selection):
        row = plot_data.iloc[selection.index]
        selection.annotation.set_text(
            f"DATE: {row['DATE']}\n"
            f"A_INDEX: {row['A_INDEX']:.1f}"
        )
    plt.show()

    sns.set_style("darkgrid")
    plt.figure(figsize=(6,4))   
    plot_data = data.dropna(subset=["DISTANCE", "K_INDEX"]).reset_index(drop=True)
    ax = sns.scatterplot(x="DISTANCE", y="K_INDEX", data=plot_data, label="K_INDEX", color="blue", s=25, edgecolor="black")
    plt.title(f"Plot 1A FT8 K_INDEX Scatterplot Analysis for Year {year_type}", fontsize=10)
    plt.xlabel("DISTANCE", fontsize=10)
    plt.ylabel("K_INDEX", fontsize=10)
    plt.xticks(rotation=30)
    plt.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)

    cursor = mplcursors.cursor(ax, hover=True)

    @cursor.connect("add")
    def show_date_and_k_index(selection):
        row = plot_data.iloc[selection.index]
        selection.annotation.set_text(
            f"DATE: {row['DATE']}\n"
            f"K_INDEX: {row['K_INDEX']:.1f}"
        )
    plt.show()




    sys.exit(0)
    
    # Convert MONTH to numeric and sort
    #data=data.sort_values('SFI')
    data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    data = data.sort_values('MONTH')   

    # Line plot A_INDEX, K_INDEX and SFI
    sns.set_style("whitegrid")
    plt.figure(figsize=(10,4))
    #data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.scatterplot(x='MONTH', y='SFI', data=data, label='SFI')
    plt.title(f'FT8 SFI Analysis for {band_type} in Year {year_type}')
    plt.xticks(rotation=30)
    plt.legend(loc='upper left', prop={'size': 14, 'weight': 'bold'})
    plt.grid(20)
    #dates = ['DATE']
    #values = ['SFI']
    cursor = mplcursors.cursor(hover=True)
   
    plt.show()
        
if __name__ == "__main__":
    main()
