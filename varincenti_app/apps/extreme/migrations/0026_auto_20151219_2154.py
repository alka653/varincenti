# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0025_product_extreme_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_extreme',
            name='state',
            field=models.ForeignKey(default=9, to='principal.State', null=True),
        ),
    ]
