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
