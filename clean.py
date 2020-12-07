import pandas as pd
import numpy as np

from progress.bar import Bar

from os import listdir
from os.path import isfile, join

from search import get_name
from join import join
from find import find_missing

path_instrument = 'data/instrument/'
path_meta = 'data/meta'

# df.replace({col : {row_a : val_1 , row_b : val_2 }})
# df.replace({'COMPOUND' : {index : name}})

# creates list of files
data = listdir(path_instrument)
meta = listdir(path_meta)

# sanity check
if len(data) != len(meta):
    print("DIFFERENT NUMBER OF DATA AND META ENTRIES")
else:
    print("data size matches")

# create series 7000x
series = [] 
for n in data:
    series.append(data[n].split('.')[0])

# Clean Data
meta_bar = Bar('Meta Cleaning', max=len(meta))
df = pd.empty()
for plate in meta:
    df, missing = find_missing(path_meta+plate)
    for n in missing:
        name = get_name(df.loc[n, 'CATALOG'])
        df.replace({'COMPOUND' : {n : name}})
    df.to_csv(plate)
    meta_bar.next()
meta_bar.finish()

# join data
