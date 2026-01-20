import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "28.6139,77.2090"   # New Delhi coordinates




url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"
response = requests.get(url).json()
print("Resolved location from API:")
print(response["location"])
print("Temperature (C):", response["current"]["temp_c"])

# 1️⃣ Validate API response
if "location" not in response or "current" not in response:
    print("API error response:", response)
    exit()

# 2️⃣ Extract temperature safely
temp_c = response["current"]["temp_c"]

# 3️⃣ Sanity check (VERY IMPORTANT)
# Delhi realistic range check
if temp_c < -5 or temp_c > 55:
    print(f"Invalid temperature detected: {temp_c} °C")
    exit()

weather_record = {
    "city": response["location"]["name"],
    "country": response["location"]["country"],
    "temperature_c": temp_c,
    "humidity": response["current"]["humidity"],
    "wind_kph": response["current"]["wind_kph"],
    "condition_text": response["current"]["condition"]["text"],
    "timestamp": datetime.now()
}

df = pd.DataFrame([weather_record])

# 4️⃣ Prevent duplicate timestamps
file_exists = os.path.isfile("weather_raw.csv")

if file_exists:
    existing_df = pd.read_csv("weather_raw.csv")
    if weather_record["timestamp"] in existing_df["timestamp"].values:
        print("Duplicate record detected. Skipping insert.")
        exit()

df.to_csv("weather_raw.csv", mode="a", header=not file_exists, index=False)

print("STEP 1 ✔ Weather data ingested safely")
