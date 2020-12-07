'''
search sellcheck for compounds
'''

import pandas as pd
import numpy as np

import re # REEEEEE

import requests
from time import sleep # kill me

REGEX = '(?:<a\ href="/products/)(.*)(?:\.html">)'
LINK = 'https://www.selleckchem.com/search.html?searchDTO.searchParam='
OK = 200
TIMEOUT = 429
FORTYFIVE_SECONDS = 45

'''
cat_num : Catalouge number
reg : regex for displayed html
link : website search link
'''
def get_name(cat_num, reg=REGEX, link=LINK):
    path = link+cat_num
    name = ""
    request = requests.get(path)
    code = request.status_code
    if code == OK:
        page = request.text
        out = re.search(reg, page)
        name = out.group(1)
    elif code == TIMEOUT:
        sleep(FORTYFIVE_SECONDS)
        name = get_name(cat_num=cat_num) # oh yeah baby recursion
    else:
        print(f'STATUS CODE: {code}')
        name = "MISSING"
    return(name)