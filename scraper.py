import json
import urllib.request as request

import dateparser
from bs4 import BeautifulSoup

from utils.utility import *


def scrape(file, date):
    output_file = make_filename(file, date, file_date_pattern)

    body = {}
    estrazioni = []
    response = request.urlopen(url)
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    for tr in soup.findAll('tr'):

        if not tr.findChildren('th'):
            e = {}
            date_str = tr.span.text

            parsed = dateparser.parse(date_str, languages=['it'])
            date_time = parsed.strftime(date_pattern)
            e['data'] = date_time

            num = []
            for n in tr.findAll('td'):
                if not n.findChildren('span'):
                    num.append(n.text)
            e['numeri'] = num
            estrazioni.append(e)
    body['estrazioni'] = estrazioni

    with open(output_file, 'w+') as outfile:
        json.dump(body, outfile, indent=4, sort_keys=True)
