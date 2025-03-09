import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#import data
reviews = pd.read_csv('reviews.csv')

#print column names and info
print(reviews.columns)
print(reviews.info())

#look at the counts of recommended
print(reviews['recommended'].value_counts())

#create binary dictionary
binary_dict = {True: 1, False: 0}

#transform column
reviews['transformed_column'] = reviews['recommended'].map(binary_dict)

#print your transformed column
print(reviews['transformed_column'].value_counts())

#look at the counts of rating
print(reviews['rating'].value_counts())

#create dictionary
rating_dict = {"Loved it": 5,
                "Liked it": 4,
                "Was okay": 3,
                "Not great": 2,
                "Hated it": 1}


#transform rating column
reviews['transformed_rating'] = reviews['rating'].map(rating_dict)

#print your transformed column values
print(reviews['transformed_rating'].value_counts())

#get the number of categories in a feature
print(reviews.department_name.value_counts())

#perform get_dummies
department_dummies = pd.get_dummies(reviews['department_name'])

#join the new columns back onto the original
reviews = pd.concat([reviews, department_dummies], axis=1)

#print column names
print(reviews.info())

#transform review_date to date-time data
reviews['review_date'] = pd.to_datetime(reviews['review_date'])

#print review_date data type
print(reviews['review_date'].dtype)

#get numerical columns
numerical = reviews.select_dtypes(include=[np.number])

#reset index
numerical = numerical.set_index('clothing_id')
print(numerical.head())

#instantiate standard scaler
scaler = StandardScaler()

#fit transform data
numerical_scaled = scaler.fit_transform(numerical)

#convert to dataframe
numerical_scaled = pd.DataFrame(numerical_scaled, columns=numerical.columns)

print(numerical_scaled.head())
