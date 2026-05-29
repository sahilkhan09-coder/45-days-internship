# This file classifies student grades

students = [
    {"name": "sahil", "score": 95},
    {"name": "mansi", "score": 82},
    {"name": "huzaifa", "score": 74},
    {"name": "sameer", "score": 61},
    {"name": "arav", "score": 40}
]


def classify(score):

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 50:
        return "D"

    else:
        return "F"


sorted_students = sorted(
    students,
    key=lambda x: x["score"],
    reverse=True
)


for student in sorted_students:

    grade = classify(student["score"])

    print(f"{student['name']} : {grade}")
