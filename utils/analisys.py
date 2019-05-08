import itertools
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


def frequencies_pairs(estrazioni: List[Estrazione]) -> OrderedDict:
    base_num = list(range(1, 56))
    pairs = list(itertools.combinations(base_num, 2))
    res = np.zeros(len(pairs))
    i = 0
    for pair in pairs:
        pair_count = 0
        for es in estrazioni:
            set_pair = set(pair)
            set_es = set(es.numeri)
            isSub = set_pair.issubset(set_es)
            if (isSub):
                pair_count += 1
        res[i] = pair_count
        i += 1
    frequencies = dict(zip(pairs, res))
    return OrderedDict(sorted(frequencies.items(), key=lambda t: t[1], reverse=True))


def frequencies_triplets(estrazioni: List[Estrazione]) -> OrderedDict:
    base_num = list(range(1, 56))
    triplets = list(itertools.combinations(base_num, 3))
    res = np.zeros(len(triplets))
    i = 0
    for tris in triplets:
        tris_count = 0
        for es in estrazioni:
            set_pair = set(tris)
            set_es = set(es.numeri)
            isSub = set_pair.issubset(set_es)
            if (isSub):
                tris_count += 1
        res[i] = tris_count
        i += 1
    frequencies = dict(zip(triplets, res))
    return OrderedDict(sorted(frequencies.items(), key=lambda t: t[1], reverse=True))


def verify_win(estrazione: Estrazione, numeri: List[int]) -> Win:
    return Win(estrazione, numeri)
