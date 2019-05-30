# importing the requests library
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth

from config import *
from utils.utility import make_filename


def upload(json_data):
    # sending post request and saving response as response object
    data = make_filename(filename, datetime.now(), file_date_pattern)

    r = requests.post(url=url_be_upload, auth=HTTPBasicAuth('admin', 'cinino'), json=json_data)

    # extracting response text
    result = r.text
    print("Response: %s" % result)
