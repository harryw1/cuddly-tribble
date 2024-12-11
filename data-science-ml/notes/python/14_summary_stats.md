# Summary Statistics

Critical to a data scientist is the ability to summarize and condense
a large amount of data into a few key statistics. In order to decide
what kinds of summary statistics to use, it is important to understand
two things:

1. The question being asked (and how many variables are involved)
2. The type of data being analyzed (quantitative or categorical)

## Univariate Statistics

Univariate statistics are statistics that describe a single variable.
They are useful for answering questions about a single feature in tabular
data. Some questions we might ask about a table on cars include:

- How much does a typical car cost?
- What proportion of cars have a manual transmission?
- How old is the oldest listed car?

## Quantitative Variables

When summarizing quantitative variables, we are most often interested in
the center and spread of the data.

### Central Location

Central location, or central tendency, is often used to communicate
the "typical" value of a dataset. The most common measures of central
location are the mean, median, and mode. We also have the "trimmed mean"
which is the mean of a dataset with a certain percentage of the smallest
and largest values removed.

Some times we need to know a little bit about the dataset we are working
with because the mean and median can be very different. For example, if
we have a dataset with a few very large values, the mean will be much
larger than the median.

### Spread

Spread, or dispersion, describes the variability within a feature. It
can provide context for the measures of central location. To measure
spread, we can use the range, interquartile range, variance, standard
deviation, and mean absolute deviation (the mean absolute value of the
distance between each data point and the mean).

IQR is often useful because it will trim away outliers in the data. When
variance is large, using the MAD can be more informative and is less
impacted by outliers than standard deviation.

## Categorical Variables

When summarizing categorical variables, we are most often interested in
the frequency and proportion of each category. We can visualize this
information using a frequency table and a bar chart.

In practice, this may look like this:

```python
cars.fuel.value_counts()
```

Which would return a frequency table of the fuel types in the `cars`, but
we may want to take this one step further and convert these frequencies
to proportions to compare across categories more easily.

```python
cars.fuel.value_counts(normalize=True)
```

## Bivariate Statistics

Bivariate statistics are statistics that describe the relationship between
two variables. They are useful for answering questions like:

- Do manual transmission cars tend to cost more or less than automatic
  transmission cars?
- Do older cars tend to cost less money?
- Are automatic transmission cars more likely to be sold by individuals
  or dealerships?

Depending on the variables, we should choose different summary statistics.

### Quantitative and Categorical

> If we want to know whether manual transmission cars tend to cost more
or less than automatic transmission cars, we are interested in the
relationship between transmission (categorical) and selling_price
(quantitative). To answer this question, we can use a mean or median
difference. For example, we could calculate that the median price of
automatic transmission cars is 100000 Rupees higher than for manual
transmission cars.

### Quantitative and Quantitative

> If we want to know whether older cars tend to cost less money, we are
interested in the relationship between `year` and `selling_price`, both
of which are quantitative. To answer this question, we can use the Pearson
correlation. For example, if we calculate that the correlation between
`year` and `selling_price` is 0.4, we can conclude that there is a
moderate positive relationship between the two variables (older cars
do tend to cost less money).

### Categorical and Categorical

> If we want to know whether automatic transmission cars are more likely
to be sold by individuals or dealers, we are interested in the
relationship between `transmission` and `seller_type`, both of which are
categorical. We can explore this relationship using a contingency table
and the Chi-Square statistic.

> [!note] Chi-Square
> Dr. Wiener would argue that the chi-square statistic is a weak test
and that it is a last resort.

## Example of Overlapping Histogram Setup

```python
    #create the overlapping histograms here:
    plt.hist(scores_urban, color="blue", label="Urban", normed=True, alpha=0.5)
    plt.hist(scores_rural, color="red", label="Rural", normed=True, alpha=0.5)
    plt.legend()
    plt.show()
```
