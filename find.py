'''
Find missing compound names
'''

import pandas as pd
import numpy as np

from progress.bar import Bar
import requests

from search import get_name

# reads in csv, finds missing, returns both
def find_missing(csv, col='COMPOUND_NAME'):
    df = pd.read_csv(csv)
    # df['COMPOUND_NAME'] = None
    missing = np.where(pd.isnull(df['COMPOUND_NAME']))
    return df, missing

# df, miss = find_missing('data/meta/Stock_Plate70010.csv')

# cat_num = df.loc[miss,'CATALOG']

# bar = Bar("Getting Names", max=len(cat_num))
# names = []
# for c in cat_num:
#     names.append(get_name(c))
#     bar.next()
# bar.finish()
# print(names)