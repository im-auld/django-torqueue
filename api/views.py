from django.shortcuts import render
from models import Player, Server
from rest_framework import viewsets, permissions
from serializers import PlayerSerializer, ServerSerializer


def index(request):
    queue = {server: [p for p in server] for server in Server.objects.all()}
    context = {'queue': queue}
    return render(request, 'api/index.html', context=context)

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

# class CharacterViewSet(viewsets.ModelViewSet):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer
