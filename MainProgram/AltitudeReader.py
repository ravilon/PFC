import json

class AltitudeReader:
    def __init__(self, json_data):
        self.data = json.loads(json_data)

    def get_solar_position_for_month_and_day(self, month, day, time):
        """Retrieves the solar position for the given month, day, and time."""
        try:
            month_data = self.data["MONTHS"][month.upper()][str(day)]
            for entry in month_data:
                if entry["Time"] == time:
                    return float(entry["Solar Position"])
            raise ValueError(f"Time '{time}' not found for month '{month}' and day '{day}'")
        except KeyError:
            raise ValueError(f"Invalid month '{month}' or day '{day}'")

    def get_all_data_for_month(self, month):
        """Retrieves all data for the given month."""
        try:
            return self.data["MONTHS"][month.upper()]
        except KeyError:
            raise ValueError(f"Invalid month '{month}'")
