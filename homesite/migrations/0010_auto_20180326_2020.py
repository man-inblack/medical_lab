# Generated by Django 2.0 on 2018-03-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
        ('homesite', '0009_auto_20180326_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='file',
        ),
        migrations.AddField(
            model_name='text',
            name='file',
            field=models.ManyToManyField(to='download.Download_file'),
        ),
    ]
