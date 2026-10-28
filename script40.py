import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
API_URL = 'http://api.weatherapi.com/v1'
print(WEATHER_API_KEY)

result = []
while True:
    city = input('city: ')

    if city == 'exit':
        break

    if city == 'save':
        import json
        with open('weather.json', mode='w', encoding='utf-8') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
            break


    response = requests.get(f'{API_URL}/current.json', params={
        'key': WEATHER_API_KEY,
        'q': city
    })
    data = response.json()
    temp_c = data['current']['temp_c']
    feelslike_c = data['current']['feelslike_c']
    wind_kph = data['current']['wind_kph']
    name = data['location']['name']
    text = data['current']['condition']['text']
    last_updated = data['current']['last_updated']

    print(f'''
{temp_c=}
{feelslike_c=}
{wind_kph=}
{name=}
{text=}
{last_updated=}
''')
    result.append({
        'name': name,
        'temp_c': temp_c,
        'feelslike_c': feelslike_c,
        'wind_kph': wind_kph,
        'last_updated': last_updated,
        'text': text
    })
