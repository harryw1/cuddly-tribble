# %% Import libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# %% load and investigate the data here
df = pd.read_csv(
    "/home/hweiss/Documents/cuddly-tribble/data-science-ml/practice/00_machine_learning/tennis_ace_starting/tennis_stats.csv"
)
df.info()

# %% view example data
df.head()

# %% describe
df.describe()

# %% perform exploratory analysis here:
import seaborn as sns
from sklearn.feature_selection import f_regression

# setting our features to everything but winnings and our target to winnings
X = df.drop(["Wins", "Player", "Winnings", "Year"], axis=1)
y = df["Wins"]

# calculating the F-values and p-values
F_values, p_values = f_regression(X, y)

feature_names = X.columns

# creating a list of tuples with the feature names and their F-values
feature_importance = [
    (name, F, p) for name, F, p in zip(feature_names, F_values, p_values)
]

# sort that list of tuples by the F-values
feature_importance.sort(key=lambda x: x[1], reverse=True)

for name, importance, p_value in feature_importance:
    print(f"Feature {name}: F-value = {importance}, p-value = {p_value}")

# %% plotting the feature importances
# Extract sorted names and F-values for plotting
# Sort feature importance
feature_importance = [
    (name, F, p) for name, F, p in zip(feature_names, F_values, p_values)
]
feature_importance.sort(key=lambda x: x[1], reverse=True)

# Extract sorted names and F-values for plotting
sorted_names = [item[0] for item in feature_importance]
sorted_f_values = [item[1] for item in feature_importance]

# Create a figure with a larger size for readability
plt.figure(figsize=(12, 10))

# Create horizontal bar chart
sns.barplot(x=sorted_f_values, y=sorted_names, palette="viridis")

# Add labels and title
plt.title(
    "Feature Importance for Predicting Tennis Player Winnings", fontsize=16
)
plt.xlabel("F-Value (higher means more important)", fontsize=14)
plt.ylabel("Feature", fontsize=14)

# Add grid lines for readability
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()

# %% perform single feature linear regressions here:

# using a single feature to predict winnings
feature = X[["ServiceGamesPlayed"]]
target = df["Winnings"]

x_train, x_test, y_train, y_test = train_test_split(
    feature, target, test_size=0.2, random_state=42
)

# instantiate the model
model = LinearRegression()

# fit the model
model.fit(x_train, y_train)
model.score(x_test, y_test)
# %% creating the first prediction
pred_service = model.predict(x_test)

# %% plotting the pred_service against the actual y_test
plt.scatter(x_test, y_test, color="green", alpha=0.4, label="Actual Wins")
plt.plot(
    x_test, pred_service, color="blue", linestyle="--", label="Predicted Wins"
)
plt.xlabel("Service Games Played")
plt.ylabel("Winnings")

plt.tight_layout()
plt.legend()
plt.show()
plt.clf()

# %% creating a breakpointsfaced model
feature = X[["BreakPointsFaced"]]
target = df["Winnings"]

x_train, x_test, y_train, y_test = train_test_split(
    feature, target, test_size=0.2, random_state=42
)

# instantiate the model
model = LinearRegression()

# fit the model
model.fit(x_train, y_train)
model.score(x_test, y_test)

# creating the prediction for breakpointsfaced
pred_breakpoints = model.predict(x_test)

# %% plotting the pred_breakpoints against the actual y_test
plt.scatter(x_test, y_test, alpha=0.4, label="Actual Wins")
plt.plot(
    x_test,
    pred_breakpoints,
    color="red",
    alpha=0.4,
    linestyle="--",
    label="Predicted Wins",
)
plt.xlabel("Break Points Faced")
plt.ylabel("Wins")

plt.tight_layout()
plt.legend()
plt.show()
plt.clf()

# %% perform two feature linear regressions here:
# set features for the two-feature regression
features = X[["DoubleFaults", "Aces"]]
target = df["Wins"]

# split the data
x_train, x_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2
)

# instantiate the model
model = LinearRegression()

# fit the model
model.fit(x_train, y_train)
print(model.score(x_test, y_test))
print(model.coef_)

# creating the prediction for the two-feature model
pred_faults_aces = model.predict(x_test)

# %% plotting the pred_faults_aces against the actual y_test
# Creating a plot of actual vs. predicted winnings
plt.figure(figsize=(10, 8))

# Scatter plot of actual vs. predicted values
plt.scatter(y_test, pred_faults_aces, alpha=0.7, color="blue")

# Add a diagonal line representing perfect predictions
# (where actual equals predicted)
min_val = min(y_test.min(), pred_faults_aces.min())
max_val = max(y_test.max(), pred_faults_aces.max())
plt.plot(
    [min_val, max_val],
    [min_val, max_val],
    "r--",
    lw=2,
    label="Perfect Prediction",
)

# Add labels and title
plt.xlabel("Actual Wins", fontsize=12)
plt.ylabel("Predicted Wins", fontsize=12)
plt.title("Actual vs. Predicted Wins (Double Faults & Aces Model)", fontsize=14)

# Add a grid for better readability
plt.grid(True, alpha=0.3, linestyle="--")

# Add a legend
plt.legend(loc="best")

# Make sure the axes are equal in scale
plt.axis("equal")
# Or alternatively set the same limits for both axes:
# plt.xlim([min_val, max_val])
# plt.ylim([min_val, max_val])

plt.tight_layout()
plt.show()

# %% perform multiple feature linear regressions here:
# set features for the multiple-feature regression
features = X[
    [
        "ServiceGamesPlayed",
        "ReturnGamesPlayed",
        "ServiceGamesWon",
        "ReturnGamesWon",
        "Aces",
    ]
]
y = df["Wins"]

# split the data
x_train, x_test, y_train, y_test = train_test_split(features, y, test_size=0.2)

# instantiate the model
model = LinearRegression()

# fit the model
model.fit(x_train, y_train)
print(model.score(x_test, y_test))
print(model.coef_)

# creating the prediction for the multiple-feature model
pred_multiple = model.predict(x_test)

# %% plotting the pred_multiple against the actual y_test
# Creating a plot of actual vs. predicted wins
plt.figure(figsize=(10, 8))

# Scatter plot of actual vs. predicted values
plt.scatter(y_test, pred_multiple, alpha=0.7, color="blue")

# Add a diagonal line representing perfect predictions
# (where actual equals predicted)
min_val = min(y_test.min(), pred_multiple.min())
max_val = max(y_test.max(), pred_multiple.max())
plt.plot(
    [min_val, max_val],
    [min_val, max_val],
    "r--",
    lw=2,
    label="Perfect Prediction",
)

# Add labels and title
plt.xlabel("Actual Wins", fontsize=12)
plt.ylabel("Predicted Wins", fontsize=12)

plt.title("Actual vs. Predicted Wins (Multiple Features Model)", fontsize=14)

# Add a grid for better readability
plt.grid(True, alpha=0.3, linestyle="--")

# Add a legend
plt.legend(loc="best")

# Make sure the axes are equal in scale
plt.axis("equal")

plt.tight_layout()
plt.show()
plt.clf()
