import itertools
import json
import sys

import acpr.download as d
import acpr.parse as p

def main():
    for page in itertools.count(1,1):
        response = d.search(page)
        if page > 1 and p.is_page_one(response):
            break
        else:
            for result in p.search(response):
                result['url'] = response.url
                sys.stdout.write(json.dumps(result) + '\n')
