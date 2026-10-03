# This script generates a bar plot showing the longest distance by date.
# Author: Jeff Tubbenhauer VK5IU
# Date: 18/06/2024

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FixedLocator
from pathlib import Path

# must have the data file longest_distance.xlsx in the specified path "data/longest_distance.xlsx"
DATA_FILE = Path("data/longest_distance.xlsx")
df = pd.read_excel(DATA_FILE)
df = df.rename(columns={'TIME ADL': 'TIME_ADL'})

# Load and preprocess the data
df['TIME_ADL'] = pd.to_datetime(
    df['TIME_ADL'].astype(str),
    format='%H:%M:%S',
    errors='coerce',
).dt.strftime('%H:%M')
df['CALL'] = df['CALL'].astype(str).str.strip()
df['BAND'] = df['BAND'].astype(str).str.strip()
df = df.dropna(subset=['LONGEST_DISTANCE'])
df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
df = df.set_index('DATE').sort_index().reset_index()
df = df.dropna(subset=['DATE'])
df['DATE'] = df['DATE'].dt.strftime('%d-%m-%Y')
data = df.copy()

# Create one bar per input row so bands sharing a date are not aggregated.
sns.set(style="darkgrid")
colors = sns.color_palette('viridis', n_colors=len(data))
ax = plt.subplots(figsize=(max(10, len(data) * 1.2), 6))[1]
bars = ax.bar(range(len(data)), data['LONGEST_DISTANCE'], color=colors)
for bar, (_, row) in zip(bars, data.iterrows()):
    label = f"{row['BAND']}\n{row['CALL']}\n{row['LONGEST_DISTANCE']:.0f}km\n{row['COUNTRY']}\n{row['TIME_ADL']}"
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
ax.set_xlabel('Chart 2: Longest Distance by Date', fontsize=12, fontweight='bold')
ax.set_ylabel('Longest Distance', fontsize=12, fontweight='bold')
ax.set_xticks(range(len(data)))
ax.set_xticklabels(data['DATE'])
#ax.set_title('Longest Distance Over Time')
ax.xaxis.set_major_locator(FixedLocator(ax.get_xticks()))
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10, fontweight='bold')
ax.yaxis.set_major_locator(FixedLocator(ax.get_yticks()))
ax.set_yticklabels(ax.get_yticklabels(), fontsize=10, fontweight='bold')
ax.figure.tight_layout()
plt.show()




