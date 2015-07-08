from rest_framework import serializers
from models import Player, Character


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'username', 'server', 'adv_class', 'team')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'server', 'adv_class')
