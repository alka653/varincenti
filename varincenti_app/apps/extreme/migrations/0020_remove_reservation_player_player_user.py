# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0019_auto_20151103_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation_player',
            name='player_user',
        ),
    ]
