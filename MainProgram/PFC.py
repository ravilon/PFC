# PFC.py

from AltitudeReader import AltitudeReader
import os

def main():
    # Get the absolute path to 'altitude.json' in the 'MainProgram' directory
    json_file_path = os.path.join("MainProgram", "altitude.json")

    # Initialize AltitudeReader with the absolute path to 'altitude.json'
    with open(json_file_path, "r") as file:
        json_data = file.read()

    reader = AltitudeReader(json_data)

    # Access data for a specific month (e.g., "ABR")
    position = reader.get_solar_position_for_month_and_day("ABR", 1, "06:30")
    print(position)  # Output: 9.13

    # Print data for a specific month


if __name__ == "__main__":
    main()
