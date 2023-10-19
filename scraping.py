import requests  # pulling data
from bs4 import BeautifulSoup  # xml parsing
import json  # exporting to files


# фунцкия сохранения данных формате json в фаил .txt
def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)


# функция парсинга данных
def hackernews_rss():
    article_list = [] #список для хранения данных


    # делаем запрос и получаем фаил в формате lxml
    response = requests.get('https://news.ycombinator.com/rss')
    soup = BeautifulSoup(response.text, 'xml')

    # Вытаскиваем их общего lxml блок со статьями
    articles = soup.findAll('item')

    # пробегаемся по блоку с помощью цикла и вытаскиваем интересующие нас поля в переменные
    # 1. Название статьи 2.ссылка 3.дата публикации
    for a in articles:
        title = a.find('title').text
        link = a.find('link').text
        published = a.find('pubDate').text

        # в каждой итерации цикла создаём из данных извлечённых в переменные словарь
        # from each "item"
        article = {
            'title': title,
            'link': link,
            'published': published
        }

        # в каждой итерации цикла добавляем в список формируемый выше словарь
        article_list.append(article)

    # после завершения цикла применяем функцию сохранения данных в фаил .txt
    return save_function(article_list)




hackernews_rss()
