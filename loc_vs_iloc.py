import pandas as pd

# Load dataset
df = pd.read_csv("employees.csv")

print("Original DataFrame:")
print(df)

# Set Name as index for .loc example
df_indexed = df.set_index("Name")

# .loc (label-based selection)
print("\nUsing .loc:")
print(df_indexed.loc["Priya", ["Department", "Salary"]])

# .iloc (position-based selection)
print("\nUsing .iloc:")
print(df.iloc[1, [2, 3]])

# Difference note
print("\nDifference between .loc and .iloc:")
print(".loc uses labels (row names and column names).")
print(".iloc uses integer positions (row and column numbers).")
