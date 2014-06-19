import re
from collections import OrderedDict

from lxml.html import fromstring

def search(response):
    html = fromstring(response.text)
    table = html.xpath('//table[@summary="Search results"]')[0]
    keys = [re.sub(r'[^a-z]+', '.', str(th.text_content().strip()), flags = re.IGNORECASE) for th in table.xpath('tr[position()=1]/th')]
    print(keys)
    for tr in table.xpath('tr[td]'):
        values = (td.text_content() for td in tr.xpath('td'))
        yield OrderedDict(zip(keys, values))

def is_page_one(response):
    html = fromstring(response.text)
    return ['1'] == html.xpath('//span[@class="active"]/text()')
