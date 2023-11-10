""" main.py

Code Challenge: Selecting observations in Pandas I

"""

import pandas as pd
import numpy as np

# IMPORTANT: please do not modify this import statement



# The data frame `df` includes the following information
#
# |            | AUD/USD | EUR/AUD |
# |------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
# | 2020-09-10 | NaN     | 1.6221  |
# | 2020-09-11 | 0.7263  | 1.6282  |
# | 2020-09-14 | 0.7281  | NaN     |
# | 2020-09-15 | 0.7285  | 1.6288  |
data = {
    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
    }
index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
df = pd.DataFrame(data, index)

pp = df.loc['AUD/USD']

print(pp)

