 # drop down input function


import tkinter as tk
from tkinter import ttk
from FT8_settings import get_settings as gs

def my_drop_down_box(default_band=None, default_year=None):
    """Creates a dropdown box for selecting a band and year, then returns the selected values. """
    root = tk.Tk()
    root.title("Band & Year Selector")
    root.geometry("300x200")
    root.title("Band and Year")

    # Bands and years for the dropdown options from settings
    bands = gs(settings=None)['bands']
    years = gs(settings=None)['years']

    # --- Dropdown 1: Band ---
    band_label = tk.Label(root, text="Select Band:")
    band_label.pack(pady=5)
    band_dropdown = ttk.Combobox(root, values=bands)
    if default_band in bands:
        band_dropdown.current(bands.index(default_band))
    else:
        band_dropdown.current(0)
    band_dropdown.pack()

    # --- Dropdown 2: Year ---
    year_label = tk.Label(root, text="Select Year:")
    year_label.pack(pady=5)
    year_dropdown = ttk.Combobox(root, values=years)
    if default_year in years:
        year_dropdown.current(years.index(default_year))
    else:
        year_dropdown.current(len(years) - 1)
    year_dropdown.pack()

    result = {"band": None, "year": None}

    def select_and_close():
        selected_band = band_dropdown.get()
        selected_year = year_dropdown.get()
        print(f"Selected Band: {selected_band}, Year: {selected_year}")

        result["band"] = selected_band
        result["year"] = selected_year

        print("Closing window, continuing script...")
        root.quit()

    button = tk.Button(root, text="Click to Continue", command=select_and_close)
    button.pack(pady=15)

    root.mainloop()
    root.destroy()

    return result["band"], result["year"]


if __name__ == "__main__":
    band_type, year_type = my_drop_down_box()
    print("Returned:", band_type, year_type)
    