import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "math", "science", "english"])


    writer.writerow(["sahil", 85, 90, 88])
    writer.writerow(["Riya", 70, 75, 80])
    writer.writerow(["Aman", 95, 92, 96])

print("students.csv created successfully!")


results = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        avg = (
            int(row["math"]) +
            int(row["science"]) +
            int(row["english"])
        ) / 3

    
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        else:
            grade = "C"

        results.append({
            "name": row["name"],
            "average": round(avg, 2),
            "grade": grade
        })

with open("results.csv", "w", newline="") as file:
    fieldnames = ["name", "average", "grade"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("results.csv created successfully!")
