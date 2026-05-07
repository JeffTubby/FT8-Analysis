#plot functions

from matplotlib import dates
import mplcursors


import mplcursors


def my_line_plot(band_type, year_type,data=None):
    """"Creates a line plot with subplots for the given data."""
    import seaborn as sns
    import matplotlib.pylab as plt
    
    #print(f"Creating line plot for {band_type} band in {year_type}...")
    #print(f"Data received for plotting: {data.head() if data is not None else 'No data provided'}")
    

    sns.set_style("whitegrid")
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Line plot on first subplot
    sns.lineplot(x='MONTH', y='RST_RCVD', data=data, label='RST Received', linestyle='dashed', errorbar=('ci', 20), ax=axes[0])
    sns.lineplot(x='MONTH', y='RST_SENT', data=data, label='RST Sent', linestyle='dotted', color='red', errorbar=('ci', 95), ax=axes[0])
    sns.lineplot(x='MONTH', y='A_INDEX', data=data, label='A Index', errorbar=('ci', 20), ax=axes[0])
    sns.lineplot(x='MONTH', y='K_INDEX', data=data, label='K Index', errorbar=('ci', 20), ax=axes[0])
    sns.lineplot(x='MONTH', y='SFI', data=data, label='SFI', errorbar=('ci', 20), ax=axes[0])
    axes[0].set_title(f'FT8 Analysis for {band_type} Band in {year_type}')
    axes[0].legend()

# Histogram plot on second subplot
    sns.histplot(x='MONTH', data=data, bins=12, color='lightblue', edgecolor='black', alpha=0.7, label='Number of Signals', ax=axes[1])
    axes[1].set_title('Signal Count by Month')
    axes[1].legend(loc='upper right')


    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return

def my_scatter_plot(band_type, year_type, data):
    """Creates a scatter plot for the given band and year using the provided data."""
    import seaborn as sns
    import matplotlib.pylab as plt
    
    sns.set_style("whitegrid")
    sns.scatterplot(x='MONTH', y='RST_RCVD', label='RST RCVD', color='red', data=data)
    sns.scatterplot(x='MONTH', y='RST_SENT', label='RST SENT', data=data)

    plt.title(f"Scatter Plot for {band_type} in {year_type}")
    plt.xlabel("MONTH")
    plt.ylabel("RST")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return


def my_mean_line_plot(band_type, year_type, data):
    """Creates a scatter plot for RST RCVD and RST SENT over the months for the specified band and year."""
    import pandas as pd
    import seaborn as sns
    import matplotlib.pylab as plt

    if data is None:
        raise ValueError("data cannot be None")

    df = pd.DataFrame(data)
    # Group by month and calculate the mean of both RST_RCVD and RST_SENT
    monthly_means = df.groupby('MONTH')[['RST_RCVD', 'RST_SENT']].mean().reset_index()

    # create line plot and scatter plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='MONTH', y='RST_RCVD', data=monthly_means, marker='o', label='Mean RST_RCVD', color='red')
    sns.lineplot(x='MONTH', y='RST_SENT', data=monthly_means, marker='o', color='green', label='Mean RST_SENT', linestyle='--')
    sns.scatterplot(x='MONTH', y='RST_RCVD', label='RST RCVD', color='red', data=data)
    sns.scatterplot(x='MONTH', y='RST_SENT', label='RST SENT', data=data, color='green')
    sns.set_style("whitegrid")
    plt.title(f'Monthly mean RST_RCVD and RST_SENT for {band_type} in {year_type}')
    plt.xlabel('Month')
    plt.ylabel('Mean RST value')
    plt.xticks(monthly_means['MONTH'])
    plt.legend()
    plt.grid()
    plt.show()
    return

def my_line_plot_band(band_type, year_type, data):
    """"Creates a line plot with subplots for the given data."""
    import seaborn as sns
    import matplotlib.pylab as plt
    import mplcursors
    
    sns.set_style("darkgrid")
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
# Line plot on first subplot
    sns.lineplot(x='MONTH', y='RST_RCVD', data=data, label='RST Received', linestyle='dashed', errorbar=('ci', 20), ax=axes[0])
    sns.lineplot(x='MONTH', y='RST_SENT', data=data, label='RST Sent', linestyle='dotted', color='red', errorbar=('ci', 95), ax=axes[0])
    sns.lineplot(x='MONTH', y='A_INDEX', data=data, label='A Index', errorbar=('ci', 20), ax=axes[0])
    sns.lineplot(x='MONTH', y='K_INDEX', data=data, label='K Index', errorbar=('ci', 20), ax=axes[0])
    sns.lineplot(x='MONTH', y='SFI', data=data, label='SFI', errorbar=('ci', 20), ax=axes[0])
    axes[0].set_title(f'FT8 Analysis for {band_type} Band')
    axes[0].legend()

# Histogram plot on second subplot
    sns.histplot(x='MONTH', data=data, bins=12, color='lightblue', edgecolor='black', alpha=0.7, label='Number of QSOs', ax=axes[1])
    axes[1].set_title('Signal Count by Month')
    axes[1].legend(loc='upper right')

    plt.xticks(rotation=45)
    plt.tight_layout()
    dates = ['DATE']
    values = ['DATE']
    plt.plot(dates,values)

    cursor = mplcursors.cursor(hover=True)

# Connect the "add" event to customize text
    plt.show()
    return
