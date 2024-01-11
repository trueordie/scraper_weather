from django.db import models
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    city_id = models.ForeignKey(City, on_delete=models.PROTECT, null=True)


class Weather(models.Model):
    city_weather = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    temp_max = models.CharField(max_length=100, null=True)
    temp_min = models.CharField(max_length=100, null=True)
    weather_description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f'Weather in: {self.city_weather,self.created_at}'

