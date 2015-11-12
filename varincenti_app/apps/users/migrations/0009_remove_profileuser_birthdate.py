# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profileuser_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='birthdate',
        ),
    ]
