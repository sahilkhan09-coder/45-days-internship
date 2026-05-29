# skills_counter.py --- This file prints skills with numbering

skills = [
    "Python",
    "c language",
    "vs code",
    "Canva",
    "Figma"
]

for index, skill in enumerate(skills, start=1):     #loop
    print(f"{index}. {skill}")

print(f"\nTotal skills: {len(skills)}")            #count
