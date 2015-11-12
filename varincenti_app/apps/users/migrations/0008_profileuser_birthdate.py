# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20151110_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='birthdate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
