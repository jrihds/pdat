#!/usr/bin/env python
"""Basic operations on dataframes."""

import pandas as pd

# This script isn't for execution, just for notes

# explore the shape and contents of a dataframe
df.describe()
df.info()
df.shape
df.columns
df.index
df.head(10)
df.tail(10)

type(df)
# <class 'pandas.core.frame.DataFrame'>
type(df['a'])
# <class 'pandas.core.series.Series'>
type(df['a'].values)
# <class 'numpy.ndarray'>

# copy a dataframe
df2 = df.copy()

# create a new index column
df.reset_index()

# Drop any row containing 'NaN'
df.dropna()

# double brackets returns dataframe
df[['a']]
df[['a', 'c']]

# single brackets returns a Series
series = df["a"]

# iloc uses numbers, 0 based indexing
# [row, column]
df.iloc[:5, :]      # first 5 rows, all columns
df.iloc[-5:, :]     # last 5 rows, all columns
df.iloc[:, 1]       # all rows, second column

# loc use text labels
df.loc[:, 'b':]     # all rows, columns 'b' onwards
df.loc[3, 'a']      # row 4 from column 'a'

# Filter on a multi level index
#        a
# one 0  1
#     1  2
#     2  3
# two 0  4
#     1  5
#     2  6

df.loc['one']

#    a
# 0  1
# 1  2
# 2  3

 # Filter on inner label
idx = pd.IndexSlice
df.loc[idx[:, 1], :]

#        a
# one 1  2
# two 1  5


# Convet df column type into a data type
df['a'].astype(int)

# Coerce the column to into a numeric type
df['number'] = pd.to_numeric(df['number'], errors='coerce')

# Apply a lambda function over each row in a df
df['d'] = df['a'].apply(lambda x: x+1)
df['d'] = df.apply(lambda x: x['a']+1, axis=1)

# Drop duplicates
df = df.drop_duplicates()

# Calculate statitstics for a column
df['a'].median()
df['a'].std()
df['a'].mean()
df['a'].mode()

# Fill missing values in a column
df['a'] = df.a.fillna(0)

# Count non null values
df['a'].count()

# Print the 5th and 95th percentiles
df.quantile([0.05, 0.95])

# rolling window across data
# Given
#    0
# 0  0
# 1  1
# 2  2
# 3  3
# 4  4
# 5  5
# 6  6
# 7  7
# 8  8
# 9  9

df.rolling(5).max()

#      0
# 0  NaN
# 1  NaN
# 2  NaN
# 3  NaN
# 4  4.0
# 5  5.0
# 6  6.0
# 7  7.0
# 8  8.0
# 9  9.0

df.rolling(5).mean()

#      0
# 0  NaN
# 1  NaN
# 2  NaN
# 3  NaN
# 4  2.0  (0+1+2+3+4)/5 = 2
# 5  3.0
# 6  4.0
# 7  5.0
# 8  6.0
# 9  7.0


# Sort values based on index
df.sort_index()
df.sort_index(ascending=False)

# Sort values based on column
df.sort_values('Max TemperatureF')

# reindex sorts the index according to a list
#    a
# 0  0
# 1  1
# 2  2
# 3  3
# 4  4

df.reindex([4, 3, 2, 1, 0])

#    a
# 4  4
# 3  3
# 2  2
# 1  1
# 0  0

# ffil adds values if the new list contains indexes not in the dataframe
df.reindex([0, 1, 2, 3, 4, 5, 6, 7]).ffill()

#      a
# 0  0.0
# 1  1.0
# 2  2.0
# 3  3.0
# 4  4.0
# 5  4.0
# 6  4.0
# 7  4.0
