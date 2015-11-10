# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profileuser_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='photo_2',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='state',
            field=models.ForeignKey(default=8, blank=True, to='principal.State', null=True),
        ),
    ]
