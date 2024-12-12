# %% Imports
import pandas as pd

# %% Create a DataFrame
df = pd.DataFrame(
    [
        [1, "3 inch screw", 0.5, 0.75],
        [2, "2 inch nail", 0.10, 0.25],
        [3, "hammer", 3.00, 5.50],
        [4, "screwdriver", 2.50, 3.00],
    ],
    columns=["Product ID", "Description", "Cost to Manufacture", "Price"],
)

# %% Add columns to the DataFrame
df["Sold in Bulk?"] = ["Yes", "Yes", "No", "No"]

# %% Display the DataFrame
print(df)

# %% Add a column with a default value
df["Is taxed?"] = "Yes"

# %% Display the DataFrame
print(df)

# %% Add a column through an operation on existing columns
df["Margin"] = df.Price - df["Cost to Manufacture"]

# %% Display the DataFrame
print(df)

# %% In-place operations
df["Name"] = df["Name"].apply(str.lower)

# %% Non-in-place operations with a lambda function
df["Lowercase Name"] = df["Name"].apply(lambda x: x.lower())

# %% Lambda function
# This is bad practice, but it's possible
mylambda = lambda x: x[0] + x[-1]


# Instead of the above, use this:
def mylambda(x):
    return x[0] + x[-1]


print(mylambda("This is a string"))
