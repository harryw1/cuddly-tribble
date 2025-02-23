import pandas as pd
import statsmodels.api as sm

# load data
coffee = pd.read_csv("coffee.csv")

# run and fit the model
model = sm.OLS.from_formula("sales ~ temp", data=coffee)
results = model.fit()

# print the model params
print(results.params)

# calculate `pred_75`
new_data = {"temp": 75}
pred_75 = results.predict(new_data)
