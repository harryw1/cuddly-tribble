# import libraries
# import codecademylib3

import numpy as np
import pandas as pd
from scipy.stats import f_oneway, ttest_ind
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv(
    "data-science-ml/practice/00_machine_learning/heart_disease/heart_disease.csv"
)

# print first 5 rows
print(heart.head())

# compare thalach and heart_disease
# sns.boxplot(x='thalach', y='heart_disease', data=heart)
# plt.show()

# exploring thalach
thalach_hd = heart[heart["heart_disease"] == "presence"]
thalach_no_hd = heart[heart["heart_disease"] == "absence"]

mean_thalach_hd = np.mean(thalach_hd["thalach"])
mean_thalach_no_hd = np.mean(thalach_no_hd["thalach"])

median_thalach_hd = np.median(thalach_hd["thalach"])
median_thalach_no_hd = np.median(thalach_no_hd["thalach"])

print(
    (
        f"Mean Thalac HD: {mean_thalach_hd}\n"
        f"Mean Thalac No HD: {mean_thalach_no_hd}\n"
        f"Median Thalac HD: {median_thalach_hd}\n"
        f"Median Thalac No HD: {median_thalach_no_hd}\n"
    )
)

# thalac x heart_disease significane
tstat, pval = ttest_ind(thalach_hd["thalach"], thalach_no_hd["thalach"])
print(
    f"Thalac and Heart Disease Significance\n"
    f"t-statistic: {round(tstat, 8)}\np-value: {round(pval, 8)}\n"
)

# exploring trestbps and heart_disease
# sns.boxplot(x='trestbps', y='heart_disease', data=heart)
# plt.show()
# plt.clf()

trestbps_hd = heart[heart["heart_disease"] == "presence"]
trestbps_no_hd = heart[heart["heart_disease"] == "absence"]

tstat, pval = ttest_ind(trestbps_hd["trestbps"], trestbps_no_hd["trestbps"])
print(
    f"Trestbps and Heart Disease Significance\n"
    f"t-statistic: {round(tstat, 8)}\np-value: {round(pval, 8)}\n"
)

# exploring thalac and cp
# sns.boxplot(x='thalach', y='cp', data=heart)
# plt.show()
# plt.clf()

thalac_typical_cp = heart[heart["cp"] == "typical angina"]
thalac_asymptomatic_cp = heart[heart["cp"] == "asymptomatic"]
thalac_nonangin = heart[heart["cp"] == "non-anginal pain"]
thalac_atypical_cp = heart[heart["cp"] == "atypical angina"]

fstat, pval = f_oneway(
    thalac_typical_cp["thalach"],
    thalac_asymptomatic_cp["thalach"],
    thalac_nonangin["thalach"],
    thalac_atypical_cp["thalach"],
)
print(f"Thalach and CP Significance\nF-statistic: {round(fstat, 8)}\np-value: {pval}\n")

output = pairwise_tukeyhsd(heart.thalach, heart.cp)
print(output)
