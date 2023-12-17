import json

# Specify the path to your JSON file
file_path = 'meteorological_data.json'

# Load the JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Access and print data
for month, entries in data["MONTHS"].items():
    print(f"Month: {month}")
    for entry in entries:
        time = entry["Time"]
        solar_position = entry["Solar Position"]
        print(f"  Time: {time}, Solar Position: {solar_position}")
