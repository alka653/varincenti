# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0023_place_camp_ubication'),
    ]

    operations = [
        migrations.AddField(
            model_name='place_camp',
            name='photo',
            field=models.ImageField(upload_to=b'image/extreme/camp/', blank=True),
        ),
    ]
