import json


def save_config(data: dict, filename: str):
    """Writes a dictionary to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_config(filename: str) -> dict:
    """Reads and returns data from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)


def update_config(filename: str, key: str, value):
    """Updates a key in the JSON file and saves it."""
    config = load_config(filename)
    config[key] = value
    save_config(config, filename)



config_data = {
    "model": "RandomForest",
    "learning_rate": 0.01,
    "epochs": 10
}

save_config(config_data, "config.json")

print("Original Config:")
print(load_config("config.json"))

update_config("config.json", "epochs", 20)

# Load and print updated config
print("\nUpdated Config:")
print(load_config("config.json"))



# json.dump() writes Python data directly to a JSON file.
# json.dumps() converts Python data into a JSON string without creating a file.
