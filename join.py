'''
Joined on WELLID for experiment data and meta data

7000x files: Image_Metadata_WellID
Stock_Plate7000x files: COORDINATE
'''

import pandas as pd

data = pd.read_csv('data/70003.csv')

compounds = pd.read_csv('data/Stock_Plate70003.csv')


# change WellID to be WellID

# data_temp = data.rename(columns={'Image_Metadata_WellID': 'WellID'})
# compounds_temp = data.rename(columns={'COORDINATE' : 'WellID'})

# df = data_temp.join(compounds_temp)

df = data.join(compounds.set_index('COORDINATE'), on='Image_Metadata_WellID')

print(df['COMPOUND_NAME'])

# for name in df['COMPOUND_NAME']:
#     if name == '\\s':
#         print('missing')

# print(df.head())
# print("\n")
# print(data.shape)

# df.to_csv(path_or_buf='temp.csv', index=False)