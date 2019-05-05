from typing import List

from config import *
from model.estrazione import Estrazione


class Win:
    def __init__(self, estrazione: Estrazione, estratti: List[int]):
        self.data = estrazione.data
        self.numeri = estrazione.numeri
        self.estratti = estratti

    def occurrencies(self) -> List[int]:
        occ = []
        for n in self.numeri:
            c = self.estratti.count(n)
            if c > 0:
                occ.append(n)
        return occ

    def prize(self) -> int:
        return prizes.get(len(self.occurrencies()), 0)

    def __str__(self):
        return "{} {} {} [{} €]".format(self.data.strftime(date_pattern), self.numeri,
                                        self.occurrencies(), self.prize())
