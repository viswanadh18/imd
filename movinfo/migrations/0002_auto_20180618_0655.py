# Generated by Django 2.0.6 on 2018-06-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='slug',
            field=models.SlugField(default=None, max_length=250),
        ),
    ]
