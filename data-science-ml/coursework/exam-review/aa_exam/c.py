import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data",
    names=["buying", "maint", "doors", "persons", "lug_boot", "safety", "accep"],
)

# Print contingency table for 'safety' and 'accep'
sa = pd.crosstab(df.safety, df.accep)
print(sa)


# Value of 'safety' corresponding to highest frequency for 'unacc'
highest_freq_unacc = "low"
# Calculate chi-square statistic for association between 'safety' and 'accep'
chi2_safety, p, dof, ex = chi2_contingency(sa)

# Calculate chi-square statistic for association between 'doors' and 'accep'
da = pd.crosstab(df.doors, df.accep)
chi2_doors, p, dof, ex = chi2_contingency(da)

# Which variable has a higher association with 'accep'?
print(chi2_safety, "\n", chi2_doors)
higher_association = 'safety'
