# Generated by Django 2.0.7 on 2018-08-14 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0019_auto_20180814_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productlog',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='rawmateriallog',
            old_name='raw_material',
            new_name='raw_material_id',
        ),
    ]