import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt
import seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime

from datetime import datetime
def get_data_for_year(year_type):
    """data for each year"""
    Path = pathlib.Path('data/datasheet.xlsx')
    df = pd.read_excel('data/datasheet.xlsx')
    df['BAND'] = df['BAND'].astype(str).str.strip()
    df['YEAR'] = df['YEAR'].astype(str).str.strip()
    df['A_INDEX'] = df['A_INDEX'].astype(float)
    df['K_INDEX'] = df['K_INDEX'].astype(float)
    df['SFI'] = df['SFI'].astype(float)
    df['MONTH'] = df['MONTH'].astype(str).str.strip()
    df['SFI'] = df['SFI'].astype(float)
    df['DISTANCE'] = df['DISTANCE'].astype(float)
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
    #data=data.sort_values('SFI')
    return data
    """Plot SFI by date."""

def SFI_plot_combined(data, year_type, ax=None, show=True) -> None:
    sns.set_style("darkgrid")
    plt.figure(figsize=(6,4))   
    plot_data = data.dropna(subset=["DISTANCE", "SFI"]).reset_index(drop=True)
    ax = sns.scatterplot(x="DISTANCE", y="SFI", data=plot_data, label="SFI", color="red", s=25, edgecolor="black")
    plt.title(f"Plot 1C FT8 SFI Scatterplot for Year {year_type}", fontsize=10)
    plt.xlabel("DISTANCE", fontsize=10)
    plt.ylabel("SFI", fontsize=10)
    plt.xticks(rotation=30)
    plt.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)

    cursor = mplcursors.cursor(ax, hover=True)

    @cursor.connect("add")
    def show_date_and_sfi(selection):
        row = plot_data.iloc[selection.index]
        selection.annotation.set_text(
            f"DATE: {row['DATE']}\n"
            f"SFI: {row['SFI']:.1f}"
        )
    plt.show()

 

def main():
     
    # Call the function get_for_year with the correct parameters from get_data_for_year.py
    # SFI Plot for each year
    years = ["2024", "2025", "2026"]
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(len(years), 1, figsize=(4, 8), sharex=True)
    for axis, year_type in zip(axes, years):
        data = get_data_for_year(year_type)
        sns.scatterplot(data=data, x='DISTANCE', y='SFI', ax=axis, label='SFI', color='green', s=25, edgecolor='black')
        axis.set_title(
            f'PLOT 1 Scatterplot of DISTANCE vs SFI for {year_type} year',
            fontsize=8, weight='bold'
        )
        axis.set_xlabel('DISTANCE', fontsize=8, weight='bold')
        axis.set_ylabel('SFI', fontsize=8, weight='bold')
        axis.legend(loc='upper left', fontsize=8, title_fontsize=8, frameon=True, fancybox=True, shadow=True)
    fig.tight_layout()
    plt.show()

    # Call the function get_for_year with the correct parameters from get_data_for_year.py
    # A_INDEX Plot for each year
    
    years = ["2024", "2025", "2026"]
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(len(years), 1, figsize=(4, 8), sharex=True)
    for axis, year_type in zip(axes, years):
        data = get_data_for_year(year_type)
        sns.scatterplot(data=data, x='DISTANCE', y='A_INDEX', ax=axis, label='A_INDEX', color='red', s=25, edgecolor='black')
        axis.set_title(
            f'PLOT 2 Scatterplot of DISTANCE vs A_INDEX for {year_type} year',
            fontsize=8, weight='bold'
        )
        axis.set_xlabel('DISTANCE', fontsize=8, weight='bold')
        axis.set_ylabel('A_INDEX', fontsize=8, weight='bold')
        axis.legend(loc='upper left', fontsize=8, title_fontsize=8, frameon=True, fancybox=True, shadow=True)
    fig.tight_layout()
    plt.show()

    # Call the function get_for_year with the correct parameters from get_data_for_year.py
    # K_INDEX Plot for each year
   
    years = ["2024", "2025", "2026"]
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(len(years), 1, figsize=(4, 8), sharex=True)
    for axis, year_type in zip(axes, years):
        data = get_data_for_year(year_type)
        sns.scatterplot(data=data, x='DISTANCE', y='K_INDEX', ax=axis, label='K_INDEX', color='Blue', s=25, edgecolor='black')
        axis.set_title(
            f'PLOT 3 Scatterplot of DISTANCE vs K_INDEX for {year_type} year',
            fontsize=8, weight='bold'
        )
        axis.set_xlabel('DISTANCE', fontsize=8, weight='bold')
        axis.set_ylabel('K_INDEX', fontsize=8, weight='bold')
        #axis.legend(title='K_INDEX', fontsize=8, title_fontsize=8, loc='upper left', frameon=True, fancybox=True, shadow=True)
        axis.legend(loc="upper left", fontsize=8, frameon=True, shadow=True, fancybox=True)
    fig.tight_layout()
    plt.show()
    

   
if __name__ == "__main__":
    main()          