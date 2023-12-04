from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from clients.serializers import ClientsSerializer


class ClientsView(ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

