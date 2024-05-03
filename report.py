import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('C:/Users/91942/Desktop/loan/loan_clean.csv', low_memory=False)

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("C:/Users/91942/Desktop/loan/profiling_report.html")