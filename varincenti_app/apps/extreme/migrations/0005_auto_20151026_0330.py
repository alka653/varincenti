# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0004_reservation_hour_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='hour_reservation',
            field=models.CharField(max_length=8, blank=True),
        ),
    ]
