# This module contains functions to get the specific data
import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors

class FT8DataFunctions:
    """Class-based wrapper for FT8 data functions."""
    def __init__(self, year_type: int | str | None = None, band_type: str = "20m"):
        self.data_path = 'data/datasheet.xlsx'
        self.df = pd.read_excel(self.data_path)
        self.df['BAND'] = self.df['BAND'].astype(str).str.strip()
        self.df['YEAR'] = self.df['YEAR'].astype(str).str.strip()
        self.df['A_INDEX'] = self.df['A_INDEX'].astype(float)
        self.df['K_INDEX'] = self.df['K_INDEX'].astype(float)
        self.df['SFI'] = self.df['SFI'].astype(float)
        self.df['MONTH'] = self.df['MONTH'].astype(str).str.strip()
        self.df['TIME_ADL'] = pd.to_datetime(self.df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time
        self.df['DISTANCE'] = pd.to_numeric(self.df['DISTANCE'], errors='coerce')
        self.df['DISTANCE'] = self.df['DISTANCE'].astype(float)
        self.df['SFI'] = self.df['SFI'].astype(float)    
        self.df['DATE'] = pd.to_datetime(self.df['DATE'], errors='coerce')
        self.df['CALL'] = self.df['CALL'].astype(str).str.strip()    
        self.data = self.df
        self.band_type = None
        self.year_type = None
        self.filtered_data = None
        self.band_type = band_type
        self.year_type = year_type
        self.data = None
        self.filtered_data = None
     

