# Generated by Django 2.0.7 on 2018-07-24 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0002_auto_20180724_1458'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stocks',
            new_name='RawMaterial',
        ),
    ]
