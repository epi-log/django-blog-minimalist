# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150906_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='description',
        ),
        migrations.RemoveField(
            model_name='image',
            name='active',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]
