from rest_framework import generics
from clients.models import Weather
from clients.serializers import UserWeatherSerializer


class UserWeatherView(generics.ListAPIView):
    model = Weather

    def get_queryset(self):
        qs = super().get_queryset()
        user_city = self.request.GET.get('city_id')
        return qs.filter(city_weather=user_city)


