from reader import *
from scraper import *
from upload import upload
from utils.analisys import *
from utils.json import *

scrape(filename, datetime.now())
read_file = make_filename(filename, datetime.now(), file_date_pattern)
estrazioni = read(read_file)

count_number = frequencies_counter(estrazioni)

count_pair = frequencies_pairs(estrazioni)

obj = dict()
result = dict()
result["last_draw"] = last_draw_dict(estrazioni[0].data, estrazioni[0].numeri)
result["frequencies"] = count_frequencies_dict(count_number)
result["pair_frequencies"] = count_pair_frequencies_dict(count_pair)
obj["result"] = result

json = json.dumps(obj)
print(json)

upload(obj)
