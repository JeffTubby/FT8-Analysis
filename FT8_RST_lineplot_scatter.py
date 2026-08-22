#my_get_data_year_only
import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime

from datetime import datetime
from FT8_data_functions import get_my_data as gmd

def main():
    from my_dropdown_box_func import my_drop_down_box as ddb
    # get data from box input
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}, Year selected: {year_type}")

    data = gmd(band_type, year_type)
    
    sns.set_style("whitegrid")
    plt.figure(figsize=(6,4))
    #data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.scatterplot(x='DISTANCE', y='RST_SENT', data=data, label='RST_SENT', color='blue')
    sns.scatterplot(x='DISTANCE', y='RST_RCVD', data=data, label='RST_RCVD', color='red')
    plt.xlabel('MONTH', fontsize=7)
    plt.title(f'FT8 Distance/RST Monthly Analysis for {band_type} in Year {year_type}', fontsize=10)
    plt.xlabel('MONTH', fontsize=7) 
    plt.xlabel('DISTANCE', fontsize=7)
    plt.ylabel('RST', fontsize=10) 
    plt.xticks(rotation=30)
    plt.legend(loc='upper left', prop={'size': 14, 'weight': 'bold'})
    plt.grid(20)
    plt.tight_layout()
    dates = ['DATE']
    values = ['SFI']

    cursor = mplcursors.cursor(hover=True)
    plt.show()
    
    
    # Convert MONTH to numeric and sort
    #data=data.sort_values('SFI')
    #data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    #data = data.sort_values('MONTH')   

    # Line plot A_INDEX, K_INDEX and SFI
    sns.set_style("whitegrid")
    plt.figure(figsize=(10,4))
    #data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.scatterplot(x='MONTH', y='RST_SENT', data=data, label='RST_SENT', color='blue')
    sns.scatterplot(x='MONTH', y='RST_RCVD', data=data, label='RST_RCVD', color='red')
    plt.title(f'FT8 Distance/RST Monthly Analysis for {band_type} in Year {year_type}', fontsize=10)
    plt.xlabel('MONTH', fontsize=7)
    sns.lineplot(x='MONTH', y='RST_SENT', data=data, label='RST_SENT', color='blue')
    sns.lineplot(x='MONTH', y='RST_RCVD', data=data, label='RST_RCVD', color='red')
    plt.title(f'FT8 Distance/RST Monthly Analysis for {band_type} in Year {year_type}', fontsize=10)
    plt.xlabel('MONTH', fontsize=7) 
    plt.title(f'FT8 Distance/RST MonthlyAnalysis for {band_type} in Year {year_type}')
    plt.xticks(rotation=30)
    plt.legend(loc='upper left', prop={'size': 14, 'weight': 'bold'})
    plt.grid(20)
    #dates = ['DATE']
    #values = ['SFI']
    cursor = mplcursors.cursor(hover=True)
   
    plt.show()
        
if __name__ == "__main__":
    main()
