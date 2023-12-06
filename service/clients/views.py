from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

#from clients.models import Client
from clients.models import User
from clients.serializers import ClientsSerializer


class ClientsView(ReadOnlyModelViewSet):
    #queryset = Client.objects.all()
    queryset = User.objects.all()
    serializer_class = ClientsSerializer

