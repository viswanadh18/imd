# Generated by Django 2.0.6 on 2018-06-18 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movinfo', '0002_auto_20180618_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='slug',
        ),
    ]
