# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_profileuser_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='number_cellphone',
            field=models.CharField(max_length=10),
        ),
    ]
