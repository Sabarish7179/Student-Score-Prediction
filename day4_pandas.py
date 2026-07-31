import pandas as pd

data = pd.read_csv("student_scores.csv")

print("First 5 Rows")
print(data.head())

print("\nDataset Information")
print(data.info())

print("\nStatistics")
print(data.describe())

print("\nColumns")
print(data.columns)
