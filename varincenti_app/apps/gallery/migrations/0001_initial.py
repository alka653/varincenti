# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('photo', models.ImageField(upload_to=b'image/gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='Type_gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='type_gallery',
            field=models.ForeignKey(to='gallery.Type_gallery'),
        ),
    ]
