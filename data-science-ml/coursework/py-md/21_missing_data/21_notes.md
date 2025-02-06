# Identifying and Checking for Missing Data

High-level strategies for identifying and checking for missing data include:

1. Verify that data was uploaded correctly in the first place. The easiest way to avoid missing data is to prevent
it from happening in the first place! Since most missing data use cases happen from a systematic error, try to find
the culprit and correct the faulty data feed.
2. Try looking at small chunks of the data. Oftentimes, missing data can be easy to spot when looking at the data
directly. Most commonly, data scientists, data analysts, and data professionals will look at either the beginning
or end of a dataset, or retrieve a random sampling of data to look at. If there is a significant amount of missing
data, it will be apparent by doing so.
3. Look at statistics for the entire dataset. Sometimes, however, missing data might be hard to find and could be
a small subset of the data. A quick method to find out if there are any missing values at all is to collect some
basic summary statistics about our data. In particular, we can count how many values there are in each column of
your dataset, and note any discrepancies. If a column has a count lower than our total number of rows, it has
missing data!

## Listwise versus Pairwise Deletion

Listwise deletion is the process of deleting an entire row of data if it contains a missing value. This is the most
common method of dealing with missing data, but it is also the most dangerous. By deleting an entire row of data,
you are potentially losing a lot of valuable information. This is especially true if the missing data is only in one
column of the dataset. In this case, you would be throwing away a lot of good data just because of a small error.

Pairwise deletion is the process of deleting a single data point if it contains a missing value. This is a much safer
method of dealing with missing data, as it only deletes the missing data point and not the entire row.

```python
"""Listwise Deletion"""
df.dropna(inplace=True)
```

```python
"""Pairwise Deletion"""
df.dropna(subset=['column_name', 'other_column'], inplace=True, how='any')
```

## Kinds of Missing Data

Different types of missing data
But there's more to missing data than missingness. Missing data comes in four varieties:
- Structurally Missing Data: we expect this data to be missing for some logical reason
- Missing Completely at Random (MCAR): the probability of any datapoint being MCAR is the same for all
data points - this type of missing data is mostly hypothetical
- Missing at Random (MAR): the probability of any data point being MAR is the same within groups of
the observed data - this is much more realistic than MCAR
- Missing Not at Random (MNAR): there is some reason why the data is missing

## Stock Ticker Example

In the stock ticker example, we have a dataset that contains the stock prices for a company over a period of time.

There are few different ways we can interpolate the missing data points in this dataset. One we can do so is to use last observation carried forward (LOCF). This method simply takes the last known value and carries it forward to the next missing value. This is a simple method that works well when the data is relatively stable.

In Python we can use the `.ffil()` method on a particular column to fill in missing values with the last known value.

```python
import impyute
"""Fill in missing values with the last known value for a DataFrame"""
df['column_name'].ffill(axis=0, inplace=True)

"""Fill with LOCF for a NumPy array using impyute"""
impyute.imputation.ts.locf(data, axis=0)
```

Another method we can use is *Next Observation Carried Backward* (NOCB). This method is the opposite of LOCF, and carries the next known value backward to the missing value.

```python
import impyute
"""Fill in missing values with the next known value for a DataFrame"""
df['column_name'].bfill(axis=0, inplace=True)

"""Fill with NOCB for a NumPy array using impyute"""
impyute.imputation.ts.nocb(data, axis=0)
```

Another method is *Baseline Observation Carried Forward* (BOCF). This method takes the first known, or baseline value, and carries it forward to the next missing value.

We might use this in medical data where a missing data point for a reported pain level might return to the baseline value.

```python
# Isolate the first (baseline) value for our data
baseline = df['concentration'][0]

# Replace missing values with our baseline value
df['concentration'].fillna(value=baseline, inplace=True)
```

Even further, another option is *Worst Observation Carried Forward* (WOCF). This method takes the worst known value and carries it forward to the next missing value.

```python
# Isolate worst pain value (in this case, the highest)
worst = df['pain'].max()

# Replace all missing values with the worst value
df['pain'].fillna(value=worst, inplace=True)
```

This method is useful when we want to be conservative with our data, and not assume that the missing value is better than it actually is.

## Multiple Imputation

> Imagine you are taking a final exam for a science class. As you go through the test, you find some questions that you can’t remember the answer to, so you decide to take a guess. Later on in the exam, you have jogged your memory a bit because some of the later questions have clues about the earlier answers. Luckily, you can use this new knowledge to go back and fill in the previous guesses — hopefully, you will get a better score on the exam! 
> 
> This kind of iterative process happens all the time in various data and analytical systems, and is something that we can apply to missing data as well. This kind of technique is known as multiple imputation.

This technique works by replacing the missing data multiple times. After we have tried different values, we can use some algorithm to pick the best vaues to replace the missing data. This is a powerful technique that can help us get the most accurate data possible.

> After each iteration, our predicted values for each variable should get more and more accurate, since the models continue to refine to better fit our dataset. The goal of multiple imputation is to fill in the missing data so that it can find a model — typically either a normal or chi-square model — to best fit the dataset.

There are requirements for using multiple imputation: 

> Multiple imputation is best for MAR data, so we should ensure that our data fits that description. With MAR missing data, there is an assumption that there is an underlying reason to have missing data, and we have a good understanding of why that data is missing. Since it is not completely random, using random data to fill in the blanks is not sufficient, so we must use the context of the rest of the data to help.
> 
> Assuming we meet the criteria for using multiple imputation, our dataset will receive a couple key benefits.
> 
> We can safely assume that our data won’t be biased, since we start the process off with a random assignment of values for the missing data.
> Because the goal of multiple imputation is to have a model that fits the data, we can be pretty confident that the resulting data will be a close approximation of the real data. This would include calculations like standard error and overall statistics.

```python
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd

# Create the dataset as a Python dictionary
d = {
    'X': [5.4,13.8,14.7,17.6,np.nan,1.1,12.9,3.4,np.nan,10.2],
    'Y': [18,27.4,np.nan,18.3,49.6,48.9,np.nan,13.6,16.1,42.7],
    'Z': [7.6,4.6,4.2,np.nan,4.7,8.5,3.5,np.nan,1.8,4.7]
}

dTest = {
    'X': [13.1, 10.8, np.nan, 9.7, 11.2],
    'Y': [18.3, np.nan, 14.1, 19.8, 17.5],
    'Z': [4.2, 3.1, 5.7,np.nan, 9.6]
}

# Create the pandas DataFrame from our dictionary
df = pd.DataFrame(data=d)
dfTest = pd.DataFrame(data=dTest)

# Create the IterativeImputer model to predict missing values
imp = IterativeImputer(max_iter=10, random_state=0)

# Fit the model to the test dataset
imp.fit(dfTest)

# Transform the model on the entire dataset
dfComplete = pd.DataFrame(np.round(imp.transform(df),1), columns=['X','Y','Z'])

print(dfComplete.head(10))
```