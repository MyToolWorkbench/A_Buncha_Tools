# Generated by Django 2.1.1 on 2018-11-05 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myToolWorkbench', '0004_auto_20181104_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='cost',
        ),
    ]