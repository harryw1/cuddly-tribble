import glob
import pandas as pd

# Create some dummy files
file_list = glob.glob("*.csv")

# Load the data into a DataFrame using glob
df = pd.DataFrame([pd.read_csv(file) for file in file_list])

print(df)
