# This script loads FT8 data for different bands and years, validates it, and plots RST_SENT over time.
import sys
import pathlib
import datetime as dt
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import FT8_data_functions
import my_dropdown_box_func

from FT8_data_functions import get_my_data as gmyd
from my_dropdown_box_func import my_drop_down_box as ddb

def load_year_data(year_type: str) -> pd.DataFrame:
    """loads the data"""
    data = gmyd("20m", year_type).copy()  # Assuming "20m" as the default band for year data
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.set_index('DATE').sort_index().reset_index()
    return data




def main():
    # get data from box input
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}, Year selected: {year_type}")

    df = load_year_data(year_type)

    
    # Compare the sent and received reports for each contact.
    plot_data = df[['RST_SENT', 'RST_RCVD']].apply(
        pd.to_numeric, errors='coerce'
    ).dropna()
    if plot_data.empty:
        raise ValueError("No numeric RST_SENT/RST_RCVD pairs are available to plot.")

    limits = (
        min(plot_data.min()),
        max(plot_data.max()),
    )
    plt.figure(figsize=(5, 5))
    points = plt.scatter(
        plot_data['RST_SENT'],
        plot_data['RST_RCVD'],
        color='0.35',
        alpha=0.65,
        s=32,
        edgecolors='white',
        linewidths=0.5,
        label='Contacts',
    )
    plt.plot(limits, limits, color='black', linestyle='--', label='Equal reports')
    plt.xlim(limits)
    plt.ylim(limits)
    plt.grid(True)
    plt.xlabel('RST_SENT', color='green')
    plt.ylabel('RST_RCVD', color='red')
    plt.tick_params(axis='x', colors='green')
    plt.tick_params(axis='y', colors='red')
    plt.title(f'{band_type} sent vs received RST for {year_type}')
    plt.legend(loc='upper left')
    # Click a dot to pin its label; labels stay until removed (right-click or Delete key on the label).
    cursor = mplcursors.cursor(points, hover=False, multiple=True)

    @cursor.connect("add")
    def show_values(sel):
        row = plot_data.iloc[sel.index]
        sel.annotation.set_text(
            f"RST_SENT: {row['RST_SENT']:g}\nRST_RCVD: {row['RST_RCVD']:g}"
        )

    plt.show()

if __name__ == "__main__":
    main()