'''
search sellcheck for compounds
'''

import pandas as pd
import numpy as np

import re # REEEEEE

import requests

r = requests.get('https://www.selleckchem.com/search.html?searchDTO.searchParam=S2041')
id1 = 'S2041'
rg = '(?:<a\ href="/products/)(.*)(?:\.html">)'

# print(f'First Request: {id1}')
# print(r.status_code)
# # f = open("test.json","a")
# # f.write(r.json())
# # f.close()
# temp = r.text
# out = re.search(rg, temp)
# name = out.group(1)
# print(f"Name: {name}")
# print('\n')

link = 'https://www.selleckchem.com/search.html?searchDTO.searchParam='

# id2 = 'S2362'
# print(f'Second Request: {id2}')
# r2 =requests.get(link+id2)
# print(f'Status: {r2.status_code}')
# temp2 = r2.text
# out2 = re.search(rg,temp2)
# name2 = out2.group(1)
# print(f'Name2: {name2}')

def get_name(cat_num, reg=rg, link=link):
    request = requests.get(link+cat_num)
    page = request.text
    out = re.search(reg, page)
    return(out.group(1))

    