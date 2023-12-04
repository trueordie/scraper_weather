from django.db import models


class Scraper(models.Model):
    data = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    temp_max = models.CharField(max_length=100)
    temp_min = models.CharField(max_length=100)
    weather_description = models.CharField(max_length=100)
