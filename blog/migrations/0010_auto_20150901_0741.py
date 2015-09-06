# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150828_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={},
        ),
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 9, 1, 7, 41, 20, 308113, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='thumbnail',
            field=models.ImageField(upload_to='blog/thumbnail'),
        ),
    ]
