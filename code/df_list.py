#!/usr/bin/env python3
"""Creating a dataframe from a dict."""

import pandas as pd

l = [[1,2,3,4],
     [5,6,7,8],
     [9,8,7,6]]

df = pd.DataFrame(l)
df.columns = ['a', 'b', 'c', 'd']

print(df)

#    a  b  c  d
# 0  1  2  3  4
# 1  5  6  7  8
# 2  9  8  7  6
