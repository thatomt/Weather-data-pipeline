import requests
import json

# Cape Town's coordinates
LATITUDE = -33.9249
LONGITUDE = 18.4241

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "auto",
    "past_days": 7,
}
print("Downloading weather data...")
response = requests.get(url, params=params)
data = response.json()


with open("weather_raw.json", "w") as f:
    json.dump(data, f, indent=2)

print("Done. Saved to weather_raw.json")