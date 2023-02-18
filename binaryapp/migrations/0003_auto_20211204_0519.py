# Generated by Django 3.2.1 on 2021-12-04 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binaryapp', '0002_auto_20211203_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('site', models.CharField(default='site', max_length=200, primary_key=True, serialize=False)),
                ('btc_wallet', models.CharField(blank=True, max_length=2000, null=True)),
                ('eth_wallet', models.CharField(blank=True, max_length=2000, null=True)),
                ('phone', models.CharField(blank=True, max_length=2000, null=True)),
                ('email', models.CharField(blank=True, max_length=2000, null=True)),
                ('add', models.CharField(blank=True, max_length=2000, null=True)),
                ('admin', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 4, 5, 19, 15, 348779), null=True),
        ),
    ]