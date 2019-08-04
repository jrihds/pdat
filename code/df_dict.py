#!/usr/bin/env python3
"""Creating a dataframe from a dict."""

import pandas as pd

d = {"a": [1, 2, 3],
     "b": [4, 5, 6]}

df = pd.DataFrame(d)

print(df)

#    a  b
# 0  1  4
# 1  2  5
# 2  3  6
