# Import libraries
import numpy as np
import pandas as pd
from scipy.stats import binomtest, chi2_contingency

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv(
    "/Users/harrisonweiss/Documents/GitHub/cuddly-tribble/data-science-ml/practice/00_machine_learning/farmburg_ab/clicks.csv"
)

# inspect the data
print(abdata.head())

# create crosstab
X = pd.crosstab(abdata.group, abdata.is_purchase)
print(X)

# run chi-square test
chi2, pval, dof, exp = chi2_contingency(X)
print(f"Chi-square statistic: {chi2}")
print(f"p-value: {pval}")

# save total observations
num_visits = len(abdata)
print(f"Total Observations: {num_visits}")

# number of sales needed at price a
num_sales_needed_099 = np.ceil(1000 / 0.99)
print(num_sales_needed_099)

# conversion rate needed at price a for baseline visits
p_sales_needed_099 = num_sales_needed_099 / num_visits
print(p_sales_needed_099)

# number of sales needed at price b
num_sales_needed_199 = np.ceil(1000 / 1.99)
print(num_sales_needed_199)

# conversion rate needed at price b for baseline visits
p_sales_needed_199 = num_sales_needed_199 / num_visits
print(p_sales_needed_199)

# number of sales needed at price c
num_sales_needed_499 = np.ceil(1000 / 4.99)
print(num_sales_needed_499)

# conversion rate needed at price c for baseline visits
p_sales_needed_499 = num_sales_needed_499 / num_visits
print(p_sales_needed_499)

# binomial test
samp_size_099 = 1350 + 316
sales_099 = 316

res = binomtest(sales_099, samp_size_099, p=p_sales_needed_099, alternative="greater")
print(f"p-value: {res.pvalue}")

# binomial test
samp_size_199 = 1483 + 183
sales_199 = 183

res = binomtest(sales_199, samp_size_199, p=p_sales_needed_199, alternative="greater")
print(f"p-value: {res.pvalue}")

# binomial test
samp_size_499 = 1583 + 83
sales_499 = 83

res = binomtest(sales_499, samp_size_499, p=p_sales_needed_499, alternative="greater")
print(f"p-value: {res.pvalue}")
