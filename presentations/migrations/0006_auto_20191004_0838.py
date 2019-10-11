# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-04 11:38
from __future__ import unicode_literals

from django.db import migrations
import tinymce_4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0005_auto_20190930_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='page_number',
        ),
        migrations.AlterField(
            model_name='slide',
            name='content',
            field=tinymce_4.fields.TinyMCEModelField(verbose_name='Conteúdo'),
        ),
    ]
