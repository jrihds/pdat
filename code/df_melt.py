#!/usr/bin/env python
"""Melting dataframes."""

import pandas as pd

d = {'Column A': [1, 2, 3, 4, 5, 6],
     'Column B': ['a', 'a', 'a', 'c', 'c', 'd'],
     'Column C': ['z', 'z', 'z', 'x', 'x', 'x']}
df = pd.DataFrame(d)
print(df)

#    Column A Column B Column C
# 0         1        a        z
# 1         2        a        z
# 2         3        a        z
# 3         4        c        x
# 4         5        c        x
# 5         6        d        x

df = pd.melt(df, id_vars=['Column C'], var_name='Variable Name',
             value_name='Value')
print(df)

#    Column C Variable Name Value
# 0         z      Column A     1
# 1         z      Column A     2
# 2         z      Column A     3
# 3         x      Column A     4
# 4         x      Column A     5
# 5         x      Column A     6
# 6         z      Column B     a
# 7         z      Column B     a
# 8         z      Column B     a
# 9         x      Column B     c
# 10        x      Column B     c
# 11        x      Column B     d
