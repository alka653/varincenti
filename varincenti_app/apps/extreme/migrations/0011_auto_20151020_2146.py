# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extreme', '0010_auto_20151019_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp_product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='place_camp',
            name='product_extreme',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='product_extreme',
        ),
        migrations.AddField(
            model_name='camp_product',
            name='place_camp',
            field=models.ForeignKey(to='extreme.Place_camp', null=True),
        ),
        migrations.AddField(
            model_name='camp_product',
            name='product_extreme',
            field=models.ForeignKey(to='extreme.Product_extreme', null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='camp_product',
            field=models.ForeignKey(to='extreme.Camp_product', null=True),
        ),
    ]
