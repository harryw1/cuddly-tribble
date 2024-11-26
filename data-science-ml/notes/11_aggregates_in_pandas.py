# Pandas has a lot of built-in
# methods for aggregating data
# within a dataframe.

# %% Dataframe creation
import pandas as pd

data = {
    'Product': ['Widget', 'Gadget', 'Widget', 'Doohickey', 'Gadget', 'Widget'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Sales': [100, 75, 125, 45, 80, 95],
    'Units': [10, 8, 12, 5, 9, 11]
}

df = pd.DataFrame(data)
print(df)

# %% Number of unique values in a column
print(df.Region.nunique())
# %% Median sales
print(df.Sales.median())

# The general layout for performing a command
# is:
    # dataframe.column_name.command()

# Sometimes we have data where we want to create
# groups based on a column and then perform an
# aggregate function on those groups.

# %% Groupby
df.groupby('Product').Sales.sum()

# In the above, we are grouping by the 'Product'
# and then summing the 'Sales' for each group.
# The general format for this is:
    # df.groupby('column1').column2.measurement()
