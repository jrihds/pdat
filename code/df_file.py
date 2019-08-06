#!/usr/bin/env python3
"""Creating a dataframe from a csv or json."""

import pandas as pd

# df.csv
# a,b,c,d
# 1,2,3,4
# 5,6,7,8
# 9,8,7,6

# df.json
# {"a":{"0":1,"1":5,"2":9},"b":{"0":2,"1":6,"2":8},
#  "c":{"0":3,"1":7,"2":7},"d":{"0":4,"1":8,"2":6}}

df = pd.read_csv('df.csv', header=0, sep=',', index_col=None,
                 comment='#', na_values='-1')
df = pd.read_json('df.json')
print(df)

#    a  b  c  d
# 0  1  2  3  4
# 1  5  6  7  8
# 2  9  8  7  6

for chunk in pd.read_csv('df.csv', chunksize=1):
    print(chunk)

#    a  b  c  d
# 0  1  2  3  4
#    a  b  c  d
# 1  5  6  7  8
#    a  b  c  d
# 2  9  8  7  6

df.to_csv('df.csv', index=False)
df.to_json('df.json')
