# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20151027_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='tag',
            new_name='class_tag',
        ),
    ]
