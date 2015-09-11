from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from serializers import UserSerializer, ServerSerializer, CharacterSerializer
from api.forms import LoginForm, CharacterForm, UserForm
from api.models import User, Server, Character


def get_characters(user):
    if user:
        return Character.objects.filter(player=user.pk)
    return None


def index(request):
    login_form = LoginForm()
    user = request.user
    context = {
        'queue': {server: [c for c in server] for server in Server.objects.all()},
        'login_form': login_form,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
    context['characters'] = get_characters(user)
    return render(request, 'api/index.html', context=context)


def add_character_view(request):
    character_form = CharacterForm()
    if request.method == 'POST':
        character = CharacterForm(request.POST).save(commit=False)
        character.player = request.user
        character.save()
        return redirect(reverse('index'))
    return render(request, 'api/character_form_view.html', {'character_form': character_form})


def signup_view(request):
    user_form = UserForm()
    context = {'user_form': user_form}
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            password = user.cleaned_data.get('password', None)
            username = user.cleaned_data.get('username', None)
            User.objects.create_user(username=username, password=password)
            logged_in = authenticate(username=username,password=password)
            login(request, logged_in)
            return redirect(reverse('index'))
        else:
            context['errors'] = user.errors
    return render(request, 'api/signup_view.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
