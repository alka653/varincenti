# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0008_auto_20151018_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_extreme',
            name='place_camp',
            field=models.ForeignKey(to='extreme.Place_camp', null=True),
        ),
    ]
