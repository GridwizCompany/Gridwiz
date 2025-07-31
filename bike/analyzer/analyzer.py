import pandas as pd
import matplotlib.pyplot as plt

class BikeUsageAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_excel(filepath)
        self._clean_data()

    def _clean_data(self):
        self.df['Car rental stations'] = self.df['Car rental stations'].astype(str).str.strip()
        self.df['Start time'] = pd.to_datetime(self.df['Start time'], errors='coerce')
        self.df['Car rental stations'] = self.df['Car rental stations'].fillna('Unknown')

    def get_all_parking_spots(self):
        return self.df['Car rental stations'].unique().tolist()

    def filter_by_spots(self, selected_spots):
        return self.df[self.df['Car rental stations'].isin(selected_spots)]

    def count_usage(self, selected_spots):
        filtered_df = self.filter_by_spots(selected_spots)
        return filtered_df['Car rental stations'].value_counts().sort_values(ascending=False)

    def plot_usage(self, selected_spots, title='Total Penggunaan (Filtered)'):
        usage_counts = self.count_usage(selected_spots)
        plt.figure(figsize=(10, 6))
        ax = usage_counts.plot(kind='bar', color='mediumseagreen')

        for i, value in enumerate(usage_counts.values):
            ax.text(i, value + 0.5, str(value), ha='center', va='bottom', fontsize=10)

        plt.title(title)
        plt.xlabel('Parking Spot')
        plt.ylabel('Jumlah Penggunaan')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
