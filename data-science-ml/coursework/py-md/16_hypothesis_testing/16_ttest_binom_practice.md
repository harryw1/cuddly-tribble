# Python Practice

```python
# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp as ttest
from scipy.stats import binom_test as bt

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd = yes_hd.chol
print(np.mean(chol_hd))

t, p = ttest(a= chol_hd, popmean = 240)
print(p)

chol_nhd = no_hd.chol
print(np.mean(chol_nhd))

x, y = ttest(a= chol_nhd, popmean = 240)
print(y)

num_patients = len(heart)
print(num_patients)

num_highfbs_patients = heart[heart.fbs == 1]
print(len(num_highfbs_patients))
print(len(heart)*0.08)

result = bt(45, n=303, p=0.08, alternative='greater')
print(result)
```
