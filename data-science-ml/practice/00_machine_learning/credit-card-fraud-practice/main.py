# %% import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# %% load data
transactions = pd.read_csv(
    "/Users/harrisonweiss/Documents/GitHub/cuddly-tribble/data-science-ml/practice/00_machine_learning/credit-card-fraud-practice/data.csv"
)

# %% explore data
print(transactions.head())

# %% info
print(transactions.info())

# %% num of fraud
fraud = transactions[transactions["isFraud"] == 1]
print(f"Number of fraudulent transactions: {len(fraud)}")

# %% summary statistics of amount
transactions.amount.describe().apply(lambda x: format(x, "f"))

# %% plot amount
sns.histplot(transactions.amount, bins=100)

plt.tight_layout()
plt.title("Transactions by Amount")
plt.xlabel("Amount")
plt.ylabel("Number of Transactions")

plt.show()
plt.clf()

# %% transactions by type
transactions["isPayment"] = [
    1 if x == "PAYMENT" or x == "DEBIT" else 0 for x in transactions["type"]
]

# %% movement by type
transactions["isMovement"] = [
    1 if x == "CASH_OUT" or x == "TRANSFER" else 0 for x in transactions["type"]
]

# %% display new frame
transactions.info()

# %% head for the new columns
transactions[["isPayment", "isMovement"]].head()

# %% identify difference in account balances
transactions["accountDiff"] = np.abs(
    transactions["oldbalanceOrg"] - transactions["oldbalanceDest"]
)

# %% display new column
transactions["accountDiff"].head()

# %% create features and target
X = transactions[["amount", "isPayment", "isMovement", "accountDiff"]]
y = transactions["isFraud"]

# %% split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# %% scale data
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

# %% fit model
log_reg = LogisticRegression()
log_reg.fit(X_train_scale, y_train)

# %% evaluate model - training data
print(f"Model accuracy: {log_reg.score(X_train_scale, y_train)}")

# %% evaluate model - test data
print(f"Model accuracy: {log_reg.score(X_test_scale, y_test)}")

# %% coeficients
coef_dict = {}
for coef, feat in zip(log_reg.coef_[0, :], X.columns):
    coef_dict[feat] = coef
for k, v in coef_dict.items():
    print(f"{k}: {v:.2f}")
# %% creating predictions from new transactions
# New transaction data
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])

transaction4 = np.array([12345.67, 0.0, 1.0, 2899999.01])
sample = np.stack([transaction1, transaction2, transaction3, transaction4])

# %% scale the new transactions
sample_scaled = scaler.transform(sample)

# %% predict the new transactions
print(log_reg.predict(sample_scaled))

# %% probabilities
print(log_reg.predict_proba(sample_scaled))
