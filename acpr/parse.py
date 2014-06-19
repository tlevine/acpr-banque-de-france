from lxml.html import fromstring

def categories(response):
    response = search('not-a-real-category', 'not-a-real-page')
    html = fromstring(response.text)
    return html
