import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime, argparse

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
#def main_SFI(years: tuple[str, ...] | None = None) -> None:

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

    year_type = "2024"
    
    data = get_data_for_year(year_type)
        
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(3,1, figsize=(4,8), sharex=True)
    ax1, ax2, ax3 = axes.flat
    ax1.set_title(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "SFI"]).reset_index(drop=True)
    ax1 = sns.scatterplot(x="DISTANCE", y="SFI", data=plot_data, label="SFI", color="green", s=25, edgecolor="black", ax=ax1)
    ax1.set_xlabel("DISTANCE", fontsize=10)
    ax1.set_ylabel("SFI", fontsize=10)
    ax1.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
   

    year_type = "2025"
        
    data = get_data_for_year(year_type)
    ax2.set_title(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "SFI"]).reset_index(drop=True)
    ax2 = sns.scatterplot(x="DISTANCE", y="SFI", data=plot_data, label="SFI", color="green", s=25, edgecolor="black", ax=ax2)
    ax2.set_xlabel("DISTANCE", fontsize=10)
    ax2.set_ylabel("SFI", fontsize=10)
    ax2.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
   
    year_type = "2026"
        
    data = get_data_for_year(year_type)
    ax3.set_title(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "SFI"]).reset_index(drop=True)
    ax3 = sns.scatterplot(x="DISTANCE", y="SFI", data=plot_data, label="SFI", color="green", s=25, edgecolor="black", ax=ax3)
    ax3.set_xlabel("DISTANCE", fontsize=10)
    ax3.set_ylabel("SFI", fontsize=10)
    ax3.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
    plt.show()        

# A_INDEX

    year_type = "2024"
    
    data = get_data_for_year(year_type)
        
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(3,1, figsize=(4,8), sharex=True)
    ax1, ax2, ax3 = axes.flat
    ax1.set_title(f"FT8 A_INDEX Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "A_INDEX"]).reset_index(drop=True)
    ax1 = sns.scatterplot(x="DISTANCE", y="A_INDEX", data=plot_data, label="SFI", color="red", s=25, edgecolor="black", ax=ax1)
    ax1.set_xlabel("DISTANCE", fontsize=10)
    ax1.set_ylabel("A_INDEX", fontsize=10)
    ax1.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
   

    year_type = "2025"
        
    data = get_data_for_year(year_type)
    ax2.set_title(f"FT8 A_INDEX Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "A_INDEX"]).reset_index(drop=True)
    ax2 = sns.scatterplot(x="DISTANCE", y="A_INDEX", data=plot_data, label="SFI", color="red", s=25, edgecolor="black", ax=ax2)
    ax2.set_xlabel("DISTANCE", fontsize=10)
    ax2.set_ylabel("A_INDEX", fontsize=10)
    ax2.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
   
    year_type = "2026"
        
    data = get_data_for_year(year_type)
    ax3.set_title(f"FT8 A_INDEX Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "A_INDEX"]).reset_index(drop=True)
    ax3 = sns.scatterplot(x="DISTANCE", y="A_INDEX", data=plot_data, label="SFI", color="red", s=25, edgecolor="black", ax=ax3)
    ax3.set_xlabel("DISTANCE", fontsize=10)
    ax3.set_ylabel("A_INDEX", fontsize=10)
    ax3.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
    plt.show()        

# K_INDEX
    
    year_type = "2024"
    
    data = get_data_for_year(year_type)
        
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(3,1, figsize=(4,8), sharex=True)
    ax1, ax2, ax3 = axes.flat
    ax1.set_title(f"FT8 K_INDEX Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "K_INDEX"]).reset_index(drop=True)
    ax1 = sns.scatterplot(x="DISTANCE", y="K_INDEX", data=plot_data, label="SFI", color="blue", s=25, edgecolor="black", ax=ax1)
    ax1.set_xlabel("DISTANCE", fontsize=10)
    ax1.set_ylabel("K_INDEX", fontsize=10)
    ax1.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
   

    year_type = "2025"
        
    data = get_data_for_year(year_type)
    ax2.set_title(f"FT8 K_INDEX Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "K_INDEX"]).reset_index(drop=True)
    ax2 = sns.scatterplot(x="DISTANCE", y="K_INDEX", data=plot_data, label="SFI", color="blue", s=25, edgecolor="black", ax=ax2)
    ax2.set_xlabel("DISTANCE", fontsize=10)
    ax2.set_ylabel("K_INDEX", fontsize=10)
    ax2.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
   
    year_type = "2026"
        
    data = get_data_for_year(year_type)
    ax3.set_title(f"FT8 K_INDEX Scatterplot for Year {year_type}", fontsize=10)

    plt.tight_layout(pad=3.0)
    #plt.suptitle(f"FT8 SFI Scatterplot for Year {year_type}", fontsize=12, y=1.02)
    plt.subplots_adjust(top=0.85)
    plot_data = data.dropna(subset=["DISTANCE", "K_INDEX"]).reset_index(drop=True)
    ax3 = sns.scatterplot(x="DISTANCE", y="K_INDEX", data=plot_data, label="SFI", color="blue", s=25, edgecolor="black", ax=ax3)
    ax3.set_xlabel("DISTANCE", fontsize=10)
    ax3.set_ylabel("K_INDEX", fontsize=10)
    ax3.legend(loc="upper left", fontsize=10, frameon=True, shadow=True, fancybox=True)
    plt.show()        


   
if __name__ == "__main__":
    main()          