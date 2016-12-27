from distutils.core import setup

requires = [
    'beautifulsoup4',
    'bs4',
    'html5lib',
    'lxml',
    'numpy',
    'pandas',
    'python-dateutil',
    'pytz',
    'six',
    'webencodings'
]

setup(
    name='frenchy',
    packages=['frenchy'],
    version='0.4',
    description='A pandas friendly french election scraper',
    author='Robin Linderborg',
    author_email='robin.linderborg@gmail.com',
    url='https://github.com/miroli/frenchy',
    download_url='https://github.com/miroli/frenchy/tarball/0.4',
    install_requires=requires,
    keywords=['france', 'scraper', 'elections'],
)
