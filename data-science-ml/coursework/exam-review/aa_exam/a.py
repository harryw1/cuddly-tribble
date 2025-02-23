import pandas as pd

df1 = pd.DataFrame(
    {
        "Fruit": ["guava", "apple", "orange", "mango"],
        "A": [4, 1, 3, 2],
        "B": [5, 3, 1, 1],
    }
)
df2 = pd.DataFrame(
    {
        "Fruit": ["guava", "apple", "honeydew", "orange", "mango"],
        "E": [4, 2, 5, 1, 2],
        "C": [3, 5, 2, 1, 1],
        "D": [4, 3, 5, 3, 3],
    }
)

df = pd.merge(df1, df2, on=["Fruit"], how="inner")

print(df.head())

df["mean_rating"] = df.apply(lambda x: x[["A", "B", "E", "C", "D"]].mean(), axis=1)

print(df.head())
