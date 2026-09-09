import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime

# Drop down box function to select band and year
from my_dropdown_box_func import my_drop_down_box as ddb

# get data from PythonData17326.xlsx
def get_my_band_all_data(band_type, year_type):
    """Fetches and processes data for the specified band and year."""

    

    Path = pathlib.Path('data/datasheet.xlsx')   
    df = pd.read_excel('data/datasheet.xlsx')
    df['BAND'] = df['BAND'].astype(str).str.strip()
    df['YEAR'] = df['YEAR'].astype(str).str.strip()
    df['A_INDEX'] = df['A_INDEX'].astype(str).str.strip()
    df['K_INDEX'] = df['K_INDEX'].astype(str).str.strip()
    df['SFI'] = df['SFI'].astype(str).str.strip()
    df['MONTH'] = df['MONTH'].astype(str).str.strip()
    df['TIME_ADL'] = df['TIME_ADL'].astype(str).str.strip()
    df['DATE'] = df['DATE'].astype(str).str.strip()


    # select the correct band and year
    mask = (df['BAND'] == band_type) & (df['YEAR'] == year_type)


# Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time

    df_filtered = df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                             'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE','YEAR']]

    my_data = df_filtered   
    data =my_data.copy()


# sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values('DATE')
    
    #format date to d%-m-%Y
    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')

    return data

def main():  
    
    # starts a drop down box function to select band and year
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")
    print(f"Band selected: {band_type}, Year selected: {year_type}")
    
    # Call the function get_my_band_all_data with the correct parameters from get_band_all_data.py
    data = get_my_band_all_data(band_type, year_type)
    

    # create a histogram of the RST_RCVD column
    plt.figure(figsize=(5, 3))
    sns.set_style("darkgrid")
    sns.histplot(data=data, x='RST_SENT', bins=20, kde=True)
    sns.histplot(data=data, x='RST_RCVD', bins=20, kde=True, color='orange')
    plt.title(f'Histogram of RST_SENT and RST_RCVD for {band_type} band and {year_type} year', fontsize=10)
    plt.xlabel('RST_SENT and RST_RCVD', fontsize=8)
    plt.ylabel('Count', fontsize=8)
    plt.tight_layout()
    plt.legend(['RST_SENT', 'RST_RCVD'], fontsize=8)
    plt.show()


if __name__ == "__main__":
    sys.exit(main())
