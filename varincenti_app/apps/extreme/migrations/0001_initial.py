# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place_camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
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
                ('date', models.DateTimeField()),
                ('place_camp', models.ForeignKey(to='extreme.Place_camp')),
            ],
        ),
    ]
