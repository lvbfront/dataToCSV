import bs4 
import requests
import csv
from pathlib import Path

#get the page you want

res = requests.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

table_soup = soup.find_all('table')
filtered_table = [table for table in table_soup if table.caption is not None]
#print(filtered_table)

required_table = None

#search for the table you want
for table in filtered_table:
    if str(table.caption.text).strip() == "Languages with at least 50 million first-language speakers[7]":
        required_table = table
        break
print(required_table)

rows = required_table.find_all('tr')

headers = [ head.text.replace('\n', '') for head in rows[0].find_all('th') ]
print(headers)

data = []

for row in rows:
    value = row.find_all('td')
    value_text = [db.text.strip() for db in value]

    if len(value_text) == 0:
        continue

    data.append(value_text)

#write to csv
file = open(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب\python course\CSV", 'wiki.csv'), 'w', newline='')
writer = csv.writer(file)
writer.writerow(headers)
writer.writerows(data)
file.close()
