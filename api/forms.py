from django import forms
from api.models import User, Player, Character


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'server', 'adv_class')
