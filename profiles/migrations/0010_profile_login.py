# Generated by Django 3.0.9 on 2022-01-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20220112_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='login',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]