import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read weather data
df = pd.read_csv("weather_honolulu.csv")

# Lowest temperature recorded
lowest_temp = df["minimum_temperature"].min()

# Select rows from dataframe where temp == lowest_temp
df_lowest_temp_rows = df[df["minimum_temperature"] == lowest_temp]

# Print the dates
print(df_lowest_temp_rows["date"])

# Plot average temperature versus date
plt.plot(df["date"], df["average_temperature"])
plt.show()
plt.clf()
