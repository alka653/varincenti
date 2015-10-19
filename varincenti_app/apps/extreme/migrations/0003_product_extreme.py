# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0002_auto_20151016_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_extreme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=250)),
                ('conditions', models.CharField(max_length=3000)),
                ('photo', models.FileField(upload_to=b'image/extreme/product/')),
            ],
        ),
    ]
