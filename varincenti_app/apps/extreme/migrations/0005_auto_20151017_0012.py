# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0004_reservation_product_extreme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_extreme',
            name='photo',
            field=models.FileField(upload_to=b'extreme/product/'),
        ),
    ]
