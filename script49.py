import requests
from bs4 import BeautifulSoup
import json

from script47 import result

URL = 'https://gazeta.ru'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('h3')
results = []
for item in items:
    title = item.get_text(strip=True)
    if title:
        results.append(title)
        print(title)
with open('news.json', 'w') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)