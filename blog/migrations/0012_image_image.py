# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150901_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 9, 1, 13, 46, 16, 500854, tzinfo=utc), upload_to='blog/images'),
            preserve_default=False,
        ),
    ]
