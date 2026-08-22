import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, numpy as np, mplcursors

import FT8_classes, FT8_plots_v1

from typing import cast
from mpl_toolkits.mplot3d.axes3d import Axes3D
from datetime import datetime
from my_dropdown_box_func import my_drop_down_box as ddb
from FT8_classes import FT8DataFunctions
from FT8_plots_v1 import plot_3D as plot_3D_v1
from FT8_plots_v1 import SFI_plot as SFI_plot_v1
from FT8_plots_v1 import k_index_date_plot as k_index_date_plot_v1
from FT8_plots_v1 import A_index_plot as A_index_plot_v1
    
def get_band_year():
    """Open a drop-down box for user input."""
    band_type, year_type = ddb(default_band="20m", default_year="2025") 
    # get data from box input
    return band_type, year_type


def get_processing_data(data, band_type, year_type) -> pd.DataFrame:
    """Fetches and processes data for the specified band and year."""
    data = FT8DataFunctions()
    band_type = str(band_type).strip()
    year_type = str(year_type).strip()
    
    # Parse to datetime/time with strict format validation
    data.df['TIME_ADL'] = pd.to_datetime(data.df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time

    # select the correct band and year
    mask = (data.df['BAND'] == band_type) & (data.df['YEAR'] == year_type)
    df_filtered = data.df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                                'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE','CALL','DISTANCE']]
    if df_filtered.empty:
        print('Your selection does not have band and/or year data!')
        
    my_data = df_filtered
    data = pd.DataFrame(my_data.copy())
    
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values(by='DATE')
    data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    data = data.sort_values('MONTH')
    return data

def get_processing_data_year(data, year_type) -> pd.DataFrame:
    """Fetches and processes data for the specified band and year."""
    data = FT8DataFunctions()
    
    year_type = str(year_type).strip()
    
    # Parse to datetime/time with strict format validation
    data.df['TIME_ADL'] = pd.to_datetime(data.df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time

    # select the correct band and year
    mask = (data.df['YEAR'] == year_type)
    df_filtered = data.df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                                'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE','CALL','DISTANCE']]
    if df_filtered.empty:
        print('Your selection does not have band and/or year data!')
        
    my_data = df_filtered
    data = pd.DataFrame(my_data.copy())
    
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values(by='DATE')
    data['MONTH'] = pd.to_numeric(data['MONTH'], errors='coerce')
    data = data.sort_values('MONTH')
    return data


def main():
     """Main function to execute the data processing and visualization."""  
# This is the main function to execute the data processing and visualization

band_type, year_type = get_band_year()    
data = get_processing_data(data=None, band_type=band_type, year_type=year_type)
plot_3D_v1(data, band_type, year_type)
pass
SFI_plot_v1(data, year_type)
pass
k_index_date_plot_v1(data, year_type)
pass
A_index_plot_v1(data, year_type)
pass

#band_type, year_type = get_band_year()
#data = get_processing_data_year(data=None, year_type=year_type)
#print(data)




if __name__ == "__main__":
    main()

