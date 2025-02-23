import pandas as pd

df = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data",
    names=["buying", "maint", "doors", "persons", "lug_boot", "safety", "accep"],
)
print(df.head())


# Create target variable array 'y' and set it to have a binary outcome 
# by transforming df['accep']
y = df['accep'].map({'unacc': 0, 'acc': 1, 'good': 1, 'vgood': 1})

# Create feature matrix 'X' by transforming the rest of the columns to 
# be one-hot encoded variables
X = pd.get_dummies(df.drop('accep', axis=1))
