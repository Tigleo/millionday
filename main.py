from reader import *
from scraper import *

scrape(filename, datetime.now())
read_file = make_filename(filename, datetime.now(), file_date_pattern)
estrazioni = read(read_file)

for e in estrazioni:
    print(e)
