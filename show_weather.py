import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("weather.db")
table = pd.read_sql("SELECT * FROM weather", conn)
conn.close()

