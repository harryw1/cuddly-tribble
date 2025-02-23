from scipy.stats import ttest_1samp
import numpy as np

# load dataset
visit_times = np.genfromtxt("visit_times.csv")

# find and print the mean
visit_times.mean()

# use ttest_1samp to calculate tstat and pval
tstat, pval = ttest_1samp(visit_times, 5)

# print pval
print(pval)
