# student_profile.py

# Student Profile Card using F-Strings and Type Hints

student = {
    "name": "Sahil khan",
    "course": "B.Tech IT",
    "semester": 3,
    "goal": "DevOps Engineer"
}


def create_profile_card(profile: dict) -> str:
    """
    Returns a formatted student profile card.
    """
    return (
        f"Student Name : {profile['name']}\n"
        f"Course       : {profile['course']}\n"
        f"Semester     : {profile['semester']}\n"
        f"Career Goal  : {profile['goal']}"
    )


print(create_profile_card(student))
