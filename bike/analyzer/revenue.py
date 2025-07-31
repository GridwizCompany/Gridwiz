
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class RevenueTrendAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)
        self._clean()

    def _clean(self):
        self.df.columns = self.df.columns.str.strip()
        self.df['Car rental stations'] = self.df['Car rental stations'].astype(str).str.strip()
        self.df['Car rental stations'] = self.df['Car rental stations'].fillna("Unknown")

    def total_revenue_by_spot(self, selected_spots=None):
        if 'Actual amount' not in self.df.columns:
            raise ValueError("Kolom 'Actual amount' tidak ditemukan.")
        df_filtered = self.df
        if selected_spots:
            df_filtered = df_filtered[df_filtered['Car rental stations'].isin(selected_spots)]
        return df_filtered.groupby('Car rental stations')['Actual amount'].sum().sort_values(ascending=False)

    def plot_revenue_by_spot(self, selected_spots=None, title='Total Revenue per Parking Spot'):
        revenue = self.total_revenue_by_spot(selected_spots)

        norm = plt.Normalize(revenue.min(), revenue.max())
        cmap = plt.cm.get_cmap('RdYlGn')
        colors = cmap(norm(revenue.values))

        plt.figure(figsize=(14, 8))
        bars = plt.bar(revenue.index, revenue.values, color=colors)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 5000, f"{int(yval):,}", ha='center', va='bottom', fontsize=9)

        plt.title(title, fontsize=14)
        plt.xlabel("Parking Spot", fontsize=12)
        plt.ylabel("Total Revenue (Rp)", fontsize=12)
        plt.xticks(rotation=35, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
