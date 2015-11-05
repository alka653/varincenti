# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0011_reservation_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation_player',
            name='player_user',
            field=models.ForeignKey(to='users.ProfileUser', null=True),
        ),
    ]
