# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('imdb_score', models.FloatField(null=True, blank=True)),
                ('popularity', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('genre', models.TextField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
