# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20150601_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='qr_code',
            field=models.CharField(default=datetime.datetime(2015, 6, 1, 3, 28, 34, 943103, tzinfo=utc), max_length=500, blank=True),
            preserve_default=False,
        ),
    ]
