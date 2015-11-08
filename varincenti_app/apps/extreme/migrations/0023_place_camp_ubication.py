# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0022_auto_20151103_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='place_camp',
            name='ubication',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
