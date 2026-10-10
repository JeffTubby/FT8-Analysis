# drop down input function
# This module provides a function to create a drop-down box for selecting a band and/or year.   
# Usage:
#     my_band, my_year = my_drop_down_box(default_band="20m", default_year="2025")
#     print("Returned:", my_band, my_year)
# This module requires the `tkinter` library for the graphical interface.
# Environment variable `FT8_INTERACTIVE` can be set to control interactive mode.
# Author: Jeff Tubbenhauer VK5IU
# Version: 2.0 able hide band or year independently
# band_type, _ = ddb(default_band="20m", include_year=False)
#_, year_type = ddb(default_year="2025", include_band=False)

import os
import tkinter as tk

from tkinter import ttk

def my_drop_down_box(
    default_band=None,
    default_year=None,
    interactive=None,
    include_year=True,
    include_band=True,
):  # drop down box function
    # Set up the drop down box for band and year selection
    
    """Create a band/year, band-only, or year-only selector."""
    if not include_band and not include_year:
        raise ValueError("At least one of include_band or include_year must be True.")

    bands = ["6m", "10m", "12m", "15m", "17m", "20m", "30m", "40m", "80m"]
    years = [str(year) for year in range(2023, 2027)]

    if interactive is None:
        env_value = os.environ.get("FT8_INTERACTIVE")
        if env_value is None:
            interactive = True
        else:
            interactive = env_value.strip().lower() not in {"0", "false", "no", "off"}

    selected_band = default_band if default_band in bands else bands[0]
    selected_year = default_year if default_year in years else years[-1]

    if not interactive:
        return selected_band, selected_year

    try:
        root = tk.Tk()
    except tk.TclError:
        return selected_band, selected_year

    if include_band and include_year:
        root.title("Band & Year Selector")
        root.geometry("300x200")
    elif include_band:
        root.title("Band Selector")
        root.geometry("300x130")
    else:
        root.title("Year Selector")
        root.geometry("300x130")

    if include_band:
        band_label = tk.Label(root, text="Select Band:")
        band_label.pack(pady=5)
        band_dropdown = ttk.Combobox(root, values=bands)
        if default_band in bands:
            band_dropdown.current(bands.index(default_band))
        else:
            band_dropdown.current(0)
        band_dropdown.pack()
    else:
        band_dropdown = None

    if include_year:
        year_label = tk.Label(root, text="Select Year:")
        year_label.pack(pady=5)
        year_dropdown = ttk.Combobox(root, values=years)
        if default_year in years:
            year_dropdown.current(years.index(default_year))
        else:
            year_dropdown.current(len(years) - 1)
        year_dropdown.pack()
    else:
        year_dropdown = None

    result = {"band": selected_band, "year": selected_year}

    def select_and_close():
        selected_band = band_dropdown.get() if band_dropdown is not None else result["band"]
        selected_year = year_dropdown.get() if year_dropdown is not None else result["year"]
        if include_band and include_year:
            print(f"Selected Band: {selected_band}, Year: {selected_year}")
        elif include_band:
            print(f"Selected Band: {selected_band}")
        else:
            print(f"Selected Year: {selected_year}")

        result["band"] = selected_band
        result["year"] = selected_year
        print("Closing window, continuing script...")
        root.quit()

    button = tk.Button(root, text="Click to Continue", command=select_and_close)
    button.pack(pady=15)
    #   Ensure the window is brought to the front and focused before entering the main loop.
    root.update_idletasks()
    root.deiconify()
    root.lift()
    root.attributes("-topmost", True)
    root.after(100, lambda: root.attributes("-topmost", False))
    root.focus_force()
    root.mainloop()
    root.destroy()

    return result["band"], result["year"]


if __name__ == "__main__":
    my_band, my_year = my_drop_down_box(default_band="20m", default_year="2025")
    print("Returned:", my_band, my_year)
