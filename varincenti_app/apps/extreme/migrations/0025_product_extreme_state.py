# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20151027_1703'),
        ('extreme', '0024_place_camp_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_extreme',
            name='state',
            field=models.ForeignKey(default=1, to='principal.State', null=True),
        ),
    ]
