from django.db import models
from django.contrib.auth.models import User

CITY_CHOICES = (
    ('VLG', 'Volgograd'),
    ('MSK', 'Moscow'),
    ('SPB', 'Saint-Petersburg'),
)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    selected_city = models.CharField(max_length=50, choices=CITY_CHOICES)

    def __str__(self):
        return f'Client name: {self.user}'
