# Generated by Django 2.0.7 on 2019-08-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0047_auto_20190817_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlog',
            name='time',
            field=models.TimeField(default='23:28:09'),
        ),
        migrations.AlterField(
            model_name='rawmateriallog',
            name='time',
            field=models.TimeField(default='23:28:09'),
        ),
    ]