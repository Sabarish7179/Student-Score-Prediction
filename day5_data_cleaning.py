import pandas as pd

data = pd.read_csv("student_scores.csv")

print("Original Dataset")
print(data)

print("\nMissing Values")
print(data.isnull().sum())

data = data.drop_duplicates()

print("\nDataset Statistics")
print(data.describe())

data.to_csv("clean_student_scores.csv", index=False)

print("\nData Cleaning Completed Successfully!")
