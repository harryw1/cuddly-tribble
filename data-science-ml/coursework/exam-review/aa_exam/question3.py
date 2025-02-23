import pandas as pd

## I literally had to go back to
## a way earlier version of scipy
## documentation to be able to get
## to the answer here


# read in and print data
shop = pd.read_csv("shop.csv")
print(shop.head())

# import test function from scipy.stats
from scipy.stats import chi2_contingency

# create contingency table
pd.crosstab(shop.plant, shop.status)

# run test and print p-value
chi, pval, dof, ex = chi2_contingency(pd.crosstab(shop.plant, shop.status))
print(pval)
