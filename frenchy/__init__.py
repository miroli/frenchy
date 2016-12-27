from .Commune import Commune
from .utils import df


def list_regions():
    return df[['region', 'region_code']].drop_duplicates()


def list_departments():
    return df[['department', 'department_code',
               'region_code']].drop_duplicates()


def list_communes():
    return df[['commune', 'commune_code', 'insee_code',
               'department_code', 'region_code']].drop_duplicates()


def get(code, year):
    return Commune(code, year)
