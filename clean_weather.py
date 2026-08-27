"""
read weather_raw.json, turn it into a clean table, save it as a CSV.
That's all this script does.
"""

import json
import pandas as pd

with open("weather_raw.json", "r") as f:
    data = json.load(f)

# The raw data has a "daily" section with lists of dates and values.
# We turn that into a table with one row per day.
daily = data["daily"]

table = pd.DataFrame({
    "date": daily["time"],
    "max_temp_c": daily["temperature_2m_max"],
    "min_temp_c": daily["temperature_2m_min"],
    "rain_mm": daily["precipitation_sum"],
})

print("Here's the clean table:")
print(table)

# Save it as a CSV file (opens fine in Excel too)
table.to_csv("weather_clean.csv", index=False)

print("\nDone. Saved to weather_clean.csv")