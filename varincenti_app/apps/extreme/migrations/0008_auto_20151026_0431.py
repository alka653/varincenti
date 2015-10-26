# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0007_auto_20151026_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_reservation',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='hour_reservation',
            field=models.TimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
