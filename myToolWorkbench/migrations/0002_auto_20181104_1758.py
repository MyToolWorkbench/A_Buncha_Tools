# Generated by Django 2.1.1 on 2018-11-04 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('myToolWorkbench', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myToolWorkbench.Person')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('myToolWorkbench.person',),
        ),
        migrations.RemoveField(
            model_name='user',
            name='person_ptr',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
