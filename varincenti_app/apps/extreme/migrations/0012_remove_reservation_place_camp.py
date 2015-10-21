# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0011_auto_20151020_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='place_camp',
        ),
    ]
