# Generated by Django 2.0.7 on 2018-09-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0031_auto_20180909_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlog',
            name='date',
            field=models.DateField(default='2018-09-09'),
        ),
        migrations.AlterField(
            model_name='productlog',
            name='time',
            field=models.TimeField(default='03:34:54'),
        ),
        migrations.AlterField(
            model_name='rawmateriallog',
            name='date',
            field=models.DateField(default='2018-09-09'),
        ),
        migrations.AlterField(
            model_name='rawmateriallog',
            name='time',
            field=models.TimeField(default='03:34:54'),
        ),
    ]