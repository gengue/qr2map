# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('qr_code', models.ImageField(null=True, upload_to=b'uploads/qr_codes', blank=True)),
                ('lat', models.CharField(max_length=30)),
                ('lng', models.CharField(max_length=30)),
            ],
        ),
    ]
