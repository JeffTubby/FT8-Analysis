import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime


# import sys
# import pandas as pd
# import matplotlib.pyplot as plt
# import pathlib
# import datetime as dt   
# import seaborn as sns
# import matplotlib.dates as mdates
# import sys
# import pandas as pd
from datetime import datetime
from FT8_data_functions import get_data_for_year as gdfy

from my_dropdown_box_func import my_drop_down_box as ddb


def load_year_data(year_type: int | str) -> pd.DataFrame:
    """Load all rows for the selected year."""
    year_value = str(year_type).strip()
    if not year_value:
        raise ValueError("Year selection is empty.")

    data = gdfy(year_value).copy()
    if data.empty:
        raise ValueError(f"No data available for year {year_value}")

    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.dropna(subset=['DATE']).sort_values('DATE').copy()
    return data

def RST_lineplot_by_year(data: pd.DataFrame, year_type: int | str) -> None:
    """Plot RST by year.""" 
    
    sns.set_style("darkgrid")
    plt.figure(figsize=(9,3))
    sns.lineplot(x='DATE', y='RST_SENT', data=data, label='RST_SENT', color='red', linestyle='dashed', errorbar=('ci', 95))
    sns.lineplot(x='DATE', y='RST_RCVD', data=data, label='RST_RCVD', color='blue', errorbar=('ci', 95))
    plt.title(f'Plot 2A FT8 RST Analysis for in Year {year_type}', fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('RST', fontsize=10)
    plt.gca().tick_params(axis='x', rotation=30)
    plt.legend(loc='upper left', prop={'size': 8, 'weight': 'bold'}
               , fontsize=10, title_fontsize=8, title='RST', frameon=True, shadow=True, fancybox=True, borderpad=1)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():

    # get data from box input
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}, Year selected: {year_type}")

    data = load_year_data(year_type)

    RST_lineplot_by_year(data, year_type)

       
 
if __name__ == "__main__":
    main()
