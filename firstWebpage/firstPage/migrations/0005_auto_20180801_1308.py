# Generated by Django 2.0.7 on 2018-08-01 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0004_auto_20180801_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlog',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='rawmateriallog',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]