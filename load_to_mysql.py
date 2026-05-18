import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# 1️ Load environment variables
load_dotenv()

# 2️ Read MySQL credentials from .env
DB_HOST = os.getenv("MYSQL_HOST")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")

# 3️ Connect to MySQL
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = conn.cursor()

print("Connected to MySQL")

# 4️ Read cleaned CSV data
df = pd.read_csv("weather_cleaned.csv")

# 5️ SQL insert query
insert_query = """
INSERT INTO weather_data
(city, country, temperature_c, humidity, wind_kph, condition_text, timestamp)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# 6️ Insert each row into MySQL
for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

# 7️ Commit changes
conn.commit()

# 8️ Close connection
cursor.close()
conn.close()

print("STEP ✔ Data loaded into MySQL successfully")
