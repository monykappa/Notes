# Generated by Django 4.2.5 on 2023-10-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
