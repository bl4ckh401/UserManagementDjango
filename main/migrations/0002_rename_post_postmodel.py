# Generated by Django 3.2.13 on 2022-07-22 15:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='PostModel',
        ),
    ]
