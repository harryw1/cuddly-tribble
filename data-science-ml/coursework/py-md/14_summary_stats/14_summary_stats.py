"""Module to practice using plots and summary statistics in Python."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns


def main():
    """Analyze student data with summary statistics."""
    # Load the data
    students = pd.read_csv("14_summary_stats.csv")

    # Display the first few rows of the data
    print(students.head(), "\n")

    # Summary statistics
    print(f'Summary Stats:\n {students.describe(include="all")}', "\n")

    # Calculate the mean
    print(f"Mean: {students.math_grade.mean()}")

    # Calculate the median
    print(f"Median: {students.math_grade.median()}")

    # Calculate the mode
    print(f"Mode: {students.math_grade.mode()}")

    # Calculate the range
    range = students.math_grade.max() - students.math_grade.min()
    print(f"Range: {range}")

    # Calculate mean absolute deviation
    print(f"Mean Absolute Deviation: {mad(students.math_grade):.2f}")

    # Alternatively, calculate median absolute deviation
    print(
        f"Median Absolute Deviation: {stats.median_abs_deviation(students.math_grade):.2f}"
    )

    # Visualize the data in a histogram
    # histvisual(students.math_grade)

    # Visualize the data in a boxplot
    # boxplot(students.math_grade)

    # Summary of mothers' jobs
    print(f"Frequency of mother's jobs: \n{students.Mjob.value_counts()}")

    # Mother's job as a percentage
    print(
        f"Mother's job as a percentage: \n{students.Mjob.value_counts(normalize=True)}"
    )

    # Summary of father's jobs
    print(f"Frequency of father's jobs: \n{students.Fjob.value_counts()}")

    # Father's job as a percentage
    print(
        f"Father's job as a percentage: \n{students.Fjob.value_counts(normalize=True)}"
    )

    # Countplot of mother jobs
    countplot(students.Mjob)

    # Pie chart of mother jobs
    piechart(students.Mjob)


def mad(data):
    """Calculate the mean absolute deviation."""
    return np.mean(np.abs(data - np.mean(data)))


def histvisual(data):
    """Return a histogram and a boxplot of the data."""
    sns.histplot(data)
    plt.show()
    plt.close()


def boxplot(data):
    """Return a boxplot of the data."""
    sns.boxplot(data)
    plt.show()
    plt.close()


def countplot(data):
    """Return a countplot of the data."""
    sns.countplot(data)
    plt.show()
    plt.close()


def piechart(data):
    """Return a pie chart of the data."""
    data.value_counts().plot.pie()
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()
