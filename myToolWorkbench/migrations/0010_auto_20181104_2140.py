# Generated by Django 2.1.1 on 2018-11-05 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myToolWorkbench', '0009_auto_20181104_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='origin_country',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='upc_code',
            field=models.CharField(max_length=30, null=True),
        ),
    ]