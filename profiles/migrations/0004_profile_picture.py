# Generated by Django 3.0.9 on 2021-12-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20211207_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='Picture', upload_to='media/pictures'),
        ),
    ]
