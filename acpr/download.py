import os

import requests
from picklecache import cache

@cache(os.path.join(os.path.expanduser('~'), '.acpr'))
def search(pg:int):
    '''
    pg is a natural number.
    '''
    url = 'https://www.regafi.fr/spip.php'
    params = {
        'page': 'results',
        'type': 'advanced',
        'id_secteur': '3',
        'lang': 'en',
        'denomination': '',
        'siren': '',
        'cib': '',
        'bic': '',
        'nom': '',
        'siren_agent': '',
        'num': '',
        'cat': '0',
        'retrait': '0',
        'pg': pg,
    }
    return requests.get(url, params = params)
