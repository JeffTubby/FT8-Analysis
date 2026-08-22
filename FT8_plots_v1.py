#FT8_plots
import pandas as pd, sys, matplotlib.pyplot as plt, pathlib, datetime as dt, seaborn as sns, matplotlib.dates as mdates, numpy as np, mplcursors


def plot_3D(data, band_type, year_type)-> None:
    """Generate a 3D plot for the given data."""
    # 1. Create a figure and add a 3D subplot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(projection='3d')

    # Work with a safe plot size so the 3D bars line up with the selected rows
    plot_count = min(len(data), 16)
    plot_data = data.iloc[:plot_count].copy()

    # Make sure the requested series are numeric before assigning bar heights
    sfi = pd.to_numeric(plot_data['SFI'], errors='coerce').fillna(0).to_numpy(dtype=float)
    a_index = pd.to_numeric(plot_data['A_INDEX'], errors='coerce').fillna(0).to_numpy(dtype=float)
    k_index = pd.to_numeric(plot_data['K_INDEX'], errors='coerce').fillna(0).to_numpy(dtype=float)

    # Shared x/y base positions for the bar height series
    x = np.arange(plot_count)
    y = np.zeros(plot_count)
    z = np.zeros(plot_count)
    dx = np.ones(plot_count) * 0.4
    dy = np.ones(plot_count) * 0.4

    # 2. Construct the 3D bar plot with the requested metric heights
    ax.bar3d(x, y, z, dx, dy, a_index, color='tomato', shade=True)
    ax.bar3d(x, y + 1, z, dx, dy, k_index, color='skyblue', shade=True)
    ax.bar3d(x, y + 2, z, dx, dy, sfi, color='forestgreen', shade=True)

    # 3. Add descriptive labels
    ax.set_xlabel('Observation')
    ax.set_ylabel('Metric Group')
    ax.set_zlabel('Value')
    ax.set_title('FT8 A_INDEX / K_INDEX / SFI for Band: {} Year: {}'.format(band_type, year_type))
    ax.set_xticks(x)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(['A_INDEX', 'K_INDEX', 'SFI'])
    plt.show()


def SFI_plot(data, year_type) -> None:
    """Plot SFI by date."""
    sns.set_style("darkgrid")               
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.lineplot(x='DATE', y='SFI', data=data, marker='o', label='SFI', color='forestgreen', ax=ax)
    plt.title(f'Show SFI by Date and Year for {year_type}', fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.xlabel('Date', fontsize=7)
    plt.ylabel('SFI', fontsize=10)
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(title='SFI', title_fontsize='9', fontsize='7', loc='upper left', frameon=True, fancybox=True, shadow=True)
    cursor = mplcursors.cursor(hover=True)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
  

def k_index_date_plot(data, year_type) -> None:
    """Plot K_INDEX by date."""
    data.sort_values('K_INDEX', inplace=True)
    sns.set_style("darkgrid")               
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.lineplot(x='DATE', y='K_INDEX', data=data, marker='o', label='K_INDEX', color='skyblue', ax=ax)
    plt.title(f'Show K_INDEX by Date and Year for {year_type}', fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.xlabel('Date', fontsize=7)
    plt.ylabel('K_INDEX', fontsize=10)
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(loc='upper left')
    plt.grid(True)
    cursor = mplcursors.cursor(hover=True)
    plt.tight_layout()
    plt.show()

def A_index_plot(data, year_type) -> None:
    """Plot A_INDEX by date."""
    #plot A_INDEX  by date 
    sns.set_style("darkgrid")               
    fig, ax = plt.subplots( figsize=(7, 3))
    sns.lineplot(x='DATE', y='A_INDEX', data=data, marker='o', label='A_INDEX', color='red',ax=ax)
    plt.title(f'Show A_INDEX by Date and Year for {year_type}', fontsize=10)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.xlabel('Date', fontsize=7)
    plt.ylabel('A_INDEX', fontsize=10)
    plt.gcf().autofmt_xdate()
    plt.xticks(rotation=30)
    plt.legend(loc='upper left')
    plt.grid(True)
    cursor = mplcursors.cursor(hover=True)
    plt.tight_layout()
    plt.show()
   

def scatter_plot(data, band_type, year_type) -> None:
    """Generate a scatter plot for the given data."""
    sns.set_style("whitegrid")
    plt.figure(figsize=(6,4))
    #data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.scatterplot(x='DISTANCE', y='RST_SENT', data=data, label='RST_SENT', color='blue')
    sns.scatterplot(x='DISTANCE', y='RST_RCVD', data=data, label='RST_RCVD', color='red')
    plt.xlabel('MONTH', fontsize=7)
    plt.title(f'FT8 Distance/RST Monthly Analysis for {band_type} in Year {year_type}', fontsize=10)
    plt.xlabel('MONTH', fontsize=7) 
    plt.xlabel('DISTANCE', fontsize=7)
    plt.ylabel('RST', fontsize=10) 
    plt.xticks(rotation=30)
    plt.legend(loc='upper left', prop={'size': 14, 'weight': 'bold'})
    plt.grid(True)
    plt.tight_layout()
    dates = ['DATE']
    values = ['SFI']
    cursor = mplcursors.cursor(hover=True)
    plt.show()

def scatter_plot_monthly(data, band_type, year_type) -> None:
    """Generate a scatter plot for the given data."""
    sns.set_style("whitegrid")
    plt.figure(figsize=(6,4))
    #data['DATE'] = pd.to_datetime(data['DATE'], errors='coerce')
    sns.scatterplot(x='MONTH', y='RST_SENT', data=data, label='RST_SENT', color='blue')
    sns.scatterplot(x='MONTH', y='RST_RCVD', data=data, label='RST_RCVD', color='red')
    plt.title(f'FT8 Distance/RST Monthly Analysis for {band_type} in Year {year_type}', fontsize=10)
    plt.xlabel('MONTH', fontsize=7) 
    plt.title(f'FT8 Distance/RST MonthlyAnalysis for {band_type} in Year {year_type}')
    plt.xticks(rotation=30)
    plt.legend(loc='upper left', prop={'size': 14, 'weight': 'bold'})
    plt.grid(True)
    #dates = ['DATE']
    #values = ['SFI']
    cursor = mplcursors.cursor(hover=True)
    plt.show()

def multiple_plots_v1(data: pd.DataFrame, year_type: int | str) -> None:
    """Plot multiple charts for the given data."""
    # plot all charts together in one figure
    sns.set_style("darkgrid")
    monthly_data = data.copy()
    monthly_data['MONTH'] = pd.to_numeric(monthly_data['MONTH'], errors='coerce')
    monthly_data = monthly_data.dropna(subset=['MONTH']).copy()

    rst_data = data.copy()
    rst_data['DATE'] = pd.to_datetime(rst_data['DATE'], errors='coerce')
    mean_data = rst_data.groupby('DATE').agg({'RST_RCVD': 'mean', 'RST_SENT': 'mean'}).reset_index()

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    ax1, ax2, ax3, ax4 = axes.flat

    sns.lineplot(x='DATE', y='SFI', data=data, marker='o', label='SFI', color='green', ax=ax1)
    ax1.set_title(f'Plot 1A Show SFI by Date and Year for {year_type}', fontsize=10)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    ax1.set_xlabel('Date', fontsize=10)
    ax1.set_ylabel('SFI', fontsize=10)
    fig.autofmt_xdate()
    ax1.tick_params(axis='x', rotation=30)
    ax1.legend(loc='upper left')
    ax1.grid(True)

    sns.lineplot(x='MONTH', y='SFI', data=monthly_data, marker='o', label='SFI', color='green', ax=ax2)
    ax2.set_title(f'Plot 1B Monthly SFI for year {year_type}', fontsize=10)
    ax2.set_xlabel('Month', fontsize=10)
    ax2.set_ylabel('SFI', fontsize=10)
    ax2.legend(loc='upper left')
    ax2.grid(True)

    sns.lineplot(x='DATE', y='RST_SENT', data=rst_data, ax=ax3, label='RST_SENT', color='red', linestyle='dashed', errorbar=('ci', 95))
    sns.lineplot(x='DATE', y='RST_RCVD', data=rst_data, ax=ax3, label='RST_RCVD', color='blue', errorbar=('ci', 95))
    ax3.set_title(f'Plot 2A FT8 RST Analysis for in Year {year_type}', fontsize=10)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    ax3.set_xlabel('Date', fontsize=10)
    ax3.set_ylabel('RST', fontsize=10)
    ax3.tick_params(axis='x', rotation=30)
    ax3.legend(loc='upper left')
    ax3.grid(True)

    sns.lineplot(x='DATE', y='RST_SENT', data=mean_data, ax=ax4, label='Mean SENT_RST', color='red', linestyle='dashed', errorbar=('ci', 95))
    sns.lineplot(x='DATE', y='RST_RCVD', data=mean_data, ax=ax4, label='Mean RCVD_RST', color='blue', errorbar=('ci', 95))
    ax4.set_title(f'Plot 2B FT8 mean RST for in Year {year_type}', fontsize=10)
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    ax4.tick_params(axis='x', rotation=30)
    ax4.legend(loc='upper left')
    ax4.grid(True)

    plt.tight_layout()
    plt.show()    
