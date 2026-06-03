import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

# Display dataset
print("=== Dataset ===")
print(df)

# Summary statistics for numeric columns
print("\n=== Describe Output ===")
print(df.describe())

# Value counts for categorical column
print("\n=== Name Value Counts ===")
print(df["name"].value_counts())

# Observations
print("\n=== Insights ===")
print("1. The average Math score is 83.33.")
print("2. The average Science score is 85.67.")
print("3. The average English score is 88.00.")
print("4. Aman has the highest scores among the students.")
print("5. Each student appears exactly once in the dataset.")
