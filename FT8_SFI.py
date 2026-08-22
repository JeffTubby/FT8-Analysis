#my_get_data_year_only
import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime

from datetime import datetime
# 3. Group by month and calculate the mean of both RST_RCVD and RST_SENT


# create line plot with subplot for both series

def get_data_for_year(year_type):
# get data from data/datasheet.xlsx
    """data for each year"""

    import pandas as pd
    import matplotlib.pylab as plt
    import pathlib
    import datetime
    import sys
    import matplotlib.dates as mdates
    from datetime import date

    Path = pathlib.Path('data/datasheet.xlsx')
    df = pd.read_excel('data/datasheet.xlsx')
    df['BAND'] = df['BAND'].astype(str).str.strip()
    df['YEAR'] = df['YEAR'].astype(str).str.strip()
    df['A_INDEX'] = df['A_INDEX'].astype(float)
    df['K_INDEX'] = df['K_INDEX'].astype(float)
    df['SFI'] = df['SFI'].astype(float)
    df['MONTH'] = df['MONTH'].astype(str).str.strip()
    df['SFI'] = df['SFI'].astype(float)
    # 3. Group by month and calculate the mean of both RST_RCVD and RST_SENT

    # 2. Reformat that datetime object into the new string format
    # sort date from earliest to latest

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
    data=data.sort_values('SFI')
    return data
def main():
    from my_dropdown_box_func import my_drop_down_box as ddb
    # get data from box input
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}, Year selected: {year_type}")

    data = get_data_for_year(year_type)
    # Convert MONTH to numeric and sort
    #data=data.sort_values('SFI')
    #data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    #data = data.sort_values('MONTH')   

    # Line plot A_INDEX, K_INDEX and SFI
    sns.set_style("whitegrid")
    plt.figure(figsize=(10,4))
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.lineplot(x='MONTH', y='SFI', data=data, label='SFI', errorbar=('ci', 95))
    plt.title(f'FT8 SFI Analysis for {band_type} in Year {year_type}')

    #data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    #data['MONTH'] = pd.to_datetime(data['MONTH'], format='%m', errors='coerce')

    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(loc='lower left')
    plt.grid()
    dates = ['DATE']
    values = ['SFI']
    cursor = mplcursors.cursor(hover=True)
    plt.show()

    # Daily mean SFI
    df = pd.DataFrame(data)
    # Group by month and calculate the mean of both RST_RCVD and RST_SENT
    daily_means = df.groupby('DATE')[['SFI']].mean().reset_index()

    sns.set_style("whitegrid")
    plt.figure(figsize=(10,4))
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    #sns.lineplot(x='DATE', y='A_INDEX', data=data, label='A Index', errorbar=('ci', 95))
    #sns.lineplot(x='DATE', y='K_INDEX', data=data, label='K Index', errorbar=('ci', 95))
    sns.lineplot(x='DATE', y='SFI', data=daily_means, label='SFI', errorbar=('ci', 95))
    plt.title(f'FT8 SFI Mean for {band_type} in Year {year_type}')

    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    data['MONTH'] = pd.to_datetime(data['MONTH'], format='%m', errors='coerce')

    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(loc='lower left')
    plt.grid()
    dates = ['DATE']
    values = ['SFI']
    cursor = mplcursors.cursor(hover=True)
    plt.show()

    #lineplot RST_SENT and RST_RCVD
    sns.set_style("whitegrid")
    plt.figure(figsize=(10,4))
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.lineplot(x='DATE', y='RST_SENT', data=data, label='RST_SENT', errorbar=('ci', 95))
    sns.lineplot(x='DATE', y='RST_RCVD', data=data, label='RST_RCVD', errorbar=('ci', 95))
    #sns.lineplot(x='DATE', y='SFI', data=data, label='SFI', errorbar=('ci', 95))
    plt.title(f'FT8 SFI Analysis for {band_type} in Year {year_type}')

    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    data['MONTH'] = pd.to_datetime(data['MONTH'], format='%m', errors='coerce')

    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(loc='lower left')
    plt.grid()
    dates = ['DATE']
    values = ['RST_SENT', 'RST_RCVD']
    cursor = mplcursors.cursor(hover=True)
    plt.show()



if __name__ == "__main__":
    main()
