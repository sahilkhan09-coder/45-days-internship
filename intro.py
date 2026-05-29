# intro.py — Collects personal info from the user and prints a formatted introduction.

# --- Collect input from the user ---
name           = input("Enter your name: ")
age            = input("Enter your age: ")
city           = input("Enter your city: ")
favorite_subject = input("Enter your favorite subject: ")
target_role = input("Enter your target role: ")


# --- Store everything in a single dict ---
student = {
    "name": name,
    "age": age,
    "city": city,
    "favorite_subject": favorite_subject,
    "target_role": target_role
}

# --- Print a 4-line introduction using f-strings ---
print()
print(f"Hi! My name is {student['name'].title()} and I am {student['age']} years old.")
print(f"I'm from {student['city'].title()}.")
print(f"My favorite subject is {student['favorite_subject']}")
print(f"I want to become a {student['target_role']}")
