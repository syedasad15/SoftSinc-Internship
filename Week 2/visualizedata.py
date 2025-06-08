import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_data(df):
    os.makedirs('plots', exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.figure(figsize=(8, 5))
    if 'species' in df.columns:
        sns.countplot(data=df, x='species', order=df['species'].value_counts().index)
        plt.title('Category-wise Counts')
        plt.xlabel('Species')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        barplot_filename = f"plots/barplot_species_counts_{timestamp}.png"
        plt.savefig(barplot_filename)
        plt.close()
    else:
        print("Column 'species' not found for bar plot.")
    if 'sepal_length' in df.columns:
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df.reset_index(), x='index', y='sepal_length', marker='o')
        plt.title('Sepal Length Trend Over Row Index')
        plt.xlabel('Row Index')
        plt.ylabel('Sepal Length')
        plt.tight_layout()
        lineplot_filename = f"plots/lineplot_sepal_length_{timestamp}.png"
        plt.savefig(lineplot_filename)
        plt.close()
    else:
        print("Column 'sepal_length' not found for line plot.")

    if 'sepal_length' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(data=df, x='sepal_length', bins=20, kde=True)
        plt.title('Sepal Length Distribution')
        plt.xlabel('Sepal Length')
        plt.ylabel('Frequency')
        plt.tight_layout()
        hist_filename = f"plots/hist_sepal_length_{timestamp}.png"
        plt.savefig(hist_filename)
        plt.close()
    else:
        print("Column 'sepal_length' not found for histogram.")

    print(f"Plots saved with timestamp {timestamp} in 'plots/' folder.")

