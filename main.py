from reader import *
from scraper import *
from utils.analisys import *

scrape(filename, datetime.now())
read_file = make_filename(filename, datetime.now(), file_date_pattern)
estrazioni = read(read_file)

print(estrazioni[0])
print(verify_win(estrazioni[0], [5, 51, 23, 0, 0]))

count_number = frequencies_counter(estrazioni)
print("Count: {}".format(dict(count_number).items()))

count_pair = frequencies_pairs(estrazioni)
print("Pair Counter: {}".format(dict(count_pair).items()))

count_tris = frequencies_triplets(estrazioni)
print("Tris Counter: {}".format(dict(count_tris).items()))
