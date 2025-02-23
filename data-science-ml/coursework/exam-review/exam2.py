import pandas as pd

df_honolulu = pd.read_csv("weather_honolulu.csv")
df_maui = pd.read_csv("weather_maui.csv")

# Merge the two DataFrames on the "date" axis
df = pd.merge(df_honolulu, df_maui, on=["date"], how="inner")

# From the merged dataframe, select the column corresponding to the maximum
# temperature in Maui and print the highest temperature value occuring in that column
print(df["maximum_temperature_y"].max())
