from datetime import datetime


class Estrazione:
    def __init__(self, data: datetime, numeri: list):
        self.data = data
        self.numeri = numeri

    def __str__(self):
        date_str = self.data.strftime("%d/%m/%Y")
        return '{} {}'.format(date_str, self.numeri)
