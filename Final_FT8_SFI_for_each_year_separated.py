import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime, argparse
import FT8_data_functions
from datetime import datetime
from FT8_data_functions import get_data_for_year as gdfy

def load_year_data(year_type: str) -> pd.DataFrame:
    """loads the data"""
    df = FT8_data_functions.get_data_for_year(year_type).copy()
    # sort date from earliest to latest
    df['DATE'] = pd.to_datetime(df['DATE'], format="%d-%m-%Y", errors='coerce')
    df = df.set_index('DATE').sort_index().reset_index()
    return df

def main():
   
    year_type = "2024"
    data = load_year_data(year_type)
    #sns.set("paper")
    sns.set_style("darkgrid")
    plt.figure(figsize=(5, 3))
    plt.title(f"Plot 2A:Scatter Plot of DISTANCE vs SFI for {year_type}")
    sns.scatterplot(data=data, x='DISTANCE', y='SFI', color='green')  # Replace 'VALUE' with the actual column name you want to plot
    plt.xlabel("DISTANCE")
    plt.ylabel("SFI")   
    plt.tight_layout()
    plt.show()

    year_type = "2025"
    data = load_year_data(year_type)
    #sns.set("paper")
    sns.set_style("darkgrid")
    plt.figure(figsize=(5,3))
    plt.title(f"Plot 2A:Scatter Plot of DISTANCE vs SFI for {year_type}")
    sns.scatterplot(data=data, x='DISTANCE', y='SFI', color='green')  # Replace 'VALUE' with the actual column name you want to plot
    plt.xlabel("DISTANCE")
    plt.ylabel("SFI")   
    plt.tight_layout()
    plt.show()

    year_type = "2026"
    data = load_year_data(year_type)
    #sns.set("paper")
    sns.set_style("darkgrid")
    plt.figure(figsize=(5,3))
    plt.title(f"Plot 2A:Scatter Plot of DISTANCE vs SFI for {year_type}")
    sns.scatterplot(data=data, x='DISTANCE', y='SFI', color='green')  # Replace 'VALUE' with the actual column name you want to plot
    plt.xlabel("DISTANCE")
    plt.ylabel("SFI")   
    plt.tight_layout()
    plt.show()
              
   
if __name__ == "__main__":
    main()