# Pandas has a lot of built-in
# methods for aggregating data
# within a dataframe.

# %% Dataframe creation
import pandas as pd
import numpy as np

data = {
    "Product": ["Widget", "Gadget", "Widget", "Doohickey", "Gadget", "Widget"],
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Sales": [100, 75, 125, 45, 80, 95],
    "Units": [10, 8, 12, 5, 9, 11],
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
df.groupby("Product").Sales.sum()

# In the above, we are grouping by the 'Product'
# and then summing the 'Sales' for each group.
# The general format for this is:
# df.groupby('column1').column2.measurement()
# In the above result, we are given a `series`
# and we would rather have a dataframe.
# To get a dataframe, we can use the `reset_index`
# method.

# %% Groupby with reset_index
grouped_example = df.groupby("Product").Sales.sum().reset_index()
print(grouped_example)

# %% Renaming columns
grouped_example.columns = ["Product", "Total Sales"]
print(grouped_example)

# %% Multiple columns with lambda and groups
# The result of the following code is a dataframe
# with the 25th percentile of sales for each product.
result = df.groupby("Product").Sales.apply(lambda x: np.percentile(x, 25)).reset_index()
print(result)

# %% Groupby with multiple columns
# The result of the following code is a dataframe
# with the total sales for each product in each region.
region_sales = df.groupby(["Product", "Region"]).Sales.sum().reset_index()
print(region_sales)

# %% Pivots
# We can also create pivots in pandas using the
# following syntax:
# df.pivot(columns='ColumnToPivot',
#        index='ColumnToBeRows',
#        values='ColumnToBeValues')
final_pivot = region_sales.pivot(
    columns="Region", index="Product", values="Sales"
).reset_index()
print(final_pivot)
