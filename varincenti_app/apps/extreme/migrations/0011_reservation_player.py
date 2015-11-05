# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extreme', '0010_remove_reservation_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation_player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('reservation', models.ForeignKey(to='extreme.Reservation', null=True)),
            ],
        ),
    ]
