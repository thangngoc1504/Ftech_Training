# Generated by Django 3.1.6 on 2021-03-10 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210310_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='create',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2021, 3, 10, 16, 38, 43, 74569)),
        ),
    ]