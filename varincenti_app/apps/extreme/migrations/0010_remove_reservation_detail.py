# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0009_reservation_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='detail',
        ),
    ]
