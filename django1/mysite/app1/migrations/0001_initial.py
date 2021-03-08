# Generated by Django 3.1.6 on 2021-03-07 15:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=25)),
                ('mail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postName', models.CharField(max_length=100)),
                ('postContent', models.TextField()),
                ('postCreate', models.DateTimeField(verbose_name=datetime.datetime(2021, 3, 7, 22, 29, 2, 775412))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.user')),
            ],
        ),
    ]