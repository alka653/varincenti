# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0003_product_extreme'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='product_extreme',
            field=models.ForeignKey(to='extreme.Product_extreme', null=True),
        ),
    ]
