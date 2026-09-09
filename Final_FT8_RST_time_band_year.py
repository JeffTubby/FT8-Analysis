import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import mplcursors
import pandas as pd
import seaborn as sns

from my_dropdown_box_func import my_drop_down_box as ddb
from FT8_data_prep import prepare_time_adl_rst_plot_data
from FT8_data_prep import prepare_rst_long_data
from FT8_data_prep import prepare_mean_rst_line_data

def get_my_data_band_year(band_type, year_type): #gmd
    """Fetches and processes data for the specified band and year."""
    df = pd.read_excel('data/datasheet.xlsx', keep_default_na=False)
    df['BAND'] = df['BAND'].astype(str).str.strip()
    df['YEAR'] = df['YEAR'].astype(str).str.strip()
    df['A_INDEX'] = df['A_INDEX'].astype(str).str.strip()
    df['K_INDEX'] = df['K_INDEX'].astype(str).str.strip()
    df['SFI'] = df['SFI'].astype(str).str.strip()
    df['MONTH'] = df['MONTH'].astype(str).str.strip()
    df['TIME_ADL'] = df['TIME_ADL'].astype(str).str.strip()
    df['DISTANCE'] = df['DISTANCE'].astype(str).str.strip() 
    df['DATE'] = df['DATE'].astype(str).str.strip()
    df['CALL'] = df['CALL'].astype(str).str.strip()
    df['DISTANCE'] = pd.to_numeric(df['DISTANCE'], errors='coerce')
    df['SFI'] = pd.to_numeric(df['SFI'], errors='coerce')
    df['A_INDEX'] = pd.to_numeric(df['A_INDEX'], errors='coerce')
    df['K_INDEX'] = pd.to_numeric(df['K_INDEX'], errors='coerce')
    df['RST_SENT'] = pd.to_numeric(df['RST_SENT'], errors='coerce')
    df['RST_RCVD'] = pd.to_numeric(df['RST_RCVD'], errors='coerce')
    df['CONT'] = df['CONT'].astype('string').str.strip()
    df['COUNTRY'] = df['COUNTRY'].astype(str).str.strip()
    # Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time

    # select the correct band and year
    mask = (df['BAND'] == band_type) & (df['YEAR'] == year_type)
    df_filtered = df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                             'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE', 
                             'CALL','DISTANCE', 'CONT', 'COUNTRY']]
    if df_filtered.empty:
        print('Your selection does not have band and/or year data!')
        
    data = df_filtered.copy()
    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    data = data.sort_values(by='DATE')

    if data.empty:
        print('No data available for the selected band and year.')
        return None
    return data

def main():
    # Get data from box input.
    print("Running drop down box function to select band and year...")
    band_type, year_type = ddb(default_band="20m", default_year="2025")

    print(f"Band selected: {band_type}, Year selected: {year_type}")
    df = get_my_data_band_year(band_type, year_type)
    if df is None or df.empty:
        print("No rows available to plot.")
        return

    # You can add further processing or visualization of the data here
    plot_df = prepare_time_adl_rst_plot_data(df)
    if plot_df.empty:
        print("No valid RST rows available to plot.")
        return
    

    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 4))
    plt.title(f"Scatter Plot of TIME_ADL vs RST by {year_type} and {band_type}", fontsize=10)
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
        selection.annotation.set_text(
            f"BAND: {row['BAND']}\n"
            f"TIME_ADL: {row['TIME_ADL']:%H:%M:%S}\n"
            f"{row['RST_TYPE']}: {row['RST_VALUE']:.1f}"
        )
    
    plt.show()  

if __name__ == "__main__":
    main()
