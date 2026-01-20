import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

query = """
SELECT DATE(timestamp) AS date,
       AVG(temperature_c) AS avg_temp
FROM weather_data
GROUP BY DATE(timestamp)
"""

df = pd.read_sql(query, conn)
conn.close()

plt.plot(df["date"], df["avg_temp"])
plt.xticks(rotation=45)
plt.title("Average Daily Temperature")
plt.show()

print("STEP 4 ✔ Analytics done")
