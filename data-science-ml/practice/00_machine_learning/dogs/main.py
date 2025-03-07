# Import libraries
import numpy as np
import pandas as pd
from scipy.stats import binomtest
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

# Import data
dogs = pd.read_csv('/Users/harrisonweiss/Documents/GitHub/cuddly-tribble/data-science-ml/practice/00_machine_learning/dogs/dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

print(dogs.head())

# check whippet rescue percent
# whippet_rescue = dogs.loc[(dogs.breed == 'whippet') & (dogs.is_rescue == 1)] this returns only the whippets that are rescues
whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']
print(whippet_rescue)

# print number of whippet rescues
num_whippets = np.sum(whippet_rescue == 1)
print(f"\nNumber of Rescued Whippets: {num_whippets}\n")

# determine signficance of whippet rescue population
res = binomtest(num_whippets, len(dogs), p=0.05)
print(f"pvalue: {res.pvalue}")

# exploring differences in average weights between breeds
wt_whippets = dogs_wtp.weight[dogs_wtp.breed == 'whippet']
wt_terriers = dogs_wtp.weight[dogs_wtp.breed == 'terrier']
wt_pitbulls = dogs_wtp.weight[dogs_wtp.breed == 'pitbull']

res = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(f"\nF-statistic: {res.statistic}")
print(f"p-value: {res.pvalue}")

# Tukey HSD test to compare means of 'weight' across breeds in dogs_wtp
res_tukey = pairwise_tukeyhsd(endog=dogs_wtp['weight'], groups=dogs_wtp['breed'], alpha=0.05)
print(res_tukey)
print(f'\n')

# exploring poodle and shihtzu colors
X = pd.crosstab(dogs_ps.breed, dogs_ps.color)
print(X)

# run chi-square test
res_chi = chi2_contingency(X)
print(f"\nChi-square statistic: {res_chi[0]}")
print(f"p-value: {res_chi[1]}")