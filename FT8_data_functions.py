# This module contains functions to get the specific data


# get data from PythonData17326.xlsx
def get_my_data(band_type, year_type):
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

# Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time

# select the correct band and year
    mask = (df['BAND'] == band_type) & (df['YEAR'] == year_type)
    df_filtered = df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                             'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE']]
    if df_filtered.empty:
        print('Your selection does not have band and/or year data!')
        
    my_data = df_filtered
    data = my_data.copy()
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values('DATE')
    if data.empty:
        print('No data available for the selected band and year.')
        return None
    return data
 
# get data from PythonData17326.xlsx
def get_my_band_all_data(band_type):
    """Fetches and processes data for the specified band"""
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

    df_filtered = df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                             'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE','YEAR']]

    my_data = df_filtered   
    data =my_data.copy()

# sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values('DATE')
    
# Convert MONTH to numeric and sort
    #data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    #data = data.sort_values('MONTH')   
    return data 
