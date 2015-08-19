from rest_framework import serializers
from models import Player, Server, Character


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'username')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'name', 'character_set')

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('player', 'name', 'server', 'adv_class')
