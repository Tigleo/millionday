from collections import OrderedDict
from typing import List

import numpy as np

from model.estrazione import Estrazione
from model.win import Win


def frequencies_counter(estrazioni: List[Estrazione]) -> OrderedDict:
    id = np.array(range(1, 56))
    res = np.zeros(len(id))
    for num in id:
        count = 0
        for e in estrazioni:
            array = e.numeri
            count += array.count(num)
        res[num - 1] = count
    frequencies = dict(zip(id, res))
    return OrderedDict(sorted(frequencies.items(), key=lambda t: t[1], reverse=True))


def verify_win(estrazione: Estrazione, numeri: List[int]) -> Win:
    return Win(estrazione, numeri)
