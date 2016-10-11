# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='image',
        ),
        migrations.AlterField(
            model_name='file',
            name='pdf',
            field=models.FileField(blank=True, default='', null=True, upload_to='pdfs/'),
        ),
    ]
