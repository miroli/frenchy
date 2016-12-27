Scrape French presidential election results at municipality level from http://www.interieur.gouv.fr/. Most methods return pandas dataframes. Works only with python 3.6 :)

```python
# Specify INSEE code and election year
machy = frenchy.get('10212', year=2012)

machy.results  # election results for both rounds
machy.meta  # metadata, such as number of votes
```

###Install

```bash
pip install frenchy
```

###Usage

```python
# Top level functionality
frenchy.get_regions()
frenchy.get_departments(<region>)
frenchy.get_communes(<department>)

# Get results for one commune
machy = frenchy.get('10212', year=2012)

# Alternatively, get multiple communes at once
communes = frenchy.get(['10212', '02271'], year=2012)

machy.region  # 'CHAMPAGNE-ARDENNE'
machy.region_code  # 21
machy.department  # 'AUBE'
machy.department_code  # 10
```

###Tests

```bash
python -m unittest
```