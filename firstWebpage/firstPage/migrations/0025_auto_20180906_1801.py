# Generated by Django 2.0.7 on 2018-09-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0024_rawmaterial_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlog',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawmateriallog',
            name='user_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
