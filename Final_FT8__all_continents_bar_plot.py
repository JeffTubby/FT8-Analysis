import pandas as pd, sys, matplotlib.pyplot as plt, pathlib
import datetime as dt, seaborn as sns, matplotlib.dates as mdates, mplcursors, numpy as np, datetime as datetime, argparse

from datetime import datetime
from my_dropdown_box_func import my_drop_down_box as ddb

def get_all_data():
    """Fetches and processes all data."""
    Path = pathlib.Path('data/datasheet.xlsx')   
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
    df['CONT'] = df['CONT'].astype('string').str.strip()
    df['COUNTRY'] = df['COUNTRY'].astype(str).str.strip()
    #df["CONT"] = df["CONT"].replace("AN", "NA")


# Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time
    data = pd.DataFrame(df.copy())

    return data

def main():
   
    df = get_all_data()
            
    df['CONT']
    #print(df['CONT'].value_counts())
    
    if df is not None:
        qso_cont = df["CONT"].value_counts().to_dict()
        
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=100)
    sns.barplot(x=list(qso_cont.keys()), y=list(qso_cont.values()),
                palette=sns.color_palette("Set2", len(qso_cont)), ax=ax)
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', padding=3)
    ax.set_title("Total QSO Counts by Continent") 
    plt.xlabel("Continent")
    plt.ylabel("QSO Counts")    
    plt.tight_layout()
    plt.show()

    
    
if __name__ == "__main__":
    main()