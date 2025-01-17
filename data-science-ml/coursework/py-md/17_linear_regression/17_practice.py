"""Module performs data analysis and visualization on Codecademy data.

It reads data from a CSV file, creates scatter plots, fits linear regression models,
checks assumptions of the models, and visualizes the results using various plots.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())

# Create a scatter plot of score vs completed
plt.scatter(x=codecademy.completed, y=codecademy.score)
# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', data=codecademy)
results = model.fit()
print(results.params)

# Intercept interpretation:
# When courses completed is 0, score is 13.214113
# Slope interpretation:
# For each course completed, score increases by 1.306826

# Plot the scatter plot with the line on top
plt.scatter(x=codecademy.completed, y=codecademy.score)
plt.plot(codecademy.completed, results.predict(codecademy))
# Show then clear plot
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
complete = {"completed": 20}
items_20 = results.predict(complete)
print(items_20)

# Calculate fitted values
fitted_values = results.predict(codecademy)

# Calculate residuals
residuals = codecademy.score - fitted_values

# Check normality assumption
plt.hist(residuals)
# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(y=residuals, x=fitted_values)
# Show then clear the plot
plt.show()
plt.clf()

# Create a boxplot of score vs lesson
sns.boxplot(y=codecademy.score, x=codecademy.lesson)
# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', data=codecademy)
results = model.fit()
print(results.params)

# Calculate and print the group means and mean difference (for comparison)
mean1 = np.mean(codecademy.score[codecademy.lesson == 'Lesson A'])
mean2 = np.mean(codecademy.score[codecademy.lesson == 'Lesson B'])
print(mean1, mean2)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x='completed', y='score', hue='lesson', data=codecademy)
plt.show()
plt.clf()
