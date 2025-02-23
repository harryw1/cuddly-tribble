import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("weather_honolulu.csv")

# Take a peek at the first 5 rows
print(df.head())

# Create a dataframe, df2 that only contains the average
# precipitation and average temperature alone
df2 = df[["average_precipitation", "average_temperature"]]

# Plot average temperature versus precipitation to see how they vary with each other
plt.plot(df2["average_temperature"], df2["average_precipitation"])
plt.show()
