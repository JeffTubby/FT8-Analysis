# drop down input function
# This module provides a function to create a dropdown box for selecting a band and year.       
# Usage:
# from my_dropdown_box_func import my_drop_down_box as ddb
# band, year = ddb(default_band="20m", default_year="2025")
#   to run the function, simply call it with optional default_band and default_year arguments.
# Author: Jeff Tubbenhauer VK5IU
# Date: 18/06/2024


import tkinter as tk
from tkinter import ttk
# Initialize the main window

def my_drop_down_box(default_band=None, default_year=None): # as ddb
    """Creates a dropdown box for selecting a band and year, then returns the selected values."""
    root = tk.Tk()
    root.title("Band & Year Selector")
    root.geometry("300x200")
    root.minsize(300, 200)

    # Bands and years for the dropdown options
    bands = ["6m","10m","12m","15m","17m","20m","30m","40m","80m"]
    years = [str(year) for year in range(2023, 2027)]

    selected_band = default_band if default_band in bands else bands[0]
    selected_year = default_year if default_year in years else years[-1]

    # --- Dropdown 1: Band ---
    band_label = tk.Label(root, text="Select Band:")
    band_label.pack(pady=5)
    band_dropdown = ttk.Combobox(root, values=bands, state="readonly")
    band_dropdown.set(selected_band)
    band_dropdown.pack()

    # --- Dropdown 2: Year ---
    year_label = tk.Label(root, text="Select Year:")
    year_label.pack(pady=5)
    year_dropdown = ttk.Combobox(root, values=years, state="readonly")
    year_dropdown.set(selected_year)
    year_dropdown.pack()

    result = {"band": selected_band, "year": selected_year}

    def select_and_close():
        selected_band = band_dropdown.get() or result["band"]
        selected_year = year_dropdown.get() or result["year"]
        print(f"Selected Band: {selected_band}, Year: {selected_year}")

        result["band"] = selected_band
        result["year"] = selected_year

        print("Closing window, continuing script...")
        root.destroy()

    def on_close():
        result["band"] = selected_band
        result["year"] = selected_year
        print("Window closed without selection; using defaults.")
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    button = tk.Button(root, text="Click to Continue", command=select_and_close)
    button.pack(pady=15)

    root.mainloop()
    return result["band"], result["year"]


if __name__ == "__main__":
    my_band, my_year = my_drop_down_box(default_band="20m", default_year="2025")

    
    #band_type, year_type = my_drop_down_box()
   # print("Returned:", band_type, year_type)
    