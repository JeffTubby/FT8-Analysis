# This script generates line plots showing the Solar Flux Index (SFI) for each year.
# Author: Jeff Tubbenhauer VK5IU
# Date: 10/09/2026
# Version: 2.0
# Description: Generates line plots showing the Solar Flux Index (SFI) for each year.
# The line plots are generated using Seaborn and Matplotlib.

import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns
import matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime, argparse
import FT8_data_functions
from datetime import datetime
from FT8_data_functions import get_data_for_year as gdfy

def load_year_data(year_type: str) -> pd.DataFrame:
    """loads the data"""
    data = FT8_data_functions.get_data_for_year(year_type).copy()
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], format="%d-%m-%Y", errors='coerce')
    data = data.set_index('DATE').sort_index().reset_index()
    return data

def main():
    # Set the Seaborn style for the plots.
    # Define the years for which the SFI data will be plotted.
    sns.set_style("darkgrid")
    years = ("2024", "2025", "2026")
    fig, axes = plt.subplots(len(years), 1, figsize=(4, 8), sharex=False)

    for year_type, ax in zip(years, axes):
        data = load_year_data(year_type)
        sns.lineplot(
            x="DATE", y="SFI", data=data, marker="o", label="SFI",
            color="green", ax=ax,
        )
        ax.set_title(f"Show SFI by Date and Year for {year_type}", fontsize=10)
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))
        ax.set_xlabel("Date", fontsize=7)
        ax.set_ylabel("SFI", fontsize=10)
        ax.legend(loc="upper left")
        ax.grid(True)
        year_start = pd.Timestamp(f"{year_type}-01-01")
        ax.set_xlim(year_start, year_start + pd.DateOffset(years=1))

    fig.autofmt_xdate(rotation=30)
    cursor = mplcursors.cursor([line for ax in axes for line in ax.lines], hover=True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()          