import numpy as np
import pandas as pd

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

data = {
    "A": [6.9, np.nan, 5.4, 4.7, 4.5, 5.1, 4.1, 4.5, 12.2, 7.5, 3.5, 7.6, 13.2],
    "B": [18.5, 21.9, np.nan, 21.2, 12.4, 16.7, 11, 11.5, 21.6, np.nan, 5.7, 11.1, 2.4],
    "C": [
        np.nan,
        36.3,
        50.6,
        48.7,
        51.9,
        np.nan,
        51.6,
        50.1,
        46.9,
        36.6,
        7.9,
        14.5,
        7.8,
    ],
    "E": [80, 70.1, 94.5, 54.3, 76.3, 84.6, np.nan, 93.6, 68.9, 82, 77.5, np.nan, 66.6],
}

## Load data onto a DataFrame
df = pd.DataFrame(data)

## Drop rows with missing data and write to new DataFrame
df_modified = df.dropna()

## Create df_train and df_test
df_train = df[0:8]
df_test = df[8:13]

## Create IterativeImputer model
imp = IterativeImputer(max_iter=10, random_state=0)

## Fit model to test data
model = imp.fit(df_train)

## Transform the entire dataset using the model
results = model.transform(df_test)
df_complete = np.round(results, 1)
