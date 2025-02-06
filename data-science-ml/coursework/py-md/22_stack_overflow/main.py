"""Walkthrough of the Stack Overflow Developer Survey dataset."""

# %% Imports
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %% Load data
df = pd.read_csv("developer_dataset.csv")

# %% Display data
print(df.head())
print(df.info)
print(df.columns)
# %% Count of records
print(df.count())

# %% Basic Summary Statistics
df.describe()
# %% Missing values
maxRows = df["RespondentID"].count()

print("% Missing Data:")
print((1 - df.count() / maxRows) * 100)
# %% Drop columns with > 60% missing data
df.drop(["NEWJobHunt", "NEWJobHuntResearch", "NEWLearn"], axis=1, inplace=True)

# %% Visualize missing data
df[["RespondentID", "Country"]].groupby("Country").count()

missingData = (
    df[["Employment", "DevType"]].isnull().groupby(df["Country"]).sum().reset_index()
)

A = sns.catplot(
    data=missingData,
    kind="bar",
    x="Country",
    y="Employment",
    height=6,
    aspect=2,
    hue="Country",
)
B = sns.catplot(
    data=missingData,
    kind="bar",
    x="Country",
    y="DevType",
    height=6,
    aspect=2,
    hue="Country",
)

# %% Drop rows with missing data
# We can drop rows with data missing from the two
# columns we explored above because we have
# determined that they are MCAR.
df.dropna(subset=["Employment", "DevType"], inplace=True, how="any")

# %% Group by developer type and employment
empfig = sns.catplot(
    x="Country",
    col="Employment",
    hue="Country",
    data=df,
    kind="count",
    height=6,
    aspect=1.5,
)
# Focus on a few of the key developer types outlined in the Stack Overflow survey
devdf = df[["Country", "DevType"]]
devdf.loc[devdf["DevType"].str.contains("back-end"), "BackEnd"] = True
devdf.loc[devdf["DevType"].str.contains("front-end"), "FrontEnd"] = True
devdf.loc[devdf["DevType"].str.contains("full-stack"), "FullStack"] = True
devdf.loc[devdf["DevType"].str.contains("mobile"), "Mobile"] = True
devdf.loc[devdf["DevType"].str.contains("administrator"), "Admin"] = True

devdf = devdf.melt(
    id_vars=["Country"],
    value_vars=["BackEnd", "FrontEnd", "FullStack", "Mobile", "Admin"],
    var_name="DevCat",
    value_name="DevFlag",
)

devdf.dropna(how="any", inplace=True)

devFig = sns.catplot(
    x="Country",
    col="DevCat",
    data=devdf,
    kind="count",
    hue="Country",
    height=6,
    aspect=1.5,
)

# %% Missing data in UndergradMajor

missingUndergrad = df["UndergradMajor"].isnull().groupby(df["Year"]).sum().reset_index()

sns.catplot(
    x="Year", y="UndergradMajor", data=missingUndergrad, kind="bar", height=4, aspect=1
)

# %% Sort missing data
# Sort by ID and Year so that each person's data is carried backwards correctly
df = df.sort_values(['RespondentID','Year'])

df['UndergradMajor'].bfill(axis=0, inplace=True)

# %% Visualize education data
# Key major groups outlined in the Stack Overflow survey
majors = ['social science','natural science','computer science','development','another engineering','never declared']

edudf = df[['Year','UndergradMajor']]
edudf.dropna(how='any', inplace=True)
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)social science'), 'SocialScience'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)natural science'), 'NaturalScience'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)computer science'), 'ComSci'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)development'), 'ComSci'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)another engineering'), 'OtherEng'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)never declared'), 'NoMajor'] = True

edudf = edudf.melt(id_vars=['Year'], 
    value_vars=['SocialScience','NaturalScience','ComSci','OtherEng','NoMajor'], 
    var_name='EduCat',
    value_name='EduFlag')

edudf.dropna(how='any', inplace=True)
edudf = edudf.groupby(['Year','EduCat']).count().reset_index()

eduFig = sns.catplot(x="Year", y='EduFlag', col="EduCat",
                data=edudf, kind="bar",
                height=6, aspect=1.5)

# %% Experience data verus salary
compFields = df[['Year','YearsCodePro','ConvertedComp']]

D = sns.boxplot(x="Year", y="YearsCodePro",
            data=compFields)
plt.show()
plt.clf()

E = sns.boxplot(x="Year", y="ConvertedComp",
            data=compFields)
plt.show()
plt.clf()

# %% Multiple imputation to fill missing data
# Fill missing data within the dataset for the YearsCodePro and ConvertedComp columns
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split

imputedf = df[['YearsCodePro','ConvertedComp']]

traindf, testdf = train_test_split(imputedf, train_size=0.1)

# Create the IterativeImputer model to predict missing values
imp = IterativeImputer(max_iter=20, random_state=0)

# Fit the model to the the test dataset
imp.fit(imputedf)

# Transform the model on the entire dataset
compdf = pd.DataFrame(np.round(imp.transform(imputedf),0), columns=['YearsCodePro','ConvertedComp'])
# %% Visualize the imputed data
compPlotdf = compdf.loc[compdf['ConvertedComp'] <= 150000]
compPlotdf['CodeYearBins'] = pd.qcut(compPlotdf['YearsCodePro'], q=5)

sns.boxplot(x="CodeYearBins", y="ConvertedComp",
            data=compPlotdf)
