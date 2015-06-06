# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import places.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceOfInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('location', places.widgets.LocationField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypePlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='place',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='place',
            name='lng',
        ),
        migrations.AddField(
            model_name='place',
            name='location',
            field=places.widgets.LocationField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='placeofinterest',
            name='types',
            field=models.ManyToManyField(to='places.TypePlace'),
        ),
    ]
