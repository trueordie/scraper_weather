import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')
django.setup()

import requests
from bs4 import BeautifulSoup

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

from clients.models import Weather, City

app = Celery('tasks')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL

app.conf.beat_schedule = {
    'scraping-task-one-min': {
        'task': 'weather_parser.weather_collector_vlg',
        'schedule': crontab(),
    },
    'scraping-task-one-min_2': {
        'task': 'weather_parser.weather_collector_msk',
        'schedule': crontab(),
    },
    'scraping-task-one-min_3': {
        'task': 'weather_parser.weather_collector_spb',
        'schedule': crontab(),
    },
}


@app.task()
def save_function(answer_list):
    for a in answer_list:
        Weather.objects.create(
            city_weather=a['city'],
            data=a['data'],
            temp_max=a['temp_max'],
            temp_min=a['temp_min'],
            weather_description=a['weather_description'])


@app.task()
def weather_collector_vlg():
    link = f'https://www.accuweather.com/en/ru/volgograd/296363/daily-weather-forecast/296363'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
    }

    response = requests.get(link, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')

    city_weather = City.objects.get(id=1)
    data = bs.find('span', class_="module-header sub date").text
    temp_max = bs.find('span', class_="high").text
    temp_min = bs.find('span', class_="low").text[1:]
    weather_description = bs.find('div', class_="phrase").text

    weather_answer = [{
        'data': data, 'city': city_weather, 'temp_max': temp_max, 'temp_min': temp_min,
        'weather_description': weather_description,
    }]

    return save_function(weather_answer)


@app.task()
def weather_collector_msk():
    link = f'https://www.accuweather.com/en/ru/moscow/294021/daily-weather-forecast/294021'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
    }

    response = requests.get(link, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')

    city_weather = City.objects.get(id=2)
    data = bs.find('span', class_="module-header sub date").text
    temp_max = bs.find('span', class_="high").text
    temp_min = bs.find('span', class_="low").text[1:]
    weather_description = bs.find('div', class_="phrase").text

    weather_answer = [{
        'data': data, 'city': city_weather, 'temp_max': temp_max, 'temp_min': temp_min,
        'weather_description': weather_description,
    }]

    return save_function(weather_answer)


@app.task()
def weather_collector_spb():
    link = f'https://www.accuweather.com/en/ru/saint-petersburg/295212/daily-weather-forecast/295212'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
    }

    response = requests.get(link, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')

    city_weather = City.objects.get(id=3)
    data = bs.find('span', class_="module-header sub date").text
    temp_max = bs.find('span', class_="high").text
    temp_min = bs.find('span', class_="low").text[1:]
    weather_description = bs.find('div', class_="phrase").text

    weather_answer = [{
        'data': data, 'city': city_weather, 'temp_max': temp_max, 'temp_min': temp_min,
        'weather_description': weather_description,
    }]

    return save_function(weather_answer)


