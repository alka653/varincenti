# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0009_product_extreme_place_camp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_extreme',
            name='place_camp',
        ),
        migrations.AddField(
            model_name='place_camp',
            name='product_extreme',
            field=models.ForeignKey(to='extreme.Product_extreme', null=True),
        ),
    ]
