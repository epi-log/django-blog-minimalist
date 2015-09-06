# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Album',
            new_name='album',
        ),
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(upload_to='blog/images/thumbnail', default=datetime.datetime(2015, 9, 6, 9, 47, 9, 639085, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='blog/images/fullsize/'),
        ),
    ]
