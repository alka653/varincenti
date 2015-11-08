# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20151027_1703'),
        ('users', '0005_auto_20151026_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='state',
            field=models.ForeignKey(blank=True, to='principal.State', null=True),
        ),
    ]
