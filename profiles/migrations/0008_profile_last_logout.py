# Generated by Django 3.0.9 on 2022-01-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_remove_profile_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_logout',
            field=models.DateField(blank=True, null=True),
        ),
    ]
