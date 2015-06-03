# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('server', models.CharField(max_length=25, choices=[(b'The Bastion', b'The Bastion'), (b'Bergeren Colony', b'Bergeren Colony'), (b'The Harbinger', b'The Harbinger'), (b'The Shadowlands', b'The Shadowlands'), (b'Jung Ma', b'Jung Ma'), (b'The Ebon Hawk', b'The Ebon Hawk'), (b'Prophecy of the Five', b'Prophecy of the Five'), (b'Jedi Covenant', b'Jedi Covenant')])),
                ('adv_class', models.CharField(max_length=25, choices=[(b'Powertech', b'Powertech'), (b'Mercenary', b'Mercenary'), (b'Vanguard', b'Vanguard'), (b'Commando', b'Commando'), (b'Sorcerer', b'Sorcerer'), (b'Assassin', b'Assassin'), (b'Sage', b'Sage'), (b'Shadow', b'Shadow'), (b'Sniper', b'Sniper'), (b'Operative', b'Operative'), (b'Gunslinger', b'Gunslinger'), (b'Scoundrel', b'Scoundrel'), (b'Juggernaut', b'Juggernaut'), (b'Marauder', b'Marauder'), (b'Guardian', b'Guardian'), (b'Sentinel', b'Sentinel')])),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(to='api.Player')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(to='api.Player'),
        ),
    ]
