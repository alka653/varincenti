# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20151026_0149'),
        ('extreme', '0020_remove_reservation_player_player_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation_player',
            name='player_user',
            field=models.ForeignKey(to='users.ProfileUser', null=True),
        ),
    ]
