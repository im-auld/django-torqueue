import random
from django.contrib.auth.hashers import make_password
import factory
from api import models


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    password = make_password('password')


class ServerFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Server

    name = factory.Sequence(lambda n: 'server{}'.format(n))


class CharacterFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Character

    player = factory.SubFactory(UserFactory)
    server = factory.SubFactory(ServerFactory)
    name = factory.Sequence(lambda n: 'character{}'.format(n))
    adv_class = random.choice(models.ADV_CLASSES)
    is_queued = False
