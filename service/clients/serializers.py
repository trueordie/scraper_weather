from rest_framework import serializers

#from clients.models import Client
from clients.models import User


class ClientsSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user')

    class Meta:
        #model = Client
        model = User
        fields = ('id', 'user_name',)
