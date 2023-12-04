import os
import requests
from bs4 import BeautifulSoup
import json
#from webscraping.models import Scraper
from celery_worker import app


#@app.task()
#def save_function(answer_list):
    #for a in answer_list:
        #Scraper.objects.create(
            #data=a['data'],
            #city=a['city'],
            #temp_max=a['temp_max'],
            #temp_min=a['temp_min'],
            #weather_description=a['weather_description'])



@app.task()
def save_function(article_list):
    with open('weather.txt', 'w') as outfile:
        json.dump(article_list, outfile)

@app.task()
def hackernews_rss():
    link = f'https://www.accuweather.com/en/ru/volgograd/296363/daily-weather-forecast/296363'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
    }

    response = requests.get(link, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')

    data = bs.find('span', class_="module-header sub date").text
    temp_max = bs.find('span', class_="high").text
    temp_min = bs.find('span', class_="low").text[1:]
    weather_description = bs.find('div', class_="phrase").text

    weather_answer = {
        'data': data, 'city': 'Volgograd', 'temp_max': temp_max, 'temp_min': temp_min,
        'weather_description': weather_description,
    }

    return save_function(weather_answer)
