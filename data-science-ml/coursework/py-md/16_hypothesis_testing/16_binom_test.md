# Binomial Hypothesis Testing Using Python

## Overview
Binomial hypothesis testing is used to determine if the observed proportion of successes in a sample differs significantly from a hypothesized population proportion. It's based on the binomial distribution, which models the number of successes in a fixed number of independent Bernoulli trials.

### Key Concepts:
- **Null Hypothesis (H0):** The true proportion of successes is equal to a specified value.
- **Alternative Hypothesis (Ha):** The true proportion of successes is different from the specified value.
- **Significance Level (α):** Commonly set at 0.05, it represents the probability of rejecting the null hypothesis when it is actually true.

## Steps for Binomial Hypothesis Testing

1. **Define the Hypotheses:**
   - Null Hypothesis \( H_0 \): \( p = p_0 \)
   - Alternative Hypothesis \( H_a \): \( p \neq p_0 \) (two-tailed), or \( p > p_0 \) / \( p < p_0 \) (one-tailed)

2. **Collect Data:**
   - Number of trials (\( n \))
   - Number of successes (\( x \))

3. **Calculate the Test Statistic:**
   - Use the formula for the z-score:
     \[
     z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0 (1 - p_0)}{n}}}
     \]
   where \( \hat{p} = \frac{x}{n} \) is the sample proportion.

4. **Determine the P-value:**
   - Use the cumulative distribution function (CDF) of the standard normal distribution to find the p-value corresponding to the calculated z-score.

5. **Make a Decision:**
   - Compare the p-value with the significance level \( \alpha \).
   - If \( p\text{-value} < \alpha \), reject the null hypothesis.
   - Otherwise, do not reject the null hypothesis.

## Example Code in Python

```python
import numpy as np
from scipy.stats import norm

# Define parameters
n = 100  # number of trials
x = 60   # number of successes
p0 = 0.5 # hypothesized population proportion
alpha = 0.05

# Calculate sample proportion
phat = x / n

# Calculate the test statistic (z-score)
z = (phat - p0) / np.sqrt(p0 * (1 - p0) / n)

# Determine the p-value for a two-tailed test
p_value = 2 * (1 - norm.cdf(abs(z)))

# Print results
print(f"Z-Score: {z}")
print(f"P-Value: {p_value}")

# Decision
if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Do not reject the null hypothesis.")
