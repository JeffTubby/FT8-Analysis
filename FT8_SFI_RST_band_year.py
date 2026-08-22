import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime

from datetime import datetime
from FT8_data_functions import get_data_for_year as gdfy
from FT8_data_functions import get_my_data as gmd
from my_dropdown_box_func import my_drop_down_box as ddb

def load_year_data(band_type: str,  year_type: int) -> pd.DataFrame:
    """loads the data"""
    data = gmd(band_type, year_type).copy()
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values('DATE')

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

    data=load_year_data(band_type, year_type)
    
    
    #plot SFI  by date 
    sns.set_style("darkgrid")               
    fig, ax = plt.subplots( figsize=(5, 3))
    sns.lineplot(x='DATE', y='SFI', data=data, marker='o', label='SFI', color='green',ax=ax)
    plt.title(f'Show SFI by Date and Year for {year_type} and Band {band_type}', fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.xlabel('Date', fontsize=7)
    plt.ylabel('SFI', fontsize=10)
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(title='SFI', title_fontsize='9', fontsize='7', loc='upper left', frameon=True, fancybox=True, shadow=True)
    
    plt.grid(5)
    
    cursor = mplcursors.cursor(hover=True)
    plt.tight_layout()
    plt.show()

    #plot SFI  by month 
    sns.set_style("darkgrid")
    fig, ax = plt.subplots( figsize=(5, 3))
    sns.lineplot(x='MONTH', y='SFI', data=data, marker='o', label='SFI', color='green',ax=ax)
    plt.title(f'Monthly SFI for year {year_type} and Band {band_type}', fontsize=10)
    plt.xlabel('Month', fontsize=7)
    plt.ylabel('SFI', fontsize=10)
    data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m'))
    #plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(title='SFI', title_fontsize='9', fontsize='7', loc='upper left', frameon=True, fancybox=True, shadow=True)
    plt.grid(5)
    cursor = mplcursors.cursor(hover=True)
    plt.tight_layout()
    plt.show()

    #plot RST_RCVD and RST_SENT
    sns.set_style("darkgrid")
    plt.figure(figsize=(5,3))
    plt.title(f'FT8 RST Analysis for {band_type} in Year {year_type}', fontsize=10)
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
    plt.legend(title='RST', title_fontsize='9', fontsize='7', loc='upper left', frameon=True, fancybox=True, shadow=True)
    plt.grid(20)
    dates = ['DATE']
    values = ['DATE', 'RST_RCVD']
    cursor = mplcursors.cursor(hover=True)
    plt.show()

    #plot mean_RST_RCVD and mean_RST_SENT

    mean_data = data.groupby('DATE').agg({'RST_RCVD': 'mean', 'RST_SENT': 'mean'}).reset_index()
    sns.set_style("darkgrid")
    plt.figure(figsize=(5,3))
    plt.title(f'FT8 mean RST for {band_type} in Year {year_type}')
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.lineplot(x='DATE', y='RST_SENT', data=mean_data, label='Mean SENT_RST', color='red', linestyle='dashed', errorbar=('ci', 95))
    sns.lineplot(x='DATE', y='RST_RCVD', data=mean_data, label='Mean RCVD_RST', color='blue', errorbar=('ci', 95))
    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    data['MONTH'] = pd.to_datetime(data['MONTH'], format='%m', errors='coerce')
    data['DATE'] = pd.to_datetime(data['DATE'], format=('%d-%m-%Y'))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(title='Mean RST', title_fontsize='9', fontsize='7', loc='upper left', frameon=True, fancybox=True, shadow=True)
    plt.grid(20)
    #dates = ['DATE']
    values = ['DATE', 'RST_RCVD']
    cursor = mplcursors.cursor(hover=True)
    plt.show()
 
if __name__ == "__main__":
    main()
