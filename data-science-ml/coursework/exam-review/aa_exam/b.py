import pandas as pd

df = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data",
    names=["buying", "maint", "doors", "persons", "lug_boot", "safety", "accep"],
)
print(df.head())
print(df.head())

# No. of fields that are categorical variables (cat_fields_no)
cat_fields_no = df.select_dtypes(include=["object"]).shape[1]
print(cat_fields_no)

# Fraction of cars that are not acceptable (frac_unacc)
frac_unacc = df["accep"].value_counts(normalize=True)["unacc"]
print(frac_unacc)
