import json
from site_parser.category import CategoryParser
from site_parser.article import ArticleParser


def main():
    category_parser = CategoryParser()
    categories = category_parser.get_categories()
    article_parser = ArticleParser()
    result = {}
    for category in categories:
        category_articles = article_parser.get_articles_data(category['url'])
        print(category_articles)
        result[category['name']] = category_articles

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

"""
ДЗ
создать таблицу categories
создать таблицу articles

записать полученные категории в БД
записать полученные новости в БД

"""

main()