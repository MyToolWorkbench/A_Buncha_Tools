# Generated by Django 2.1.1 on 2018-11-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myToolWorkbench', '0011_auto_20181104_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default='no address', max_length=150),
        ),
    ]
