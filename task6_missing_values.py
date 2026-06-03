import pandas as pd


df = pd.read_csv("employees_missing.csv")

print("Original Dataset:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nAfter dropna():")
print(df.dropna())


df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Department"] = df["Department"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(0)

print("\nAfter fillna():")
print(df)
