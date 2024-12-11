# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # EDA: Diagnosing Diabetes

# %% [markdown]
# In this project, you'll imagine you are a data scientist interested in exploring data that looks at how certain diagnostic factors affect the diabetes outcome of women patients.
#
# You will use your EDA skills to help inspect, clean, and validate the data.
#
# **Note**: This [dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database) is from the National Institute of Diabetes and Digestive and Kidney Diseases. It contains the following columns:
#
# - `Pregnancies`: Number of times pregnant
# - `Glucose`: Plasma glucose concentration per 2 hours in an oral glucose tolerance test
# - `BloodPressure`: Diastolic blood pressure
# - `SkinThickness`: Triceps skinfold thickness
# - `Insulin`: 2-Hour serum insulin
# - `BMI`: Body mass index
# - `DiabetesPedigreeFunction`: Diabetes pedigree function
# - `Age`: Age (years)
# - `Outcome`: Class variable (0 or 1)
#
# Let's get started!

# %% [markdown]
# ## Initial Inspection

# %% [markdown]
# 1. First, familiarize yourself with the dataset [here](https://www.kaggle.com/uciml/pima-indians-diabetes-database).
#
#    Look at each of the nine columns in the documentation.
#
#    What do you expect each data type to be?

# %% [markdown]
# Expected data type for each column:
#
# - `Pregnancies`: int
# - `Glucose`: int
# - `BloodPressure`: float
# - `SkinThickness`: float
# - `Insulin`: float
# - `BMI`: float
# - `DiabetesPedigreeFunction`: float
# - `Age`: int
# - `Outcome`: int

# %% [markdown]
# 2. Next, let's load in the diabetes data to start exploring.
#
#    Load the data in a variable called `diabetes_data` and print the first few rows.
#
#    **Note**: The data is stored in a file called `diabetes.csv`.

# %%
import pandas as pd
import numpy as np
import math

# %% load in data
diabetes_data = pd.read_csv("diabetes.csv")

# %% [markdown]
# 3. How many columns (features) does the data contain?
diabetes_data.info()
print(len(diabetes_data.columns))


# %%
# print number of columns
num_cols = diabetes_data.columns.value_counts().count()
print(num_cols)

# %% [markdown]
# 4. How many rows (observations) does the data contain?
num_rows = diabetes_data.index.value_counts().count()
print(num_rows)

# %%
# print number of rows


# %% [markdown]
# ## Further Inspection

# %% [markdown]
# 5. Let's inspect `diabetes_data` further.
#
#    Do any of the columns in the data contain null (missing) values?

# %%
# find whether columns contain null values
null_cols = diabetes_data.isnull().any()
# print(diabetes_data.isnull().sum())
print(null_cols)

# %% [markdown]
# 6. If you answered no to the question above, not so fast!
#
#    While it's technically true that none of the columns contain null values, that doesn't necessarily mean that the data isn't missing any values.
#
#    When exploring data, you should always question your assumptions and try to dig deeper.
#
#    To investigate further, calculate summary statistics on `diabetes_data` using the `.describe()` method.

# %%
# perform summary statistics
diabetes_data.describe()


# %% [markdown]
# 7. Looking at the summary statistics, do you notice anything odd about the following columns?
#
#    - `Glucose`: min 0
#    - `BloodPressure`: min 0
#    - `SkinThickness`: min 0
#    - `Insulin`: min 0
#    - `BMI`: min 0

# %% [markdown]
# **Your response to question 7**:

# %% [markdown]
# 8. Do you spot any other outliers in the data?

# %% [markdown]
# **Your response to question 8**:

# %% [markdown]
# 9. Let's see if we can get a more accurate view of the missing values in the data.
#
#    Use the following code to replace the instances of `0` with `NaN` in the five columns mentioned:
#
#    ```py
#    diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)
#    ```

# %%
# replace instances of 0 with NaN


# %% [markdown]
# 10. Next, check for missing (null) values in all of the columns just like you did in Step 5.
#
#     Now how many missing values are there?

# %%
# find whether columns contain null values after replacements are made


# %% [markdown]
# 11. Let's take a closer look at these rows to get a better idea of _why_ some data might be missing.
#
#     Print out all the rows that contain missing (null) values.

# %%
# print rows with missing values


# %% [markdown]
# 12. Go through the rows with missing data. Do you notice any patterns or overlaps between the missing data?

# %% [markdown]
# **Your response to question 12**:

# %% [markdown]
# 13. Next, take a closer look at the data types of each column in `diabetes_data`.
#
#     Does the result match what you would expect?

# %%
# print data types using .info() method


# %% [markdown]
# 14. To figure out why the `Outcome` column is of type `object` (string) instead of type `int64`, print out the unique values in the `Outcome` column.

# %%
# print unique values of Outcome column


# %% [markdown]
# 15. How might you resolve this issue?

# %% [markdown]
# **Your response to question 15**:

# %% [markdown]
# ## Next Steps:

# %% [markdown]
# 16. Congratulations! In this project, you saw how EDA can help with the initial data inspection and cleaning process. This is an important step as it helps to keep your datasets clean and reliable.
#
#     Here are some ways you might extend this project if you'd like:
#     - Use `.value_counts()` to more fully explore the values in each column.
#     - Investigate other outliers in the data that may be easily overlooked.
#     - Instead of changing the `0` values in the five columns to `NaN`, try replacing the values with the median or mean of each column.

# %%
