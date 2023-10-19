import os
import requests
from bs4 import BeautifulSoup
import json


from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'scraping-task-one-min': {
        'task': 'service.hackernews_rss',
        'schedule': crontab(),
    },
}


@app.task()
def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)


@app.task()
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







