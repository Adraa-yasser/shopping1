# Generated by Django 5.0.1 on 2024-02-02 21:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_userprofile_userprofile1'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile1',
            new_name='UserProfile',
        ),
    ]
