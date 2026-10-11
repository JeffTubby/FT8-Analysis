# Author: Jeff Tubbenhauer VK5IU
# Date: 11/10/2026
# Version: 1.0
# Description: This script generates scatter plots of RST values over local time
# (TIME_ADL) for a selected FT8 band across all years.
# The script uses Seaborn for plotting and mplcursors for interactive annotations.
# Usage:
#   Run this script and select the desired FT8 band from the drop-down box.
#   The script will generate a scatter plot of RST values over local time for
#   the selected band across all years.

import sys
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import mplcursors
import pandas as pd
import seaborn as sns
import FT8_data_functions

from FT8_data_functions import get_my_band_all_data as gmdad
from my_dropdown_box_func import my_drop_down_box as ddb

# Import the necessary functions from the Final_FT8_data_prep module.
# These functions are used to prepare the data for plotting RST values over time.
from Final_FT8_data_prep import prepare_time_adl_rst_plot_data
from Final_FT8_data_prep import prepare_rst_long_data
from Final_FT8_data_prep import prepare_mean_rst_line_data

def load_band_data(band_type: str) -> pd.DataFrame:
    """Load data for the selected band across all years."""
    data = gmdad(band_type).copy()
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.set_index('DATE').sort_index().reset_index()
    return data


def main():
    # get data from box input
    print("Running drop down box function to select a band...")
    band_type, _ = ddb(default_band="20m", include_year=False)
    print(f"Band selected: {band_type} (all years)")

    df = load_band_data(band_type)
    assert not df.empty, "DataFrame is empty"

    # Prepare the data for plotting RST values over local time (TIME_ADL)
    plot_df = prepare_time_adl_rst_plot_data(df)
    if plot_df.empty:
        print("No valid RST rows available to plot.")
        return

    # Create the scatter plot for RST values over local time (TIME_ADL)
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 4))
    plt.title(f"Scatter Plot of TIME_ADL vs RST for {band_type} (all years)", fontsize=10)
    sns.scatterplot(
        data=plot_df,
        x='TIME_ADL',
        y='RST_VALUE',
        hue='RST_TYPE',
        style='RST_TYPE',
        palette={'RST_SENT': '#1f77b4', 'RST_RCVD': '#d62728'},
        ax=ax
    )
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.ylabel('RST Values')
    plt.xlabel('Local Time (TIME_ADL)')
    plt.legend(loc='upper left', fontsize=10, frameon=True, shadow=True, fancybox=True)
    plt.tight_layout()
    cursor = mplcursors.cursor(ax, hover=True)

    @cursor.connect("add")
    def show_date_and_sfi(selection):
        row = plot_df.iloc[selection.index]
        date_value = row.get('DATE')
        sfi_value = row.get('SFI')
        date_text = "DATE: N/A" if pd.isna(date_value) else f"DATE: {pd.Timestamp(date_value).strftime('%Y-%m-%d')}"
        sfi_text = "SFI: N/A" if pd.isna(sfi_value) else f"SFI: {sfi_value}"
        selection.annotation.set(text=f"{date_text}\n{sfi_text}")
        selection.annotation.get_bbox_patch().set(fc="white")
        selection.annotation.get_bbox_patch().set(alpha=0.9)
        selection.annotation.get_bbox_patch().set_edgecolor("black")
        selection.annotation.get_bbox_patch().set_linewidth(1)
        selection.annotation.get_bbox_patch().set_boxstyle("round,pad=0.3")
    plt.show()        
if __name__ == "__main__":
    main()