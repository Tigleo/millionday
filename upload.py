# importing the requests library
import json
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth

from config import *
from reader import read_file_json
from utils.utility import make_filename

# sending post request and saving response as response object
data = make_filename(filename, datetime.now(), file_date_pattern)
json = json.dumps(read_file_json(data))

r = requests.post(url=url_be_upload, auth=HTTPBasicAuth('admin', 'cinino'), json=json)

# extracting response text
result = r.text
print("Response: %s" % result)
