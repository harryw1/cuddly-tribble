import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Example dictionaries (replace with your actual data)
d = {"col1": [1, 2, np.nan, 4], "col2": [5, np.nan, 7, 8]}
dTest = {"col1": [10, 20, 30, np.nan], "col2": [50, 60, np.nan, 80]}

# Create the pandas DataFrame from our dictionary
df = pd.DataFrame(data=d)
dfTest = pd.DataFrame(data=dTest)

# Create the IterativeImputer model with ten iterations to predict missing values
imp = IterativeImputer(max_iter=10, random_state=0)

# Fit the model to the test dataset
imp.fit(dfTest)

# Transform the model on the entire dataset
dfComplete = pd.DataFrame(np.round(imp.transform(df), 1), columns=df.columns)

print(dfComplete.head(10))
