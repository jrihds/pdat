#!/usr/bin/env python
"""Joining two or more dataframes together."""

import pandas as pd

# Use concat/append when to stack dfs vertically or horizontally
# Use merge when joining data between columns in two DataFrames

d1 = {'Column_A': ['a', 'a', 'a', 'c', 'c', 'd'],
      'Column_B': [1, 2, 3, 4, 5, 6]}
df1 = pd.DataFrame(d1)

d2 = {'Column_A': ['a', 'a', 'b', 'c', 'c', 'c'],
      'Column_B': [5, 3, 6, 6, 8, 9]}
df2 = pd.DataFrame(d2)

# Different join methods

# Stack two dfs together
df = df1.append(df2)
# same as
df = pd.concat([df1, df2])
print(df)

#   Column_A  Column_B
# 0        a         1
# 1        a         2
# 2        a         3
# 3        c         4
# 4        c         5
# 5        d         6
# 0        a         5
# 1        a         3
# 2        b         6
# 3        c         6
# 4        c         8
# 5        c         9

# Stack dfs, but use multilevel index
df_ml = pd.concat([df1, df2], keys=['one', 'two'])
print(df_ml)

#       Column_A  Column_B
# one 0        a         1
#     1        a         2
#     2        a         3
#     3        c         4
#     4        c         5
#     5        d         6
# two 0        a         5
#     1        a         3
#     2        b         6
#     3        c         6
#     4        c         8
#     5        c         9

# Merge two dfs on a common column, ignoring non-common values
df = pd.merge(left=df1, right=df2, on='Column_A')
# same as
df = pd.merge(left=df1, right=df2, left_on='Column_A', right_on='Column_A')
print(df)

#    Column_A  Column_B_x  Column_B_y
# 0         a           1           5
# 1         a           1           3
# 2         a           2           5
# 3         a           2           3
# 4         a           3           5
# 5         a           3           3
# 6         c           4           6
# 7         c           4           8
# 8         c           4           9
# 9         c           5           6
# 10        c           5           8
# 11        c           5           9

# 'how' specifies which values to keep, and NaN those that are missing
# left or right - keep values from the left or right df
# inner  - only values common across both
# outer - all values matching or not
df = pd.merge(df1, df2, how='right', on='Column_A')
print(df)

#    Column_A  Column_B_x  Column_B_y
# 0         a         1.0           5
# 1         a         2.0           5
# 2         a         3.0           5
# 3         a         1.0           3
# 4         a         2.0           3
# 5         a         3.0           3
# 6         c         4.0           6
# 7         c         5.0           6
# 8         c         4.0           8
# 9         c         5.0           8
# 10        c         4.0           9
# 11        c         5.0           9
# 12        b         NaN           6

# Merge ordered - sort and de-dupe two DataFrame
df = pd.merge_ordered(df1, df2)
print(df)

#    Column_A  Column_B
# 0         a         1
# 1         a         2
# 2         a         3
# 3         a         5
# 4         b         6
# 5         c         4
# 6         c         5
# 7         c         6
# 8         c         8
# 9         c         9
# 10        d         6

# Merge ordered - keep both resultant value columns and fill forward on n/a
df = pd.merge_ordered(df1, df2, on='Column_A', fill_method='ffill')
print(df)

#    Column_A  Column_B_x  Column_B_y
# 0         a           1           5
# 1         a           1           3
# 2         a           2           5
# 3         a           2           3
# 4         a           3           5
# 5         a           3           3
# 6         b           3           6
# 7         c           4           6
# 8         c           4           8
# 9         c           4           9
# 10        c           5           6
# 11        c           5           8
# 12        c           5           9
# 13        d           6           9
