# Generated by Django 3.1.6 on 2021-03-12 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='create',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 3, 12, 15, 47, 53, 766375)),
        ),
    ]