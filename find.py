'''
Find missing compound names
'''

import pandas as pd
import numpy as np

from progress.bar import Bar
import requests

# df = pd.read_csv('data/metadata/Stock_Plate70003.csv')

# # the resulting values are offset by 2
# temp = np.where(pd.isnull(df['COMPOUND_NAME']))
# print(temp)

# # D21

# test = np.where(df['COORDINATE']=='D21')
# print(test)

# print(df.loc[78, :])
# print()
# print(df.loc[79, :])
# print()

# bar = Bar('Missing', max=len(temp))
# for n in temp:
#     print(df.loc[n, ['CATALOG', 'COORDINATE']])
#     bar.next()
# bar.finish()

# reads in csv, finds missing, returns both
def find_missing(csv, col='COMPOUND_NAME'):
    df = pd.read_csv(csv)
    missing = np.where(pd.isnull(df[col]))
    return (df, missing)