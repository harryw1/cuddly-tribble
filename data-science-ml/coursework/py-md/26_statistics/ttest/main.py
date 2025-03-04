"""Suppose that a company is considering a new color-scheme for their website. They think that visitors will spend more time on the
site if it is brightly colored. To test this theory, the company shows the old and new versions of the website to 50 site visitors,
each — and finds that, on average, visitors spent 2 minutes longer on the new version compared to the old. Will this be true of
future visitors as well? Or could this have happened by random chance among the 100 people in this sample?

Running this kind of ttest requires a quantitative variable and a binary variable.
"""

import pandas as pd
import matplotlib.pyplot as plt
# import codecademylib3
from scipy.stats import ttest_ind

data = pd.read_csv('version_time.csv')

# separate out times for  two versions
old = data.time_minutes[data.version == 'old']
new = data.time_minutes[data.version == 'new']

# run the t-test here:
tstat, pval = ttest_ind(old, new)
# >> print(tstat, pval)
# >> 0.0020408264429904

# determine significance
significant = True

# plot overlapping histograms
plt.hist(old, alpha=.8, label='old')
plt.hist(new, alpha=.8, label='new')
plt.legend()
plt.show()

"""Second Example with Non-binary categories"""

# store the data
veryants = pd.read_csv('veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run t-tests
# running a multi-way t-test by comparing
# each variable to each other
abtstat, a_b_pval = ttest_ind(a,b)
actstat, a_c_pval = ttest_ind(a,c)
bctstat, b_c_pval = ttest_ind(b,c)

print(a_b_pval, a_c_pval, b_c_pval)

# determine significance
a_b_significant = True
a_c_significant = True
b_c_significant = False

# create plot
sns.boxplot(data=veryants, x='Store', y='Sale')
plt.show()