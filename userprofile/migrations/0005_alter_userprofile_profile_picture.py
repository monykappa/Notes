# Generated by Django 4.2.5 on 2023-10-01 10:31

from django.db import migrations, models
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=userprofile.models.user_directory_path, validators=[userprofile.models.validate_file_extension]),
        ),
    ]
