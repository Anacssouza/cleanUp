# Generated by Django 3.1.4 on 2023-10-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleanUpSite', '0009_auto_20231026_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfor',
            name='data_participacao',
            field=models.DateTimeField(),
        ),
    ]
