import pandas as pd, seaborn as sns, matplotlib.pylab as plt, pathlib, sys, datetime
from datetime import datetime as dt

# get data from PythonData17326.xlsx
def get_my_band_all_data(band_type, year_type):
    """Fetches and processes data for the specified band and year."""
    Path = pathlib.Path('data/datasheet.xlsx')   
    df = pd.read_excel('data/datasheet.xlsx')
    df['BAND'] = df['BAND'].astype(str).str.strip()
    df['YEAR'] = df['YEAR'].astype(str).str.strip()
    df['A_INDEX'] = df['A_INDEX'].astype(str).str.strip()
    df['K_INDEX'] = df['K_INDEX'].astype(str).str.strip()
    df['SFI'] = df['SFI'].astype(str).str.strip()
    df['MONTH'] = df['MONTH'].astype(str).str.strip()
    df['TIME_ADL'] = df['TIME_ADL'].astype(str).str.strip()
    df['DATE'] = df['DATE'].astype(str).str.strip()

    # select the correct year
    mask = (df['YEAR'] == year_type)
   
    # Parse to datetime/time with strict format validation
    df['TIME_ADL'] = pd.to_datetime(df['TIME_ADL'], format='%H:%M:%S', errors='coerce').dt.time

    df_filtered = df.loc[mask, ['BAND', 'MONTH', 'RST_RCVD', 'RST_SENT',
                             'A_INDEX', 'K_INDEX', 'SFI','TIME_ADL','DATE','YEAR']]

    my_data = df_filtered   
    data =my_data.copy()

    # sort date from earliest to latest
    data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    #data = data.sort_values('DATE')
    
    #format date to d%-m-%Y
    data['DATE'] = data['DATE'].dt.strftime('%d-%m-%Y')
    return data

def main():  
    
    #band_type = "20m"
    
    # Call the function get_my_band_all_data with the correct parameters from get_band_all_data.py
    years = ["2024", "2025", "2026"]
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(len(years), 1, figsize=(6, 9), sharex=True)

    for axis, year_type in zip(axes, years):
        data = get_my_band_all_data(None, year_type)
        sns.histplot(data=data, x='RST_SENT', bins=20, kde=True, ax=axis,
                     label='RST_SENT')
        sns.histplot(data=data, x='RST_RCVD', bins=20, kde=True, color='orange',
                     ax=axis, label='RST_RCVD')
        axis.set_title(
            f'Histogram of RST_SENT/RST_RCVD for {year_type} year',
            fontsize=10,
        )
        axis.set_xlabel('RST_SENT and RST_RCVD', fontsize=8)
        axis.set_ylabel('Count', fontsize=8)
        axis.legend(title='RST Sent/Received', fontsize=8, title_fontsize=8, loc='upper left', frameon=True, fancybox=True, shadow=True)


    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    sys.exit(main())
