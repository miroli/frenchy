import os
import pandas as pd
from .config import BASE_URL


dirname = os.path.dirname(os.path.abspath(__file__))
df = pd.read_pickle(os.path.join(dirname, 'data.p'))


def get_geo(code, year):
    row = df[df['insee_code'] == code]
    return row.to_dict('records')[0]


def url_resolver(code, year, region_code, department_code):
    zero_pad = lambda num: f'0{str(num)}'

    if year == 2012:
        reg_code = zero_pad(region_code)
        dep_code = zero_pad(department_code)
        com_code = zero_pad(code)
        url = (f'{BASE_URL}elecresult__PR2012/(path)/PR2012/'
               f'{reg_code}/{dep_code}/{com_code}.html')

    return url
