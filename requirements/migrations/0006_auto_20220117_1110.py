# Generated by Django 3.0.9 on 2022-01-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0005_auto_20220117_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='project',
            field=models.CharField(max_length=300),
        ),
    ]
