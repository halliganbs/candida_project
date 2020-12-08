import numpy as np
import pandas as pd

from find import find_missing
from join import join
# df=  pd.read_csv('joined/70003.csv')

df = pd.read_csv('data/Candida2ndBatch_allResults.tsv', sep='\t')
dt = pd.read_csv('data/Well_vs_Cond.csv')
print(df.columns)
print(df.shape)
print()
print(dt.columns)
print(dt.shape)
# NOTE: Stock_Plate70012.csv S3768 is not in selleckchem database 
# Stock_plate70011.csv S2023 missing

# Candid2nd wellLocation
# Well v Cond LC_WELLID

# temp = join(meta='data/Well_vs_Cond.csv',instrument='data/Candida2ndBatch_allResults.tsv', 
# metaID='LC_WELLID',instID='wellLocation')

temp = dt.join(df.set_index('wellLocation'), on='LC_WellID')
temp.to_csv('test.csv')
print(temp.columns)
print(temp.shape)