# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extreme', '0002_auto_20151023_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='name_complete',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='number_cellphone',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='number_telephone',
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
