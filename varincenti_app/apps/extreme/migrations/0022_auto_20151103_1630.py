# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0021_reservation_player_player_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation_player',
            name='player_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
