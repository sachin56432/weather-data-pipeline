import pandas as pd

df = pd.read_csv("weather_raw.csv")

df.drop_duplicates(inplace=True)
df["temperature_c"] = df["temperature_c"].astype(float)
df["humidity"] = df["humidity"].astype(int)

df.to_csv("weather_cleaned.csv", index=False)

print("STEP 2 ✔ Data cleaned")
