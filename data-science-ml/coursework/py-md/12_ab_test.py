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

# %% checking data types
ad_clicks.info()
print(ad_clicks['ad_click_timestamp'].isna().sum())  # Count of NaN values

# %% add column for true if clicked
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)
# %% count of group from utm source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

# %% pivoted table
clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id'
)
print(clicks_pivot)

# %% calculated on pivot
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) * 100
print(clicks_pivot)
# %% experimental
print(ad_clicks['experimental_group'])

# %% ad counts
experimental = ad_clicks.groupby(['experimental_group', 'is_click']).count().reset_index()
print(experimental.pivot(
    columns='is_click',
    index='experimental_group',
    values='user_id'
))

# %% clicks by day
a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']
b_clicks = ad_clicks[
    ad_clicks.experimental_group
    == 'B'
]

# %% num count by day
a_by_day = a_clicks.groupby(['is_click', 'day']).count().reset_index()
a_by_day_pivot = a_by_day.pivot(
    columns='is_click',
    index='day',
    values='user_id')
b_by_day = b_clicks.groupby(['is_click', 'day']).count().reset_index()
b_by_day_pivot = b_by_day.pivot(
    columns='is_click',
    index='day',
    values='user_id')
print(b_by_day_pivot)
# %% a percent click by day
a_by_day_pivot['percent_click'] = a_by_day_pivot[True] / (a_by_day_pivot[False] + a_by_day_pivot[True]) * 100
print(a_by_day_pivot)

# %% b percent click by day
b_by_day_pivot['percent_click'] = b_by_day_pivot[True] / (b_by_day_pivot[False] + b_by_day_pivot[True]) * 100
print(b_by_day_pivot)
