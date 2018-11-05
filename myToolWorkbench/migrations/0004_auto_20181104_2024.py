# Generated by Django 2.1.1 on 2018-11-05 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myToolWorkbench', '0003_auto_20181104_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tool',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='tool',
            name='regular_retail',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tool',
            name='special_retail',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
