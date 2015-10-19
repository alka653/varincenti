# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0007_auto_20151018_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_extreme',
            name='photo',
            field=models.ImageField(upload_to=b'image/extreme/product/'),
        ),
    ]
