# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-11 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=10)),
                ('experience', models.IntegerField(default=0)),
                ('zipcode', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('resume', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
    ]
