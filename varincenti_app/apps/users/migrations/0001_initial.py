# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(upload_to=b'image/users/')),
                ('number_telephone', models.CharField(unique=True, max_length=10, blank=True)),
                ('number_cellphone', models.CharField(unique=True, max_length=10)),
            ],
        ),
    ]
