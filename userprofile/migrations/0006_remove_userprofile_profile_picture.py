# Generated by Django 4.2.5 on 2023-10-01 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]