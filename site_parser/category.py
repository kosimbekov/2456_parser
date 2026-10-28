from .base import BaseParser

class CategoryParser(BaseParser):
    def get_categories(self):
        soup = self.get_soup()

        nav_row = soup.find('div', class_='nav_row')
        items = nav_row.find('ul').find_all('a')
        result = []
        for item in items:
            result.append({
                'name': item.get_text,
                'url': self.URL + item.get('href')
            })
            return result
