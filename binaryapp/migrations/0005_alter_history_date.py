# Generated by Django 3.2.1 on 2021-12-04 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binaryapp', '0004_alter_history_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 4, 5, 24, 24, 161653), null=True),
        ),
    ]
