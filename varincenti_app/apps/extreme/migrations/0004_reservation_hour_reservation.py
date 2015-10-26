# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0003_auto_20151023_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='hour_reservation',
            field=models.TimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
