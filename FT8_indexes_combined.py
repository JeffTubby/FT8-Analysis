import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime

from datetime import datetime

# create line plot with subplot for both series

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

def main():

    year_type = "2024"
    
    data = get_data_for_year(year_type)
    
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
if __name__ == "__main__":
    main()          