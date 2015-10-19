# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0005_auto_20151017_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_extreme',
            name='photo',
            field=models.FileField(upload_to=b'image/extreme/product/'),
        ),
    ]
