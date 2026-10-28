# venv
# активировать его
# добавить пайтон
# bs4 requests
# создать requirements.txt

import requests
from bs4 import BeautifulSoup

URL = 'https://upl.uz'


response = requests.get(URL)
response.raise_for_status()
response_html = response.text
# print(response_html)

# 500, 401, 404
soup = BeautifulSoup(response_html, 'html.parser')

# .find(tag, attribute)
# .find_all(tag, attribute)

wrapper = soup.find('div', id='upl-content')
# print(wrapper)

items = wrapper.find_all('div', class_='sh-news')
# print(len(items))
result = []
for i in items:
    title = i.find('h2', class_='sh-title').get_text()
    print(title)
    img_url = i.find('img').get('data-src')
    print(img_url)
    # найти дату публикации
    date = i.find('div', class_='side-date').find('span').get_text(strip=True)
    print(date)
    descr = i.find('div', class_='sh-text').next.get_text(strip=True)
    print(descr)

    result.append({
        'title': title,
        'img_url': img_url,
        'date': date,
        'descr': descr
    })

import json

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)