# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150901_0741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='author',
        ),
        migrations.AddField(
            model_name='image',
            name='Album',
            field=models.ForeignKey(to='blog.Album'),
        ),
    ]
