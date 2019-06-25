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

tst = dict()
result = dict()
result["last_draw"] = last_draw_dict(estrazioni[0].data, estrazioni[0].numeri)
result["frequenze"] = count_frequencies_dict(count_pair)
tst["result"] = result

json = json.dumps(tst)
print(json)

upload(tst)
