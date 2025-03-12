# %% import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# %% Load data
col_names = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "income",
]
df = pd.read_csv(
    "/home/hweiss/Documents/git/cuddly-tribble/data-science-ml/practice/00_machine_learning/roc_auc/adult.data",
    header=None,
    names=col_names,
)

# %% Clean columns by stripping extra whitespace for columns of type "object"
for c in df.select_dtypes(include=["object"]).columns:
    df[c] = df[c].str.strip()
print(df.head())

# %% 1. Check Class Imbalance
print(df.income.value_counts(normalize=True))

# %% 2. Create feature dataframe X with feature columns and dummy variables for categorical features
feature_cols = [
    "age",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "sex",
    "race",
    "hours-per-week",
    "education",
]
X = pd.get_dummies(df[feature_cols], drop_first=True)


# %% 3. Create a heatmap of X data to see feature correlation
sns.heatmap(X.corr(), annot=True, cmap="coolwarm")
plt.tight_layout()
plt.title("Heatmap of Feature Correlation")
plt.show()
plt.clf()

# %% 4. Create output variable y which is binary, 0 when income is less than 50k, 1 when it is greater than 50k
y = pd.get_dummies(df["income"], drop_first=True)


# %% 5a. Split data into a train and test set
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# %% 5b. Fit LR model with sklearn on train set, and predicting on the test set
log_reg = LogisticRegression(C=0.05, penalty="l1", solver="liblinear")
log_reg.fit(x_train, y_train)
y_pred = log_reg.predict(x_test)

# %% 6. Print model parameters (intercept and coefficients)
print(f"Model Parameters, Intercept: {log_reg.intercept_}")

print(f"Model Parameters, Coeff: {log_reg.coef_}")


# %% 7. Evaluate the predictions of the model on the test set. Print the confusion matrix and accuracy score.
confusion_test = confusion_matrix(y_test, y_pred)
accuracy_test = accuracy_score(y_test, y_pred)
print(f"Confusion Matrix on test set: \n{confusion_test}")
print(f"Accuracy Score on test set:\n{accuracy_test}")

# %% 8.Create new DataFrame of the model coefficients and variable names; sort values based on coefficient
df_coef = pd.DataFrame(
    {"Variable": x_train.columns, "Coefficient": log_reg.coef_[0]}
)
df_coef = df_coef.sort_values(by="Coefficient", ascending=False)
df_coef.head()

# %% 9. barplot of the coefficients sorted in ascending order
sns.barplot(
    x="Coefficient", y="Variable", data=df_coef.sort_values(by="Coefficient")
)
plt.tight_layout()
plt.title("Coefficients of Logistic Regression Model")
plt.show()
plt.clf()


# %% 10. Plot the ROC curve and print the AUC value.
y_pred_prob = log_reg.predict_proba(x_test)
roc_auc = roc_auc_score(y_test, y_pred_prob[:, 1])
print(roc_auc)
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob[:, 1])
plt.plot(
    fpr,
    tpr,
    color="navy",
    linestyle="-",
    label="ROC curve (area = %0.2f)" % roc_auc,
)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.plot([0, 1], [0, 1], color="red", linestyle="--")
plt.title("ROC Curve")
plt.grid()
plt.legend(loc="lower right")
plt.show()
