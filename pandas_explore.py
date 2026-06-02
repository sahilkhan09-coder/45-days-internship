import pandas as pd

data = {
    "name": ["sahil", "Riya", "Karan", "Priya", "Rohit",
             "Sneha", "Arjun", "Neha", "Vikas", "Pooja"],
    "city": ["Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi",
             "Mumbai", "Jaipur", "Delhi", "Mumbai", "Jaipur"],
    "math_score": [80, 75, 90, 65, 78, 88, 72, 95, 70, 85],
    "science_score": [85, 70, 92, 68, 80, 90, 75, 89, 73, 87],
    "english_score": [78, 82, 88, 72, 76, 91, 74, 93, 71, 84]
}

df = pd.DataFrame(data)


df["total_score"] = (
    df["math_score"] +
    df["science_score"] +
    df["english_score"]
)

print("Average Scores:")
print(df[["math_score", "science_score", "english_score"]].mean())

print("\nHighest Total Score Student:")
print(df.loc[df["total_score"].idxmax()])

print("\nStudents Per City:")
print(df.groupby("city").size())

print("\nMath Score Above 75:")
print(df[df["math_score"] > 75])

# Top 3 students by total score
print("\nTop 3 Students:")
print(df.nlargest(3, "total_score"))
