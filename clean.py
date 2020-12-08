import pandas as pd
import numpy as np

from progress.bar import Bar

from os import listdir
from os.path import isfile, join

from search import get_name
from join import join
from find import find_missing

PATH_TO_META = 'data/meta/'
PATH_OUT = 'out/'
# df.loc[df.ID == 103, 'FirstName'] = "Matt"

# creates list of files
# meta = listdir(PATH_TO_META)

# # Clean Data
# df = pd.DataFrame()
# print('Finding Names:')
# for plate in meta:
#     # create a dataframe and list rows missing compound names
#     df, missing = find_missing(PATH_TO_META+plate)
#     # get CATALOG id number
#     cat_num = df.loc[missing, 'CATALOG']
#     bar = Bar(plate, max=len(cat_num))
#     for c in cat_num:
#         df.loc[df.CATALOG == c, 'COMPOUND_NAME'] = get_name(c)
#         bar.next()
#     bar.finish()
#     df.to_csv(PATH_OUT+plate)

def get_meta_data(plate):
    df, missing = find_missing(PATH_TO_META+plate)
    cat_num = df.loc[missing, 'CATALOG']
    bar = Bar('Finding Loss data', max=len(cat_num))
    for c in cat_num:
        df.loc[df.CATALOG == c, 'COMPOUND_NAME'] = get_name(c)
        bar.next()
    bar.finish()
    df.to_csv(PATH_OUT+plate, index=False)

get_meta_data('Stock_Plate70012.csv')