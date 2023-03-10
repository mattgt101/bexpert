# Generated by Django 3.2.1 on 2021-12-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('fname', models.CharField(blank=True, max_length=200, null=True)),
                ('lname', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('pword', models.CharField(blank=True, max_length=200, null=True)),
                ('invest', models.FloatField(blank=True, default=0.0, null=True)),
                ('profit', models.FloatField(blank=True, default=0.0, null=True)),
                ('bonus', models.FloatField(blank=True, default=0.0, null=True)),
                ('bal', models.FloatField(blank=True, default=0.0, null=True)),
                ('btc_equ', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
