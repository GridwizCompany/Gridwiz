from Gridwiz.bike.analyzer.analyzer import BikeUsageAnalyzer
from Gridwiz.bike.analyzer.revenue import RevenueTrendAnalyzer

# Analisis penggunaan sepeda
bike = BikeUsageAnalyzer("data.xlsx")
bike.plot_usage(["Gridwiz Parking Area", "Fakultas Teknik", "Fakultas Kedokteran"])

# Analisis revenue
revenue = RevenueTrendAnalyzer("use_1753680644456.xlsx")
revenue.plot_revenue_by_spot()
