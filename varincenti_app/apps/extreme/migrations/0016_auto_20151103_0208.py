# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0015_auto_20151103_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(to='users.ProfileUser', null=True),
        ),
        migrations.AlterField(
            model_name='reservation_player',
            name='player_user',
            field=models.ForeignKey(to='users.ProfileUser', null=True),
        ),
    ]
