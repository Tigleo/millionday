import json
import datetime
import dateparser
import urllib.request as request
from bs4 import BeautifulSoup

today = datetime.datetime.now()
today = today.strftime("%d_%m_%y")
filename = "millionday"
output_file = "{}_{}.json".format(filename, today)
estrazioni = []
response = request.urlopen("http://www.millionday.cloud/archivio-estrazioni.php")
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

for tr in soup.findAll('tr'):

    if not tr.findChildren('th'):
        e = {}
        date_str = tr.span.text

        parsed = dateparser.parse(date_str, languages=['it'])
        date_time = parsed.strftime("%d/%m/%Y")
        e['data'] = date_time

        num = []
        for n in tr.findAll('td'):
            if not n.findChildren('span'):
                num.append(n.text)
        e['numeri'] = num
        estrazioni.append(e)
json_data = json.dumps(estrazioni, indent=4, sort_keys=True)
print(json_data)

# Open the file with writing permission
file = open(output_file, 'w')

# Write a line to the file
file.write(json_data)

# Close the file
file.close()

