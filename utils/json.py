from collections import OrderedDict
from datetime import datetime
from typing import Dict
from typing import List

from config import date_pattern


def last_draw_dict(data: datetime, estrazione: List) -> Dict:
    ld = dict()
    ld["data"] = data.strftime(date_pattern)
    ld["estrazione"] = estrazione
    return ld


def count_frequencies_dict(frequencies: OrderedDict) -> List:
    arr = []

    for f in frequencies:
        fr = dict()
        fr["numero"] = f[1]
        fr["frequenza"] = f[0]
        arr.append(fr)
    return arr
