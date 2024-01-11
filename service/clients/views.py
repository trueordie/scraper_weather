from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet

from rest_framework import generics, permissions
from clients.models import User, Weather, City
from clients.serializers import ClientsSerializer, UserWeatherSerializer


class ClientsView(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = ClientsSerializer


class UserWeatherView(generics.ListAPIView):
    serializer_class = UserWeatherSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = Weather

    def get_queryset(self):
        #user_city = self.request.GET.get('city_id')
        user_city = self.request.user.city_id
        return Weather.objects.filter(city_weather=user_city).all()
    queryset = get_queryset
