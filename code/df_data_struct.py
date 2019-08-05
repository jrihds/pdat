#!/usr/bin/env python3
"""Creating a dataframe from a dict."""

import pandas as pd

d = {"a": [1, 2, 3],
     "b": [4, 5, 6],
     "c": [7, 8, 9]}

l = [[1,4,7],
     [2,5,8],
     [3,6,9]]

df = pd.DataFrame(d)
print(df)

df = pd.DataFrame(l)
df.columns = ['a', 'b', 'c']
print(df)

#    a  b  c
# 0  1  4  7
# 1  2  5  8
# 2  3  6  9
