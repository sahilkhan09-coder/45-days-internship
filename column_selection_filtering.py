import pandas as pd

df = pd.read_csv("studentss.csv")

print("Original DataFrame:")
print(df)


selected_columns = df[["Name", "Math", "Science"]]

print("\nSelected Columns:")
print(selected_columns)


filter1 = df[df["Math"] > 90]

print("\nStudents with Math > 90:")
print(filter1)


filter2 = df[(df["Math"] > 90) & (df["Science"] > 85)]

print("\nStudents with Math > 90 and Science > 85:")
print(filter2)

# Notes
print("\nFilter 1: Shows students scoring more than 90 in Math.")
print("Filter 2: Shows students scoring more than 90 in Math AND more than 85 in Science.")
