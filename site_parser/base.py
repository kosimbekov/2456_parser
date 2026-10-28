from bs4 import BeautifulSoup
import requests

class BaseParser:
    URL = 'https://upl.uz'

    def get_soup(self, url=URL):
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
