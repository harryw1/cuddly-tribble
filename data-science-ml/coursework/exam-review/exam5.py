import pandas as pd
import statsmodels.api as sm

# load data
students = pd.read_csv("student_data.csv")

# fit the model
model = sm.OLS.from_formula("screentime ~ apps", students)
results = model.fit()

# predict using model parameters
results.params[1] * 30 + results.params[0]

# predict using .predict() method
newdata = {"apps": [30]}
results.predict(newdata)
