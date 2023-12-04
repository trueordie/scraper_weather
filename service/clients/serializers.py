from rest_framework import serializers

from clients.models import Client


class ClientsSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user')


    class Meta:
        model = Client
        fields = ('id', 'user_name', 'selected_city',)
