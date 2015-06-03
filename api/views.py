from models import Player, Character
from rest_framework import viewsets, permissions
from serializers import PlayerSerializer, CharacterSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
