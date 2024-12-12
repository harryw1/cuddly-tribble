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
# - `Pregnancies`: `int64`
# - `Glucose`: `int64`
# - `BloodPressure`: `int64`
# - `SkinThickness`: `int64`
# - `Insulin`: `int64`
# - `BMI`: `float64`
# - `DiabetesPedigreeFunction`: `float64`
# - `Age`: `int64`
# - `Outcome`: `int64`

# %% [markdown]
# 2. Next, let's load in the diabetes data to start exploring.
#
#    Load the data in a variable called `diabetes_data` and print the first few rows.
#    
#    **Note**: The data is stored in a file called `diabetes.csv`.

# %%
import pandas as pd
import numpy as np

# load in data
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())

# %% [markdown]
# 3. How many columns (features) does the data contain?

# %%
# print number of columns
print(len(diabetes_data.columns))

# %% [markdown]
# 4. How many rows (observations) does the data contain?

# %%
# print number of rows
print(len(diabetes_data))

# %% [markdown]
# ## Further Inspection

# %% [markdown]
# 5. Let's inspect `diabetes_data` further.
#
#    Do any of the columns in the data contain null (missing) values?

# %%
# find whether columns contain null values
print(diabetes_data.isnull().sum())

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
print(diabetes_data.describe())

# %% [markdown]
# 7. Looking at the summary statistics, do you notice anything odd about the following columns?
#
#    - `Glucose`
#    - `BloodPressure`
#    - `SkinThickness`
#    - `Insulin`
#    - `BMI`

# %% [markdown]
# **Our response to question 7**: If you take a look at the minimum values for these five columns, you'll notice that they are all `0`. 
#
# How can Blood Pressure or BMI be `0`? That makes no sense! These values also seem to be way off from their respective medians and means, another indicator that something is off.
#
# One way to interpret this is that there are missing values in the data.

# %% [markdown]
# 8. Do you spot any other outliers in the data?

# %% [markdown]
# **Our response to question 8**: In addition to the `0` values that show up for the columns above, there appear to be additional outliers, such as:
#
# - The maximum value of the `Insulin` column is `846`, which is abnormally high.
# - The maximum value of the `Pregnancies` column is `17`. While having 17 pregnancies is not impossible, this case might be something to look further into to determine its accuracy.
#
# As you can see, EDA helps inform the data cleaning process by helping catch things that aren't immediately obvious.

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
diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)

# %% [markdown]
# 10. Next, check for missing (null) values in all of the columns just like you did in Step 5.
#
#     Now how many missing values are there?

# %%
# find whether columns contain null values after replacements are made
print(diabetes_data.isnull().sum())

# %% [markdown]
# 11. Let's take a closer look at these rows to get a better idea of _why_ some data might be missing.
#
#     Print out all the rows that contain missing (null) values.

# %%
# print rows with missing values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

# %% [markdown]
# 12. Go through the rows with missing data. Do you notice any patterns or overlaps between the missing data?

# %% [markdown]
# **Our response to question 12**: One thing you might notice is that most rows with missing data have missing values in more than one column. In fact, every single row with at least one missing value also has a missing value in the `Insulin` column. This is a clue as to why the data is missing! If patients did not have their insulin measured, why might they also not have had these other measurements taken?
#
# Depending on how much data is missing, you might choose to remove specific rows or impute the missing values somehow.

# %% [markdown]
# 13. Next, take a closer look at the data types of each column in `diabetes_data`.
#
#     Does the result match what you would expect?

# %%
# print data types using .info() method
print(diabetes_data.info())

# %% [markdown]
# 14. To figure out why the `Outcome` column is of type `object` (string) instead of type `int64`, print out the unique values in the `Outcome` column.

# %%
# print unique values of Outcome column
print(diabetes_data.Outcome.unique())

# %% [markdown]
# 15. How might you resolve this issue?

# %% [markdown]
# **Our response to question 15**: A possible next step would be to replace instances of `'O'` with `0` and convert the `Outcome` column to type `int64`.

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
