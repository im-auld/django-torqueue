from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import viewsets, permissions
from serializers import PlayerSerializer, ServerSerializer, CharacterSerializer
from api.forms import LoginForm, CharacterForm
from api.models import Player, Server, Character


def index(request):
    login_form = LoginForm()
    queue = {server: [c for c in server] for server in Server.objects.all()}
    print(queue)
    context = {
        'queue': queue,
        'login_form': login_form,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            context['user'] = user
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

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
