import requests
from bs4 import BeautifulSoup
import json

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0'
}

output = []

# SCRAPPING THE EBAY WEBPAGES AND PLACING THE ITEMS INTO THE ITEMS DICTIONARY
pg_nums = ['1','2','3','4','5','6','7','8','9','10']
for pg in pg_nums:
    url = 'https://www.ebay.com/sch/i.html?_nkw=dslr+cameras&_pgn='+pg
    r = requests.get(url, headers=headers)   
    print('r.status_code=', r.status_code) 

    soup = BeautifulSoup(r.text, 'html.parser')

    boxes = soup.select('li.s-item--watch-at-corner.s-item')
    for box in boxes:
        x = {}
        names = box.select('.s-item__title')
        for name in names:
            x['name'] = name.text
        prices = box.select('.s-item__price')
        for price in prices:
            x['price'] = price.text
        statuss = box.select('.SECONDARY_INFO')
        for status in statuss:
            x['status'] = status.text
        output.append(x)

# SORTING THE ITEMS AND REMOVING DUPLICATES
items = []
for i in output:
    if i not in items:
        items.append(i)

# WRITING THE JSON FILE
json_object = json.dumps(items, indent = 4)
with open('items.json', "w") as outfile:
    outfile.write(json_object)












