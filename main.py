from reader import *
from scraper import *
from utils.analisys import *


scrape(filename, datetime.now())
read_file = make_filename(filename, datetime.now(), file_date_pattern)
estrazioni = read(read_file)

count_number = frequencies_counter(estrazioni)
print("Count: ")
print(count_number)
