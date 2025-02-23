import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt

df = pd.read_csv("annual-co-emissions-by-region.csv")
print(df.head())

# Create DataFrame df_USA
df_USA = df[df["Entity"] == "United States"]

# Create line plot
fig = plt.gca()
plt.plot(df_USA["Year"], df_USA["Annual CO₂ emissions (zero filled)"])
plt.xlabel("Year")
plt.ylabel("Annual CO₂ emissions (zero filled)")
plt.title("CO2 Emissions in United States Over Time")
