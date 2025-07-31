import pandas as pd
import matplotlib.pyplot as plt

class HourlyPeakAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_excel(filepath)
        self._clean()

    def _clean(self):
        # Clean and prepare data
        self.df['Car rental stations'] = self.df['Car rental stations'].astype(str).str.strip()
        self.df['Car rental stations'] = self.df['Car rental stations'].fillna('Unknown')
        self.df['Start time'] = pd.to_datetime(self.df['Start time'], errors='coerce')
        self.df['hour'] = self.df['Start time'].dt.hour  # Extract hour of the day

    def get_hourly_usage(self, selected_spots):
        """
        Returns total ride counts per hour for the selected parking spots.
        """
        if not selected_spots:
            raise ValueError("selected_spots cannot be empty.")
        filtered_df = self.df[self.df['Car rental stations'].isin(selected_spots)]
        usage = filtered_df.groupby(['Car rental stations', 'hour']).size().reset_index(name='count')
        return usage

    def plot_hourly_usage(self, selected_spots, title='Hourly Usage per Parking Spot'):
        """
        Plots the total number of bike uses for each hour of the day.
        """
        usage = self.get_hourly_usage(selected_spots)

        plt.figure(figsize=(12, 6))
        for spot in selected_spots:
            spot_data = usage[usage['Car rental stations'] == spot]
            plt.plot(spot_data['hour'], spot_data['count'], marker='o', label=spot)

            # Add value labels to each point
            for _, row in spot_data.iterrows():
                plt.text(row['hour'], row['count'] + 0.5, str(row['count']),
                         ha='center', va='bottom', fontsize=8)

        plt.title(title)
        plt.xlabel("Hour of Day (0–23)")
        plt.ylabel("Number of Uses")
        plt.xticks(range(0, 24))
        plt.grid(True, axis='y', linestyle='--', alpha=0.5)
        plt.legend(title='Parking Spot')
        plt.tight_layout()
        plt.show()
