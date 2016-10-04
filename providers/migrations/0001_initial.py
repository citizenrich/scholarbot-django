# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.TextField()),
                ('keywords', models.TextField()),
                ('title', models.TextField()),
                ('url', models.TextField()),
                ('doi', models.TextField()),
                ('pubdate', models.DateTimeField()),
            ],
        ),
    ]
