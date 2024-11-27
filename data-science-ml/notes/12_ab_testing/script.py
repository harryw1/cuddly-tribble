# %% imports
import pandas as pd
import numpy as np

# %% initial dataframe
ad_clicks = pd.read_csv('ad_clicks.csv')
# %% examine the first few rows
print(ad_clicks.head())

# %% number of views per utm_source
views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views)
