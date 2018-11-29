# Generated by Django 2.1.1 on 2018-11-29 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myToolWorkbench', '0017_merge_20181129_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='user_account',
        ),
        migrations.AddField(
            model_name='business',
            name='created_by',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
