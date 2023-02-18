# Generated by Django 3.2.1 on 2021-12-04 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binaryapp', '0007_alter_history_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 4, 7, 20, 9, 994991), null=True),
        ),
    ]