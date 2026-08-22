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
from FT8_plots_v1 import multiple_plots_v1 as multiple_plots_v1


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



def main():

    # get data from box input
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}, Year selected: {year_type}")

    data = load_year_data(year_type)

    multiple_plots_v1(data, year_type)
    sys.exit()


   
 
if __name__ == "__main__":
    main()
