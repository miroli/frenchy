import pandas as pd
from .utils import url_resolver, get_geo


class Commune():
    "Base class for commune results"
    def __init__(self, code, year):
        self._geo = get_geo(code, year)
        self.url = url_resolver(code, year, self._geo['region_code'],
                                self._geo['department_code'])

        tables = pd.read_html(self.url, header=0, encoding='utf8', decimal=',',
                              thousands=' ')
        self._parse(tables)

    def _parse(self, tables):
        results_round1 = self._parse_results(tables[3], 1)
        results_round2 = self._parse_results(tables[1], 2)
        self.results = pd.concat([results_round1, results_round2])

        meta_round1 = self._parse_meta(tables[2], 1)
        meta_round2 = self._parse_meta(tables[0], 2)
        self.meta = pd.concat([meta_round1, meta_round2])

    def _parse_results(self, table, round_):
        results_cols = {'Liste des candidats': 'candidate', 'Voix': 'votes'}
        table = table.rename(columns=results_cols)
        table['candidate'] = table['candidate'].str.replace('\xa0', ' ')
        table['round'] = round_
        table = table[['round', 'candidate', 'votes']]
        table = table.set_index(['candidate', 'round'])
        return table

    def _parse_meta(self, table, round_):
        clean = lambda x: int(str(x).replace('\xa0', ''))
        table = table[['Unnamed: 0', 'Nombre']].iloc[0:4].set_index('Unnamed: 0').T
        meta_cols = {'Inscrits': 'registered', 'Votants': 'votes',
                     'Blancs ou nuls': 'blanks_or_nulls',
                     'Abstentions': 'abstentions'}
        table = table.rename(columns=meta_cols)
        table['round'] = round_
        table = table.set_index('round')
        table.columns.name = None
        table['registered'] = table['registered'].apply(clean)
        table['votes'] = table['votes'].apply(clean)
        table['blanks_or_nulls'] = table['blanks_or_nulls'].apply(clean)
        table['abstentions'] = table['abstentions'].apply(clean)

        return table

    @property
    def region(self):
        return self._geo['region']

    @property
    def region_code(self):
        return self._geo['region_code']

    @property
    def department(self):
        return self._geo['department']

    @property
    def department_code(self):
        return self._geo['department_code']

    @property
    def name(self):
        return self._geo['commune']

    def __repr__(self):
        return f'<Commune name=\'{self._geo["commune"]}\'>'
