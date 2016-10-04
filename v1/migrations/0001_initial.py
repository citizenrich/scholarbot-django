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
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, max_length=36, unique=True)),
                ('subject_pref', models.TextField()),
                ('journal_pref', models.TextField()),
                ('search1', models.TextField()),
                ('search1_date', models.DateTimeField()),
                ('search2', models.TextField()),
                ('search2_date', models.DateTimeField()),
                ('search3', models.TextField()),
                ('search3_date', models.DateTimeField()),
            ],
        ),
    ]
