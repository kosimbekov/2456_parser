from .base import BaseParser

class ArticleParser(BaseParser):
    def get_article_data(self, articles, category_url):
        category_soup = self.get_soup(category_url)
        content_block = category_soup.find('div', class_='content-block')
        items = content_block.find_all('div', class_='sh-news')
        # print(len(items))
        result = []
        for i in items:
            title = i.find('h2', class_='sh-title').get_text()
            print(title)
            img_url = i.find('img').get('data-src')
            # print(img_url)
            # найти дату публикации
            date = i.find('div', class_='side-date').find('span').get_text(strip=True)
            # print(date)
            descr = i.find('div', class_='sh-text').next.get_text(strip=True)
            # print(descr)

            result.append({
                'title': title,
                'img_url': img_url,
                'date': date,
                'descr': descr
            })

