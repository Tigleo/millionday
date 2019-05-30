import json
from typing import List

import dateparser

from model.estrazione import Estrazione


def read(in_file) -> List[Estrazione]:
    estrazioni = []
    with open(in_file) as json_file:
        data = json.load(json_file)
        for p in data['estrazioni']:
            date_str = p['data']
            parsed = dateparser.parse(date_str, languages=['it'])
            e = Estrazione(parsed, p['numeri'])
            estrazioni.append(e)

    return estrazioni


def read_file_json(filename):
    file = open(filename, "r")
    return file.read()
