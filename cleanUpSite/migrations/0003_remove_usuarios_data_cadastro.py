# Generated by Django 3.1.4 on 2023-09-23 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanUpSite', '0002_auto_20230916_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='data_cadastro',
        ),
    ]
