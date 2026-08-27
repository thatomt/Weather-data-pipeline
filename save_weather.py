"""
read weather_clean.csv, save it into a database file called weather.db.
That's all this script does.
"""

import pandas as pd
import sqlite3

table = pd.read_csv("weather_clean.csv")

# Connect to a database file 
conn = sqlite3.connect("weather.db")

# Save the table into the database, into a table called "weather"
# if_exists="replace" means: if we run this again, overwrite old data
table.to_sql("weather", conn, if_exists="replace", index=False)

conn.close()

print("Done. Saved into weather.db, table name: weather")