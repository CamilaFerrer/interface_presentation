# Generated by Django 2.1 on 2019-09-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0004_auto_20190930_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='content',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
    ]
