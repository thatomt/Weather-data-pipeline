import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("weather.db")
table = pd.read_sql("SELECT * FROM weather", conn)
conn.close()

# Draw the chart
plt.plot(table["date"], table["max_temp_c"], label="Max Temp (C)", marker="o")
plt.plot(table["date"], table["min_temp_c"], label="Min Temp (C)", marker="o")

plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.title("Cape Town Temperature - Last 14 Days")
plt.legend()
plt.tight_layout()

# Save the chart as an image file
plt.savefig("weather_chart.png")

print("Done. Saved chart to weather_chart.png")