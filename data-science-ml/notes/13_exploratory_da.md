# Exploratory Data Analysis

We're now coming to the point where we are bringning
together the different concepts we've learned.
Earlier in the course we learned about exploratory data
analysis in a non-python setting, and now we are going
to go into a deeper dive of the concept and how to apply
those techniques.

## Learning Outcomes

After this course, you will be able to:

1. Identify different variable types
2. Determine what kinds of analysis are appropriate based
   on the variable type
3. Summarize a single variable
4. Summarize the relationship between two variables
5. Inspect and clean a dataset.

## What is EDA?

_Exploratory Data Analysis_ or EDA, is about exploring the
dataset and determining things like:

- data structure, layout, and coding,
- summarzing and visualizing data,
- detecting ouliers, missing data, or other
  issues with the data set and how to address them,
- and finding avenues for further research and model building
  and analysis.

## Techniques

Techniques for EDA usually fall under three categories:

1. Data inspection
2. Numerical summarization
3. Data visualization

### Inspection

Easy enough:

```python
print(data.head())
```

will allow us to view the dataset's first five rows and
any kinds of data we may be dealing with.

### Summarization

Again, numerical summaries are a great way to condense
information once we've done some data cleaning:

```python
data.describe(include = 'all')
```

The `.describe()` method of the DataFrame object allows
us to perform some common operations across the entire
dataset.

### Visualization

We can also use other functions to create things like
histograms, scatterplots, and other visual representations
of the relationships between the data points.
