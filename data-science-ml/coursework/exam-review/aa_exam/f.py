import pandas as pd
import codecademylib3
import matplotlib.pyplot as plt

df = pd.read_csv("co2_emissions.csv")
print(df)

# Calulate proportion of total emissions contributed by each emission source
df["prop"] = df["emissions"] / df["emissions"].sum()
wedge_sizes = df["prop"]

fig, ax = plt.subplots()
ax.pie(wedge_sizes, labels=df.source)
plt.title("Distribution of CO2 Emissions")
plt.show()
