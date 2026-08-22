# This module contains functions to get the specific data
import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors


# get data from PythonData17326.xlsx
from ast import If


def get_my_data(band_type, year_type): #gmd
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
    df['DISTANCE'] = df['DISTANCE'].astype(str).str.strip() 
    df['DATE'] = df['DATE'].astype(str).str.strip()
    df['CALL'] = df['CALL'].astype(str).str.strip()
    df['DISTANCE'] = df['DISTANCE'].astype(float)
    df['SFI'] = df['SFI'].astype(float)
    

# Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')

    
# select the correct band and year
    mask = (df['BAND'] == band_type) & (df['YEAR'] == year_type)
    df_filtered = df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                             'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE','CALL','DISTANCE']]
    if df_filtered.empty:
        print('Your selection does not have band and/or year data!')
        
    my_data = df_filtered
    data = my_data.copy()
# sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.dropna(subset=['DATE']).sort_values('DATE').reset_index(drop=True).copy()
    
    if data.empty:
        print('No data available for the selected band and year.')
        return None
    return data
if __name__ == "__main__":
        get_my_data(band_type='20m', year_type='2023')  # Example usage

# get data from PythonData17326.xlsx
def get_my_band_all_data(band_type):
    """Fetches and processes data for the specified band and year."""
    import pathlib
    import pandas as pd
    import sys  

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
#mask = (df['BAND'] == band_type) & (df['YEAR'] == year_type)
    mask = (df['BAND'] == band_type)


# Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')

    df_filtered = df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                             'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE','YEAR']]

    my_data = df_filtered   
    data = my_data.copy()


# sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.dropna(subset=['DATE']).sort_values('DATE').reset_index(drop=True).copy()

    return data
if __name__ == "__main__":
    get_my_band_all_data(band_type='20m')  # Example usage
    
     
     

def get_data_for_year(year_type): #gdfy
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
    data = df_filtered.copy()

    # make DATE a real datetime, then sort it
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.dropna(subset=['DATE']).sort_values('DATE').reset_index(drop=True).copy()
    return data
if __name__ == "__main__":
    get_data_for_year(year_type='2023')  # Example usage    
