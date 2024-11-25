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
