from django.contrib import admin

from clients.models import City, Weather, User

admin.site.register(User)
admin.site.register(City)
admin.site.register(Weather)

