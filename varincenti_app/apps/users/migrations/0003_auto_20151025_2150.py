# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151025_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='number_telephone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
