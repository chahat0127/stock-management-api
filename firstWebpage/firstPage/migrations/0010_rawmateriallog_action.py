# Generated by Django 2.0.7 on 2018-08-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0009_remove_rawmateriallog_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmateriallog',
            name='action',
            field=models.CharField(default='add', max_length=20),
            preserve_default=False,
        ),
    ]
