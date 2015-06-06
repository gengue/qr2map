# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20150601_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='coverage',
            field=models.IntegerField(default=1000),
        ),
    ]
