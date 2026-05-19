import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("MYSQL_HOST")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")
DB_PORT = int(os.getenv("MYSQL_PORT", 3306))

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=DB_PORT
)

cursor = conn.cursor()
print("Connected to MySQL")

df = pd.read_csv("weather_cleaned.csv")

insert_query = """
INSERT INTO weather_data
(city, country, temperature_c, humidity, wind_kph, condition_text, timestamp)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("STEP 3 ✔ Data loaded into MySQL successfully")
