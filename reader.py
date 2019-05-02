import json
from datetime import datetime

import dateparser

from config import *
from model.estrazione import Estrazione
from utils.utility import *

output_file = make_filename(filename, datetime.now())

estrazioni = []
with open(output_file) as json_file:
    data = json.load(json_file)
    for p in data['estrazioni']:
        date_str = p['data']
        parsed = dateparser.parse(date_str, languages=['it'])
        e = Estrazione(parsed, p['numeri'])
        estrazioni.append(e)

for l in estrazioni:
    print(l)
