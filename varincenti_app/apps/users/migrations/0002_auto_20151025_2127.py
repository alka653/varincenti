# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='number_telephone',
            field=models.CharField(max_length=10, unique=True, null=True, blank=True),
        ),
    ]
