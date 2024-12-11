"""Module to practice using plots and summary statistics in Python."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():
    # Load the data
    students = pd.read_csv("14_summary_stats.csv")

    # Display the first few rows of the data
    print(students.head())

    # Summary statistics
    print(students.describe())

    # Calculate the mean
    print(students.math_grade.mean())

    # Calculate the median
    print(students.math_grade.median())

    # Calculate the mode
    print(students.math_grade.mode())


if __name__ == "__main__":
    main()
