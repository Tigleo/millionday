from datetime import datetime

from config import *


def make_filename(name: str, date: datetime, pattern: str):
    date_str = date.strftime(pattern)
    return filename_pattern.format(name, date_str)
