# Generated by Django 2.0.7 on 2018-09-17 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0033_auto_20180910_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlog',
            name='date',
            field=models.DateField(default='2018-09-17'),
        ),
        migrations.AlterField(
            model_name='productlog',
            name='time',
            field=models.TimeField(default='17:03:40'),
        ),
        migrations.AlterField(
            model_name='rawmateriallog',
            name='date',
            field=models.DateField(default='2018-09-17'),
        ),
        migrations.AlterField(
            model_name='rawmateriallog',
            name='time',
            field=models.TimeField(default='17:03:40'),
        ),
    ]
