import requests
from bs4 import BeautifulSoup

website = "https://w3schools.com"
resp = requests.get(website)
bs = BeautifulSoup(resp.text, "html.parser")

links = bs.find_all("a")

print(f'Links Count : {len(links)}')

unique_links = set()
for link in links:
    href = link['href']
    if href.startswith("javascript:void"):
        continue

    if not href.startswith("http"):
        href = website + href

    unique_links.add(href)

print(f"Unique Links Count : {len(unique_links)}")
for link in unique_links:
    print(link)
