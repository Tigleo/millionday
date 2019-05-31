import requests
from requests.auth import HTTPBasicAuth

from config import *


def upload(json_data):

    r = requests.post(url=url_be_upload, auth=HTTPBasicAuth('admin', 'cinino'), json=json_data)

    # extracting response text
    result = r.text
    print("Response: %s" % result)
