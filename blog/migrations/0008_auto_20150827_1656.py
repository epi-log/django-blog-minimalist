# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150827_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='thumbnail',
            field=sorl.thumbnail.fields.ImageField(upload_to='blog/static/blog/media/thumbnail'),
        ),
    ]
