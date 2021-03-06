# Generated by Django 3.1.7 on 2021-05-06 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('describe', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(-1, 'Doing'), (0, 'NotDo'), (1, 'Done')], default=0)),
                ('note', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['status', 'create_at'],
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subdomain_prefix', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shared_DB_Schema.projects')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shared_DB_Schema.tenant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('describe', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(-1, 'Doing'), (0, 'NotDo'), (1, 'Done')], default=0)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('update_by', models.CharField(blank=True, default=None, editable=False, max_length=30, null=True)),
                ('is_view', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shared_DB_Schema.projects')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shared_DB_Schema.tenant')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['status', '-create_at', 'project'],
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='members',
            field=models.ManyToManyField(through='Shared_DB_Schema.UserProject', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projects',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shared_DB_Schema.tenant'),
        ),
    ]
