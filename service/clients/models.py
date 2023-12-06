from django.db import models
from django.contrib.auth.models import User as UserModel


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(UserModel):
    city_id = models.ForeignKey(City, on_delete=models.PROTECT, null=True)

    #def __str__(self):
   #     return f'Client name: {self.user}'


class Weather(models.Model):
    city_weather = models.OneToOneField(City, on_delete=models.PROTECT, null=True)
    data = models.CharField(max_length=100, null=True)
    temp_max = models.CharField(max_length=100, null=True)
    temp_min = models.CharField(max_length=100, null=True)
    weather_description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'Weather in: {self.city_weather, self.data}'

