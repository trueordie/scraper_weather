from rest_framework import serializers

from clients.models import User, Weather


class ClientsSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(source='user')
    class Meta:
        model = User
        fields = ('id', 'username', 'city_id')


class UserWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('city_weather', 'created_at', 'temp_max', 'temp_min', 'weather_description')


