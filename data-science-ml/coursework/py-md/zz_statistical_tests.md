# Statistical Tests in Python

This document outlines several statistical tests, their applications, and Python implementations using libraries like `scipy.stats` and `statsmodels`.  Note that the examples provided are simplified and may require adjustments based on specific datasets and research questions.  It is crucial to consult statistical literature and potentially a statistician for complex analyses.

This information is current as of the above date.  Statistical methods and software packages are constantly evolving, so it's essential to verify the latest best practices.

## T-tests

* **Purpose:** Compare means between two groups.
* **Types:**
  * **Independent samples t-test:**  For comparing means of two independent groups (e.g., treatment vs. control).
  * **Paired samples t-test:** For comparing means of two related groups (e.g., pre-test vs. post-test scores).
  * **One-sample t-test:** For comparing the mean of a sample to a known population mean.
* **Assumptions:**  Data should be approximately normally distributed, especially with smaller sample sizes.  Independent samples t-test assumes equal variances between groups (unless Welch's t-test is used).
* **Python Example (Independent samples t-test):**

```python
import scipy.stats as st

group1 = [1, 2, 3, 4, 5]
group2 = [6, 7, 8, 9, 10]

t_statistic, p_value = st.ttest_ind(group1, group2)
print(f"T-statistic: {t_statistic:.2f}")
print(f"P-value: {p_value:.3f}")
```

## ANOVA (Analysis of Variance)

* **Purpose:** Compare means between three or more groups.
* **Types:**
  * **One-way ANOVA:** One independent variable with three or more levels.
  * **Two-way ANOVA:** Two or more independent variables.
* **Assumptions:**  Data should be approximately normally distributed within each group.  Homogeneity of variances across groups.
* **Python Example (One-way ANOVA):**

```python
import statsmodels.formula.api as sm

data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'], 'value': [1, 2, 3, 4, 5, 6]}
import pandas as pd
df = pd.DataFrame(data)

model = sm.ols('value ~ C(group)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
```

## Chi-Square Test

* **Purpose:** Analyze categorical data to determine if there's an association between variables.
* **Types:**
  * **Chi-square test of independence:**  For testing the association between two categorical variables.
  * **Chi-square goodness-of-fit test:** For testing if a sample distribution matches a hypothesized distribution.
* **Assumptions:** Expected cell counts should be sufficiently large (generally > 5).
* **Python Example (Chi-square test of independence):**

```python
import scipy.stats as st
import numpy as np

observed = np.array([[10, 20], [30, 40]])
chi2, p, dof, expected = st.chi2_contingency(observed)
print(f"Chi-square statistic: {chi2:.2f}")
print(f"P-value: {p:.3f}")
```

## Correlation

* **Purpose:** Measure the strength and direction of the linear relationship between two continuous variables.
* **Types:** Pearson correlation, Spearman rank correlation (for non-linear relationships).
* **Assumptions:** Pearson correlation assumes linearity and normally distributed data.
* **Python Example (Pearson correlation):**

```python
import scipy.stats as st

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

correlation, p_value = st.pearsonr(x, y)
print(f"Correlation coefficient: {correlation:.2f}")
print(f"P-value: {p_value:.3f}")
```

### Regression

* **Purpose:** Model the relationship between a dependent variable and one or more independent variables.
* **Types:** Linear regression, multiple regression, logistic regression.
* **Assumptions:** Linear regression assumes linearity, independence of errors, constant variance of errors (homoscedasticity), and normality of errors.
* **Python Example (Linear Regression):**

```python
import statsmodels.api as sm

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]
x = sm.add_constant(x)  # Add an intercept term

model = sm.OLS(y, x).fit()
print(model.summary())
```

## Non-parametric Tests

These tests are used when the assumptions of parametric tests are not met (e.g., non-normal data). Examples include:

* **Mann-Whitney U test:** Non-parametric equivalent of the independent samples t-test.
* **Wilcoxon signed-rank test:** Non-parametric equivalent of the paired samples t-test.
* **Kruskal-Wallis test:** Non-parametric equivalent of one-way ANOVA.


