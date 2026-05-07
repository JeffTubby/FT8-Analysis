# FT8_main_program_V2.2 - This program is the main program for the FT8 data analysis and visualization.
#  It imports the necessary libraries and functions, and then runs the main function which calls the drop down box function to select band and year, gets the data for the selected band and year, and then creates the line plot and mean line plot for the selected data.    

import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import pathlib
import sys
# Drop down box function to select band and year
from my_dropdown_box_func import my_drop_down_box as ddb

# FT8 data functions to get data for specific band and year, and to get all data for a specific band
from FT8_data_functions import get_my_data as gmd
from FT8_data_functions import get_my_band_all_data as gmbd

# FT8 plot functions to create line plot and mean line plot
from FT8_plot_functions import my_line_plot as mlpt
from FT8_plot_functions import my_mean_line_plot as mmlp


def main():  
# starts a drop down box function to select band and year
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")
    print(f"Band selected: {band_type}, Year selected: {year_type}")

# Call the function get_my_data with the correct parameters from my_FT8_functions.py
    data = gmd(band_type, year_type)

# Call the function my_line_plot_test from my_FT8_functions.py
    mlpt(band_type, year_type, data)

# Call the function my_mean_line_plot from my_mean_line_plot_function.py
    mmlp(band_type, year_type, data)
      
if __name__ == "__main__":
    sys.exit(main())
