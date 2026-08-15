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
