# %% Lambda with conditions
mylambda = lambda x: "Welcome to BattleCity!" if x >= 13 else "You must be 13 or older"

# %% Lambda within a DataFrame
df["last_name"] = df.name.apply(lambda x: x.split(" ")[-1])

# %% Sometimes we also want to operate on a row
df["total_earned"] = df.apply(
    lambda row: (row.hourly_wage * 40)
    + ((row.hourly_wage * 1.5) * (row.hours_worked - 40))
    if row.hours_worked > 40
    else row.hourly_wage * row.hours_worked,
    axis=1,
)

# total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) if row.hours_worked > 40 else row.hourly_wage * row.hours_worked

# %% Lambda with multiple conditions
import pandas as pd

orders = pd.read_csv("shoefly.csv")
print(orders.head())
orders["shoe_source"] = orders.apply(
    lambda x: "vegan" if x["shoe_material"] != "leather" else "animal", axis=1
)
print(orders.head())
orders["salutation"] = orders.apply(
    lambda x: f"Dear Mr. {x.last_name}"
    if x.gender == "male"
    else f"Dear Ms. {x.last_name}",
    axis=1,
)
print(orders.head())
