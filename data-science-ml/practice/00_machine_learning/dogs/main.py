# Import libraries
import numpy as np
import pandas as pd
from scipy.stats import binomtest
from scipy.stats import ttest_1samp

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
num_whippets = np.sum(whippet_rescue==1)
print(f"\nNumber of Rescued Whippets: {num_whippets}\n")

# determine signficance of whippet rescue population
res = binomtest(num_whippets, len(dogs), p=0.05)
print(res.pvalue)
