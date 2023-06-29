# Generated by Django 4.0.3 on 2023-06-29 13:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2023, 6, 29, 13, 45, 57, 701868, tzinfo=utc))),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='imgs/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
    ]
