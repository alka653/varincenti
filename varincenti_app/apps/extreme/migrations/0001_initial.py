# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp_product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place_camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_extreme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=250)),
                ('conditions', models.CharField(max_length=3000)),
                ('photo', models.ImageField(upload_to=b'image/extreme/product/')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_complete', models.CharField(max_length=50)),
                ('number_telephone', models.CharField(max_length=10, blank=True)),
                ('number_cellphone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('date_reservation', models.DateField(null=True)),
                ('camp_product', models.ForeignKey(to='extreme.Camp_product', null=True)),
                ('state', models.ForeignKey(default=1, to='principal.State', null=True)),
            ],
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
    ]
