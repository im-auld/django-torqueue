from django.contrib.auth.models import User
from django.db import models


Q_NOTICE = '{p.username} on Team: {p.team} has queued on {p.server}'
UNQ_NOTICE = '{p.username} on Team: {p.team} has left the queue on {p.server}'


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


class Server(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def __iter__(self):
        for character in self.character_set.all():
            if character.is_queued:
                yield character


class Character(models.Model):
    player = models.ForeignKey(User)
    name = models.CharField(max_length=25)
    server = models.ForeignKey(Server, blank=True, null=True)
    adv_class = models.CharField(
        choices=[(c, c) for c in ADV_CLASSES],
        max_length=25
    )
    is_queued = models.BooleanField(default=False)

    def __str__(self):
        return '{s.name} - {s.server}'.format(s=self)
