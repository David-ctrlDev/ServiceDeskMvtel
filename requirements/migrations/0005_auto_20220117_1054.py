# Generated by Django 3.0.9 on 2022-01-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0004_auto_20220117_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='project',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
