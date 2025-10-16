import requests
from bs4 import BeautifulSoup

website = "https://www.tiobe.com/tiobe-index/"
resp = requests.get(website)
bs = BeautifulSoup(resp.text, "html.parser")

# get table
table = bs.find(id="top20")
body = table.tbody
rows = body.find_all("tr")
for row in rows[:10]:
    cols = row.find_all('td')
    name = cols[4].text
    rating = cols[5].text

    print(f"{name:20}  {rating:6}")
