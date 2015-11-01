# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0008_auto_20151026_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='detail',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
