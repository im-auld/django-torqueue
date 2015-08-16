from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from serializers import PlayerSerializer, ServerSerializer, CharacterSerializer
from api.forms import LoginForm, CharacterForm
from api.models import Player, Server, Character


def index(request):
    login_form = LoginForm()
    character_form = CharacterForm()
    context = {
        'queue': {server: [c for c in server] for server in Server.objects.all()},
        'login_form': login_form,
        'character_form': character_form,
        'characters': Character.objects.filter(player=request.user)
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
    return render(request, 'api/index.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('index')

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
