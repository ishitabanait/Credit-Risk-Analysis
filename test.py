import pandas as pd
from pandas_profiling import ProfileReport

# Load your dataset
file_path = "C:/Users/91942/Desktop/loan/loan_clean.csv"
data = pd.read_csv(file_path)

# Generate the EDA report
profile = ProfileReport(data, title="Exploratory Data Analysis Report", explorative=True)

# Save the report to an HTML file
profile.to_file("eda_report.html")
