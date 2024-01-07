import os
import csv
import json

def process_altitude(csv_folder_path, output_json):
    data = {}

    for month_folder in os.listdir(csv_folder_path):
        month_path = os.path.join(csv_folder_path, month_folder)
        
        if os.path.isdir(month_path):
            month_data = {}
            for day_folder in os.listdir(month_path):
                day_path = os.path.join(month_path, day_folder)
                if os.path.isdir(day_path):
                    day_data = []
                    for file_name in os.listdir(day_path):
                        if file_name.endswith(".csv"):
                            day_number = int(file_name.split('-')[-1].split('.')[0])
                            file_path = os.path.join(day_path, file_name)
                            with open(file_path, 'r') as csv_file:
                                csv_reader = csv.DictReader(csv_file)
                                for row in csv_reader:
                                    # Getting only Time and solar point coluns
                                    row = {'Time': row['Time'], 'Solar Position': row['Solar Position']}
                                    day_data.append(row)

                    # Ensure that the month key exists in the month_data dictionary
                    month_data[day_folder] = day_data

            # Assign day_data to the specific month in the data dictionary
            data[month_folder] = month_data

    with open(output_json, 'w') as json_file:
        json.dump(data, json_file, indent=2)
        


# Get Raw_Meteorological_Data file path
raw_data_path = os.path.join(os.getcwd(), 'Raw_MeteoroLogic_Data_Altitude')
output_json = os.path.join(os.getcwd(), 'altitude.json')

process_altitude(raw_data_path, output_json)
