from django.contrib.auth.models import User
from django.db import models


SERVERS = (
    'The Bastion',
    'Bergeren Colony',
    'The Harbinger',
    'The Shadowlands',
    'Jung Ma',
    'The Ebon Hawk',
    'Prophecy of the Five',
    'Jedi Covenant',
)

ADV_CLASSES = (
    'Powertech',
    'Mercenary',
    'Vanguard',
    'Commando',
    'Sorcerer',
    'Assassin',
    'Sage',
    'Shadow',
    'Sniper',
    'Operative',
    'Gunslinger',
    'Scoundrel',
    'Juggernaut',
    'Marauder',
    'Guardian',
    'Sentinel'
)

class Player(User):
    friends = models.ManyToManyField("self", symmetrical=False)


class Character(models.Model):
    player = models.ForeignKey(Player)
    name = models.CharField(max_length=25)
    server = models.CharField(choices=[(c, c) for c in SERVERS], max_length=25)
    adv_class = models.CharField(
        choices=[(c, c) for c in ADV_CLASSES],
        max_length=25
    )

    def __repr__(self):
        return '{s.name} - {s.server}'.format(s=self)
