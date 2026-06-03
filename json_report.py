import json

with open("data.json", "r") as file:
    data = json.load(file)

skills_upper = [skill.upper() for skill in data["skills"]]

print(f"Name   : {data['name']}")
print(f"Role   : {data['role']}")
print(f"Skills : {', '.join(skills_upper)}")
