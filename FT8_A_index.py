#FT8_A_index.py
# This script calculates the FT8 A index based on the provided data.
import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors

from datetime import datetime
from FT8_data_functions import get_data_for_year as gdfy
from my_dropdown_box_func import my_drop_down_box as ddb

def load_year_data(year_type: str) -> pd.DataFrame:
    """loads the data"""
    data = gdfy(year_type).copy()
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')git reset --hard HEAD~1

    data = data.set_index('DATE').sort_index().reset_index()
    
    
    #data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    #data = data.sort_values('MONTH')
    #data=data.sort_values('SFI')
     
    #data['MONTH'] = pd.to_datetime(data['MONTH'], format='%m', errors='coerce')
    return data

def main():

    # get data from box input
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}, Year selected: {year_type}")

    data=load_year_data(year_type)
   

    #plot A_INDEX  by date 
    sns.set_style("darkgrid")               
    fig, ax = plt.subplots( figsize=(7, 3))
    sns.lineplot(x='DATE', y='A_INDEX', data=data, marker='o', label='A_INDEX', color='red',ax=ax)
    plt.title(f'Show A_INDEX by Date and Year for {year_type}', fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.xlabel('Date', fontsize=7)
    plt.ylabel('A_INDEX', fontsize=10)
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(loc='upper left')
    plt.grid(5)
    
    cursor = mplcursors.cursor(hover=True)
    plt.tight_layout()
    plt.show()

    #plot A_INDEX  by month 
    sns.set_style("darkgrid")
    fig, ax = plt.subplots( figsize=(7, 3))
    sns.lineplot(x='MONTH', y='A_INDEX', data=data, marker='o', label='A_INDEX', color='green',ax=ax)
    plt.title(f'Monthly A_INDEX for year {year_type}', fontsize=10)
    plt.xlabel('Month', fontsize=7)
    plt.ylabel('A_INDEX', fontsize=10)
    data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m'))
    #plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.legend(loc='upper left')
    plt.grid(5)
    cursor = mplcursors.cursor(hover=True)
    plt.tight_layout()
    plt.show()

    #plot RST_RCVD and RST_SENT
    sns.set_style("darkgrid")
    plt.figure(figsize=(7,3))
    plt.title(f'FT8 RST Analysis for in Year {year_type}', fontsize=10)
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.lineplot(x='DATE', y='RST_SENT', data=data, label='RST_SENT', color='red', linestyle='dashed', errorbar=('ci', 95))
    sns.lineplot(x='DATE', y='RST_RCVD', data=data, label='RST_RCVD', color='blue', errorbar=('ci', 95))
    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    data['MONTH'] = pd.to_datetime(data['MONTH'], format='%m', errors='coerce')
    data['DATE'] = pd.to_datetime(data['DATE'], format=('%d-%m-%Y'))
    plt.xlabel('Date', fontsize=7)
    plt.ylabel('RST', fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(loc='lower left')
    plt.grid(20)
    #dates = ['DATE']
    values = ['DATE', 'RST_RCVD']
    cursor = mplcursors.cursor(hover=True)
    plt.show()

    #plot mean_RST_RCVD and mean_RST_SENT

    mean_data = data.groupby('DATE').agg({'RST_RCVD': 'mean', 'RST_SENT': 'mean'}).reset_index()
    sns.set_style("darkgrid")
    plt.figure(figsize=(7,3))
    plt.title(f'FT8 mean RST for in Year {year_type}')
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.lineplot(x='DATE', y='RST_SENT', data=mean_data, label='Mean SENT_RST', color='red', linestyle='dashed', errorbar=('ci', 95))
    sns.lineplot(x='DATE', y='RST_RCVD', data=mean_data, label='Mean RCVD_RST', color='blue', errorbar=('ci', 95))
    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    data['MONTH'] = pd.to_datetime(data['MONTH'], format='%m', errors='coerce')
    data['DATE'] = pd.to_datetime(data['DATE'], format=('%d-%m-%Y'))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(loc='lower left')
    plt.grid(20)
    #dates = ['DATE']
    values = ['DATE', 'RST_RCVD']
    cursor = mplcursors.cursor(hover=True)
    plt.show()
 
if __name__ == "__main__":
    main()
