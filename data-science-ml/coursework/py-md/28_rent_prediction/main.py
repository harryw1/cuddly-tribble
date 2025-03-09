import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

streeteasy = pd.read_csv(
    "https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv"
)

df = pd.DataFrame(streeteasy)

x = df[
    [
        "bedrooms",
        "bathrooms",
        "size_sqft",
        "min_to_subway",
        "floor",
        "building_age_yrs",
        "no_fee",
        "has_roofdeck",
        "has_washer_dryer",
        "has_doorman",
        "has_elevator",
        "has_dishwasher",
        "has_patio",
        "has_gym",
    ]
]

y = df[["rent"]]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, test_size=0.2, random_state=6
)

# Add the code here:

mlr = LinearRegression()

mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

my_apt = [[1, 1, 625, 6, 5, 130, 0, 0, 0, 0, 0, 1, 0, 0]]

my_predict = mlr.predict(my_apt)

print(f"Predicted rent: {my_predict}")
