from datetime import datetime

from config import *


class Estrazione:
    def __init__(self, data: datetime, numeri: list):
        self.data = data
        self.numeri = numeri

    def __str__(self):
        date_str = self.data.strftime(date_pattern)
        return '{} {}'.format(date_str, self.numeri)
