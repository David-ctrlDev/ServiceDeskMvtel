# Generated by Django 3.0.9 on 2022-01-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20211213_1601'),
        ('requirements', '0006_auto_20220117_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]