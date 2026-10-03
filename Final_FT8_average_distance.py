# This script generates a bar plot showing the average distance by band.
# Author: Jeff Tubbenhauer VK5IU
# Date: 18/06/2024

import pandas as pd
import sys
from matplotlib.ticker import FixedLocator
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path("data/datasheet.xlsx")

def get_all_data():
    """Load only the band and distance columns from the data file."""

    df = pd.read_excel(DATA_FILE)
    df['BAND'] = df['BAND'].astype(str).str.strip()
    df['DISTANCE'] = df['DISTANCE'].astype(float).round(2)
    df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%m-%Y', errors='coerce')
    df = df.dropna(subset=['DATE'])
    df = df.dropna(subset=['BAND', 'DISTANCE'])
    #df = df.sort_values(by='DATE')
    df = df.sort_values(by='BAND')
    return df[['DATE', 'BAND', 'DISTANCE']].copy()


def main():
    df = get_all_data()
        
    sns.set(style="darkgrid")
    plt.figure(figsize=(7,5.5))
    average_distance = (
        df.groupby('BAND', as_index=False)['DISTANCE']
        .mean()
        .rename(columns={'DISTANCE': 'average_distance'})
    )
    
    #band_order = ['6m'] + sorted(
    #    (band for band in average_distance['BAND'] if band != '6m'),
    #    key=lambda band: int(band.rstrip('m')),
    #)
    #average_distance['BAND'] = pd.Categorical(
    #    average_distance['BAND'], categories=band_order, ordered=True
    #)
    average_distance = average_distance.sort_values('BAND')
    ax = sns.barplot(
        data=average_distance,
        x='BAND',
        y='average_distance',
        hue='BAND',
        width=0.5,
        palette='viridis',
        legend=False,
    )
    for bar, (_, row) in zip(ax.patches, average_distance.iterrows()):
        label = f"{row['average_distance']:.2f} km"
        ax.annotate(
            label,
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight='bold',
            color='red',
        )
    plt.title('Chart 1: Average Distance by Band', fontsize=12, fontweight='bold')
    plt.xlabel('Band', fontsize=12, fontweight='bold')
    plt.ylabel('Average distance (km)', fontsize=12, fontweight='bold')
    plt.gca().xaxis.set_major_locator(FixedLocator(ax.get_xticks()))
    plt.gca().set_xticklabels(ax.get_xticklabels(), rotation=0, ha='right', fontsize=10, fontweight='bold')
    plt.gca().yaxis.set_major_locator(FixedLocator(ax.get_yticks()))
    plt.gca().set_yticklabels(ax.get_yticklabels(), fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()