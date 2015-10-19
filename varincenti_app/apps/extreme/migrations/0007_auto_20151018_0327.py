# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0006_auto_20151017_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_extreme',
            name='photo',
            field=models.ImageField(upload_to=b'extreme/product/'),
        ),
    ]
