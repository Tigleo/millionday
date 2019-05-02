from datetime import datetime


def make_filename(name: str, date: datetime):
    date_str = date.strftime("%d_%m_%y")
    return "{}_{}.json".format(name, date_str)
