import json
import os

def main():
    json_file_path = os.path.join("MainProgram", "azimuthal.json")

    with open(json_file_path, "r") as file:
        json_data = file.read()

    data = json.loads(json_data)

    # Buffer to store formatted data
    buffer = {}
    for i in data:
        date = i["Date"]
        month = date.split(" ")[1].upper()
        day = date.split(" ")[0].lstrip("0")  # Remove leading zero
        time = i["Solar Noon"]
        angle = i[""].replace("°", "")  # Remove the degree symbol
        if month not in buffer:
            buffer[month] = {}
        if day not in buffer[month]:
            buffer[month][day] = []
        buffer[month][day].append({"Time": time, "Solar Noon": angle})
        
    # remove from angle \u00c2 from all buffer data
    for month in buffer:
        for day in buffer[month]:
            for i in range(len(buffer[month][day])):
                buffer[month][day][i]["Solar Noon"] = buffer[month][day][i]["Solar Noon"].replace("\u00c2", "")

    # Write buffer to a new JSON file
    with open("azimuthal_processed.json", "w") as file:
        json.dump(buffer, file, indent=4)

    print(buffer)

if __name__ == "__main__":
    main()
